# Study 5 Data — Group B: Handoff Chain
Project: Recipe Collector Web App vibe coding (6 sessions)

---

## Handoff1 — T1 Test Context (after S1)

# Handoff - recipe-collector - Session 1: Foundation

## Current Goal
API selection, data schema, and project structure are locked in. Next session: wire up the favorites toggle and build the favorites view.

## Key Decisions
- TheMealDB chosen → free, no API key, CORS-open for direct browser fetch; alternatives required paid plans or server-side proxies
- Ingredients stored as `[{name, measure}]` objects (not concatenated strings) → S3 serving scaler needs to split quantity from unit; object shape makes that trivial
- File load order is explicit and load-order-safe → no bundler; each file uses only names from earlier files
- `PLACEHOLDER_IMAGE` constant in constants.js → single-source fallback URL for broken thumbnails; img onerror sets `e.target.src = PLACEHOLDER_IMAGE`

## Completed This Session
- TheMealDB API integration: search.php?s=, lookup.php?i=, categories.php, list.php?a=list
- Unified Recipe schema: `{id, title, thumbnail, category, area, tags, ingredients [{name, measure}], youtubeUrl, sourceUrl}`
- mapper.js: normalizes raw TheMealDB response (strIngredient1-20, strMeasure1-20) into schema
- Search UI: query → search.php → render recipe cards (title, thumbnail, category, area)
- File load order: constants.js → mapper.js → api.js → ui.js → app.js
- localStorage favorites structure established: JSON array of ID strings

