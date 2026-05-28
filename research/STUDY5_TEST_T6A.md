# Study 5 — T6 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary6 — T6 Test Context (after S6)
Date: 2026-05-27

---

**Q51**: Describe the complete Recipe Collector architecture: persistence layers, key constants, all Safety Rules, file load order, and the most important implementation constraints from all six sessions.

**File load order**: `constants.js` → `mapper.js` → `api.js` → `ui.js` → `favorites.js` → `customRecipes.js` → `app.js`. Each file uses only names from earlier files. No build tooling.

**Recipe schema**: `{id, title, thumbnail, category, area, tags, ingredients [{name, measure}], youtubeUrl, sourceUrl}`. Uniform across TheMealDB recipes and custom recipes.

**Three Safety Rules**:
- Rule #1: `STORAGE_KEYS.FAVORITES = 'recipe-favorites'`. Never change. Renaming orphans all saved favorites.
- Rule #2: Favorites stored as ID string array only — never full Recipe objects. `loadFavorites` fetches full data via `lookup.php?i=` per ID.
- Rule #3: `CUSTOM_RECIPE_PREFIX = 'custom-'`. All custom recipe IDs must start with `'custom-'` to prevent collision with TheMealDB integer IDs in `getAnyRecipeById`.

**Persistence — three layers**:
1. Memory: ephemeral state (`recipeCache`, `currentFilters`, active view). Cleared on tab close.
2. localStorage: three locked keys — `'recipe-favorites'` (ID string array), `'recipe-search-history'` (max-10 query array, deduplicated), `'recipe-custom'` (full custom Recipe object array). All in `STORAGE_KEYS`; new keys must be added to `STORAGE_KEYS` before use.
3. Cache API: `'recipe-collector-v1'` namespace. Caches `categories.php` and `list.php?a=list`. 24-hour TTL tracked via `X-Cached-At` header. `fetchWithCache` wrapped in `try/catch` for graceful degradation. Manual refresh button: `cache.delete()` + re-fetch. PWA/Service Workers explicitly rejected.

**Key constraints**:
- All modals: `<div>` overlay with `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, manual focus trapping. Native `<dialog>` banned due to cross-browser inconsistency.
- `parseQuantity`: splits fractions on `/`, returns non-numeric strings unchanged, applies `Math.round(v * 100) / 100` for float safety.
- Compound filter: AND logic. `currentFilters = {category, area}`. Non-matching recipes hidden with `display: none` — DOM preserved.
- Filter chips: roving tabindex (one chip has `tabindex="0"`, others `tabindex="-1"`, arrow keys move focus).
- `createRecipeCard`: `textContent` for all user-content fields (XSS prevention).
- `getAnyRecipeById`: routes `'custom-'` prefix to localStorage; other IDs to `lookup.php?i=`.
- `loading="lazy"` on recipe card images only; never on above-fold images.
- Scripts at bottom of `<body>`.

**Accessibility**: `role="tablist"` + `role="tab"` + `aria-selected` on nav. `tabindex="0"` + `role="article"` on cards. `role="status"` + `aria-live="polite"` on status div. `.visually-hidden` CSS label for search input. `<fieldset>` + `<legend>` for filter chip groups. Skip-to-content link (`top: -100%` → `top: 0` on `:focus`).

**Deployment**: GitHub Pages via `/docs` folder on `main` branch. Zero configuration, zero backend. TheMealDB CORS allows all origins — no proxy needed.

**Score**: 2/2 — all required elements present: file load order (7 files in order), schema (all fields including ingredients object shape), all three Safety Rules with key strings and consequences, all three persistence layers with correct details (X-Cached-At, 24h TTL, 'recipe-collector-v1', three localStorage keys), and all major constraints (modal, parseQuantity, AND filter, roving tabindex, textContent, getAnyRecipeById routing, lazy loading)

---

## Summary Scores

SCORES: Q51=2

**Total: 2 / 2**

---

**Coverage assessment:**

- **S1** — Fully covered: TheMealDB API selection, Recipe schema (all fields + ingredients object shape), file load order, PLACEHOLDER_IMAGE onerror, STORAGE_KEYS.FAVORITES (Rule #1), localStorage ID-string array pattern, mapper.js normalization.
- **S2** — Fully covered: Safety Rule #2 (ID strings only), toggleFavorite read-modify-write, loadFavorites network-per-ID, two-grid DOM architecture, try/catch empty-array default.
- **S3** — Fully covered: div overlay modal (not native dialog), all three ARIA attributes, focus trapping Tab loop, parseQuantity fractions + Math.round float fix, serving scaler default 4 + ratio formula, return-focus-to-card on close.
- **S4** — Fully covered: compound AND filter, currentFilters object, roving tabindex, STORAGE_KEYS.SEARCH_HISTORY key (max 10, dedup), display:none DOM preservation.
- **S5** — Fully covered: Safety Rule #3 (CUSTOM_RECIPE_PREFIX), STORAGE_KEYS.CUSTOM_RECIPES, getAnyRecipeById prefix routing, image URL hidden-img validation, star rating radiogroup, form add/edit hidden-ID mode, export blob URL, import FileReader+validation, textContent XSS prevention.
- **S6** — Fully covered: Cache API ('recipe-collector-v1', X-Cached-At, 24h TTL, fetchWithCache try/catch), manual refresh, PWA rejection, GitHub Pages /docs, accessibility (tablist/tab/aria-selected, article+tabindex, aria-live, visually-hidden label, fieldset/legend, skip-to-content), three-layer persistence summary.

No gaps — Summary6 contains a complete cumulative account of all six sessions.
