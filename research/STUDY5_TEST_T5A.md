# Study 5 — T5 Test Answers (Agent A)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_A.md § Summary5 — T5 Test Context (after S5)
Date: 2026-05-27

---

**Q41**: What carry-forward rule from S4 applies to the custom recipe feature being built in S5?

The localStorage key stability rule: any new key introduced for custom recipes must be defined in `STORAGE_KEYS` in `constants.js` and treated as permanent once data exists under it. This led to `STORAGE_KEYS.CUSTOM_RECIPES` being defined in `constants.js` before any custom recipe code was written.

**Score**: 2/2 — key stability rule, constants.js location, and "defined before code" discipline all stated

---

**Q42**: How does the existing getAnyRecipeById function need to be extended for custom recipes?

It is extended to check the ID prefix: if the ID starts with `CUSTOM_RECIPE_PREFIX` (`'custom-'`), it reads from `localStorage` `CUSTOM_RECIPES`; otherwise it calls `lookup.php?i=`. This routing is applied consistently everywhere the app looks up a recipe by ID.

**Score**: 2/2 — prefix-based routing, both branches (localStorage vs network), and "everywhere" scope all stated

---

**Q43**: What is Safety Rule #3 and what problem does it prevent?

Safety Rule #3: `CUSTOM_RECIPE_PREFIX = 'custom-'`. All custom recipe IDs must begin with `'custom-'`. This prevents collision with TheMealDB IDs, which are plain integers (e.g., `52772`). If a custom recipe had ID `"52772"`, `getAnyRecipeById` would be unable to determine whether to look in localStorage or call TheMealDB — the prefix makes the routing unambiguous.

**Score**: 2/2 — prefix value, collision scenario with integer IDs, and routing ambiguity consequence all stated

---

**Q44**: How does image URL validation work for custom recipe images?

When the user enters an image URL, a hidden `<img>` element's `src` is set to that URL. Its `onload` event confirms the URL resolves to a loadable image (accepted). Its `onerror` event marks it as invalid (rejected with inline error). Only the URL string is stored — image binary data is never fetched or stored.

**Score**: 2/2 — hidden img, onload/onerror mechanism, URL-only storage all stated

---

**Q45**: How are custom recipes exported and imported?

Export: `JSON.stringify` of the full `CUSTOM_RECIPES` array, wrapped in a `Blob`, downloaded by programmatically clicking an `<a>` element with `href = URL.createObjectURL(blob)`. The file has a `.json` extension. Import: a `<input type="file">` accepts a file; `FileReader.readAsText` reads it; `JSON.parse` deserializes; each recipe is validated for required fields and a valid `'custom-'` prefix before being written to localStorage.

**Score**: 2/2 — blob URL export mechanism and FileReader + validation import process both fully described

---

**Q46**: Why does createRecipeCard use textContent instead of innerHTML for user-provided data?

Using `innerHTML` would allow XSS if a custom recipe's title or description contains HTML tags or `<script>` content. `textContent` inserts content as literal text without HTML parsing, preventing injection. Applied to all user-provided fields: title, description, ingredient display.

**Score**: 2/2 — XSS risk, textContent prevents HTML parsing, user-provided fields scope all stated

---

**Q47**: How does the star rating system work in the custom recipe form?

The star rating uses `<input type="radio">` elements (values 1–5) inside a container with `role="radiogroup"` and an `aria-label`. Keyboard navigation works via native radio button behavior (arrow keys within the group) — no JavaScript needed for navigation. The rating value is stored as a number on the Recipe object.

**Score**: 2/2 — radio inputs, radiogroup ARIA, native arrow-key behavior, stored as number all stated

---

**Q48**: How does the custom recipe form handle both add and edit mode?

A hidden input field holds the ID of the recipe being edited (empty for new recipes). On submit: if the ID field is empty, a new ID is generated as `CUSTOM_RECIPE_PREFIX + Date.now()`. If populated, the handler finds the matching entry in `CUSTOM_RECIPES` by ID and updates it in place. Same form component handles both modes.

**Score**: 2/2 — hidden ID field, empty → new ID generation, populated → in-place update, shared form all stated

---

**Q49**: Why is custom recipe data stored in localStorage rather than IndexedDB?

The data volume is small (personal recipe collection, unlikely to exceed tens of recipes). `JSON.stringify`/`JSON.parse` is sufficient for serialization. IndexedDB would add significant API complexity — async, transaction-based, cursor iteration — for no practical benefit at this scale.

**Score**: 2/2 — small data volume, JSON serialization sufficiency, and explicit IndexedDB complexity comparison all stated

---

**Q50**: What is the complete feature set at the end of S5?

Search, favorites (toggle + view), recipe detail modal with serving scaler and focus trapping, compound filter (AND logic, roving tabindex), search history (max 10, deduplicated). Custom recipe CRUD: add form (title, image URL validation, ingredients, star rating, description), edit mode, delete with confirmation, favorites integration via `getAnyRecipeById`. Export to JSON file, import from JSON with field + prefix validation. `createRecipeCard` uses `textContent` for user content. All three Safety Rules documented. Offline cache and deployment — S6.

**Score**: 2/2 — comprehensive S5 feature set with S6 boundary correctly identified

---

## Summary Scores

SCORES: Q41=2,Q42=2,Q43=2,Q44=2,Q45=2,Q46=2,Q47=2,Q48=2,Q49=2,Q50=2

**Total: 20 / 20**
