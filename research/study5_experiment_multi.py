#!/usr/bin/env python3
"""
Study 5 Multi-Session Experiment — uses `claude --print` as the engine.
Tests T1–T6 (Q1–Q51) against pre-generated contexts from STUDY5_DATA_A and B.

Groups:
  A  — Auto-compaction chain (Summary1–Summary6 from DATA_A)
  B  — Handoff chain (Handoff1–Handoff6 from DATA_B)

Flow per group:
  For each test point T1–T6:
    Fresh Claude answers the 10 questions (or 1 for T6) using ONLY the
    pre-generated context for that test point.
    Fresh Claude scores each answer against ground truth (0/1/2).
"""

import subprocess, json, re, textwrap, time, sys
from pathlib import Path

DATA_A = Path("/Users/hoxuan/Desktop/context-relay/research/STUDY5_DATA_A.md")
DATA_B = Path("/Users/hoxuan/Desktop/context-relay/research/STUDY5_DATA_B.md")
OUT_DIR = Path("/Users/hoxuan/Desktop/context-relay/research")

CLAUDE_BIN = "/opt/homebrew/bin/claude"

def claude(prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            result = subprocess.run(
                [CLAUDE_BIN, "--print"],
                input=prompt, text=True,
                capture_output=True, timeout=120
            )
            text = result.stdout.strip()
            # Detect error responses (rate limit, auth issues, etc.)
            if result.returncode != 0 or not text or text.lower().startswith("error"):
                print(f"    [WARN] claude returned rc={result.returncode} text={repr(text[:60])}", flush=True)
                if attempt < retries - 1:
                    time.sleep(5)
                    continue
            time.sleep(0.5)  # pace calls to avoid rate limiting
            return text
        except Exception as e:
            print(f"    [ERR] attempt {attempt}: {e}", flush=True)
            if attempt < retries - 1:
                time.sleep(5)
    return ""

# ── Extract contexts from DATA files ─────────────────────────────────────────
def extract_sections(filepath: Path, markers: list[tuple[str, str]]) -> dict[str, str]:
    """Extract sections from a markdown file by start/end markers."""
    text = filepath.read_text()
    sections = {}
    for label, start_marker, end_marker in markers:
        start = text.find(start_marker)
        if start == -1:
            sections[label] = ""
            continue
        if end_marker:
            end = text.find(end_marker, start + len(start_marker))
            sections[label] = text[start:end].strip() if end != -1 else text[start:].strip()
        else:
            sections[label] = text[start:].strip()
    return sections

# DATA_A: Summary1–Summary6
A_MARKERS = [
    ("T1", "## Summary1 —", "## Summary2 —"),
    ("T2", "## Summary2 —", "## Summary3 —"),
    ("T3", "## Summary3 —", "## Summary4 —"),
    ("T4", "## Summary4 —", "## Summary5 —"),
    ("T5", "## Summary5 —", "## Summary6 —"),
    ("T6", "## Summary6 —", ""),
]

# DATA_B: Handoff1–Handoff6
B_MARKERS = [
    ("T1", "## Handoff1 —", "## Handoff2 —"),
    ("T2", "## Handoff2 —", "## Handoff3 —"),
    ("T3", "## Handoff3 —", "## Handoff4 —"),
    ("T4", "## Handoff4 —", "## Handoff5 —"),
    ("T5", "## Handoff5 —", "## Handoff6 —"),
    ("T6", "## Handoff6 —", ""),
]

CONTEXTS_A = extract_sections(DATA_A, A_MARKERS)
CONTEXTS_B = extract_sections(DATA_B, B_MARKERS)

for tp, ctx in CONTEXTS_A.items():
    print(f"A/{tp}: {len(ctx.split())} words", flush=True)
for tp, ctx in CONTEXTS_B.items():
    print(f"B/{tp}: {len(ctx.split())} words", flush=True)

# ── Questions by test point ──────────────────────────────────────────────────
QUESTIONS_BY_TP = {
    "T1": [
        ("Q1",  "What is Safety Rule #1 and where is it stored?"),
        ("Q2",  "Which recipe API was chosen in S1, and why was it selected over alternatives?"),
        ("Q3",  "What is the shape of the unified Recipe schema established in S1?"),
        ("Q4",  "How does the app handle broken or missing recipe images?"),
        ("Q5",  "What are the TheMealDB API endpoints used for searching and looking up a recipe by ID?"),
        ("Q6",  "What TheMealDB endpoints are used to fetch the list of categories and areas?"),
        ("Q7",  "Why are ingredients stored as [{name, measure}] objects rather than a flat string array?"),
        ("Q8",  "What is the file load order of the JavaScript modules established in S1?"),
        ("Q9",  "Why was localStorage chosen to store favorites rather than a backend or IndexedDB?"),
        ("Q10", "What is built and working at the end of S1?"),
    ],
    "T2": [
        ("Q11", "What is the exact localStorage key used for favorites, and what is the carry-forward rule about it?"),
        ("Q12", "How are ingredients structured in the Recipe schema, and why does this matter for future sessions?"),
        ("Q13", "What is Safety Rule #2 and what does it prohibit?"),
        ("Q14", "How does loadFavorites work — what does it do with the stored ID strings?"),
        ("Q15", "How does the toggleFavorite function work?"),
        ("Q16", "What is the two-grid architecture introduced in S2?"),
        ("Q17", "Why are favorites stored as ID strings instead of full Recipe objects, given that loading them requires extra network calls?"),
        ("Q18", "What try/catch pattern is used when reading from localStorage?"),
        ("Q19", "What functionality is complete at the end of S2?"),
        ("Q20", "Why does the favorites view require network calls on load rather than showing stored data immediately?"),
    ],
    "T3": [
        ("Q21", "What carry-forward constraint from S2 applies to the detail view being built in S3?"),
        ("Q22", "How is the detail view triggered — what data does the grid click handler pass to the modal?"),
        ("Q23", "Why was a div overlay used for the recipe detail modal instead of the native HTML dialog element?"),
        ("Q24", "How does the modal handle focus trapping and keyboard dismissal?"),
        ("Q25", "How does parseQuantity handle fractions like '1/2' and floating-point rounding?"),
        ("Q26", "How does the serving scaler work — what is the default serving count and how are quantities scaled?"),
        ("Q27", "Is there a carry-forward rule about the modal implementation established in S3?"),
        ("Q28", "What ARIA attributes does the modal div use to communicate its role to screen readers?"),
        ("Q29", "How does the app handle measures that cannot be parsed as numbers (e.g., 'to taste', 'as needed')?"),
        ("Q30", "What is complete at the end of S3?"),
    ],
    "T4": [
        ("Q31", "What constraint from S3 carries into S4's filter UI implementation?"),
        ("Q32", "How does the compound filter work — what logic is applied when both a category and an area are selected?"),
        ("Q33", "How is search history stored and managed?"),
        ("Q34", "What is roving tabindex and how is it implemented for the filter chips?"),
        ("Q35", "Why was AND logic chosen for the compound filter instead of OR?"),
        ("Q36", "Is the STORAGE_KEYS.SEARCH_HISTORY key subject to the same 'never change' rule as FAVORITES?"),
        ("Q37", "How does the filter chip clear/reset work — how does a user remove an active filter?"),
        ("Q38", "Where does the filter chip data (category names and area names) come from?"),
        ("Q39", "Why is display:none used to hide non-matching recipes rather than removing and re-rendering cards?"),
        ("Q40", "What is the complete feature set at the end of S4?"),
    ],
    "T5": [
        ("Q41", "What carry-forward rule from S4 applies to the custom recipe feature being built in S5?"),
        ("Q42", "How does the existing getAnyRecipeById function need to be extended for custom recipes?"),
        ("Q43", "What is Safety Rule #3 and what problem does it prevent?"),
        ("Q44", "How does image URL validation work for custom recipe images?"),
        ("Q45", "How are custom recipes exported and imported?"),
        ("Q46", "Why does createRecipeCard use textContent instead of innerHTML for user-provided data?"),
        ("Q47", "How does the star rating system work in the custom recipe form?"),
        ("Q48", "How does the custom recipe form handle both add and edit mode?"),
        ("Q49", "Why is custom recipe data stored in localStorage rather than IndexedDB?"),
        ("Q50", "What is the complete feature set at the end of S5?"),
    ],
    "T6": [
        ("Q51", "Describe the complete Recipe Collector architecture: persistence layers, key constants, all Safety Rules, file load order, and the most important implementation constraints from all six sessions."),
    ],
}

# ── Ground truths ────────────────────────────────────────────────────────────
GROUND_TRUTH = {
    # T1 — after S1
    "Q1":  "Safety Rule #1: STORAGE_KEYS.FAVORITES = 'recipe-favorites'. Must never change. Changing orphans saved favorites. Stored in constants.js.",
    "Q2":  "TheMealDB. Free, no API key, CORS-open for direct browser fetch. Alternatives required paid plans or server-side proxies.",
    "Q3":  "{id, title, thumbnail, category, area, tags, ingredients [{name, measure}], youtubeUrl, sourceUrl}. ingredients is array of {name, measure} objects.",
    "Q4":  "img onerror handler sets e.target.src = PLACEHOLDER_IMAGE. PLACEHOLDER_IMAGE is a constant in constants.js.",
    "Q5":  "Search: search.php?s={query}. Lookup: lookup.php?i={id}. Base URL: https://www.themealdb.com/api/json/v1/1/",
    "Q6":  "Categories: categories.php. Areas: list.php?a=list",
    "Q7":  "S3 serving scaler needs numeric quantity separate from unit. Object shape allows direct access; flat string requires re-parsing.",
    "Q8":  "constants.js → mapper.js → api.js → ui.js → app.js. No build bundler.",
    "Q9":  "Personal tool, no auth, no backend. Favorites are small (ID strings), 5MB limit fine. IndexedDB adds complexity without benefit.",
    "Q10": "Search functional. Recipe cards render. Image onerror fallback. Recipe schema in place. STORAGE_KEYS.FAVORITES locked. Favorites toggle NOT wired — that is S2.",
    # T2 — after S2
    "Q11": "STORAGE_KEYS.FAVORITES = 'recipe-favorites'. Never change — renaming silently orphans all saved favorites. Stored in constants.js.",
    "Q12": "ingredients: [{name, measure}] objects. S3 serving scaler needs numeric quantity separate from unit — object shape allows direct access.",
    "Q13": "Safety Rule #2: favorites stored as JSON array of ID strings only. Full Recipe objects must never be stored. Reasons: 5MB localStorage limit; architectural clarity (index vs data).",
    "Q14": "loadFavorites reads ID array from localStorage. For each ID calls lookup.php?i= to fetch full Recipe. Renders results to favoritesGrid.",
    "Q15": "toggleFavorite reads ID array (JSON.parse), adds or removes ID, writes back (JSON.stringify). Updates heart icon on card.",
    "Q16": "searchGrid and favoritesGrid both persist in DOM. Tab switching shows/hides with display toggle. Search results preserved across tab switches — no re-fetch.",
    "Q17": "Explicit tradeoff accepted: IDs avoid 5MB localStorage limit. Personal tool = small favorites list. Network calls acceptable.",
    "Q18": "JSON.parse in try/catch on every localStorage read. Catch returns empty array as default — corrupted data does not crash.",
    "Q19": "Search with result cards, favorites toggle (heart icon, localStorage), favorites view (fetch + render), two-tab navigation. Recipe detail modal is S3.",
    "Q20": "Safety Rule #2 prohibits storing full Recipe objects. Only IDs stored. Full data must be fetched via lookup.php?i= per ID on load.",
    # T3 — after S3
    "Q21": "Safety Rule #2 carries forward: full Recipe objects not stored in localStorage. Detail view reads from in-memory recipeCache, not localStorage.",
    "Q22": "Click handler reads data-recipeId from card. Looks up Recipe from recipeCache. Passes full Recipe object to modal open function.",
    "Q23": "Three reasons: ::backdrop inconsistency between Chrome/Firefox; returnFocus behavior differs; polyfilling <dialog> adds maintenance cost.",
    "Q24": "keydown listener traps Tab/Shift+Tab within focusable modal elements. Opens with .focus() on close button. Escape key and backdrop click dismiss. Return focus to triggering card element.",
    "Q25": "Splits on / for fractions (1/2 → 0.5). Applies Math.round(value * 100) / 100 for float safety. Non-numeric strings returned unchanged.",
    "Q26": "Default serving count is 4. +/- buttons adjust count (min 1). Quantities scaled by newServings/originalServings. parseQuantity handles fraction/non-numeric cases.",
    "Q27": "Yes — all modals must use div overlay with role=dialog and manual focus trapping. No native <dialog> element ever. Applies to all future overlay UI.",
    "Q28": "role='dialog', aria-modal='true', aria-labelledby pointing to modal heading element.",
    "Q29": "parseQuantity returns non-numeric string unchanged. Serving scaler displays original measure string as-is without scaling.",
    "Q30": "Search, favorites toggle + view, recipe detail modal (full ingredients, serving scaler, focus trapping, Escape + backdrop dismiss, return-focus, YouTube + source links).",
    # T4 — after S4
    "Q31": "Modal-as-div rule from S3 carries forward: all overlay UI must use <div> with role=dialog, not native <dialog>.",
    "Q32": "AND logic. Both category and area must match. currentFilters = {category: string|null, area: string|null}. Non-matching cards hidden with display:none.",
    "Q33": "STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history'. Max 10 entries, oldest evicted. Deduplicated (exact duplicates removed before prepend). Shown as chips on input focus.",
    "Q34": "One chip has tabindex=0, all others tabindex=-1. Arrow keys move focus and transfer tabindex=0. Tab exits the chip group.",
    "Q35": "User wanted to narrow results by combining filters (e.g., Italian AND Dessert). OR would expand results — opposite of intent.",
    "Q36": "Yes. STORAGE_KEYS.SEARCH_HISTORY = 'recipe-search-history' is permanent once data exists. Same never-change rule as FAVORITES.",
    "Q37": "Clicking an already-active chip deselects it (sets field back to null). No separate Clear button needed.",
    "Q38": "Category names from categories.php. Area names from list.php?a=list. Both fetched on app load.",
    "Q39": "Re-rendering discards fetched recipe data. display:none preserves DOM nodes and data-recipeId attributes — faster filter changes, no re-fetch.",
    "Q40": "Search, favorites, recipe detail modal (serving scaler, focus trapping), compound category+area filter (AND logic, roving tabindex), search history (localStorage, max 10, deduplicated, auto-shown on input focus).",
    # T5 — after S5
    "Q41": "localStorage key stability rule: any new key must be defined in STORAGE_KEYS in constants.js and treated as permanent. Led to STORAGE_KEYS.CUSTOM_RECIPES = 'recipe-custom'.",
    "Q42": "Extended to check ID prefix: 'custom-' prefix → read from localStorage CUSTOM_RECIPES; otherwise call lookup.php?i=. Routing applied consistently throughout app.",
    "Q43": "Safety Rule #3: CUSTOM_RECIPE_PREFIX = 'custom-'. All custom IDs must start with 'custom-'. Prevents collision with TheMealDB integer IDs in getAnyRecipeById.",
    "Q44": "Hidden <img> src set to URL. onload = valid. onerror = invalid. Submit blocked until validation passes or user skips. No server-side check.",
    "Q45": "Export: JSON.stringify → Blob → programmatic <a> click with createObjectURL. .json extension. Import: <input type=file> → FileReader.readAsText → JSON.parse → validate fields + custom- prefix → write to CUSTOM_RECIPES.",
    "Q46": "innerHTML would allow XSS if custom recipe title/description contains HTML or <script>. textContent inserts literal text, no HTML parsing.",
    "Q47": "<input type=radio> values 1-5, role=radiogroup, aria-label. Arrow key navigation via native radio behavior.",
    "Q48": "Hidden input holds ID of recipe being edited (empty for new). On submit: empty ID = new recipe with CUSTOM_RECIPE_PREFIX + Date.now(). Populated ID = update existing record in CUSTOM_RECIPES array.",
    "Q49": "Small data volume (personal collection). JSON.stringify/parse sufficient. IndexedDB adds significant API complexity without benefit at this scale.",
    "Q50": "Search, favorites, detail modal + serving scaler + focus trapping, compound filter + roving tabindex, search history, full custom recipe CRUD (add/edit/delete, image URL validation, star rating, export/import), XSS-safe card rendering, getAnyRecipeById routing.",
    # T6 — after S6
    "Q51": "File load order: constants→mapper→api→ui→favorites→customRecipes→app. Three Safety Rules: #1 STORAGE_KEYS.FAVORITES='recipe-favorites' never change; #2 favorites as ID strings only; #3 CUSTOM_RECIPE_PREFIX='custom-' prevents ID collision. Three persistence layers: memory (recipeCache, currentFilters), localStorage (three locked keys), Cache API (recipe-collector-v1, categories.php + list.php?a=list, 24h TTL via X-Cached-At, graceful degradation). Key constraints: div overlay modal with role=dialog, no native <dialog>; parseQuantity fraction+float handling; AND compound filter; roving tabindex; textContent for user content; getAnyRecipeById routing; loading=lazy on card images only.",
}

# ── QA + Scoring prompts ─────────────────────────────────────────────────────
def qa_prompt(context: str, question: str) -> str:
    return textwrap.dedent(f"""
        You have the following context document. Answer the question using ONLY what is stated in the context.
        If the information is absent, reply exactly: NOT IN CONTEXT

        <context>
        {context}
        </context>

        Question: {question}

        Answer with specific values (exact key strings, URLs, field names) where available. Be concise.
    """)

def score_prompt(gt: str, answer: str) -> str:
    return textwrap.dedent(f"""
        Score this answer against the ground truth. Reply ONLY with one of:
        SCORE:2  (all key facts present — exact values, both parts of multi-part answers)
        SCORE:1  (some key facts correct, missing important details)
        SCORE:0  (wrong, incomplete, or "not in context")

        Ground truth: {gt}
        Answer: {answer}
    """)

def extract_score(text: str) -> int:
    m = re.search(r'SCORE:\s*([012])', text)
    return int(m.group(1)) if m else 0

# ── Run one test point for one group ─────────────────────────────────────────
def run_test_point(group: str, tp: str, context: str) -> dict:
    questions = QUESTIONS_BY_TP[tp]
    max_score = len(questions) * 2
    print(f"\n  [{group}/{tp}] {len(questions)} questions (max {max_score}pts)...", flush=True)

    rows = []
    total = 0
    for qid, question in questions:
        answer = claude(qa_prompt(context, question))
        raw_score = claude(score_prompt(GROUND_TRUTH[qid], answer))
        s = extract_score(raw_score)
        total += s
        rows.append({"q": qid, "score": s, "answer": answer[:150]})
        print(f"    {qid}: {s}/2", flush=True)

    print(f"  → {group}/{tp}: {total}/{max_score}", flush=True)
    return {"group": group, "tp": tp, "total": total, "max": max_score, "rows": rows}

# ── Known results from previous runs ─────────────────────────────────────────
PREVIOUS_A = {
    "T1": {"group": "A", "tp": "T1", "total": 18, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(1,11), [2,2,2,2,2,2,2,2,0,2])]},
    "T2": {"group": "A", "tp": "T2", "total": 19, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(11,21), [2,2,1,2,2,2,2,2,2,2])]},
    "T3": {"group": "A", "tp": "T3", "total": 17, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(21,31), [1,0,2,2,2,2,2,2,2,2])]},
    "T4": {"group": "A", "tp": "T4", "total": 15, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(31,41), [0,2,2,2,0,2,2,2,1,2])]},
    "T5": {"group": "A", "tp": "T5", "total": 16, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(41,51), [0,2,2,2,2,2,2,2,0,2])]},
    "T6": {"group": "A", "tp": "T6", "total": 2, "max": 2,
           "rows": [{"q": "Q51", "score": 2, "answer": ""}]},
}

