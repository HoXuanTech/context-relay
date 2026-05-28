# Study 2 Data — Group B: Handoff Chain

## Handoff1 (T1 test context — after S1)

# Handoff - api-gateway - S1: JWT Async Refactor

## Current Goal
Refactor `verifyToken` from sync to async to enable future Redis token invalidation without blocking the event loop.

## Key Decisions
- `jwt.verify` wrapped in `new Promise()` constructor → cleaner try-catch boundary, clean stack traces vs. `util.promisify` shim
- Separate `TokenExpiredError` / `JsonWebTokenError` catch branches in `authMiddleware.ts` → deterministic client retry logic (401 not 500)
- No changes to JWT_SECRET rotation → deferred; requires coordinated ops deploy

## In Progress
- `adminHandler.ts` line 47 `castAs<AdminTokenPayload>` — load-bearing but reason not fully understood; structural mismatch suspected

## Completed Detail
- Async `verifyToken` integrated in all 5 handlers: `userHandler`, `orderHandler`, `productHandler`, `adminHandler`, `auditHandler`
- `authMiddleware.ts` error differentiation complete: `TOKEN_EXPIRED` → 401, `INVALID_TOKEN` → 401

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens pre-schema migration; removal causes runtime type errors

## Last Actions
- Wrapped `jwt.verify` in Promise constructor in `verifyToken`
- Updated all 5 handler call sites: `verifyToken(token)` → `await verifyToken(token)` + try-catch
- Added split error handling in `authMiddleware.ts`

## Next Actions
- Investigate `adminHandler.ts` line 47 cast: identify what fields legacy tokens carry vs. current schema; determine if runtime guard needed

## Recon Notes
- Cast on line 47 flagged as load-bearing during call-site audit of `adminHandler.ts`
- Full reason for cast deferred to S2 investigation

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---

## Handoff2 (after S2)

# Handoff - api-gateway - S2: AdminHandler Cast Investigation

## Current Goal
Resolve the `adminHandler.ts` line 47 cast mystery; implement safe handling for the legacy token `adminScope` gap.

## Key Decisions
- Keep `castAs<AdminTokenPayload>` — removing forces compiler to reject legacy shapes at compile time; optional chaining is the real safety net
- `token.adminScope ?? ""` fallback on non-sensitive endpoints → legacy tokens (~40% of active admin sessions) continue working
- `AdminTokenValidationError` on sensitive endpoints (`/admin/users`, `/admin/reports`) → HTTP 403 `ADMIN_SCOPE_REQUIRED`

## In Progress
- Tests for `AdminTokenValidationError` behavior on `/admin/users` and `/admin/reports` — not yet written
- Redis race condition investigation flagged (staging surfaced concurrent cache overwrite issue)

## Completed Detail
- `AdminTokenValidationError` class created: extends `Error`, carries `{ endpoint, tokenAge }` metadata
- Optional chaining `token.adminScope ?? ""` deployed to dev
- Both sensitive endpoints updated to throw on missing `adminScope`
- Line 47 cast structural mismatch fully understood: `adminScope` absent from pre-migration tokens

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens; optional chaining is the safety net, not cast removal
- SAFETY-3: DO NOT add `adminScope` as required field on `AdminTokenPayload` — ~40% of active admin sessions use legacy tokens without it; requires token re-issuance campaign with admin team

## Last Actions
- Identified `adminScope` as missing field on ~40% of admin tokens
- Implemented `token.adminScope ?? ""` at access sites
- Created and integrated `AdminTokenValidationError` on sensitive admin endpoints

## Next Actions
- Write tests for `AdminTokenValidationError` on `/admin/users` and `/admin/reports`
- Investigate Redis token cache race condition surfaced in staging last week

## Recon Notes
- Legacy token gap discovered by diffing `AdminTokenPayload` interface fields against token payloads from production session sample
- ~40% estimate from ops token issuance records pre-schema migration date

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---

## Handoff3 (T2 test context — after S3)

# Handoff - api-gateway - S3: Redis Race Condition Fix

## Current Goal
Fix Redis token cache race condition where concurrent requests within same millisecond overwrite each other's cache entries.

## Key Decisions
- Redis `SET NX EX` over `async-mutex` → atomic at Redis level, no new dependency, safe across multi-pod deployments
- Connection pool: `maxConnections=10`, `idleTimeoutMillis=30000` → 15 caused 503s in staging load test; 10 is tested ceiling
- `testcontainers` for integration test Redis → replaced in-memory mock that gave false positives on `SET NX EX` atomicity

## In Progress
- Tests for `AdminTokenValidationError` on `/admin/users` and `/admin/reports` — still not written (carried from S2)
- `orderHandler.ts` has no async `verifyToken` tests; `TokenExpiredError` handling suspected gap

