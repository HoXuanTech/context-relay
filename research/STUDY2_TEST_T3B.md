# Test Results: T3B (Handoff, Test Point 3)
Context used: Handoff6 from STUDY2_DATA_B.md
Questions: T3 (Q31–Q45)
Agent: Group B (handoff)

---

**Q31** SAFETY-1 and SAFETY-2 from S1 are still in force across all 6 sessions. What is SAFETY-2, and has anything changed about its status since S1?
**Answer:** SAFETY-2: DO NOT remove the `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47. It is required for legacy admin tokens pre-schema migration; removal causes runtime type errors. Its status has not changed — the cast was kept in S2 after investigation. The S2 work added optional chaining and `AdminTokenValidationError` as safety nets around the cast, but the cast itself remains in place. SAFETY-2 is still fully in force as of Handoff6.
**Confidence:** High

---

**Q32** Which two endpoints were specifically updated in S2 to throw `AdminTokenValidationError` when `adminScope` is missing?
**Answer:** `/admin/users` and `/admin/reports`. These are the sensitive endpoints where missing `adminScope` causes `AdminTokenValidationError` to be thrown, returning HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }`. Non-sensitive endpoints fall back to `token.adminScope ?? ""`.
**Confidence:** High

---

**Q33** What are the exact Redis connection pool settings from S3, and what is the consequence of exceeding the `maxConnections` limit?
**Answer:** `maxConnections=10`, `idleTimeoutMillis=30000`. Exceeding the limit — specifically setting `maxConnections=15` was tested in staging — caused 503 errors under the expected concurrent load profile. SAFETY-4 prohibits raising this ceiling without completing a new load test.
**Confidence:** High

---

**Q34** What atomic Redis operation was used to fix the token cache race condition, and what alternative was considered but rejected?
**Answer:** `SET NX EX` (Set if Not eXists with Expiry) was used. The rejected alternative was the `async-mutex` Node.js library. `async-mutex` was rejected because it only serializes writes within a single process and would not protect against multi-pod deployments where two instances race on the same Redis key. `SET NX EX` is atomic at the Redis level regardless of instance count.
**Confidence:** High

---

**Q35** What bug was discovered during S4 test coverage work, and what was its visible symptom in production?
**Answer:** `orderHandler.ts` was not handling `TokenExpiredError` explicitly. When an expired JWT was used on an order endpoint, the error fell through all catch branches and returned HTTP 500 instead of HTTP 401. This would incorrectly trigger server-error alerting and prevent clients from distinguishing a retryable token expiry from a genuine server failure.
**Confidence:** High

---

**Q36** How was the `TokenExpiredError` gap in `orderHandler.ts` fixed, and what prior work established the pattern?
**Answer:** A dedicated `catch (err)` branch was added that checks `err instanceof TokenExpiredError` and returns `{ status: 401, code: "TOKEN_EXPIRED" }`. This mirrors the pattern established in `authMiddleware.ts` during S1, where `TokenExpiredError` and `JsonWebTokenError` were given separate explicit handling. The S4 fix brings `orderHandler` into conformance with the S1 standard.
**Confidence:** High

---

**Q37** What is SAFETY-5 and what incident motivated it?
**Answer:** SAFETY-5: DO NOT mock Redis in `orderHandler` tests — real Redis via testcontainers is mandatory. The motivation was a prior incident where a mock-based test produced a false positive in staging: the mock did not reproduce the timing behavior of `SET NX EX`, so a race condition that appeared "fixed" per tests was still present in production. The mock gave false confidence.
**Confidence:** High

---

**Q38** What conflict was discovered about the middleware pipeline order in S5, and what was the resolution?
**Answer:** Placing `rateLimitMiddleware` after `authMiddleware` meant requests with deliberately expired or malformed tokens still passed through `authMiddleware` (doing JWT verification work) before hitting the rate limiter — an attacker could flood the server with invalid tokens and drive JWT verification load without consuming their rate limit budget. Resolution: `rateLimitMiddleware` was moved BEFORE `authMiddleware` in `app.ts`. Pipeline order: `rateLimitMiddleware` → `authMiddleware` → route handlers.
**Confidence:** High

---

**Q39** What is SAFETY-6 and what specific attack does it prevent?
**Answer:** SAFETY-6: DO NOT revert the pipeline order (rate limit must come before auth). It prevents a token-flooding attack: if rate limiting ran after auth, an attacker could send a high volume of requests with invalid or expired tokens, each causing JWT verification work in `authMiddleware`, without being rate-limited. The current order ensures all requests — including unauthenticated ones — are rate-limited before any verification work occurs.
**Confidence:** High

---

**Q40** What are the rate limit parameters (algorithm, limit, time window, backing store) and which endpoints are exempt?
**Answer:** Algorithm: sliding window. Limit: 100 requests per minute per IP. Backing store: Redis sorted sets using `ZADD` / `ZREMRANGEBYSCORE` / `ZCARD` with a Lua script for atomic TOCTOU-safe counting. Exempt endpoints: `GET /health` and `GET /metrics`. These are whitelisted because load balancers and Prometheus need unrestricted access.
**Confidence:** High

---

**Q41** What two items were carried over from S5 as next actions into S6?
**Answer:** (1) Profile `verifyToken` performance under realistic load to determine if an in-memory cache layer is needed to reduce Redis round-trips. (2) Write automated tests for `rateLimitMiddleware` — the S5 work was validated only by manual testing; automated test coverage was not completed in S5.
**Confidence:** High

---

**Q42** What format is used for the LRU cache key for verified tokens, and what is the specific security reason for this choice?
**Answer:** The cache key is `SHA256(tokenString)` — the SHA256 hash of the raw JWT string, generated in `tokenCacheUtils.ts`. The security reason: storing the raw JWT as a cache key would mean the cache holds valid bearer credentials at rest, creating a cache poisoning risk if the cache is ever serialized, logged, or inspected. An opaque SHA256 hash reveals nothing exploitable even if the cache is exposed. This is a security requirement, not a performance choice.
**Confidence:** High

---

**Q43** Which tokens are excluded from the LRU cache and why?
**Answer:** Tokens with a non-empty `adminScope` are excluded from the LRU cache entirely (SAFETY-7). Admin tokens must always hit Redis so that real-time revocation takes effect immediately — for example, when an admin account is compromised and its tokens are revoked in Redis, the revocation must take effect on the next request, not after the 60-second LRU TTL expires. The LRU cache check is skipped entirely when `token.adminScope` is non-empty.
**Confidence:** High

---

**Q44** Why was `lru-cache` v10 used instead of v7?
**Answer:** `lru-cache` v7 has a known memory leak in async callback paths (found via GitHub issue search). Because `verifyToken` is async and the cache's `fetchMethod` uses async callbacks, using v7 would leak memory proportional to the cache miss rate. v10 fixes this bug. The dependency is pinned to `^10.0.0` in `package.json` to prevent accidental downgrade.
**Confidence:** High

---

**Q45** What are the Redis TTL values for access tokens and refresh tokens, and how are they defined in the codebase?
**Answer:** Access tokens: 900 seconds (15 minutes). Refresh tokens: 604800 seconds (7 days). They are defined as named constants in `tokenCacheService.ts`: `ACCESS_TOKEN_TTL_SECONDS = 900` and `REFRESH_TOKEN_TTL_SECONDS = 604800`. Named constants were used explicitly to prevent magic numbers from proliferating through the codebase.
**Confidence:** High