PREVIOUS_B = {
    "T1": {"group": "B", "tp": "T1", "total": 17, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(1,11), [2,2,2,2,1,2,2,2,0,2])]},
    "T2": {"group": "B", "tp": "T2", "total": 16, "max": 20,
           "rows": [{"q": f"Q{i}", "score": s, "answer": ""} for i, s in
                    zip(range(11,21), [1,0,2,2,2,2,2,2,1,2])]},
}

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Study 5 Multi-Session Experiment — T1–T6, Q1–Q51")
    print("Groups: A (auto-compaction summaries) vs B (handoff documents)\n")
    print("NOTE: A all + B/T1-T2 loaded from previous runs. Running B/T3-T6 only.\n")

    results = {"A": dict(PREVIOUS_A), "B": dict(PREVIOUS_B)}

    for group, contexts in [("B", CONTEXTS_B)]:
        print(f"\n{'='*60}", flush=True)
        print(f"GROUP {group}", flush=True)
        print("="*60, flush=True)
        for tp in ["T1", "T2", "T3", "T4", "T5", "T6"]:
            # Skip already-completed test points
            if group == "A" and tp in PREVIOUS_A:
                print(f"  [A/{tp}] skipped — loaded from previous run", flush=True)
                continue
            if group == "B" and tp in PREVIOUS_B:
                print(f"  [B/{tp}] skipped — loaded from previous run", flush=True)
                continue
            ctx = contexts[tp]
            if not ctx:
                print(f"  WARN: no context for {group}/{tp}", flush=True)
                continue
            r = run_test_point(group, tp, ctx)
            results[group][tp] = r

    # ── Summary table ─────────────────────────────────────────────────────────
    print("\n\n" + "="*70)
    print("RESULTS SUMMARY")
    print("="*70)

    # Per test point comparison
    tp_labels = ["T1", "T2", "T3", "T4", "T5"]
    tp_max    = [20,   20,   20,   20,   20]
    t6_max    = 2

    print(f"\n{'Test Point':<12} {'A (auto-compact)':>18} {'B (handoff)':>14} {'Winner':>8}")
    print("─"*56)
    a_weighted = 0
    b_weighted = 0
    weight_total = 0
    for i, tp in enumerate(tp_labels):
        w = i + 1
        ar = results.get("A", {}).get(tp, {})
        br = results.get("B", {}).get(tp, {})
        a_score = ar.get("total", 0)
        b_score = br.get("total", 0)
        a_pct = a_score / tp_max[i] * 100
        b_pct = b_score / tp_max[i] * 100
        winner = "A" if a_pct > b_pct else ("B" if b_pct > a_pct else "tie")
        print(f"{tp:<12} {a_score:>4}/{tp_max[i]} ({a_pct:4.1f}%)   {b_score:>4}/{tp_max[i]} ({b_pct:4.1f}%)  {winner:>6}")
        a_weighted += a_score * w
        b_weighted += b_score * w
        weight_total += tp_max[i] * w

    # T6
    ar6 = results.get("A", {}).get("T6", {})
    br6 = results.get("B", {}).get("T6", {})
    a6 = ar6.get("total", 0)
    b6 = br6.get("total", 0)
    print(f"{'T6 (arch)':<12} {a6:>4}/{t6_max}            {b6:>4}/{t6_max}")

    print("─"*56)
    a_comp_pct = a_weighted / weight_total * 100
    b_comp_pct = b_weighted / weight_total * 100
    print(f"{'Weighted (T1×1..T5×5)':<12} {a_weighted:>4}/{weight_total} ({a_comp_pct:4.1f}%)   {b_weighted:>4}/{weight_total} ({b_comp_pct:4.1f}%)")

    # Per-question breakdown
    print("\n\nPer-question breakdown:")
    all_qids = []
    for tp in ["T1", "T2", "T3", "T4", "T5", "T6"]:
        qs = QUESTIONS_BY_TP[tp]
        all_qids.extend([qid for qid, _ in qs])

    print(f"{'Q':<6}  {'A':>3}  {'B':>3}")
    print("─"*16)

    a_rows_all = {}
    b_rows_all = {}
    for tp in ["T1", "T2", "T3", "T4", "T5", "T6"]:
        for row in results.get("A", {}).get(tp, {}).get("rows", []):
            a_rows_all[row["q"]] = row["score"]
        for row in results.get("B", {}).get(tp, {}).get("rows", []):
            b_rows_all[row["q"]] = row["score"]

    for qid in all_qids:
        a_s = a_rows_all.get(qid, "?")
        b_s = b_rows_all.get(qid, "?")
        a_sym = "✓✓" if a_s == 2 else ("✓·" if a_s == 1 else "✗✗")
        b_sym = "✓✓" if b_s == 2 else ("✓·" if b_s == 1 else "✗✗")
        print(f"{qid:<6}  {a_sym:>3}  {b_sym:>3}")

    # ── Save JSON ──────────────────────────────────────────────────────────────
    out = OUT_DIR / "STUDY5_MULTI_RESULTS.json"
    summary = {
        "a_weighted": a_weighted,
        "b_weighted": b_weighted,
        "weight_total": weight_total,
        "a_composite_pct": round(a_comp_pct, 1),
        "b_composite_pct": round(b_comp_pct, 1),
        "t6": {"A": a6, "B": b6},
        "by_test_point": {
            tp: {
                "A": results.get("A", {}).get(tp, {}).get("total"),
                "B": results.get("B", {}).get(tp, {}).get("total"),
            }
            for tp in ["T1", "T2", "T3", "T4", "T5", "T6"]
        },
        "raw": results,
    }
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"\nFull results → {out}")
