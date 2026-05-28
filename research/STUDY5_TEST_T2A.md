# Study 5 — T2 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary2 — T2 Test Context (after S2)
Date: 2026-05-27

---

**Q11**: What is the exact localStorage key used for favorites, and what is the carry-forward rule about it?

The key is `'recipe-favorites'`, defined as `STORAGE_KEYS.FAVORITES` in `constants.js`. Carry-forward rule: this key must never change regardless of refactoring or renaming. Changing it would silently orphan all existing saved favorites — data would remain under the old key with no migration.

**Score**: 2/2 — exact key string, constants.js location, and "never change" consequence all stated

---

**Q12**: How are ingredients structured in the Recipe schema, and why does this matter for future sessions?

Ingredients are `[{name: string, measure: string}]` — objects, not flat strings. This matters because the S3 serving scaler needs to separate the numeric quantity from the unit string. Object shape allows direct field access; a flat concatenated string would require re-parsing the measure to extract the number.

**Score**: 2/2 — object shape stated; forward-planning for S3 serving scaler explained

---

**Q13**: What is Safety Rule #2 and what does it prohibit?

Safety Rule #2: favorites must be stored as a JSON array of recipe ID strings only. Full Recipe objects must never be stored under the favorites key. Two justifications: (1) the localStorage 5MB origin limit would be approached if full objects with ingredient arrays, thumbnails, and text were stored for each favorited recipe; (2) keeping favorites as a lightweight ID index is architecturally cleaner — it separates "which recipes the user cares about" from "what those recipes contain."

**Score**: 2/2 — prohibition stated; both justifications (size limit + architectural clarity) present

---

**Q14**: How does loadFavorites work — what does it do with the stored ID strings?

`loadFavorites` reads the ID string array from localStorage. For each ID, it calls the TheMealDB `lookup.php?i=` endpoint to fetch the full Recipe object. It collects the resolved recipes and renders them into `favoritesGrid`. This means favorites always reflect TheMealDB's current data for those IDs — and require network calls on load.

**Score**: 2/2 — read IDs, one lookup call per ID, render to favoritesGrid, network-call-per-ID consequence all stated

---

**Q15**: How does the toggleFavorite function work?

`toggleFavorite(id)` reads the current ID array from localStorage using `JSON.parse`. If the ID is present, it removes it (unfavorite); if absent, it adds it (favorite). The updated array is written back to localStorage with `JSON.stringify`. The heart icon on the card is updated to reflect the new state.

**Score**: 2/2 — read-modify-write pattern, add/remove logic, and UI update all described

---

**Q16**: What is the two-grid architecture introduced in S2?

`searchGrid` and `favoritesGrid` are two separate DOM containers. Both are present in the HTML at all times — switching tabs shows one and hides the other with CSS `display` toggling rather than re-rendering. Search results are preserved when the user switches to Favorites and back; no re-fetch is triggered by tab switching. A third tab for custom recipes is planned for S5 but not yet present.

**Score**: 2/2 — two grids, both persist in DOM, display-toggle mechanism, search-results-preserved detail all present

---

**Q17**: Why are favorites stored as ID strings instead of full Recipe objects, given that loading them requires extra network calls?

The tradeoff is explicitly accepted: network calls on favorites load are acceptable because the app targets a personal use case where the favorites list is expected to be small (tens of recipes, not hundreds). The 5MB localStorage limit and the simpler data model outweigh the extra network cost at this scale.

**Score**: 2/2 — explicit acceptance of tradeoff; personal-tool scale justification; 5MB and simplicity mentioned

---

**Q18**: What try/catch pattern is used when reading from localStorage?

All localStorage reads use `JSON.parse` wrapped in `try/catch`. If the stored value is corrupted or manually edited to invalid JSON, the catch block returns an empty array as the default rather than propagating an exception. This defensive read pattern applies to every localStorage key in the app.

**Score**: 2/2 — try/catch pattern, empty-array default, and "every localStorage key" scope stated

---

**Q19**: What functionality is complete at the end of S2?

Search with result cards, favorites toggle on each card (heart icon, localStorage read/write), favorites view that fetches and renders full recipe data for each saved ID, two-tab navigation (Search / Favorites). Not yet built: the recipe detail modal with ingredient list and serving scaler — that is S3.

**Score**: 2/2 — completed features and not-yet-built distinction (modal is S3) both correct

---

**Q20**: Why does the favorites view require network calls on load rather than showing stored data immediately?

Because Safety Rule #2 prohibits storing full Recipe objects in localStorage — only ID strings are stored. To display a full recipe card (thumbnail, title, category, etc.), the full data must be fetched via `lookup.php?i=` on each load. This consequence is explicitly accepted as appropriate for a small personal favorites list.

**Score**: 2/2 — chain of reasoning (Rule #2 → IDs only → network calls required) complete; tradeoff acceptance present

---

## Summary Scores

SCORES: Q11=2,Q12=2,Q13=2,Q14=2,Q15=2,Q16=2,Q17=2,Q18=2,Q19=2,Q20=2

**Total: 20 / 20**
