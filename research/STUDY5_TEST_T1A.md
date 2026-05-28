# Study 5 — T1 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary1 — T1 Test Context (after S1)
Date: 2026-05-27

---

**Q1**: What is Safety Rule #1 and where is it stored?

Safety Rule #1: `STORAGE_KEYS.FAVORITES = 'recipe-favorites'`. This localStorage key must never be changed. Changing it would silently orphan all saved favorites — the data would remain under the old key with no migration path and no visible error to the user. The rule is stored as a constant in `constants.js`, which is the single source of truth for all localStorage key strings.

**Score**: 2/2 — full and specific answer including key string, consequence of change, and file location

---

**Q2**: Which recipe API was chosen in S1, and why was it selected over alternatives?

TheMealDB was chosen. It is free with no API key required, and it allows direct browser fetch calls because its responses include permissive CORS headers. Alternatives were rejected for requiring paid plans, needing server-side proxies to avoid CORS restrictions, or returning poor ingredient data.

**Score**: 2/2 — choice and all three differentiating reasons present

---

**Q3**: What is the shape of the unified Recipe schema established in S1?

`{id, title, thumbnail, category, area, tags, ingredients, youtubeUrl, sourceUrl}`. The `ingredients` field is an array of objects with two string fields each: `{name, measure}` — not a flat string array.

**Score**: 2/2 — all field names listed; ingredients object shape with name and measure specified

---

**Q4**: How does the app handle broken or missing recipe images?

An `onerror` handler on each card's `<img>` element catches load failures and replaces `e.target.src` with `PLACEHOLDER_IMAGE`. `PLACEHOLDER_IMAGE` is a constant defined in `constants.js`, so the fallback URL is managed in one place and never hardcoded in rendering code.

**Score**: 2/2 — onerror mechanism, PLACEHOLDER_IMAGE constant, and constants.js location all present

---

**Q5**: What are the TheMealDB API endpoints used for searching and looking up a recipe by ID?

Search: `search.php?s={query}`. Lookup by ID: `lookup.php?i={id}`. Both are under the base URL `https://www.themealdb.com/api/json/v1/1/`.

**Score**: 2/2 — both endpoints and the full base URL stated

---

**Q6**: What TheMealDB endpoints are used to fetch the list of categories and areas (cuisines)?

Categories: `categories.php`. Areas (cuisines): `list.php?a=list`. Both are under the same TheMealDB base URL.

**Score**: 2/2 — both endpoint paths stated correctly

---

**Q7**: Why are ingredients stored as [{name, measure}] objects rather than as a flat string array?

Because a serving scaler planned for Session 3 will need to extract the numeric portion of the measure separately from the unit text (e.g., separate "1/2" from "cup"). That separation is only feasible if name and measure are already stored in separate fields. Concatenating them into a single string like "1/2 cup flour" would require re-parsing later.

**Score**: 2/2 — forward-planning rationale and the specific serving scaler reason stated

---

**Q8**: What is the file load order of the JavaScript modules established in S1?

`constants.js` → `mapper.js` → `api.js` → `ui.js` → `app.js`. Files are included via `<script>` tags at the bottom of `index.html` in this order. Each file only uses names defined in earlier files. No module bundler is used.

**Score**: 2/2 — all five files in correct order; no-bundler rationale present

---

**Q9**: Why was localStorage chosen to store favorites in S1 rather than a backend or IndexedDB?

The app is a personal tool with no authentication and no backend. localStorage is sufficient for single-user, single-device use. The favorites are small (an array of ID strings), so the 5MB localStorage limit is not a concern. IndexedDB would add complexity without benefit at this scale.

**Score**: 2/2 — personal tool rationale, small data size, and explicit IndexedDB comparison all present

---

**Q10**: What is built and working at the end of S1?

Search is functional: querying returns recipe cards with title, thumbnail, category, and area. Broken images fall back to PLACEHOLDER_IMAGE. The unified Recipe schema is in place. `STORAGE_KEYS.FAVORITES` is locked in. The favorites heart icon is visible on cards but the toggle logic and the favorites view are not yet wired — those are S2.

**Score**: 2/2 — what IS done (search, schema, key) and what is NOT done (favorites toggle/view) both stated

---

## Summary Scores

SCORES: Q1=2,Q2=2,Q3=2,Q4=2,Q5=2,Q6=2,Q7=2,Q8=2,Q9=2,Q10=2

**Total: 20 / 20**
