# Study 5 — T2 Test Answers (Agent B)
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY5_DATA_B.md § Handoff2 — T2 Test Context (after S2)
Date: 2026-05-27

---

**Q11**: What is the exact localStorage key used for favorites, and what is the carry-forward rule about it?

`'recipe-favorites'` — stated in Handoff2's Safety Rules as "Favorites key `'recipe-favorites'` still locked (Rule #1)." The carry-forward rule is that the key must never change.

**Score**: 2/2 — key string and "never change" rule both present

---

**Q12**: How are ingredients structured in the Recipe schema, and why does this matter for future sessions?

Handoff2 does not carry forward an explanation of ingredient object structure or the forward-planning rationale for S3. The schema is referred to ("unified Recipe schema") but the `{name, measure}` object shape and the serving-scaler motivation are not restated in Handoff2.

**Score**: 0/2 — information not present in Handoff2

---

**Q13**: What is Safety Rule #2 and what does it prohibit?

Safety Rule #2: favorites must be stored as a JSON array of ID strings only — never full Recipe objects. Justification from Key Decisions: "storing full Recipe objects would approach the 5MB localStorage limit; IDs are a few bytes each." The rule is explicit: "Favorites must be stored as ID string array only — never full Recipe objects. `loadFavorites` always fetches full data via network; this design is intentional, not an oversight."

**Score**: 2/2 — prohibition and size-limit justification both present; "intentional not oversight" emphasis noted

---

**Q14**: How does loadFavorites work — what does it do with the stored ID strings?

From Completed: "`loadFavorites`: reads ID array, calls `lookup.php?i=` per ID, renders results to `favoritesGrid`." One network call per ID to fetch full data before rendering.

**Score**: 2/2 — read IDs, one lookup per ID, render to favoritesGrid all stated

---

**Q15**: How does the toggleFavorite function work?

From Completed: "`toggleFavorite(id)`: reads ID array, adds or removes ID, writes back; updates heart icon state." Read-modify-write pattern via JSON.parse / JSON.stringify.

**Score**: 2/2 — all steps present (read, add/remove, write, UI update)

---

**Q16**: What is the two-grid architecture introduced in S2?

From Key Decisions: "Two-grid architecture → `searchGrid` and `favoritesGrid` both stay in DOM; switching tabs shows/hides rather than re-renders; search results preserved across tab switches."

**Score**: 2/2 — both grids persist in DOM, show/hide mechanism, search-preservation detail all present

---

**Q17**: Why are favorites stored as ID strings instead of full Recipe objects, given that loading them requires extra network calls?

From Key Decisions: "Favorites stored as ID strings only → storing full Recipe objects would approach 5MB localStorage limit; IDs are a few bytes each; `loadFavorites` fetches full data per ID on demand."

**Score**: 2/2 — 5MB limit, small size of IDs, and on-demand fetch pattern all stated

---

**Q18**: What try/catch pattern is used when reading from localStorage?

From Key Decisions: "All localStorage reads use `JSON.parse` in `try/catch` → corrupted data returns empty array, not a crash." And from Safety Rules: "Every localStorage read must use `JSON.parse` in `try/catch`; default to `[]` on parse error."

**Score**: 2/2 — try/catch pattern and empty-array default both explicit

---

**Q19**: What functionality is complete at the end of S2?

From Current Goal: "Favorites system is complete. Next session: recipe detail modal." From Completed: search UI (inherited from S1), `toggleFavorite`, `loadFavorites`, two-tab navigation. Modal not yet built — that is S3.

**Score**: 2/2 — completed features and not-yet-built modal distinction both clear

---

**Q20**: Why does the favorites view require network calls on load rather than showing stored data immediately?

Safety Rule #2 prohibits storing full Recipe objects — only IDs are stored. To display recipe cards with full data, `loadFavorites` must call `lookup.php?i=` per ID. Handoff2 explicitly states: "`loadFavorites` always fetches full data via network; this design is intentional."

**Score**: 2/2 — Rule #2 as root cause, network-fetch consequence, and explicit intentionality all present

---

## Summary Scores

SCORES: Q11=2,Q12=0,Q13=2,Q14=2,Q15=2,Q16=2,Q17=2,Q18=2,Q19=2,Q20=2

**Total: 18 / 20**
