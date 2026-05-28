# Real Compression — C_autocompact_sim
Word count: 285

---

**Project: Recipe Collector — Vanilla JS, no frameworks**

**API: TheMealDB** (no key required)
- Search: `https://www.themealdb.com/api/json/v1/1/search.php?s={query}` → returns **full** data
- Lookup: `https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}` → full data
- Filter by category: `https://www.themealdb.com/api/json/v1/1/filter.php?c={cat}` → **partial** data only
- Filter by area: `https://www.themealdb.com/api/json/v1/1/filter.php?a={area}` → partial data only
- Categories: `https://www.themealdb.com/api/json/v1/1/categories.php`

**LOCKED: Recipe schema fields** (never rename — breaks localStorage):
`id, title, thumbnail, category, area, tags, ingredients, youtubeUrl, sourceUrl`
- `ingredients` is `null` for partial (filter endpoint) data; populated array for full (search/lookup) data

**SAFETY RULE #1 — PERMANENT**: localStorage key for favorites = `'recipe-favorites'`
Defined as `STORAGE_KEYS.FAVORITES` in `constants.js`. Never use raw string. Never rename.

**File structure** (plain script tags, no modules, load order matters):
```
constants.js → mapper.js → api.js → ui.js → app.js
```
- `constants.js`: STORAGE_KEYS
- `mapper.js`: `mapMealToRecipe()` — converts TheMealDB raw meal to clean Recipe
- `api.js`: `searchRecipes()`, `getFullRecipe()`, `getRecipesByCategory()`, `recipeCache{}` (private, session-scoped)
- `ui.js`: `createRecipeCard()`, `renderRecipes()`
- `app.js`: event listeners, `performSearch()`, stubs for `toggleFavorite()` and `openDetailView()`

**Permanent decisions:**
- `meals: null` guard required on every API function (`if (!data.meals) return []`)
- Event delegation on `#recipe-grid` (one listener handles both `.favorite-btn` and `.recipe-card` clicks)
- Race condition guard via `currentSearchId` counter in `performSearch()`
- `recipeCache` is private to `api.js` — access only via `getFullRecipe()`
- Card animations: `fadeInUp` 0.25s + stagger `index * 30ms` per card
- `innerHTML` acceptable for TheMealDB data; user-supplied data must use `textContent`
- `loading="lazy"` on all card thumbnails; `onerror` → `opacity:0` + gradient background fallback
- Click-to-search (no debounce); `searchInput.focus()` on load; default search: `'chicken'`

**Next session (S2):** Favorites system — `favorites.js`, localStorage read/write, heart button toggle, Favorites tab view. Decision pending: store full Recipe objects vs. IDs only in localStorage (tradeoff: offline access vs. 5MB limit).