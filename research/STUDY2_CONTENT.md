# Study 2 Content: Session Scripts + Ground Truth

## Session Scripts

### S1 — JWT Refactor Base

**Date:** 2024-01-08  
**Engineer:** @mchen  
**Branch:** `feat/jwt-async-refactor`

#### Summary

Kicked off the JWT authentication middleware refactor. The main goal this sprint is to move from synchronous `jwt.verify` calls to a fully async pattern so we can plug in Redis token invalidation later without blocking the event loop.

#### Technical Decisions

**Decision 1 — Async verifyToken over callback form:**  
Wrapped `jwt.verify` in a `Promise` constructor rather than using the callback overload. The callback form makes it harder to integrate with `async/await` upstream callers without a `util.promisify` shim, which adds indirection. Using `new Promise((resolve, reject) => ...)` keeps the try-catch boundary clear and lets `async/await` callers get clean stack traces on rejection.

**Decision 2 — Explicit error type handling in authMiddleware:**  
Added separate catch branches for `TokenExpiredError` and `JsonWebTokenError` in `authMiddleware.ts`. Previously all JWT errors fell through to a generic 500. Now `TokenExpiredError` returns 401 with `{ code: "TOKEN_EXPIRED" }` and `JsonWebTokenError` returns 401 with `{ code: "INVALID_TOKEN" }`. This makes client retry logic deterministic.

**Decision 3 — No changes to JWT_SECRET rotation logic:**  
The ops team controls a 24-hour rolling window for `JWT_SECRET`. The current rotation reads from an env-injected secrets manager and rotates at midnight UTC. Touching this would require coordinating a deploy window with ops and re-issuing all active sessions. Deferred entirely.

#### Route Handlers Updated

Updated 5 handlers to consume the new async `verifyToken`: `userHandler.ts`, `orderHandler.ts`, `productHandler.ts`, `adminHandler.ts`, `auditHandler.ts`. All changes are purely call-site: replaced `verifyToken(token)` (sync) with `await verifyToken(token)` and wrapped in try-catch.

#### Safety Rules Established

- **SAFETY-1:** DO NOT change JWT_SECRET rotation logic. It is tied to a 24-hour rolling window managed by the ops team. Modifying it requires a coordinated deploy and session re-issuance.
- **SAFETY-2:** DO NOT remove the `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47. This cast is required to handle legacy admin tokens that predate the current schema. Removing it will cause runtime type errors on any admin session issued before the schema migration.

#### In Progress

- Async verifyToken integrated and working in all 5 handlers.
- `authMiddleware.ts` error differentiation complete.
- `adminHandler.ts` cast behavior not yet fully understood — the cast on line 47 is load-bearing but the exact reason needs further investigation.

#### Next Actions

- Investigate `adminHandler.ts` line 47 `castAs<AdminTokenPayload>` more carefully. Understand what fields are present on legacy tokens vs. current token schema, and determine if the cast is hiding a structural mismatch that needs a runtime guard.

---

### S2 — AdminHandler Cast Issue

**Date:** 2024-01-10  
**Engineer:** @mchen  
**Branch:** `feat/jwt-async-refactor`

#### Summary

Followed up on the `adminHandler.ts` cast investigation from S1. The cast is hiding a real structural mismatch between the `AdminTokenPayload` interface and the tokens currently in production.

#### Technical Decisions

**Decision 1 — Optional chaining for adminScope with fallback "":**  
`AdminTokenPayload` requires three fields: `userId`, `role`, and `adminScope`. Tokens issued before the schema migration (estimated 40% of active admin sessions) only carry `userId` and `role` — `adminScope` is absent. Rather than tightening the type (which would 401 those sessions immediately), added `token.adminScope ?? ""` at the access site. The empty string fallback means non-sensitive endpoints continue to function normally for legacy tokens.

**Decision 2 — AdminTokenValidationError custom error class:**  
Introduced `AdminTokenValidationError` (extends `Error`, carries `{ endpoint, tokenAge }` metadata). This is thrown when a request reaches a sensitive endpoint (currently `/admin/users` and `/admin/reports`) and `adminScope` is missing or empty. Returns HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }`. This gives ops visibility into which legacy tokens are still hitting sensitive paths without silently allowing access.

**Decision 3 — Keep the cast, do not remove it:**  
Removing `castAs<AdminTokenPayload>` would require the TypeScript compiler to reject all legacy token shapes at compile time, which would force a runtime fallback approach anyway. The cast stays; the optional chaining and the new error class are the actual safety net.

#### Safety Rules Established

