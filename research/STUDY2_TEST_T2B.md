# Test Results: T2B (Handoff, Test Point 2)
Context used: Handoff3 from STUDY2_DATA_B.md
Questions: T2 (Q16–Q30)
Agent: Group B (handoff)

---

**Q16** Both SAFETY-1 and SAFETY-2 from S1 are still in force. What does SAFETY-1 protect and who owns that system?
**Answer:** SAFETY-1 protects the JWT_SECRET rotation logic. It is owned by the ops team, which manages a 24-hour rolling window rotation. No changes are permitted without a coordinated deploy and session re-issuance.
**Confidence:** High

---

**Q17** The async `verifyToken` refactor was completed in S1 across 5 handlers. What was the explicit error-handling decision made in `authMiddleware.ts` that established a pattern now expected to be followed in all handlers?
**Answer:** Handoff3 notes that async `verifyToken` was integrated in all 5 handlers and that `authMiddleware.ts` error differentiation was complete: `TOKEN_EXPIRED` → 401, `INVALID_TOKEN` → 401. However, Handoff3 does not explicitly describe this as "a pattern expected to be followed in all handlers." It records the split error handling as a completed item from S1 work.
**Confidence:** Medium

---

**Q18** The `adminHandler.ts` cast investigation was the next action at the end of S1. Was the cast removed during S2?
**Answer:** No. Handoff3 carries SAFETY-2 forward explicitly: "DO NOT remove `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47 — required for legacy admin tokens." The cast was not removed.
**Confidence:** High

---

**Q19** What are the three required fields on `AdminTokenPayload`, and which field is missing from legacy admin tokens?
**Answer:** Handoff3 does not explicitly list the three required fields of `AdminTokenPayload`. It does state that ~40% of active admin sessions lack `adminScope` and that SAFETY-3 prohibits adding `adminScope` as a required field, implying `adminScope` is the missing field. The other two fields (`userId`, `role`) are not named in Handoff3.
**Confidence:** Low

---

**Q20** What runtime behavior was introduced to handle the missing `adminScope` on non-sensitive endpoints?
**Answer:** Handoff3 does not mention optional chaining or a `token.adminScope ?? ""` fallback. It records the `AdminTokenValidationError` class and SAFETY-3, but does not describe the non-sensitive endpoint fallback behavior in this handoff.
**Confidence:** Cannot answer

---

**Q21** What is the name and purpose of the custom error class added in S2, and what metadata does it carry?
**Answer:** Handoff3 mentions `AdminTokenValidationError` was created (it extends `Error` and carries `{ endpoint, tokenAge }` metadata) and is used on sensitive endpoints. However, Handoff3 itself only records the class name and that it is integrated on sensitive admin endpoints. The metadata fields (`endpoint`, `tokenAge`) and the HTTP 403 / `ADMIN_SCOPE_REQUIRED` response are not stated in Handoff3 directly — only that the class exists and that tests for it are still not written.
**Confidence:** Low

---

**Q22** What is SAFETY-3 and what is the quantitative reason behind it?
**Answer:** SAFETY-3: DO NOT add `adminScope` as a required field on `AdminTokenPayload`. The quantitative reason is that approximately 40% of active admin sessions use legacy tokens that do not carry `adminScope`. Making it required would immediately invalidate those sessions; a token re-issuance campaign with the admin team is required before this can change.
**Confidence:** High

---

**Q23** After the S2 investigation, what is the layered defense for the `adminScope` gap — what three mechanisms work together?
**Answer:** Handoff3 does not describe all three layers as a combined defense. It records: (1) SAFETY-2 keeping the cast in place, and (2) `AdminTokenValidationError` on sensitive endpoints. The optional chaining fallback (`token.adminScope ?? ""`) for non-sensitive endpoints is not mentioned in Handoff3. A complete three-mechanism answer cannot be constructed from Handoff3 alone.
**Confidence:** Low

---

**Q24** What was the race condition discovered in S3, and what was its observable symptom?
**Answer:** Two concurrent requests arriving within the same millisecond could write and immediately overwrite each other's Redis token cache entries. The symptom was that one request would find a cache miss on a token it had just cached, leading to double-validation calls hitting the token store. This was reproduced in staging under concurrent load (two pods, same-millisecond requests).
**Confidence:** High

---

**Q25** Why was Redis `SET NX EX` chosen over the `async-mutex` library to fix the race condition?
**Answer:** Three reasons: (1) `SET NX EX` is atomic at the Redis level with no application-layer locking needed. (2) It requires no new Node.js dependency. (3) `async-mutex` only serializes writes in-process and would not protect against multi-pod deployments where two pods race on the same Redis key. `SET NX EX` is safe regardless of instance count.
**Confidence:** High

---

**Q26** What are the exact connection pool settings established in S3 and why is the upper limit significant?
**Answer:** `maxConnections=10`, `idleTimeoutMillis=30000`. The upper limit of 10 is significant because staging load tests showed that setting `maxConnections=15` caused 503 errors under the target load profile. 10 is the tested safe ceiling. SAFETY-4 prohibits increasing this without a load test.
**Confidence:** High

---

**Q27** What is SAFETY-4 and what evidence is it based on?
**Answer:** SAFETY-4: DO NOT increase `maxConnections` above 10 without a load test. It is based on empirical staging evidence: 503 errors were observed when `maxConnections` was set to 15 during a staging load test. The value of 10 is the last tested value that did not produce errors.
**Confidence:** High

---

**Q28** What test infrastructure was introduced in S3 and what problem did it solve?
**Answer:** A `createRedisTestClient()` helper was added in `tests/helpers/` using `testcontainers` to spin up a real Redis container for integration tests. This replaced an in-memory mock that was producing false positives — the mock did not correctly reproduce the atomic `SET NX EX` behavior, causing tests to pass while the race condition remained exploitable.
**Confidence:** High

---

**Q29** How does the `SET NX EX` operation prevent the specific race condition identified in S3?
**Answer:** Handoff3 records the decision to use `SET NX EX` and confirms the race condition integration tests are passing, but does not explain the atomic mechanics (NX = "not exists" semantics, no window between check and write). The "why it works" explanation is not present in Handoff3.
**Confidence:** Low

---

**Q30** At the end of S3, what was identified as the next testing gap, and what specific error-handling problem was suspected?
**Answer:** The next testing gap identified was `orderHandler.ts`, which had no async `verifyToken` tests. The suspected problem was that `TokenExpiredError` handling was missing — a suspected gap in the catch branch for expired tokens.
**Confidence:** High
