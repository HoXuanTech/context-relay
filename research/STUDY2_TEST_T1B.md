# Test Results: T1B (Handoff, Test Point 1)
Context used: Handoff1 from STUDY2_DATA_B.md
Questions: T1 (Q1–Q15)
Agent: Group B (handoff)

---

**Q1** What is the safety rule regarding JWT_SECRET rotation, and what is the specific reason it must not be changed?
**Answer:** SAFETY-1: DO NOT change the JWT_SECRET rotation logic. The specific reason is that the rotation is tied to a 24-hour rolling window owned and managed by the ops team. Changing it requires a coordinated deployment window with ops and would force re-issuance of all currently active sessions. The Handoff1 phrases it as "requires coordinated ops deploy + session re-issuance."
**Confidence:** High

---

**Q2** What is the safety rule on `adminHandler.ts` line 47, and why must it be preserved?
**Answer:** SAFETY-2: DO NOT remove the `castAs<AdminTokenPayload>` on `adminHandler.ts` line 47. It must be preserved because it is required to handle legacy admin tokens that predate the current schema migration. Removing it causes runtime type errors on admin sessions issued before the schema migration.
**Confidence:** High

---

**Q3** How many safety rules were established in S1, and what are their subjects?
**Answer:** Two safety rules were established in S1. SAFETY-1 covers JWT_SECRET rotation logic (ops-owned 24h rolling window, must not be changed). SAFETY-2 covers the `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47 (required for legacy admin tokens pre-schema migration, must not be removed).
**Confidence:** High

---

**Q4** If a developer asks whether they can refactor the secrets manager integration as part of the JWT refactor, what is the correct answer based on S1 decisions?
**Answer:** No. SAFETY-1 explicitly prohibits any changes to the JWT_SECRET rotation logic, which includes the secrets manager integration. The Handoff1 notes this requires "coordinated ops deploy + session re-issuance" and is explicitly deferred. Any refactor touching that area violates SAFETY-1.
**Confidence:** High

---

**Q5** What are the consequences of violating SAFETY-2 (removing the adminHandler cast)?
**Answer:** Removing `castAs<AdminTokenPayload>` from `adminHandler.ts` line 47 will cause runtime type errors. The Handoff1 states "removal causes runtime type errors" for legacy admin tokens pre-schema migration — i.e., any admin session issued before the schema migration would break at runtime.
**Confidence:** High

---

**Q6** Why was `jwt.verify` wrapped in a `Promise` constructor rather than using the callback overload?
**Answer:** The Handoff1 states: using `new Promise()` constructor was chosen for "cleaner try-catch boundary, clean stack traces vs. `util.promisify` shim." The callback overload requires a `util.promisify` shim to integrate with async/await, which adds indirection and produces less clean stack traces on rejection.
**Confidence:** High

---

**Q7** Why were `TokenExpiredError` and `JsonWebTokenError` given separate handling rather than being caught by a single generic JWT error handler?
**Answer:** The Handoff1 states that separate catch branches in `authMiddleware.ts` provide "deterministic client retry logic (401 not 500)." Previously all JWT errors fell through to a generic 500. With separate handling, `TokenExpiredError` returns 401 with `TOKEN_EXPIRED` and `JsonWebTokenError` returns 401 with `INVALID_TOKEN`, allowing clients to distinguish a recoverable expiry from an invalid signature.
**Confidence:** High

---

**Q8** What was the async vs. synchronous architecture decision made for `verifyToken`, and what does this enable for the future?
**Answer:** The Handoff1 states the current goal is to "Refactor `verifyToken` from sync to async to enable future Redis token invalidation without blocking the event loop." The specific decision was to wrap `jwt.verify` in a `new Promise()` constructor. This enables future Redis token invalidation because Redis calls are inherently async and a synchronous `verifyToken` would block the event loop.
**Confidence:** High

---

**Q9** Why was the JWT refactor scoped only to call-site changes in the 5 route handlers, rather than deeper handler logic changes?
**Answer:** The Handoff1 describes the completed work as updating all 5 handlers with call-site changes only: "`verifyToken(token)` → `await verifyToken(token)` + try-catch." Deeper logic issues, such as the `adminHandler.ts` cast mystery, were flagged as in-progress or next actions rather than addressed in S1. The scope was the async migration itself.
**Confidence:** High

---

**Q10** Where was the decision made to handle `TokenExpiredError` differently from other JWT errors, and what HTTP status does each return?
**Answer:** The decision was made in `authMiddleware.ts` during S1. Per Handoff1: "authMiddleware.ts error differentiation complete: `TOKEN_EXPIRED` → 401, `INVALID_TOKEN` → 401." Both return HTTP 401, but with different error codes: `TokenExpiredError` returns `{ code: "TOKEN_EXPIRED" }` and `JsonWebTokenError` returns `{ code: "INVALID_TOKEN" }`.
**Confidence:** High

---

**Q11** Which 5 route handlers were updated in S1 to use the async `verifyToken`?
**Answer:** The 5 handlers updated are: `userHandler`, `orderHandler`, `productHandler`, `adminHandler`, and `auditHandler`. Per Handoff1: "Async `verifyToken` integrated in all 5 handlers: `userHandler`, `orderHandler`, `productHandler`, `adminHandler`, `auditHandler`."
**Confidence:** High

---

**Q12** What specific file was modified to add the two new error type handlers, and what is the current state of that file?
**Answer:** `authMiddleware.ts` was modified. Per Handoff1, the error differentiation is complete: `TOKEN_EXPIRED` → 401 and `INVALID_TOKEN` → 401. This is listed under "Completed Detail," indicating the two separate catch branches for `TokenExpiredError` and `JsonWebTokenError` are fully implemented.
**Confidence:** High

---

**Q13** What is the exact next action planned at the end of S1?
**Answer:** Per Handoff1 under "Next Actions": "Investigate `adminHandler.ts` line 47 cast: identify what fields legacy tokens carry vs. current schema; determine if runtime guard needed."
**Confidence:** High

---

**Q14** What is the current understanding of the `adminHandler.ts` line 47 cast at the end of S1 — what is known and what is unknown?
**Answer:** What is known: the cast `castAs<AdminTokenPayload>` on line 47 is "load-bearing" (SAFETY-2 explicitly prohibits removing it). What is unknown: the exact reason the cast is needed has not been fully investigated. The Handoff1 states it was "flagged as load-bearing during call-site audit" and the "full reason for cast deferred to S2 investigation." A "structural mismatch" is suspected but not yet confirmed or understood.
**Confidence:** High

---

**Q15** What branch is the JWT async refactor work on, and what was the branch state at the end of S1?
**Answer:** The Handoff1 does not explicitly name the branch. It describes the session as "S1: JWT Async Refactor" and lists completed work (async verifyToken in all 5 handlers, authMiddleware.ts error differentiation) and in-progress items (adminHandler.ts line 47 cast investigation). The branch name `feat/jwt-async-refactor` is not mentioned in Handoff1 itself.
**Confidence:** Medium (branch name not present in Handoff1; completed/in-progress state is clear)
