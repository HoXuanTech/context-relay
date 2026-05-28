# Test Results: T3A (Auto-Compact, Test Point 3)
Context used: Summary6 from STUDY2_DATA_A.md
Questions: T3 (Q31–Q45)
Agent: Group A (auto-compaction)

---

**Q31** SAFETY-1 and SAFETY-2 from S1 are still in force across all 6 sessions. What is SAFETY-2, and has anything changed about its status since S1?
**Answer:** SAFETY-2 is: DO NOT remove the `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47. Its status has not changed — Summary6 confirms it is still one of the active safety rules. The cast was kept after S2 investigation; optional chaining and `AdminTokenValidationError` were added as the runtime safety net around it, but the cast itself remains in place. SAFETY-2 is still fully in force.
**Confidence:** High

---

**Q32** Which two endpoints were specifically updated in S2 to throw `AdminTokenValidationError` when `adminScope` is missing?
**Answer:** `/admin/users` and `/admin/reports`. These are the sensitive endpoints where a missing or empty `adminScope` causes `AdminTokenValidationError` to be thrown, returning HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }`.
**Confidence:** High

---

**Q33** What are the exact Redis connection pool settings from S3, and what is the consequence of exceeding the `maxConnections` limit?
**Answer:** `maxConnections=10`, `idleTimeoutMillis=30000`. Exceeding the limit — specifically, staging tests showed that raising `maxConnections` to 15 — caused 503 errors under the target load profile. SAFETY-4 prohibits raising `maxConnections` above 10 without completing a new load test.
**Confidence:** High

---

**Q34** What atomic Redis operation was used to fix the token cache race condition, and what alternative was considered but rejected?
**Answer:** `SET NX EX` (Set if Not eXists with Expiry) was chosen for the atomic fix. The rejected alternative was the `async-mutex` Node.js library. `async-mutex` was rejected because it only serializes writes within a single process and would not protect against multi-pod deployments where two separate instances race on the same Redis key. `SET NX EX` is atomic at the Redis level regardless of instance count.
**Confidence:** High

---

**Q35** What bug was discovered during S4 test coverage work, and what was its visible symptom in production?
**Answer:** `orderHandler.ts` was not handling `TokenExpiredError` explicitly. When an expired JWT was used on an order endpoint, the error fell through all catch branches and returned HTTP 500 instead of HTTP 401. Summary6 notes this was confirmed as a real bug: "fixing a real bug where expired tokens returned 500 instead of 401."
**Confidence:** High

---

**Q36** How was the `TokenExpiredError` gap in `orderHandler.ts` fixed, and what prior work established the pattern?
**Answer:** A dedicated `catch (err)` branch was added that checks `err instanceof TokenExpiredError` and returns `{ status: 401, code: "TOKEN_EXPIRED" }`. This mirrors the pattern established in `authMiddleware.ts` (from the S1 work), where `TokenExpiredError` and `JsonWebTokenError` were given separate explicit handling. Summary6 references this as part of the 6 `orderHandler` tests that covered it.
**Confidence:** High

---

**Q37** What is SAFETY-5 and what incident motivated it?
**Answer:** SAFETY-5: DO NOT mock Redis in `orderHandler` tests — real Redis via testcontainers is mandatory. The motivation was a prior false positive: a mock-based approach failed to reproduce the `SET NX EX` timing/atomic behavior, causing a real race condition to appear fixed in tests while it remained present in production. Summary6 states: "SAFETY-5 (no Redis mocks in orderHandler tests — testcontainers only)."
**Confidence:** High

---

**Q38** What conflict was discovered about the middleware pipeline order in S5, and what was the resolution?
**Answer:** The conflict: placing `rateLimitMiddleware` after `authMiddleware` (the intuitive order) meant a client could flood the server with malformed or expired tokens, driving JWT verification work in `authMiddleware` without ever consuming their rate limit budget — because each request passed through auth before hitting the rate limiter. Resolution: `rateLimitMiddleware` was moved BEFORE `authMiddleware` in `app.ts`. Current pipeline order: `rateLimitMiddleware` → `authMiddleware` → route handlers.
**Confidence:** High

---

**Q39** What is SAFETY-6 and what specific attack does it prevent?
**Answer:** SAFETY-6: DO NOT revert the pipeline order (rate limit must come before auth). It prevents a token-flooding attack: if rate limiting ran after auth, an attacker could send a high volume of requests with invalid or expired tokens, each causing JWT verification work in `authMiddleware`, without being rate-limited. The current order ensures all requests are rate-limited before any verification work occurs.
**Confidence:** High

---

**Q40** What are the rate limit parameters (algorithm, limit, time window, backing store) and which endpoints are exempt?
**Answer:** Algorithm: sliding window. Limit: 100 requests per minute per IP. Backing store: Redis sorted sets with a Lua script for atomic TOCTOU-safe counting (`ZADD` / `ZREMRANGEBYSCORE` / `ZCARD`). Exempt endpoints: `/health` and `/metrics` — whitelisted because load balancers and Prometheus need unrestricted access.
**Confidence:** High

---

**Q41** What two items were carried over from S5 as next actions into S6?
**Answer:** (1) Profile `verifyToken` performance to determine if an in-memory cache layer would reduce Redis round-trips. (2) Write automated tests for `rateLimitMiddleware` (S5 only completed manual testing). Summary6 confirms both: the LRU cache work was done in S6 (item 1 fulfilled), while automated tests for `rateLimitMiddleware` remain in the "Remaining work" section (item 2 still pending).
**Confidence:** High

---

**Q42** What format is used for the LRU cache key for verified tokens, and what is the specific security reason for this choice?
**Answer:** The cache key is `SHA256(tokenString)` — the SHA256 hash of the raw JWT string. The security reason: storing the raw JWT as a cache key would mean the cache holds valid bearer credentials, creating a cache poisoning risk if the cache is ever serialized, logged, or inspected. An opaque SHA256 hash reveals nothing exploitable even if the cache is exposed. Summary6 explicitly states: "This is a security requirement, not a performance optimization."
**Confidence:** High

---

**Q43** Which tokens are excluded from the LRU cache and why?
**Answer:** Admin tokens — specifically, tokens with a non-empty `adminScope` — are excluded from the LRU cache entirely (SAFETY-7). They must always hit Redis so that real-time revocation takes effect immediately. If an admin account is compromised and its tokens are revoked in Redis, that revocation must take effect on the next request, not after a 60-second LRU TTL expires. The LRU check is skipped when `token.adminScope` is non-empty.
**Confidence:** High

---

**Q44** Why was `lru-cache` v10 used instead of v7?
**Answer:** `lru-cache` v7 has a known memory leak in async callback paths. Because `verifyToken` is async and the cache's `fetchMethod` uses async callbacks, using v7 would leak memory proportional to the cache miss rate. v10 fixes this bug. The dependency is pinned to `^10.0.0` in `package.json` to prevent accidental downgrade.
**Confidence:** High

---

**Q45** What are the Redis TTL values for access tokens and refresh tokens, and how are they defined in the codebase?
**Answer:** Access tokens: `ACCESS_TOKEN_TTL_SECONDS = 900` (15 minutes). Refresh tokens: `REFRESH_TOKEN_TTL_SECONDS = 604800` (7 days). Both are defined as named constants in `tokenCacheService.ts` to prevent magic numbers from proliferating through the codebase.
**Confidence:** High