## Safety Rules
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` — locked in constants.js; never change; renaming this key silently orphans all saved favorites with no migration path (**Safety Rule #1**)
- File load order must be maintained; new files added only between existing entries that match their dependency direction

## Last Actions
- Locked in STORAGE_KEYS.FAVORITES and added to constants.js
- Confirmed img onerror fallback works on cards with broken thumbnail URLs

## Next Actions
- Build `toggleFavorite(id)`: read ID array from localStorage, add/remove ID, write back
- Build `loadFavorites`: read IDs, call lookup.php?i= per ID, render to favoritesGrid
- Add favorites.js to file load order (after ui.js, before app.js)
- Wire favorites tab button to show/hide searchGrid vs favoritesGrid

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs

---

## Handoff2 — T2 Test Context (after S2)

# Handoff - recipe-collector - Session 2: Favorites

## Current Goal
Favorites system is complete. Next session: recipe detail modal with ingredient list and serving scaler.

## Key Decisions
- Favorites stored as ID strings only → storing full Recipe objects would approach 5MB localStorage limit; IDs are a few bytes each; `loadFavorites` fetches full data per ID on demand
- Two-grid architecture → `searchGrid` and `favoritesGrid` both stay in DOM; switching tabs shows/hides rather than re-renders; search results preserved across tab switches
- All localStorage reads use `JSON.parse` in `try/catch` → corrupted data returns empty array, not a crash

## Completed This Session
- `toggleFavorite(id)`: reads ID array, adds or removes ID, writes back; updates heart icon state
- `loadFavorites`: reads ID array, calls `lookup.php?i=` per ID, renders results to favoritesGrid
- Two-tab navigation: Search tab ↔ Favorites tab; grid show/hide on tab switch
- favorites.js added to load order between ui.js and app.js

## Safety Rules
- Favorites key `'recipe-favorites'` still locked (**Rule #1**)
- Favorites must be stored as ID string array only — never full Recipe objects (**Safety Rule #2**); `loadFavorites` always fetches full data via network; this design is intentional, not an oversight
- Every localStorage read must use `JSON.parse` in `try/catch`; default to `[]` on parse error

## Last Actions
- Confirmed toggleFavorite correctly handles both add and remove on repeated clicks
- Confirmed loadFavorites renders the correct cards when switching to Favorites tab

## Next Actions
- Build recipe detail modal: opens on card click, shows title, thumbnail, full ingredient list, serving scaler, YouTube link, source link
- Modal must use div overlay (not native `<dialog>` — evaluate first)
- Add focus trapping and Escape key dismissal to modal

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs

---

## Handoff3 — T3 Test Context (after S3)

# Handoff - recipe-collector - Session 3: Detail Modal + Serving Scaler

## Current Goal
Recipe detail modal with serving scaler is complete. Next session: compound filter (category + area) and search history.

## Key Decisions
- Modal uses div overlay, not native `<dialog>` → `::backdrop` styling is inconsistent across browsers; `returnFocus` behavior differs between Chrome and Firefox; polyfilling dialog adds maintenance cost; div with role="dialog" + manual focus management gives full control
- `parseQuantity` handles fractions with `/` split → "1/2" becomes 0.5; `Math.round(v * 100) / 100` applied to all scaled values to prevent floating-point artifacts like 0.30000000000000004
- Serving scaler default is 4 → non-numeric measures ("to taste", "as needed") are returned unchanged, not scaled

## Completed This Session
- Recipe detail modal: div overlay, `role="dialog"`, `aria-modal="true"`, `aria-labelledby` → modal heading
- Focus trapping: Tab/Shift+Tab loop within modal focusables; modal opens with focus on close button
- Escape key + backdrop click → close modal; return focus to the card element that triggered open
- Serving scaler: +/- buttons, default 4 servings, `parseQuantity` handles fractions and non-numeric strings

## Safety Rules
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` (**Rule #1**)
- Favorites as ID strings only (**Rule #2**)
- All modals must use div overlay with `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, and manual focus trapping — native `<dialog>` element is banned for this project due to cross-browser inconsistency

## Last Actions
- Confirmed focus returns to originating card on Escape close and X button close
- Confirmed parseQuantity handles "1/2 cup", "2", "to taste" correctly
- Confirmed Math.round prevents float artifacts in serving scaler output

## Next Actions
- Fetch category list from `categories.php` and render as clickable filter chips
- Fetch area list from `list.php?a=list` and render as separate chip row
- Implement AND filter logic: `currentFilters = {category: null, area: null}`; recipe must match both active constraints
- Add search history to localStorage: `STORAGE_KEYS.SEARCH_HISTORY`; max 10 queries; show as chips on input focus

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs

---

## Handoff4 — T4 Test Context (after S4)

# Handoff - recipe-collector - Session 4: Compound Filter + Search History

## Current Goal
Compound filter and search history are complete. Next session: custom recipe add/edit/delete.

## Key Decisions
- Filter uses AND logic → user wanted to narrow results (e.g., "Italian desserts" = Italian AND Dessert, not either); OR would expand the set instead of narrowing
- Recipes hidden with `display: none` → DOM preserved; no re-fetch when filter changes; card data-recipeId attributes and event listeners intact
- Roving tabindex on filter chips → only one chip has `tabindex="0"` at a time; arrow keys move focus; Tab exits chip group; prevents Tab-through-every-chip UX
- Search history max 10 with deduplication → new query moved to front if duplicate exists; oldest evicted when limit exceeded

## Completed This Session
- Category chips (from `categories.php`) and area chips (from `list.php?a=list`) rendered on app load
- `currentFilters = {category: null, area: null}`; chip click sets or clears the field; filter re-applied on every change
- Compound AND filter: recipes with neither, one, or both matches handled correctly
- Roving tabindex: arrow key listener on chip container moves `tabindex` attribute between chips
- Search history: `STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'`; max 10; deduplicated; chips shown on input focus; click to populate and search

## Safety Rules
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` (**Rule #1**)
- Favorites as ID strings only (**Rule #2**)
- `STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'` is locked in constants.js — same "never change" principle as Rule #1; renaming would silently orphan existing history

## Last Actions
- Confirmed AND logic: selecting category + area only shows recipes matching both
- Confirmed deduplication: searching "chicken" twice only adds one history entry
- Confirmed roving tabindex: arrow keys navigate chips; Tab exits to next element

## Next Actions
- Add `STORAGE_KEYS.CUSTOM_RECIPES` to constants.js before writing any custom recipe code
- Define `CUSTOM_RECIPE_PREFIX = 'custom-'` in constants.js
- Build custom recipe add form: title, image URL (with validation), ingredients, star rating, description
- Build `getAnyRecipeById(id)`: routes 'custom-' prefix to localStorage, others to `lookup.php?i=`

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs

---

## Handoff5 — T5 Test Context (after S5)

# Handoff - recipe-collector - Session 5: Custom Recipe CRUD

## Current Goal
Custom recipe CRUD with export/import is complete. Next session: Cache API, performance, accessibility, deployment.

## Key Decisions
- `CUSTOM_RECIPE_PREFIX = 'custom-'` → TheMealDB IDs are plain integers; collision would make `getAnyRecipeById` routing ambiguous; prefix makes routing deterministic (**Safety Rule #3**)
- Custom recipes stored as full objects in localStorage → no backing API to fetch from; must store everything locally; same schema as TheMealDB recipes so rest of app needs no special-casing
- Image URL validated via hidden img onload/onerror → URL only stored, not image binary; confirmed loadable before accepting
- Star rating uses radio inputs with `role="radiogroup"` → native keyboard behavior (arrow keys) works without JS; accessible by default
- `createRecipeCard` uses `textContent` for user content → prevents XSS from custom recipe titles/descriptions containing HTML tags

## Completed This Session
- `STORAGE_KEYS.CUSTOM_RECIPES = 'recipe-custom'` locked in constants.js
- `getAnyRecipeById(id)`: `id.startsWith(CUSTOM_RECIPE_PREFIX)` → localStorage; else → `lookup.php?i=`
- Custom recipe form: add mode (empty hidden ID field → generate `'custom-' + Date.now()`) and edit mode (populated hidden ID → update in-place)
- Image URL validation: hidden img, `onload` = accept, `onerror` = reject with inline error
- Star rating: `<input type="radio">` in `role="radiogroup"` container, values 1–5
- Export: `JSON.stringify` → `Blob` → `URL.createObjectURL` → anchor click download
- Import: file input → `FileReader.readAsText` → `JSON.parse` → validate fields + 'custom-' prefix → write to localStorage
- Delete with confirmation; `getAnyRecipeById` routes correctly for favorites tab on custom IDs
- `createRecipeCard` uses `textContent` for title, description, ingredient display fields

## Safety Rules
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` (**Rule #1**)
- Favorites as ID strings only (**Rule #2**)
- `CUSTOM_RECIPE_PREFIX = 'custom-'`: all custom recipe IDs must start with this prefix (**Safety Rule #3**); importing recipes must validate this prefix before writing
- `createRecipeCard` must continue using `textContent` (not `innerHTML`) for any user-provided field

## Next Actions
- Cache API: cache `categories.php` and `list.php?a=list` responses with 24-hour TTL; use `X-Cached-At` header (not server Date header) for TTL tracking
- Add manual cache refresh button as escape hatch
- Review `loading="lazy"` usage on recipe card images; confirm not applied to above-fold images
- Deploy to GitHub Pages via `/docs` folder; evaluate PWA/Service Worker setup
- Accessibility audit: nav tablist/tab roles, card tabindex, aria-live on status, search input label, filter fieldset/legend, skip-to-content link

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs

---

## Handoff6 — T6 Test Context (after S6, project complete)

# Handoff - recipe-collector - Session 6: Cache, Accessibility, Deployment

## Current Goal
Project is complete and deployed. All six sessions done. All three Safety Rules in place and documented.

## Key Decisions
- Cache API over Service Worker → PWA complexity (install/activate/fetch lifecycle, versioning, background sync) was judged disproportionate for a personal single-user tool; Cache API used as a simple read-through cache only
- `X-Cached-At` header for TTL tracking → server `Date` header unreliable (CDN servers may return stale or offset timestamps); custom header written at cache time is the authoritative timestamp
- `fetchWithCache` wrapped in `try/catch` → Cache API unavailable in private browsing or on storage quota exceeded; falls back to plain `fetch()`; app degrades gracefully, not crashes
- GitHub Pages `/docs` folder → zero configuration, zero backend, no CORS proxy needed (TheMealDB allows all origins)
- `loading="lazy"` on recipe card images only → above-fold and hero images must not use lazy loading (would cause blank flash on slow connections)

## Completed This Session
- Cache API: `caches.open('recipe-collector-v1')` for `categories.php` and `list.php?a=list`; `X-Cached-At: Date.now()` header; `CACHE_TTL_MS` = 24 hours; `cache.delete()` + re-fetch for manual refresh
- `fetchWithCache(url)`: check cache → validate TTL via `X-Cached-At` → return cached or fetch-and-cache; `try/catch` wraps all Cache API calls
- Accessibility: `role="tablist"` + `role="tab"` + `aria-selected` on nav; `tabindex="0"` + `role="article"` on cards; `role="status"` + `aria-live="polite"` on status div; `.visually-hidden` label for search input; `<fieldset>`+`<legend>` for filter groups; skip-to-content link (`top: -100%` → `top: 0` on `:focus`)
- Deployment: all static files under `/docs`; pushed to main; GitHub Pages serves from `/docs`

## Safety Rules (all three, complete)
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` — never change (**Rule #1**)
- Favorites stored as ID string array only (**Rule #2**)
- `CUSTOM_RECIPE_PREFIX = 'custom-'` — all custom IDs must have this prefix (**Rule #3**)
- Modal pattern: div overlay + `role="dialog"` + manual focus trap — no native `<dialog>`
- `STORAGE_KEYS.CUSTOM_RECIPES = 'recipe-custom'` and `STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'` are permanent once data exists

## Persistence Summary (three layers)
- Memory: `recipeCache`, `currentFilters`, active view — cleared on tab close
- localStorage: three locked keys in `STORAGE_KEYS` (`'recipe-favorites'`, `'recipe-search-history'`, `'recipe-custom'`)
- Cache API: `'recipe-collector-v1'` — two cached endpoints, 24h TTL, graceful degradation

## Background
→ read ~/Desktop/context-relay/research/STUDY5_CONTENT.md for full session logs
