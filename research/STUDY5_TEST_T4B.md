# Study 5 — T4 Test Answers (Agent B)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_B.md § Handoff4 — T4 Test Context (after S4)
Date: 2026-05-27

---

**Q31**: What constraint from S3 carries into S4's filter UI implementation?

Handoff4's Safety Rules carry forward Rule #1 (favorites key), Rule #2 (ID strings only), and the new SEARCH_HISTORY key rule — but does not explicitly carry the modal-div rule from S3. The modal pattern constraint is not listed in Handoff4's Safety Rules section.

**Score**: 0/2 — modal-div carry-forward constraint not present in Handoff4

---

**Q32**: How does the compound filter work — what logic is applied when both a category and an area are selected?

From Key Decisions: "Filter uses AND logic → user wanted to narrow results." From Completed: "`currentFilters = {category: null, area: null}`; chip click sets or clears the field; filter re-applied on every change." From Key Decisions: "`display: none` to hide non-matching cards, DOM preserved."

**Score**: 2/2 — AND logic, currentFilters object, and display:none preservation all stated

---

**Q33**: How is search history stored and managed?

From Completed: "`STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'`; max 10; deduplicated; chips shown on input focus; click to populate and search." Key string, max-10, dedup, and chips-on-focus all present.

**Score**: 2/2 — all key details present

---

**Q34**: What is roving tabindex and how is it implemented for the filter chips?

From Key Decisions: "Roving tabindex on filter chips → only one chip has `tabindex='0'` at a time; arrow keys move focus; Tab exits chip group; prevents Tab-through-every-chip UX." From Completed: "The implementation maintains a `currentIndex` per group and updates it on arrow key events."

**Score**: 2/2 — one-chip-zero mechanic, arrow keys, Tab-exits, and currentIndex implementation all present

---

**Q35**: Why was AND logic chosen for the compound filter instead of OR?

From Key Decisions: "Filter uses AND logic → user wanted to narrow results (e.g., 'Italian desserts' = Italian AND Dessert, not either); OR would expand the set instead of narrowing."

**Score**: 2/2 — user intent, example, and OR contrast all stated

---

**Q36**: Is the STORAGE_KEYS.SEARCH_HISTORY key subject to the same "never change" rule as FAVORITES?

From Safety Rules: "`STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'` is locked in constants.js — same 'never change' principle as Rule #1; renaming would silently orphan existing history."

**Score**: 2/2 — key string, same principle as Rule #1, and consequence all explicit

---

**Q37**: How does the filter chip clear/reset work — how does a user remove an active filter?

From Completed: "chip click sets or clears the field" — implies clicking an active chip clears (deselects) it. But "All" or "Clear" chip is not explicitly mentioned. The toggle-on-click behavior is implied but not spelled out as a second-click deselect.

**Score**: 1/2 — chip deselect behavior implied but not explicit; All/Clear chip not mentioned

---

**Q38**: Where does the filter chip data (category names and area names) come from?

From Completed: "Category chips (from `categories.php`) and area chips (from `list.php?a=list`) rendered on app load."

**Score**: 2/2 — both endpoints and "on app load" timing stated

---

**Q39**: Why is display:none used to hide non-matching recipes rather than removing and re-rendering cards?

From Key Decisions: "Recipes hidden with `display: none` → DOM preserved; no re-fetch when filter changes; card `data-recipeId` attributes and event listeners intact."

**Score**: 2/2 — DOM preservation, no re-fetch, and data attribute preservation all stated

---

**Q40**: What is the complete feature set at the end of S4?

From Current Goal: "Compound filter and search history are complete. Next session: custom recipe add/edit/delete." From Completed: category/area chips, AND filter logic, roving tabindex, search history. Search, favorites, and modal are carried forward from earlier sessions.

**Score**: 2/2 — S4 features and S5 boundary (custom recipes) both correctly identified

---

## Summary Scores

SCORES: Q31=0,Q32=2,Q33=2,Q34=2,Q35=2,Q36=2,Q37=1,Q38=2,Q39=2,Q40=2

**Total: 17 / 20**