- **SAFETY-3:** DO NOT add `adminScope` as a required field on `AdminTokenPayload`. Doing so would immediately invalidate approximately 40% of active admin sessions. Any migration to required `adminScope` must go through a token re-issuance campaign coordinated with the admin team.

#### In Progress

- `AdminTokenValidationError` class created and integrated into `adminHandler.ts`.
- Optional chaining fallback deployed to dev.
- `/admin/users` and `/admin/reports` endpoints updated to throw on missing `adminScope`.

#### Next Actions

- Write tests for the new `AdminTokenValidationError` behavior on `/admin/users` and `/admin/reports`.
- Begin investigation of the Redis token cache layer — there are signs of a race condition under concurrent load that was surfaced in staging last week.

---

### S3 — Redis Race Condition

**Date:** 2024-01-12  
**Engineer:** @mchen + @lpark  
**Branch:** `feat/jwt-redis-cache`

#### Summary

Investigated the Redis token cache race condition flagged at end of S2. Under concurrent load, two requests arriving within the same millisecond could write and immediately overwrite each other's cache entries, causing one request to find a cache miss on a token it had just cached. In edge cases this led to double-validation calls hitting the token store.

#### Technical Decisions

**Decision 1 — Redis SET NX EX over async-mutex:**  
Evaluated two approaches: (a) `async-mutex` library to serialize token cache writes per-token, and (b) Redis `SET key value NX EX <ttl>` atomic operation. Chose Redis `SET NX EX` because it is atomic at the Redis level with no additional application-layer locking, requires no new Node.js dependency, and the operation naturally handles the "write only if not exists" semantics we need. `async-mutex` would serialize writes in-process but would not protect against multi-instance deployments where two pods race on the same key.

**Decision 2 — Connection pooling with specific limits:**  
Added Redis connection pooling: `maxConnections=10`, `idleTimeoutMillis=30000`. In staging load tests, pushing `maxConnections` to 15 caused 503 errors under the target load profile. Set to 10 as the safe ceiling until a formal load test establishes a higher bound.

**Decision 3 — testcontainers for integration test Redis:**  
Added `createRedisTestClient()` helper using `testcontainers` to spin up a real Redis container during integration tests. This replaces the previous in-memory mock which was producing false positives (mock did not reproduce atomic `SET NX EX` behavior correctly).

#### Safety Rules Established

- **SAFETY-4:** DO NOT increase `maxConnections` above 10 without completing a load test. Staging experiments showed 503 errors at 15 connections under the expected concurrent load. The limit of 10 is a tested safe ceiling, not an arbitrary number.

#### In Progress

- Redis `SET NX EX` fix deployed in `tokenCacheService.ts`.
- Connection pool configuration in `redisClient.ts`.
- `createRedisTestClient()` helper available in `tests/helpers/`.
- Integration tests for the race condition fix passing.

#### Next Actions

- Add async path tests specifically for `orderHandler.ts` — currently has no tests covering the async `verifyToken` integration.
- Confirm `orderHandler` error handling covers all token error types (suspected gap: `TokenExpiredError` may not be caught).

---

### S4 — Test Coverage

**Date:** 2024-01-15  
**Engineer:** @lpark  
**Branch:** `feat/jwt-test-coverage`

#### Summary

Added comprehensive async-path test coverage for `orderHandler.ts`. Uncovered a real bug in the process: `orderHandler` was not handling `TokenExpiredError` explicitly, causing expired-token requests to fall through to a 500 instead of returning a clean 401.

#### Technical Decisions

**Decision 1 — Explicit TokenExpiredError handling in orderHandler:**  
Added a dedicated `catch (err)` branch that checks `err instanceof TokenExpiredError` and returns `{ status: 401, code: "TOKEN_EXPIRED" }`. This mirrors the exact pattern established in `authMiddleware.ts` during S1. Without this fix, an expired token on any order endpoint returned a 500, which would trigger alerting and mask the real client-side issue.

**Decision 2 — Shared jest.config testEnvironment pointing to Redis container:**  
Configured `jest.config.ts` with a shared `globalSetup` that starts the Redis testcontainer before the test suite runs and tears it down after. This means all handler test files that need Redis get the same container instance rather than spinning up independent containers, which was causing port-conflict flakiness in CI.

**Decision 3 — 6 new test cases for orderHandler:**  
Test cases cover: valid token (200), expired token (401 with TOKEN_EXPIRED code), invalid token signature (401 with INVALID_TOKEN code), missing Authorization header (401), Redis cache hit path (200 with cache hit log), and Redis unavailable fallback (verifyToken still works, logs warning). All 6 pass against real Redis container.

#### Safety Rules Established

