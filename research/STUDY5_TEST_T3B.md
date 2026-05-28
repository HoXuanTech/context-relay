# Study 5 — T3 Test Answers (Agent B)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_B.md § Handoff3 — T3 Test Context (after S3)
Date: 2026-05-27

---

**Q21**: What carry-forward constraint from S2 applies to the detail view being built in S3?

Handoff3 carries forward Safety Rules #1 (favorites key) and #2 (ID strings only) in the Safety Rules section, plus the new modal-div rule. It does not explicitly state that the detail view reads from an in-memory cache rather than localStorage. Rule #2 is present, but the application of Rule #2 to the detail view's data source (memory not localStorage) is not described.

**Score**: 1/2 — Rule #2 carried forward but its specific implication for the detail view data source not stated

---

**Q22**: How is the detail view triggered — what data does the grid click handler pass to the modal?

Handoff3's Completed section describes what the modal does after opening but does not describe the triggering mechanism (event delegation, `data-recipeId` attribute, or `recipeCache` lookup). This implementation detail is not in the handoff.

**Score**: 0/2 — event delegation, data-recipeId, and recipeCache not mentioned in Handoff3

---

**Q23**: Why was a div overlay used for the recipe detail modal instead of the native HTML dialog element?

From Key Decisions: "Modal uses div overlay, not native `<dialog>` → `<dialog>` element was explicitly evaluated and rejected. The reasons: `::backdrop` styling is inconsistent between Chrome and Firefox... the `returnFocus` behavior on dialog close differs between implementations... and polyfilling dialog adds maintenance cost."

**Score**: 2/2 — all three specific rejection reasons present

---

**Q24**: How does the modal handle focus trapping and keyboard dismissal?

From Completed: "Focus trapping: Tab/Shift+Tab loop within modal focusables; modal opens with focus on close button." "Escape key + backdrop click → close modal; return focus to the card element that triggered open."

**Score**: 2/2 — Tab loop, open-on-close-button, Escape, backdrop click, and return-focus all present

---

**Q25**: How does parseQuantity handle fractions like "1/2" and floating-point rounding?

From Key Decisions: "`parseQuantity` handles fractions with `/` split → `'1/2'` becomes 0.5; `Math.round(v * 100) / 100` applied to all scaled values to prevent floating-point artifacts."

**Score**: 2/2 — split-on-slash and Math.round fix both stated

---

**Q26**: How does the serving scaler work — what is the default serving count and how are quantities scaled?

From Completed: "Serving scaler: +/- buttons, default 4 servings, `parseQuantity` handles fractions and non-numeric strings." Default of 4 is stated but the scaling formula `(newServings / originalServings)` is not explicitly given.

**Score**: 1/2 — default 4 and +/- buttons present; ratio formula not stated

---

**Q27**: Is there a carry-forward rule about the modal implementation established in S3?

From Safety Rules: "All modals must use div overlay with `role='dialog'`, `aria-modal='true'`, `aria-labelledby`, and manual focus trapping — native `<dialog>` element is banned for this project due to cross-browser inconsistency."

**Score**: 2/2 — rule stated with all required attributes and reasoning

---

**Q28**: What ARIA attributes does the modal div use to communicate its role to screen readers?

From Completed: "div overlay, `role='dialog'`, `aria-modal='true'`, `aria-labelledby` → modal heading." All three attributes explicitly listed.

**Score**: 2/2 — all three ARIA attributes present

---

**Q29**: How does the app handle measures that cannot be parsed as numbers (e.g., "to taste", "as needed")?

From Completed: "`parseQuantity` handles fractions and non-numeric strings." The handoff confirms non-numeric strings are handled, but does not describe the specific behavior (returned unchanged, scaler skips, no error shown).

**Score**: 1/2 — non-numeric handling confirmed but specific behavior (returned unchanged) not described

---

**Q30**: What is complete at the end of S3?

From Current Goal: "recipe detail modal with serving scaler is complete. Next session: compound filter (category + area) and search history." Modal features (focus trapping, Escape, backdrop, return-focus) listed in Completed. Filter and history are not done — S4.

**Score**: 2/2 — S3 complete features and S4 boundary both clearly stated

---

## Summary Scores

SCORES: Q21=1,Q22=0,Q23=2,Q24=2,Q25=2,Q26=1,Q27=2,Q28=2,Q29=1,Q30=2

**Total: 15 / 20**