## Completed Detail
- `SET NX EX` fix deployed in `tokenCacheService.ts`
- Redis connection pool configured in `redisClient.ts`
- `createRedisTestClient()` helper added in `tests/helpers/` via testcontainers
- Race condition integration tests passing

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens
- SAFETY-3: DO NOT add `adminScope` as required field on `AdminTokenPayload` — ~40% active admin sessions lack it; needs re-issuance campaign
- SAFETY-4: DO NOT increase `maxConnections` above 10 without a load test — staging showed 503s at 15 connections under target load

## Last Actions
- Evaluated `async-mutex` vs. `SET NX EX`; chose `SET NX EX` for multi-instance safety
- Set connection pool limits in `redisClient.ts`
- Added `createRedisTestClient()` using testcontainers; confirmed atomic semantics reproduced correctly

## Next Actions
- Add async path tests for `orderHandler.ts`; confirm `TokenExpiredError` handling (suspected missing catch branch)

## Recon Notes
- Race condition reproduced in staging under concurrent load test (two pods, same-millisecond requests)
- 503 errors at `maxConnections=15` observed in staging load profile; not reproduced at 10
- In-memory mock false positive discovered when atomic `SET NX EX` behavior was manually verified against mock behavior

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---

## Handoff4 (after S4)

# Handoff - api-gateway - S4: Test Coverage

## Current Goal
Add comprehensive async-path test coverage for `orderHandler.ts`; discovered and fixed a real `TokenExpiredError` bug in the process.

## Key Decisions
- Explicit `TokenExpiredError` catch in `orderHandler` → mirrors `authMiddleware.ts` S1 pattern; expired tokens now return 401 not 500
- Shared `jest.config.ts` globalSetup for Redis testcontainer → eliminates port-conflict flakiness from per-file container spin-up
- 6 test cases for `orderHandler`: valid, expired, invalid sig, missing header, cache hit, Redis unavailable fallback

## In Progress
- Tests for `AdminTokenValidationError` on `/admin/users` and `/admin/reports` — still not written (carried from S2)
- Rate limiting middleware — not yet started; requirements defined

## Completed Detail
- `TokenExpiredError` bug fixed in `orderHandler.ts` — was returning 500; now returns 401 `TOKEN_EXPIRED`
- All 6 `orderHandler` test cases green against real Redis container
- `jest.config.ts` shared Redis testcontainer setup complete and merged to branch

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens
- SAFETY-3: DO NOT add `adminScope` as required field on `AdminTokenPayload` — ~40% active admin sessions lack it
- SAFETY-4: DO NOT increase `maxConnections` above 10 without a load test — staging showed 503s at 15
- SAFETY-5: DO NOT mock Redis in `orderHandler` tests — prior mock gave false positive in staging; real Redis via testcontainers is mandatory

## Last Actions
- Discovered `TokenExpiredError` not caught in `orderHandler`; confirmed 500 response on expired token
- Added explicit `err instanceof TokenExpiredError` catch branch returning 401 `TOKEN_EXPIRED`
- Configured shared Redis testcontainer in `jest.config.ts`; all 6 tests green

## Next Actions
- Implement rate limiting middleware: sliding window, 100 req/min per IP, Redis sorted sets
- Decide pipeline position of rate limiter relative to `authMiddleware`

## Recon Notes
- `TokenExpiredError` gap confirmed by writing the expired-token test case and watching it return 500
- Port-conflict flakiness in CI traced to multiple test files each spinning up independent Redis containers

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---

## Handoff5 (after S5)

# Handoff - api-gateway - S5: Rate Limiting Middleware

## Current Goal
Implement `rateLimitMiddleware.ts` using sliding window algorithm and determine correct pipeline order relative to `authMiddleware`.

## Key Decisions
- Sliding window 100 req/min per IP via Redis `ZADD`/`ZREMRANGEBYSCORE`/`ZCARD` + Lua script for atomic TOCTOU-safe count
- `rateLimitMiddleware` BEFORE `authMiddleware` in pipeline → prevents token-flooding attack (invalid tokens drive JWT work without consuming rate limit budget)
- Whitelist `GET /health` and `GET /metrics` → load balancers and Prometheus need unrestricted access

## In Progress
- Automated tests for `rateLimitMiddleware` — manual testing done; automated not yet written
- `verifyToken` performance profiling — suspected bottleneck; in-memory cache layer not yet implemented