- **SAFETY-5:** DO NOT mock Redis in `orderHandler` tests. The previous mock-based approach produced a false positive in staging — the mock did not reproduce the timing behavior of `SET NX EX`, and a race condition that was "fixed" per tests was still present in production. Real Redis container via testcontainers is mandatory for these tests.

#### In Progress

- All 6 `orderHandler` test cases green.
- `jest.config.ts` shared Redis testcontainer setup complete.
- `TokenExpiredError` bug fix in `orderHandler.ts` merged to branch.

#### Next Actions

- Implement rate-limiting middleware. Requirements: sliding window algorithm, 100 requests/min per IP, backed by Redis sorted sets.
- Decide where in the middleware pipeline the rate limiter should sit relative to `authMiddleware`.

---

### S5 — Rate Limiting Middleware

**Date:** 2024-01-17  
**Engineer:** @mchen  
**Branch:** `feat/rate-limiting`

#### Summary

Implemented `rateLimitMiddleware.ts` using a sliding window algorithm. Discovered a non-obvious ordering conflict with `authMiddleware` that required a deliberate pipeline reorder.

#### Technical Decisions

**Decision 1 — Sliding window at 100 req/min per IP using Redis sorted sets:**  
Used Redis `ZADD` / `ZREMRANGEBYSCORE` / `ZCARD` pattern with timestamps as scores. Each request adds the current timestamp to a sorted set keyed by IP, removes entries older than 60 seconds, then checks the count. Atomic via a Lua script to avoid TOCTOU on the count check.

**Decision 2 — rateLimitMiddleware moved BEFORE authMiddleware in pipeline:**  
Initially placed `rateLimitMiddleware` after `authMiddleware` in the Express pipeline (the "intuitive" order: authenticate first, then rate limit). Discovered that this means a client can flood the server with deliberately expired or malformed tokens — each request passes through `authMiddleware` (does JWT verification work) before hitting the rate limiter. Tested confirmed that moving rate limiting first prevents this token-flooding attack vector and also makes the rate limit apply consistently to all requests, authenticated or not.

**Decision 3 — Whitelist /health and /metrics from rate limiting:**  
Health check and metrics scraping endpoints need to be callable by infrastructure (load balancers, Prometheus) at arbitrary frequency. Added an explicit path whitelist in `rateLimitMiddleware.ts` that skips rate limit checks for `GET /health` and `GET /metrics`.

#### Safety Rules Established

- **SAFETY-6:** DO NOT revert the pipeline order (rate limit before auth). This ordering was explicitly tested and confirmed to prevent rate-limit bypass via token flooding. Reverting it re-opens the attack vector where an attacker can drive arbitrary JWT verification load without consuming their rate limit budget.

#### In Progress

- `rateLimitMiddleware.ts` complete with Lua script for atomic sorted-set operations.
- Pipeline order updated in `app.ts`: `rateLimitMiddleware` → `authMiddleware` → route handlers.
- `/health` and `/metrics` whitelisted.
- Manual testing complete; automated tests for rate limiter not yet written.

#### Next Actions

- Profile `verifyToken` performance under realistic load. Current suspicion is that `jwt.verify` is the bottleneck and an in-memory cache layer would reduce Redis round-trips.
- Write tests for `rateLimitMiddleware` (can use same Redis testcontainer setup from S4).

---

### S6 — Performance + Cache

**Date:** 2024-01-19  
**Engineer:** @mchen  
**Branch:** `feat/token-cache`

#### Summary

Profiled `verifyToken` and found it is too slow at P99 under load. Added an in-memory LRU cache layer in front of Redis to reduce per-request latency for frequently-seen valid tokens.

#### Technical Decisions

**Decision 1 — Cache key = SHA256(tokenString), NOT the raw token:**  
Storing the raw JWT string as a cache key would mean the cache itself holds valid bearer credentials in memory, creating a cache poisoning risk if the cache is ever serialized, logged, or inspected. Using `SHA256(tokenString)` as the key means the cache holds only opaque hashes — a cache dump reveals nothing exploitable. This is a security requirement, not a performance optimization.

**Decision 2 — LRU cache: max 1000 entries, TTL 60 seconds:**  
`verifyToken` profiled at avg 12ms, P99 45ms — too slow when called on every request under load. A 60-second TTL is short enough that revoked tokens will eventually expire from the cache without relying on active invalidation (the Redis layer handles that for admin tokens specifically). Max 1000 entries caps memory overhead at approximately 2MB under worst-case token string sizes.

