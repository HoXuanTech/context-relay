# Study 5 — T4 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary4 — T4 Test Context (after S4)
Date: 2026-05-27

---

**Q31**: What constraint from S3 carries into S4's filter UI implementation?

The modal-as-div rule from S3: all overlay UI must use `<div>` with `role="dialog"`, not the native `<dialog>` element. The S4 filter chips and search history dropdowns are not modals, so this rule does not directly affect them — but any S4 feature that opens a full overlay must follow it.

**Score**: 2/2 — rule stated; correct scope qualification (chips/history dropdowns are not affected) present

---

**Q32**: How does the compound filter work — what logic is applied when both a category and an area are selected?

AND logic: a recipe must match both the selected category and the selected area to remain visible. Filter state is tracked in `currentFilters = {category: string|null, area: string|null}`. Non-matching recipes are hidden with `display: none` — DOM preserved, no re-fetch needed.

**Score**: 2/2 — AND logic, currentFilters object structure, and display:none mechanism all stated

---

**Q33**: How is search history stored and managed?

Stored in localStorage under `STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'`. Maximum 10 entries — oldest evicted when limit exceeded. Duplicate queries not added. On search input focus, history appears as clickable chips. Clicking a chip fills the input and fires an immediate search.

**Score**: 2/2 — key string, max-10, dedup, eviction, and chips-on-focus behavior all present

---

**Q34**: What is roving tabindex and how is it implemented for the filter chips?

Only one chip per group has `tabindex="0"` at any time; all others have `tabindex="-1"`. Left/right arrow keys move focus and transfer `tabindex="0"` to the newly focused chip. Tab exits the chip group entirely. This avoids pressing Tab for every chip and matches expected keyboard navigation patterns.

**Score**: 2/2 — one-chip-has-zero mechanic, arrow key navigation, Tab-exits detail all present

---

**Q35**: Why was AND logic chosen for the compound filter instead of OR?

The user explicitly wanted to narrow results by combining filters (e.g., "Italian desserts" = both Italian AND Dessert, not either). OR logic would expand the result set, which is the opposite of the intended behavior. The AND decision was confirmed by the user during S4.

**Score**: 2/2 — user intent (narrow), example (Italian desserts), and OR-would-expand contrast all stated

---

**Q36**: Is the STORAGE_KEYS.SEARCH_HISTORY key subject to the same "never change" rule as FAVORITES?

Yes. `STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'` is locked in since S4. The same "never change" principle applies: once a localStorage key is in use, renaming it would silently orphan existing data. Both keys are permanent.

**Score**: 2/2 — key string, same principle as Rule #1, and "never change" consequence stated

---

**Q37**: How does the filter chip clear/reset work — how does a user remove an active filter?

Clicking an active chip a second time deselects it, setting the corresponding `currentFilters` field back to `null` and re-applying the filter with only the remaining active constraint. An "All" or "Clear" chip resets all filters. The chip's visual `.active` class is updated accordingly.

**Score**: 2/2 — toggle-on-second-click, null reset, All/Clear chip, visual state update all stated

---

**Q38**: Where does the filter chip data (category names and area names) come from?

Category names come from TheMealDB's `categories.php` endpoint. Area names come from `list.php?a=list`. Both are fetched on app load and rendered as chip buttons.

**Score**: 2/2 — both endpoints correctly identified; "fetched on app load" timing noted

---

**Q39**: Why is display:none used to hide non-matching recipes rather than removing and re-rendering cards?

Re-rendering on every filter change is expensive and discards already-fetched recipe data attached to the card. Using `display: none` preserves DOM nodes and their `data-recipeId` attributes, making filter toggling fast and avoiding extra API calls.

**Score**: 2/2 — performance rationale, data preservation, and API-call avoidance all stated

---

**Q40**: What is the complete feature set at the end of S4?

Search with results, favorites toggle and view, recipe detail modal with serving scaler and focus trapping, compound category+area filter (AND logic) with roving tabindex, search history (localStorage, max 10, deduplicated). Custom recipe CRUD is not yet built — that is S5.

**Score**: 2/2 — all S4 features enumerated; S5 boundary (custom recipes) correctly identified

---

## Summary Scores

SCORES: Q31=2,Q32=2,Q33=2,Q34=2,Q35=2,Q36=2,Q37=2,Q38=2,Q39=2,Q40=2

**Total: 20 / 20**