## Completed Detail
- `rateLimitMiddleware.ts` complete with Lua script
- Pipeline order updated in `app.ts`: `rateLimitMiddleware` → `authMiddleware` → route handlers
- `/health` and `/metrics` whitelisted in `rateLimitMiddleware.ts`
- Tests for `AdminTokenValidationError` still not written (carried from S2/S3/S4)

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens
- SAFETY-3: DO NOT add `adminScope` as required field on `AdminTokenPayload` — ~40% active admin sessions lack it
- SAFETY-4: DO NOT increase `maxConnections` above 10 without a load test — staging showed 503s at 15
- SAFETY-5: DO NOT mock Redis in `orderHandler` tests — real Redis via testcontainers is mandatory
- SAFETY-6: DO NOT revert pipeline order (rate limit before auth) — reverting reopens token-flooding attack vector

## Last Actions
- Identified token-flooding vulnerability with rate-limit-after-auth ordering via manual test
- Moved `rateLimitMiddleware` before `authMiddleware` in `app.ts`
- Added path whitelist for `/health` and `/metrics`

## Next Actions
- Profile `verifyToken` under realistic load; determine if in-memory LRU cache needed to reduce Redis round-trips
- Write automated tests for `rateLimitMiddleware` (use same Redis testcontainer setup from S4)

## Recon Notes
- Token-flooding attack vector discovered by testing: flooded server with expired tokens, confirmed JWT verification work occurred before rate limit was checked
- Whitelist requirement surfaced by load balancer team during code review of `rateLimitMiddleware.ts` draft

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---

## Handoff6 (T3 test context — after S6)

# Handoff - api-gateway - S6: Performance + LRU Cache

## Current Goal
Profile `verifyToken` bottleneck and add in-memory LRU cache layer to reduce Redis round-trips under load.

## Key Decisions
- Cache key = `SHA256(tokenString)` NOT raw token → security requirement; raw JWT in cache = bearer credentials at rest; hash is non-exploitable
- LRU: max 1000 entries, TTL 60s → avg 12ms / P99 45ms profiled; 60s TTL short enough for eventual revocation without active invalidation
- `lru-cache` v10, NOT v7 → v7 has known memory leak in async callback paths; `verifyToken` uses async fetchMethod, so leak is proportional to cache miss rate
- Redis TTL constants: `ACCESS_TOKEN_TTL_SECONDS=900`, `REFRESH_TOKEN_TTL_SECONDS=604800` in `tokenCacheService.ts` → no magic numbers

## In Progress
- k6 load test targeting P99 < 10ms for `verifyToken` with cache warm — not yet run
- Automated tests for admin token LRU bypass — manually verified only
- Automated tests for `rateLimitMiddleware` — still not written (carried from S5)
- Tests for `AdminTokenValidationError` — still not written (carried from S2)

## Completed Detail
- LRU cache integrated in `verifyToken`; admin token bypass implemented
- SHA256 key generation in `tokenCacheUtils.ts`
- Redis TTL named constants defined in `tokenCacheService.ts`
- `lru-cache` pinned to `^10.0.0` in `package.json`

## Safety Rules
- SAFETY-1: DO NOT change JWT_SECRET rotation logic — ops-owned 24h rolling window; requires coordinated deploy + session re-issuance
- SAFETY-2: DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens
- SAFETY-3: DO NOT add `adminScope` as required field on `AdminTokenPayload` — ~40% active admin sessions lack it
- SAFETY-4: DO NOT increase `maxConnections` above 10 without a load test — staging showed 503s at 15
- SAFETY-5: DO NOT mock Redis in `orderHandler` tests — real Redis via testcontainers is mandatory
- SAFETY-6: DO NOT revert pipeline order (rate limit before auth) — reopens token-flooding attack vector
- SAFETY-7: DO NOT cache tokens with non-empty `adminScope` in LRU cache — admin tokens must always hit Redis for real-time revocation to take effect immediately

## Last Actions
- Profiled `verifyToken`: avg 12ms, P99 45ms — confirmed bottleneck
- Implemented LRU cache with SHA256 key and admin bypass in `verifyToken`
- Pinned `lru-cache` to v10 after discovering v7 memory leak in async paths

## Next Actions
- Run k6 load test: verify P99 < 10ms for `verifyToken` with cache warm
- Write automated tests covering admin token LRU bypass (SAFETY-7 compliance)
- Write automated tests for `rateLimitMiddleware` (Redis testcontainer setup available from S4)

## Recon Notes
- v7 memory leak found via GitHub issue search during `lru-cache` version evaluation
- P99 45ms baseline established by k6 profiling run against staging before cache implementation
- Admin token bypass requirement derived from SAFETY-7 threat model: compromised admin account needs immediate revocation, not eventual

## Background
→ read research/STUDY2_CONTENT.md for full session scripts

---
Note: Handoff1 = T1 test context, Handoff3 = T2 test context, Handoff6 = T3 test context
