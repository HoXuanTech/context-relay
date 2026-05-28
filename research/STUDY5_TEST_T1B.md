# Study 5 — T1 Test Answers (Agent B)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_B.md § Handoff1 — T1 Test Context (after S1)
Date: 2026-05-27

---

**Q1**: What is Safety Rule #1 and where is it stored?

Safety Rule #1: `STORAGE_KEYS.FAVORITES = 'recipe-favorites'`, locked in `constants.js`. Never change — renaming this key silently orphans all saved favorites with no migration path and no error visible to the user.

**Score**: 2/2 — key string, file location, and consequence all present

---

**Q2**: Which recipe API was chosen in S1, and why was it selected over alternatives?

TheMealDB was chosen — free, no API key required, CORS-open for direct browser fetch. Alternatives required paid plans or server-side proxies, which were dealbreakers for a client-side-only app.

**Score**: 2/2 — choice and both key rejection reasons stated

---

**Q3**: What is the shape of the unified Recipe schema established in S1?

`{id, title, thumbnail, category, area, tags, ingredients [{name, measure}], youtubeUrl, sourceUrl}`. The ingredients field is an array of `{name, measure}` objects, normalized from TheMealDB's raw `strIngredient1–20` / `strMeasure1–20` fields by `mapper.js`.

**Score**: 2/2 — full schema with object-shape ingredients and mapper.js normalization noted

---

**Q4**: How does the app handle broken or missing recipe images?

`PLACEHOLDER_IMAGE` constant is defined in `constants.js` as a fallback URL. Each card's `<img>` element has an `onerror` handler that sets `e.target.src = PLACEHOLDER_IMAGE` when the image fails to load. Single-source fallback: the URL is updated in one place only.

**Score**: 2/2 — onerror, PLACEHOLDER_IMAGE, constants.js location all stated

---

**Q5**: What are the TheMealDB API endpoints used for searching and looking up a recipe by ID?

`search.php?s=` for text search and `lookup.php?i=` for recipe by ID. The context lists both endpoints but does not explicitly state the full base URL `https://www.themealdb.com/api/json/v1/1/`.

**Score**: 1/2 — both endpoint paths present; base URL not explicitly stated in Handoff1

---

**Q6**: What TheMealDB endpoints are used to fetch the list of categories and areas (cuisines)?

`categories.php` for categories and `list.php?a=list` for areas. Both are listed in the Handoff1 endpoint inventory.

**Score**: 2/2 — both endpoints correctly identified

---

**Q7**: Why are ingredients stored as [{name, measure}] objects rather than as a flat string array?

The S3 serving scaler needs to split the numeric quantity from the unit string. With objects, the measure field is directly accessible. With a flat concatenated string like "1/2 cup", splitting would require re-parsing.

**Score**: 2/2 — S3 serving scaler rationale and contrast with flat strings both stated

---

**Q8**: What is the file load order of the JavaScript modules established in S1?

`constants.js` → `mapper.js` → `api.js` → `ui.js` → `app.js`. Stated explicitly in the Completed section of Handoff1.

**Score**: 2/2 — correct five-file order

---

**Q9**: Why was localStorage chosen to store favorites in S1 rather than a backend or IndexedDB?

Handoff1 establishes that localStorage is used (JSON array of ID strings) but does not explain why it was chosen over a backend or IndexedDB. No rationale comparing to alternatives is present in the handoff.

**Score**: 0/2 — localStorage use confirmed but no rationale comparing to alternatives present in context

---

**Q10**: What is built and working at the end of S1?

From "Completed This Session": TheMealDB API integration, unified Recipe schema, `mapper.js`, search UI (query → results → rendered cards), file load order, and localStorage favorites structure (key locked in). From "Next Actions": `toggleFavorite`, `loadFavorites`, and the favorites tab UI are not yet built — those are S2 tasks.

**Score**: 2/2 — what's done and what's not done clearly distinguishable from Completed vs Next Actions sections

---

## Summary Scores

SCORES: Q1=2,Q2=2,Q3=2,Q4=2,Q5=1,Q6=2,Q7=2,Q8=2,Q9=0,Q10=2

**Total: 17 / 20**
