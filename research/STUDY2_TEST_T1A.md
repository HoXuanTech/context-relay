# Test Results: T1A (Auto-Compact, Test Point 1)
Context used: Summary1 from STUDY2_DATA_A.md
Questions: T1 (Q1–Q15)
Agent: Group A (auto-compaction)

---

**Q1** What is the safety rule regarding JWT_SECRET rotation, and what is the specific reason it must not be changed?
**Answer:** SAFETY-1 states: do not change the JWT_SECRET rotation logic. The specific reason is that the ops team manages a 24-hour rolling window that rotates at midnight UTC via an env-injected secrets manager. Touching this logic requires a coordinated deploy window with ops and re-issuance of all active sessions. It is not a developer-controlled parameter.
**Confidence:** High

---

**Q2** What is the safety rule on `adminHandler.ts` line 47, and why must it be preserved?
**Answer:** SAFETY-2 states: do not remove the `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47. It must be preserved because it is needed to handle legacy admin tokens issued before the current schema — removing it causes runtime type errors for those sessions.
**Confidence:** High

---

**Q3** How many safety rules were established in S1, and what are their subjects?
**Answer:** Two safety rules were established. SAFETY-1 covers the JWT_SECRET rotation logic (ops-controlled 24h rolling window, must not be changed). SAFETY-2 covers the `castAs<AdminTokenPayload>` cast on `adminHandler.ts` line 47 (must not be removed; required for legacy admin token compatibility).
**Confidence:** High

---

**Q4** If a developer asks whether they can refactor the secrets manager integration as part of the JWT refactor, what is the correct answer based on S1 decisions?
**Answer:** No. SAFETY-1 explicitly prohibits any changes to the JWT_SECRET rotation logic, which includes the env-injected secrets manager integration that rotates at midnight UTC. Any change to this would require a coordinated deploy window with ops and re-issuance of all active sessions.
**Confidence:** High

---

**Q5** What are the consequences of violating SAFETY-2 (removing the adminHandler cast)?
**Answer:** Removing `castAs<AdminTokenPayload>` from `adminHandler.ts` line 47 will cause runtime type errors for admin sessions that were issued before the current schema migration. Those legacy token shapes will be rejected, breaking authentication for those sessions.
**Confidence:** High

---

**Q6** Why was `jwt.verify` wrapped in a `Promise` constructor rather than using the callback overload?
**Answer:** The callback form of `jwt.verify` is harder to integrate with `async/await` upstream callers without a `util.promisify` shim, which adds indirection. Using `new Promise((resolve, reject) => ...)` directly keeps the try-catch boundary explicit and lets upstream `async/await` callers receive clean stack traces on rejection.
**Confidence:** High

---

**Q7** Why were `TokenExpiredError` and `JsonWebTokenError` given separate handling rather than being caught by a single generic JWT error handler?
**Answer:** Separate handling was chosen so that client retry logic can be deterministic. Previously all JWT errors fell through to a generic 500 response, making it impossible for clients to distinguish a recoverable expiry from a truly invalid token. Now `TokenExpiredError` returns 401 with `{ code: "TOKEN_EXPIRED" }` and `JsonWebTokenError` returns 401 with `{ code: "INVALID_TOKEN" }`, allowing clients to react appropriately to each case.
**Confidence:** High

---

**Q8** What was the async vs. synchronous architecture decision made for `verifyToken`, and what does this enable for the future?
**Answer:** `verifyToken` was refactored from synchronous to asynchronous by wrapping `jwt.verify` in a Promise constructor. This enables future integration of Redis token invalidation without blocking the Node.js event loop, since Redis calls are inherently async and a synchronous `verifyToken` would block execution.
**Confidence:** High

---

**Q9** Why was the JWT refactor scoped only to call-site changes in the 5 route handlers, rather than deeper handler logic changes?
**Answer:** Summary1 states the changes were "purely call-site — replacing the synchronous invocation with `await verifyToken(token)` wrapped in try-catch." The scope was the async migration itself. Deeper issues (such as the adminHandler cast) were flagged for follow-up rather than addressed in the same session.
**Confidence:** Medium (Summary1 confirms the scope was call-site only, but does not explicitly state the reason the scope was limited — this is inferred from the structure of the session notes.)

---

**Q10** Where was the decision made to handle `TokenExpiredError` differently from other JWT errors, and what HTTP status does each return?
**Answer:** The decision was made in `authMiddleware.ts`. `TokenExpiredError` returns HTTP 401 with `{ code: "TOKEN_EXPIRED" }`. `JsonWebTokenError` returns HTTP 401 with `{ code: "INVALID_TOKEN" }`.
**Confidence:** High

---

**Q11** Which 5 route handlers were updated in S1 to use the async `verifyToken`?
**Answer:** The five handlers updated are: `userHandler.ts`, `orderHandler.ts`, `productHandler.ts`, `adminHandler.ts`, and `auditHandler.ts`. All changes were call-site only: replacing the synchronous call with `await verifyToken(token)` wrapped in try-catch.
**Confidence:** High

---

**Q12** What specific file was modified to add the two new error type handlers, and what is the current state of that file?
**Answer:** `authMiddleware.ts` was modified. It now contains separate catch branches: one for `TokenExpiredError` (returns 401 with `{ code: "TOKEN_EXPIRED" }`) and one for `JsonWebTokenError` (returns 401 with `{ code: "INVALID_TOKEN" }`). This error differentiation is complete as of S1.
**Confidence:** High

---

**Q13** What is the exact next action planned at the end of S1?
**Answer:** Investigate `adminHandler.ts` line 47 `castAs<AdminTokenPayload>` more carefully — specifically, understand what fields are present on legacy tokens versus current tokens, and determine if a runtime guard is needed in addition to the compile-time cast.
**Confidence:** High

---

**Q14** What is the current understanding of the `adminHandler.ts` line 47 cast at the end of S1 — what is known and what is unknown?
**Answer:** What is known: the cast is load-bearing and must not be removed (SAFETY-2). It appears to be hiding a structural mismatch between legacy token shapes and the current `AdminTokenPayload` interface. What is unknown: which specific fields are involved in the mismatch, and whether a runtime guard is needed in addition to the compile-time cast. This remains the explicit next action.
**Confidence:** High

---

**Q15** What branch is the JWT async refactor work on, and what was the branch state at the end of S1?
**Answer:** The branch is `feat/jwt-async-refactor`. At the end of S1, the branch contains: the async `verifyToken` implementation (using a Promise constructor), updated call sites in all 5 handlers, `authMiddleware.ts` with explicit `TokenExpiredError` / `JsonWebTokenError` differentiation, and SAFETY-1 and SAFETY-2 rules. The `adminHandler.ts` cast investigation is flagged as in progress but not yet resolved.
**Confidence:** High