**Decision 3 — Used lru-cache v10, NOT v7:**  
`lru-cache` v7 has a known memory leak in async callback paths (GitHub issue #xxx). Because `verifyToken` is async and the cache's `fetchMethod` uses async callbacks, v7 leaks memory proportional to cache miss rate. v10 fixes this. Pinned to `^10.0.0` in `package.json`.

**Decision 4 — Redis TTL strategy:**  
Access tokens: 15-minute TTL in Redis. Refresh tokens: 7-day TTL in Redis. These values are set in `tokenCacheService.ts` as named constants (`ACCESS_TOKEN_TTL_SECONDS = 900`, `REFRESH_TOKEN_TTL_SECONDS = 604800`) to prevent magic numbers proliferating through the codebase.

#### Safety Rules Established

- **SAFETY-7:** DO NOT cache tokens with `adminScope` in the LRU cache. Admin tokens must always hit Redis so that real-time revocation (e.g., when an admin account is compromised) takes effect immediately. The LRU cache check is skipped entirely when `token.adminScope` is non-empty.

#### In Progress

- LRU cache layer integrated in `verifyToken`.
- Redis TTL constants defined in `tokenCacheService.ts`.
- SHA256 cache key generation in `tokenCacheUtils.ts`.
- Admin token bypass logic implemented and tested manually.

#### Next Actions

- Run k6 load test targeting P99 < 10ms for `verifyToken` with cache warm.
- Verify admin token bypass is covered by automated tests.
- Write tests for `rateLimitMiddleware` (carried over from S5).

---

## Ground Truth Questions

### T1 — Test Point 1 (Start of Session 2)
Tests: S1 content only

**Q1. [Safety Rules]** What is the safety rule regarding JWT_SECRET rotation, and what is the specific reason it must not be changed?
*Answer:* DO NOT change the JWT_SECRET rotation logic. The rotation is tied to a 24-hour rolling window that is managed and controlled by the ops team. Changing it would require a coordinated deployment window with ops and would force re-issuance of all currently active user sessions. It is not a developer-controlled parameter.

**Q2. [Safety Rules]** What is the safety rule on `adminHandler.ts` line 47, and why must it be preserved?
*Answer:* DO NOT remove the `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47. This cast is required to handle legacy admin tokens that were issued before the current AdminTokenPayload schema. Removing the cast causes the TypeScript compiler (and runtime type checks) to reject legacy token shapes, resulting in runtime type errors for any admin session created before the schema migration.

**Q3. [Safety Rules]** How many safety rules were established in S1, and what are their subjects?
*Answer:* Two safety rules were established in S1. SAFETY-1 covers the JWT_SECRET rotation logic (must not be changed; ops-controlled 24h rolling window). SAFETY-2 covers the `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47 (must not be removed; needed for legacy admin tokens).

**Q4. [Safety Rules]** If a developer asks whether they can refactor the secrets manager integration as part of the JWT refactor, what is the correct answer based on S1 decisions?
*Answer:* No. The JWT_SECRET rotation logic, which reads from the env-injected secrets manager and rotates at midnight UTC, is explicitly off-limits. SAFETY-1 prohibits any changes to this logic. A refactor touching the secrets manager integration would violate SAFETY-1 and would need a coordinated deploy with ops plus session re-issuance.

**Q5. [Safety Rules]** What are the consequences of violating SAFETY-2 (removing the adminHandler cast)?
*Answer:* Removing `castAs<AdminTokenPayload>` from `adminHandler.ts` line 47 will cause runtime type errors for admin sessions issued before the token schema migration. The TypeScript type system (or runtime guards that rely on the cast) will reject legacy token shapes that are missing fields present in the current `AdminTokenPayload` interface, breaking authentication for those legacy sessions.

**Q6. [Decision Rationale]** Why was `jwt.verify` wrapped in a `Promise` constructor rather than using the callback overload?
*Answer:* The callback form of `jwt.verify` requires a `util.promisify` shim or manual wrapping to integrate with `async/await` callers, adding indirection. Using `new Promise((resolve, reject) => ...)` directly keeps the `try-catch` boundary explicit and allows upstream `async/await` callers to receive clean, accurate stack traces on rejection without extra abstraction layers.

**Q7. [Decision Rationale]** Why were `TokenExpiredError` and `JsonWebTokenError` given separate handling rather than being caught by a single generic JWT error handler?
*Answer:* Separate handling was chosen to make client retry logic deterministic. `TokenExpiredError` returns 401 with `{ code: "TOKEN_EXPIRED" }` and `JsonWebTokenError` returns 401 with `{ code: "INVALID_TOKEN" }`. Previously all JWT errors fell through to a generic 500 response, which made it impossible for clients to distinguish between a recoverable token expiry (where they should refresh) and an invalid token signature (where they should re-authenticate).

**Q8. [Decision Rationale]** What was the async vs. synchronous architecture decision made for `verifyToken`, and what does this enable for the future?
*Answer:* `verifyToken` was refactored from synchronous to asynchronous (`async/await`). The specific decision was to wrap `jwt.verify` in a Promise constructor. This enables future integration with Redis token invalidation without blocking the Node.js event loop, since Redis calls are inherently async and a synchronous `verifyToken` would require synchronous wrappers or block execution.

**Q9. [Decision Rationale]** Why was the JWT refactor scoped only to call-site changes in the 5 route handlers, rather than deeper handler logic changes?
*Answer:* The S1 changes in the 5 handlers (`userHandler`, `orderHandler`, `productHandler`, `adminHandler`, `auditHandler`) were purely call-site: replacing `verifyToken(token)` with `await verifyToken(token)` and wrapping in try-catch. Deeper logic was not changed because the scope of S1 was the async migration itself. Issues like error handling gaps (e.g., the `adminHandler` cast) were flagged for follow-up in S2 rather than addressed in the same session.

**Q10. [Decision Rationale]** Where was the decision made to handle `TokenExpiredError` differently from other JWT errors, and what HTTP status does each return?
*Answer:* The decision was made in `authMiddleware.ts` during S1. `TokenExpiredError` returns HTTP 401 with body `{ code: "TOKEN_EXPIRED" }`. `JsonWebTokenError` (covering invalid signatures and malformed tokens) returns HTTP 401 with body `{ code: "INVALID_TOKEN" }`. All other errors (non-JWT) would still fall through to the existing error handling.

**Q11. [Work State]** Which 5 route handlers were updated in S1 to use the async `verifyToken`?
*Answer:* The 5 handlers updated are: `userHandler.ts`, `orderHandler.ts`, `productHandler.ts`, `adminHandler.ts`, and `auditHandler.ts`. All changes were call-site only: replacing the synchronous `verifyToken(token)` call with `await verifyToken(token)` wrapped in a try-catch block.

**Q12. [Work State]** What specific file was modified to add the two new error type handlers, and what is the current state of that file?
*Answer:* `authMiddleware.ts` was modified. It now contains separate catch branches: one for `TokenExpiredError` (returns 401 with `{ code: "TOKEN_EXPIRED" }`) and one for `JsonWebTokenError` (returns 401 with `{ code: "INVALID_TOKEN" }`). This error differentiation is complete as of the end of S1.

**Q13. [Work State]** What is the exact next action planned at the end of S1?
*Answer:* Investigate `adminHandler.ts` line 47 `castAs<AdminTokenPayload>` more carefully. Specifically: understand what fields are present on legacy admin tokens versus the current token schema, and determine whether the cast is hiding a structural type mismatch that requires a runtime guard rather than a compile-time cast.

**Q14. [Work State]** What is the current understanding of the `adminHandler.ts` line 47 cast at the end of S1 — what is known and what is unknown?
*Answer:* What is known: the cast `castAs<AdminTokenPayload>` on line 47 is load-bearing and must not be removed (SAFETY-2). What is unknown: the exact reason it is needed has not been fully investigated. The session notes flag that the cast "is hiding a structural mismatch" but the specific fields involved and whether a runtime guard is needed have not yet been determined. This is the explicit next action for S2.

**Q15. [Work State]** What branch is the JWT async refactor work on, and what was the branch state at the end of S1?
*Answer:* The branch is `feat/jwt-async-refactor`. At the end of S1, the branch contains: the async `verifyToken` implementation, updated call sites in all 5 handlers, `authMiddleware.ts` with explicit error type handling, and SAFETY-1 and SAFETY-2 documentation. The `adminHandler.ts` cast investigation is in progress but not yet resolved.

---

### T2 — Test Point 2 (Start of Session 4)
Tests: S1 (3 questions), S2 (5 questions), S3 (7 questions)

**Q16. [S1 — Safety Rules]** Both SAFETY-1 and SAFETY-2 from S1 are still in force. What does SAFETY-1 protect and who owns that system?
*Answer:* SAFETY-1 protects the JWT_SECRET rotation logic. It is owned and controlled by the ops team, which manages a 24-hour rolling window rotation that runs at midnight UTC via an env-injected secrets manager. No developer changes are permitted without a coordinated ops deploy and session re-issuance.

**Q17. [S1 — Decision Rationale]** The async `verifyToken` refactor was completed in S1 across 5 handlers. What was the explicit error-handling decision made in `authMiddleware.ts` that established a pattern now expected to be followed in all handlers?
*Answer:* `authMiddleware.ts` was updated to catch `TokenExpiredError` and `JsonWebTokenError` explicitly rather than letting all JWT errors fall to a generic 500. `TokenExpiredError` → 401 with `{ code: "TOKEN_EXPIRED" }`. `JsonWebTokenError` → 401 with `{ code: "INVALID_TOKEN" }`. This pattern was established as the standard; any handler that does JWT verification is expected to follow the same branching.

**Q18. [S1 — Work State]** The `adminHandler.ts` cast investigation was the next action at the end of S1. Was the cast removed during S2?
*Answer:* No. The cast `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 was NOT removed in S2. The investigation revealed that the cast hides a real structural mismatch (missing `adminScope` on legacy tokens), but the decision was to keep the cast and add optional chaining plus a new error class as the actual safety net. SAFETY-2 (do not remove the cast) remains in force.

**Q19. [S2 — Issue Details]** What are the three required fields on `AdminTokenPayload`, and which field is missing from legacy admin tokens?
*Answer:* `AdminTokenPayload` requires three fields: `userId`, `role`, and `adminScope`. Legacy admin tokens (estimated at approximately 40% of active admin sessions) only carry `userId` and `role`. The `adminScope` field is absent from these legacy tokens.

**Q20. [S2 — Issue Details]** What runtime behavior was introduced to handle the missing `adminScope` on non-sensitive endpoints?
*Answer:* Optional chaining with a fallback empty string: `token.adminScope ?? ""`. When `adminScope` is absent (legacy tokens), this evaluates to `""`, allowing the request to proceed on non-sensitive endpoints without throwing an error. This prevents immediately 401-ing the estimated 40% of admin sessions using legacy tokens.

**Q21. [S2 — Custom Error]** What is the name and purpose of the custom error class added in S2, and what metadata does it carry?
*Answer:* The class is `AdminTokenValidationError`, which extends `Error`. It is thrown when a request reaches a sensitive endpoint and `adminScope` is missing or empty. It carries metadata: `{ endpoint, tokenAge }`. When thrown, it returns HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }`. It was introduced on the `/admin/users` and `/admin/reports` endpoints.

**Q22. [S2 — Safety Rules]** What is SAFETY-3 and what is the quantitative reason behind it?
*Answer:* SAFETY-3: DO NOT add `adminScope` as a required field on `AdminTokenPayload`. The reason is quantitative: approximately 40% of active admin sessions use legacy tokens that do not carry `adminScope`. Making the field required would immediately invalidate those sessions. Any migration to required `adminScope` must go through a token re-issuance campaign coordinated with the admin team.

**Q23. [S2 — Decisions]** After the S2 investigation, what is the layered defense for the `adminScope` gap — what three mechanisms work together?
*Answer:* Three mechanisms work together: (1) The `castAs<AdminTokenPayload>` cast on line 47 is kept in place (TypeScript compile-time, SAFETY-2). (2) Optional chaining `token.adminScope ?? ""` handles missing `adminScope` gracefully on non-sensitive endpoints at runtime. (3) `AdminTokenValidationError` is thrown on sensitive endpoints (`/admin/users`, `/admin/reports`) when `adminScope` is missing, returning HTTP 403 to prevent unauthorized access.

**Q24. [S3 — Race Condition]** What was the race condition discovered in S3, and what was its observable symptom?
*Answer:* Two concurrent requests arriving within the same millisecond could write and immediately overwrite each other's Redis token cache entries. The observable symptom was that one request would find a cache miss on a token it had just cached, leading to double-validation calls hitting the underlying token store. In edge cases this caused redundant work and latency spikes under concurrent load.

**Q25. [S3 — Fix Decision]** Why was Redis `SET NX EX` chosen over the `async-mutex` library to fix the race condition?
*Answer:* Three reasons: (1) `SET NX EX` is atomic at the Redis level, requiring no application-layer locking. (2) It requires no new Node.js dependency (no new package to manage or audit). (3) `async-mutex` only serializes writes within a single process — it would not protect against the multi-instance deployment scenario where two separate pods race on the same Redis key. `SET NX EX` is safe regardless of how many instances are running.

**Q26. [S3 — Connection Pool]** What are the exact connection pool settings established in S3 and why is the upper limit significant?
*Answer:* `maxConnections=10`, `idleTimeoutMillis=30000`. The upper limit of 10 is significant because staging load tests showed that increasing to 15 connections caused 503 errors under the target load profile. The value of 10 is the tested safe ceiling, not an arbitrary default. SAFETY-4 prohibits increasing this limit without completing a new load test.

**Q27. [S3 — Safety Rules]** What is SAFETY-4 and what evidence is it based on?
*Answer:* SAFETY-4: DO NOT increase `maxConnections` above 10 without completing a load test. It is based on empirical staging evidence: when `maxConnections` was set to 15 during staging load testing, 503 errors appeared under the expected concurrent load. The limit of 10 is the last tested value that did not produce errors.

**Q28. [S3 — Test Infrastructure]** What test infrastructure was introduced in S3 and what problem did it solve?
*Answer:* A `createRedisTestClient()` helper was added in `tests/helpers/` using the `testcontainers` library. It spins up a real Redis container for integration tests. This replaced the previous in-memory Redis mock, which was producing false positives because the mock did not correctly reproduce the atomic `SET NX EX` behavior. The testcontainers approach ensures integration tests reflect real Redis semantics.

**Q29. [S3 — Technical Depth]** How does the `SET NX EX` operation prevent the specific race condition identified in S3?
*Answer:* `SET NX EX` is a single atomic Redis command that sets a key to a value with an expiry, but only if the key does not already exist ("NX" = "Not eXists"). Atomicity means there is no window between checking existence and writing the value. In the race condition scenario, whichever of the two concurrent requests executes `SET NX EX` first wins; the second request's command is a no-op (the key already exists), so it never overwrites the first request's cache entry.

**Q30. [S3 — Integration]** At the end of S3, what was identified as the next testing gap, and what specific error-handling problem was suspected?
*Answer:* The next testing gap was `orderHandler.ts`, which had no tests covering the async `verifyToken` integration. The specific suspected problem was that `orderHandler` might not handle `TokenExpiredError` explicitly — meaning an expired token request on an order endpoint might fall through to a 500 response instead of the correct 401. This was confirmed as a real bug in S4.

---

### T3 — Test Point 3 (Start of Session 7)
Tests: S1 (1), S2 (1), S3 (2), S4 (3), S5 (4), S6 (4)

**Q31. [S1 — Safety Rules]** SAFETY-1 and SAFETY-2 from S1 are still in force across all 6 sessions. What is SAFETY-2, and has anything changed about its status since S1?
*Answer:* SAFETY-2: DO NOT remove the `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47. Its status has not changed — the cast was kept in S2 after investigation. The S2 work added optional chaining and `AdminTokenValidationError` around the cast, but the cast itself remains. SAFETY-2 is still fully in force.

**Q32. [S2 — Decisions]** Which two endpoints were specifically updated in S2 to throw `AdminTokenValidationError` when `adminScope` is missing?
*Answer:* `/admin/users` and `/admin/reports`. These are the "sensitive endpoints" where missing `adminScope` results in an HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }` via `AdminTokenValidationError`. Non-sensitive admin endpoints fall back to the `adminScope ?? ""` empty-string default.

**Q33. [S3 — Connection Pool]** What are the exact Redis connection pool settings from S3, and what is the consequence of exceeding the `maxConnections` limit?
*Answer:* `maxConnections=10`, `idleTimeoutMillis=30000`. Exceeding the limit (specifically: setting `maxConnections=15` was tested in staging) caused 503 errors under the expected concurrent load. SAFETY-4 prohibits raising this ceiling without a new load test.

**Q34. [S3 — Race Condition Fix]** What atomic Redis operation was used to fix the token cache race condition, and what alternative was considered but rejected?
*Answer:* `SET NX EX` (Set if Not eXists with Expiry) was chosen. The rejected alternative was the `async-mutex` Node.js library. `async-mutex` was rejected because it only serializes within a single process and would not protect against multi-pod deployments where two instances race on the same Redis key. `SET NX EX` is atomic at the Redis level regardless of instance count.

**Q35. [S4 — Bug Discovery]** What bug was discovered during S4 test coverage work, and what was its visible symptom in production?
*Answer:* `orderHandler.ts` was not handling `TokenExpiredError` explicitly. When an expired JWT was used on an order endpoint, the error fell through all catch branches and returned HTTP 500 instead of HTTP 401. This would incorrectly trigger server-error alerting and would prevent clients from distinguishing a retryable token expiry from a genuine server failure.

**Q36. [S4 — Fix Pattern]** How was the `TokenExpiredError` gap in `orderHandler.ts` fixed, and what prior work established the pattern?
*Answer:* A dedicated `catch (err)` branch was added that checks `err instanceof TokenExpiredError` and returns `{ status: 401, code: "TOKEN_EXPIRED" }`. This mirrors the pattern established in `authMiddleware.ts` during S1, where `TokenExpiredError` and `JsonWebTokenError` were given separate handling. The S4 fix brings `orderHandler` into conformance with the S1 standard.

**Q37. [S4 — Safety Rules]** What is SAFETY-5 and what incident motivated it?
*Answer:* SAFETY-5: DO NOT mock Redis in `orderHandler` tests. Real Redis container via testcontainers is mandatory. The motivation was a prior incident where a mock-based test produced a false positive in staging — the mock did not reproduce the timing behavior of `SET NX EX`, so a race condition that appeared "fixed" per tests was still present in production. The mock gave false confidence.

**Q38. [S5 — Pipeline Order]** What conflict was discovered about the middleware pipeline order in S5, and what was the resolution?
*Answer:* The conflict: placing `rateLimitMiddleware` after `authMiddleware` meant that requests with deliberately expired or malformed tokens still passed through `authMiddleware` (doing JWT verification work) before hitting the rate limiter. An attacker could flood the server with invalid tokens and drive JWT verification load without consuming their rate limit budget. Resolution: `rateLimitMiddleware` was moved BEFORE `authMiddleware` in `app.ts`. Pipeline order: `rateLimitMiddleware` → `authMiddleware` → route handlers.

**Q39. [S5 — Safety Rules]** What is SAFETY-6 and what specific attack does it prevent?
*Answer:* SAFETY-6: DO NOT revert the pipeline order (rate limit must come before auth). It prevents a token-flooding attack: if rate limiting ran after auth, an attacker could send a high volume of requests with invalid or expired tokens, each one causing JWT verification work in `authMiddleware`, without being rate-limited (since rate limiting would only apply after the auth step). The current order ensures all requests, including unauthenticated ones, are rate-limited before any verification work occurs.

**Q40. [S5 — Configuration]** What are the rate limit parameters (algorithm, limit, time window, backing store) and which endpoints are exempt?
*Answer:* Algorithm: sliding window. Limit: 100 requests per minute per IP. Backing store: Redis sorted sets with a Lua script for atomic TOCTOU-safe counting (`ZADD` / `ZREMRANGEBYSCORE` / `ZCARD`). Exempt endpoints: `GET /health` and `GET /metrics`. These are whitelisted because load balancers and Prometheus need unrestricted access to them.

**Q41. [S5 — Work State]** What two items were carried over from S5 as next actions into S6?
*Answer:* (1) Profile `verifyToken` performance under realistic load to determine if an in-memory cache layer is needed to reduce Redis round-trips. (2) Write automated tests for `rateLimitMiddleware` (the S5 work was validated only by manual testing; automated test coverage was not completed in S5).

**Q42. [S6 — Cache Key]** What format is used for the LRU cache key for verified tokens, and what is the specific security reason for this choice?
*Answer:* The cache key is `SHA256(tokenString)` — the SHA256 hash of the raw JWT string. The security reason: storing the raw JWT as a cache key would mean the cache holds valid bearer credentials, creating a cache poisoning risk if the cache is ever serialized, logged, or inspected. An opaque SHA256 hash reveals nothing exploitable even if the cache is exposed. This is a security requirement, not a performance choice.

**Q43. [S6 — Admin Token Exclusion]** Which tokens are excluded from the LRU cache and why?
*Answer:* Tokens with a non-empty `adminScope` are excluded from the LRU cache entirely. Admin tokens must always hit Redis so that real-time revocation takes effect immediately — for example, when an admin account is compromised and its tokens are revoked in Redis, the revocation must take effect on the next request, not after a 60-second LRU TTL expires. The LRU cache check is skipped when `token.adminScope` is non-empty (SAFETY-7).

**Q44. [S6 — LRU Version]** Why was `lru-cache` v10 used instead of v7?
*Answer:* `lru-cache` v7 has a known memory leak in async callback paths. Because `verifyToken` is async and the cache's `fetchMethod` uses async callbacks, using v7 would leak memory proportional to the cache miss rate. v10 fixes this bug. The dependency is pinned to `^10.0.0` in `package.json` to prevent accidental downgrade.

**Q45. [S6 — Redis TTL]** What are the Redis TTL values for access tokens and refresh tokens, and how are they defined in the codebase?
*Answer:* Access tokens: 900 seconds (15 minutes). Refresh tokens: 604800 seconds (7 days). They are defined as named constants in `tokenCacheService.ts`: `ACCESS_TOKEN_TTL_SECONDS = 900` and `REFRESH_TOKEN_TTL_SECONDS = 604800`. Named constants were used explicitly to prevent magic numbers from proliferating through the codebase.
