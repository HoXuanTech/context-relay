# Study 5 — T3 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary3 — T3 Test Context (after S3)
Date: 2026-05-27

---

**Q21**: What carry-forward constraint from S2 applies to the detail view being built in S3?

Safety Rule #2 carries forward: full Recipe objects must not be stored in localStorage. The consequence for the detail view is that it reads recipe data from the already-fetched Recipe object held in memory (passed from the grid click handler via the in-memory `recipeCache`), not from a localStorage store. No new localStorage keys should be introduced for recipe detail data.

**Score**: 2/2 — Rule #2 carry-forward, memory (not localStorage) as data source, and no-new-key implication all stated

---

**Q22**: How is the detail view triggered — what data does the grid click handler pass to the modal?

The grid has an event delegation click handler that reads the clicked card's `data-recipeId` attribute. It looks up the recipe object from the in-memory `recipeCache` (not from localStorage) and passes the full Recipe object to the modal opening function. The modal displays data from the passed object directly.

**Score**: 2/2 — event delegation, data-recipeId attribute, recipeCache (not localStorage), and pass-full-object all stated

---

**Q23**: Why was a div overlay used for the recipe detail modal instead of the native HTML dialog element?

Three reasons: (1) `::backdrop` pseudo-element styling is inconsistent between Chrome and Firefox; (2) `returnFocus` behavior on dialog close differs between implementations; (3) polyfilling `<dialog>` for older browsers adds maintenance cost. A div overlay with `role="dialog"` and manual focus management gives full, predictable cross-browser control.

**Score**: 2/2 — all three specific technical reasons stated

---

**Q24**: How does the modal handle focus trapping and keyboard dismissal?

Focus trapping: a `keydown` listener on the modal intercepts Tab and Shift+Tab and loops focus within the focusable elements inside the modal. Modal opens with `.focus()` called on the close button. Keyboard dismissal: Escape key closes the modal and returns focus to the recipe card that was clicked to open it (card reference stored before opening). Overlay backdrop click also closes the modal.

**Score**: 2/2 — Tab loop, open-on-close-button, Escape key, return-focus-to-card, and backdrop click all present

---

**Q25**: How does parseQuantity handle fractions like "1/2" and floating-point rounding?

`parseQuantity` splits the measure string on `/` — if two parts exist, it divides them (e.g., `"1"` / `"2"` = 0.5). For serving scaling, the result is passed through `Math.round(value * 100) / 100` to eliminate floating-point artifacts like `0.30000000000000004`.

**Score**: 2/2 — split-on-slash fraction logic and Math.round rounding fix both stated

---

**Q26**: How does the serving scaler work — what is the default serving count and how are quantities scaled?

Default serving count is 4. The user uses +/- buttons to adjust. Each ingredient's measure quantity is scaled by `(newServings / originalServings)`. The `originalServings` from the recipe data serves as the base ratio denominator.

**Score**: 2/2 — default 4, +/- buttons, and new/original ratio formula all present

---

**Q27**: Is there a carry-forward rule about the modal implementation established in S3?

Yes — all modals in the app must use div overlay with `role="dialog"` and manual focus trapping, not the native HTML `<dialog>` element. This applies to any future modal-like UI (e.g., the custom recipe form planned for S5). The rule is locked in due to cross-browser behavior issues with native dialog.

**Score**: 2/2 — rule stated, forward scope (including S5 form) noted, reason cited

---

**Q28**: What ARIA attributes does the modal div use to communicate its role to screen readers?

Three attributes: `role="dialog"` (identifies it as a dialog), `aria-modal="true"` (tells screen readers to treat the rest of the page as inert while the dialog is open), and `aria-labelledby` pointing to the modal's heading element.

**Score**: 2/2 — all three ARIA attributes and their purposes stated

---

**Q29**: How does the app handle measures that cannot be parsed as numbers (e.g., "to taste", "as needed")?

`parseQuantity` returns the original string unchanged for non-numeric measures. The serving scaler skips scaling for those ingredients and displays the original measure string as-is, regardless of serving count. No error is shown to the user.

**Score**: 2/2 — returned unchanged, scaler skips scaling, no error — all three behaviors correct

---

**Q30**: What is complete at the end of S3?

Search, favorites toggle and view, and the recipe detail modal. The modal shows the full ingredient list, serving scaler (default 4 servings, +/- buttons), YouTube link, and source link. Focus trapping and keyboard dismissal are working. Compound filtering (category + area) and search history are not yet built — those are S4.

**Score**: 2/2 — S3 complete features listed; S4 boundary (filter + history) correctly identified as not done

---

## Summary Scores

SCORES: Q21=2,Q22=2,Q23=2,Q24=2,Q25=2,Q26=2,Q27=2,Q28=2,Q29=2,Q30=2

**Total: 20 / 20**
