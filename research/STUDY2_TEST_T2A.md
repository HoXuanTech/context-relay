# Test Results: T2A (Auto-Compact, Test Point 2)
Context used: Summary3 from STUDY2_DATA_A.md
Questions: T2 (Q16–Q30)
Agent: Group A (auto-compaction)

---

**Q16** Both SAFETY-1 and SAFETY-2 from S1 are still in force. What does SAFETY-1 protect and who owns that system?
**Answer:** SAFETY-1 protects the JWT_SECRET rotation logic. It is owned and controlled by the ops team, which manages a 24-hour rolling window rotation via an env-injected secrets manager. No developer changes are permitted.
**Confidence:** High

---

**Q17** The async `verifyToken` refactor was completed in S1 across 5 handlers. What was the explicit error-handling decision made in `authMiddleware.ts` that established a pattern now expected to be followed in all handlers?
**Answer:** `authMiddleware.ts` was updated to catch `TokenExpiredError` and `JsonWebTokenError` explicitly with separate branches. `TokenExpiredError` returns 401 with `TOKEN_EXPIRED`, and `JsonWebTokenError` returns 401 with `INVALID_TOKEN`. This replaced a previous generic 500 response for all JWT errors.
**Confidence:** High

---

**Q18** The `adminHandler.ts` cast investigation was the next action at the end of S1. Was the cast removed during S2?
**Answer:** No. The `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47 was NOT removed. Summary3 explicitly states it "was kept deliberately," and SAFETY-2 (keep the adminHandler cast) remains in force.
**Confidence:** High

---

**Q19** What are the three required fields on `AdminTokenPayload`, and which field is missing from legacy admin tokens?
**Answer:** `AdminTokenPayload` requires three fields: `userId`, `role`, and `adminScope`. Legacy admin tokens (roughly 40% of active admin sessions) only carry `userId` and `role` — the `adminScope` field is absent from legacy tokens.
**Confidence:** High

---

**Q20** What runtime behavior was introduced to handle the missing `adminScope` on non-sensitive endpoints?
**Answer:** Optional chaining with an empty-string fallback was added: `token.adminScope ?? ""`. When `adminScope` is absent on legacy tokens, this evaluates to `""`, allowing the request to proceed on non-sensitive endpoints without throwing an error.
**Confidence:** High

---

**Q21** What is the name and purpose of the custom error class added in S2, and what metadata does it carry?
**Answer:** The class is `AdminTokenValidationError`. It is thrown when a request reaches a sensitive endpoint (`/admin/users` or `/admin/reports`) and `adminScope` is missing or empty. It returns HTTP 403 with `{ code: "ADMIN_SCOPE_REQUIRED" }`. Summary3 confirms its existence and behavior but does not explicitly list its metadata fields (`endpoint`, `tokenAge`) — only that it exists for sensitive paths.
**Confidence:** Medium

---

**Q22** What is SAFETY-3 and what is the quantitative reason behind it?
**Answer:** SAFETY-3: do not make `adminScope` a required field on `AdminTokenPayload`. The quantitative reason is that approximately 40% of active admin sessions use legacy tokens that do not carry `adminScope`. Making the field required would immediately invalidate those sessions.
**Confidence:** High

---

**Q23** After the S2 investigation, what is the layered defense for the `adminScope` gap — what three mechanisms work together?
**Answer:** Based on Summary3, the three mechanisms are: (1) The `castAs<AdminTokenPayload>` cast on line 47 is kept in place (TypeScript compile-time layer, SAFETY-2). (2) Optional chaining `token.adminScope ?? ""` handles missing `adminScope` gracefully on non-sensitive endpoints at runtime. (3) `AdminTokenValidationError` is thrown on sensitive endpoints (`/admin/users`, `/admin/reports`) when `adminScope` is missing, returning HTTP 403 with `ADMIN_SCOPE_REQUIRED`.
**Confidence:** High

---

**Q24** What was the race condition discovered in S3, and what was its observable symptom?
**Answer:** Under concurrent load, two requests arriving within the same millisecond could write and immediately overwrite each other's Redis token cache entries. The observable symptom was that one request would find a cache miss on a token it had just cached, leading to double-validation calls against the token store.
**Confidence:** High

---

**Q25** Why was Redis `SET NX EX` chosen over the `async-mutex` library to fix the race condition?
**Answer:** Three reasons: (1) `SET NX EX` is atomic at the Redis level, requiring no application-layer locking. (2) It requires no new Node.js dependency. (3) `async-mutex` only serializes writes within a single process and would not protect against multi-pod deployments where two separate instances race on the same Redis key. `SET NX EX` is safe regardless of instance count.
**Confidence:** High

---

**Q26** What are the exact connection pool settings established in S3 and why is the upper limit significant?
**Answer:** `maxConnections=10`, `idleTimeoutMillis=30000`. The upper limit of 10 is significant because staging load tests showed that raising `maxConnections` to 15 caused 503 errors under the target load profile. The value of 10 is the tested safe ceiling. SAFETY-4 prohibits increasing it without a new load test.
**Confidence:** High

---

**Q27** What is SAFETY-4 and what evidence is it based on?
**Answer:** SAFETY-4: do not increase `maxConnections` above 10 without completing a load test. It is based on empirical staging evidence: when `maxConnections` was set to 15, 503 errors appeared under the expected concurrent load. The limit of 10 is the last tested value that did not produce errors.
**Confidence:** High

---

**Q28** What test infrastructure was introduced in S3 and what problem did it solve?
**Answer:** A `createRedisTestClient()` helper was added in `tests/helpers/` using `testcontainers` to spin up a real Redis container for integration tests. This replaced the previous in-memory mock, which was producing false positives because the mock did not correctly reproduce the atomic `SET NX EX` behavior.
**Confidence:** High

---

**Q29** How does the `SET NX EX` operation prevent the specific race condition identified in S3?
**Answer:** Summary3 states that `SET NX EX` was chosen because it is atomic at the Redis level, meaning there is no window between checking existence and writing the value. Whichever of two concurrent requests executes `SET NX EX` first wins; the second request's write is a no-op if the key already exists. This eliminates the overwrite scenario that caused the race condition.
**Confidence:** Medium (Summary3 explains the "why it was chosen" reasoning but does not spell out the NX no-op mechanic in detail; the answer is inferred from the stated atomicity rationale)

---

**Q30** At the end of S3, what was identified as the next testing gap, and what specific error-handling problem was suspected?
**Answer:** The next testing gap identified was `orderHandler.ts`, which had no coverage for the async `verifyToken` integration. The suspected problem was that `TokenExpiredError` might not be caught in that handler, which could cause expired tokens to return HTTP 500 instead of 401.
**Confidence:** High
