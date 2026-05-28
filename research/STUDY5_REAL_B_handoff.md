# Real Compression — B_handoff
Word count: 744

---

# Handoff - recipe-collector - Session 1

## Current Goal
Build a vanilla JS recipe collector app (no frameworks) with search, card grid, and favorites — using TheMealDB as the data source.

## Key Decisions
- TheMealDB over Spoonacular → no API key, no rate limits, CORS-enabled, zero setup friction
- Excluded `instructions` from schema → app is a collector, not a cooking guide; users click out to source
- Plain `<script>` tags over ES modules → avoids local server requirement for `file://` protocol
- Click-to-search over debounced-as-you-type → TheMealDB needs full words; intermediate empty states feel janky
- `innerHTML` for card rendering (not `textContent`) → TheMealDB is a controlled dataset, not user input; user-provided content (future custom recipes) must use `textContent`
- `ingredients: null` as the partial-load signal → no separate `isFullyLoaded` flag needed
- CSS spinner (Option A) over skeleton cards (Option B) → right effort/value tradeoff for session 1
- Generic error messages → not over-engineering at this stage; refine if users report confusion

## Completed This Session
- TheMealDB selected as data source
- Recipe schema finalized: `id, title, thumbnail, category, area, tags, ingredients, youtubeUrl, sourceUrl`
- `mapMealToRecipe()` written: loops `strIngredient1–20`, uses `break` on empty name, merges tags from `strTags` + category + area with `filter(Boolean)` + `Set` dedup
- HTML scaffold: `<header>` with search input/button, `<main>` with `#status-message` and `#recipe-grid`
- `searchRecipes(query)` with `encodeURIComponent` and `meals: null` guard — returns full Recipe objects (search endpoint gives full data)
- `getRecipesByCategory(category)` — returns partial Recipe objects (`ingredients: null`) from filter endpoint
- `getFullRecipe(id)` with in-memory `recipeCache` object — checks cache before fetching; populates cache on fetch
- `renderRecipes()` auto-populates `recipeCache` for any fully-loaded recipes (search endpoint bonus)
- `createRecipeCard()` with `loading="lazy"`, `onerror` fallback setting `img-error` class, `data-recipe-id` and `data-id` attributes
- `performSearch()` with race condition fix: `currentSearchId` counter discards stale responses
- `handleSearch()` with `.trim()` guard and empty-input bail
- CSS responsive grid: `repeat(auto-fill, minmax(240px, 1fr))`
- Card hover lift: `transform: translateY(-4px)` — compositor-thread safe
- CSS spinner via `::before` pseudo-element on `.status-message.loading`
- `fadeInUp` entry animation with 30ms stagger per card index
- `onerror` image fallback: `opacity: 0` on `.img-error`, gradient background shows through
- Event delegation on `#recipe-grid`: one listener handles both `.favorite-btn` and `.recipe-card` clicks; `return` after favorite click prevents double-fire
- Stub functions: `toggleFavorite(id)` and `openDetailView(id)` with `console.log`
- `STORAGE_KEYS.FAVORITES = 'recipe-favorites'` constant in `constants.js`
- Auto-focus `#search-input` on `DOMContentLoaded`; pre-fills "chicken" results on load
- Nav tab architecture decided: `activeView` state variable, `switchView('search' | 'favorites')`, `#search-view` / `#favorites-view` toggle with `.hidden`
- File structure locked: `constants.js → mapper.js → api.js → ui.js → app.js` (load order matters)

## Safety Rules
- **`STORAGE_KEYS.FAVORITES = 'recipe-favorites'`** — permanently locked; never change this string; never use the raw string directly; changing it silently orphans every user's saved data
- **Schema fields are final**: `id, title, thumbnail, category, area, tags, ingredients, youtubeUrl, sourceUrl` — do not rename any field in any future session; renaming silently breaks localStorage-stored recipes
- **`meals: null` guard**: TheMealDB returns `meals: null` (not `[]`) for zero results — every new API function must check `if (!data.meals) return []` before mapping
- **`ingredients: null` means partial data**: filter/category endpoints never populate ingredients; all UI that renders ingredients must null-check first
- **`recipeCache` is private to `api.js`**: never read it directly from `app.js`; always go through `getFullRecipe()`
- **User-provided content** (future custom recipes): must use `textContent`, never `innerHTML` — this is the one XSS boundary in the app

## Next Actions
- Session 2: build `favorites.js` — localStorage read/write, `toggleFavorite()` implementation, heart button filled/empty state, Favorites tab view with `renderFavorites()`
- Decide storage strategy: full Recipe objects vs. IDs only in localStorage (5MB limit is the tradeoff — full objects support offline; IDs require network on reload)
- Flesh out `switchView()` and wire up nav tab HTML

## Recon Notes
- Base URL: `https://www.themealdb.com/api/json/v1/1`
- `search.php?s={query}` — full recipe data including ingredients; CORS-enabled; no key
- `filter.php?c={category}` — partial: `idMeal, strMeal, strMealThumb` only
- `filter.php?a={area}` — same structure as category filter
- `lookup.php?i={id}` — full recipe by ID; use for detail fetch
- `categories.php` — all categories
- `list.php?a=list` — all areas
- Raw field mapping: `idMeal→id`, `strMeal→title`, `strMealThumb→thumbnail`, `strCategory→category`, `strArea→area`, `strTags→tags`, `strIngredient1-20 + strMeasure1-20→ingredients[]`, `strYoutube→youtubeUrl`, `strSource→sourceUrl`
- Ingredients loop assumption: slots are consecutive (uses `break`, not `continue`); revisit if a broken recipe is encountered
- `encodeURIComponent` used on all query params
- Card DOM: `.recipe-card[data-recipe-id]`, `.favorite-btn[data-id]`
- Animation stagger: `index * 30ms` delay, `fadeInUp` 0.25s ease