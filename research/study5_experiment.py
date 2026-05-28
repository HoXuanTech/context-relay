#!/usr/bin/env python3
"""
Study 5 Real Experiment — uses `claude --print` as the engine.
Each subprocess starts a FRESH Claude session with no access to this conversation.

Conditions:
  A_manual_compact   — free-form narrative summary (~1000 words)
  B_handoff          — structured decision/state document
  C_autocompact_sim  — aggressive ~400-word compression mimicking auto-compact

Flow per condition:
  1. Fresh Claude compresses S1 (does NOT see ground truth questions)
  2. Fresh Claude answers Q1–Q10 using ONLY the compressed context
  3. Fresh Claude scores each answer against ground truth (0/1/2)
"""

import subprocess, sys, json, re, textwrap
from pathlib import Path

CONTENT_FILE = Path("/Users/hoxuan/Desktop/context-relay/research/STUDY5_CONTENT.md")
OUT_DIR = Path("/Users/hoxuan/Desktop/context-relay/research")

def claude(prompt: str, max_words_hint: int = 2000) -> str:
    result = subprocess.run(
        ["claude", "--print"],
        input=prompt, text=True,
        capture_output=True, timeout=120
    )
    return result.stdout.strip()

# ── Extract S1 (lines 5–1008) ────────────────────────────────────────────────
lines = CONTENT_FILE.read_text().splitlines()
S1_RAW = "\n".join(lines[4:1008])   # 0-indexed: lines 5–1008
print(f"S1 raw: {len(S1_RAW.split())} words", flush=True)

# ── Ground truth ─────────────────────────────────────────────────────────────
QUESTIONS = [
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
]
GROUND_TRUTH = {
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
}

# ── Compression prompts ───────────────────────────────────────────────────────
COMPRESS_PROMPTS = {
    "A_manual_compact": textwrap.dedent("""
        Summarize the following vibe coding session in ~1000 words of continuous prose (no bullet points, no headers).
        Cover: what was built, key technical decisions with exact values, any permanent constraints locked in, and what remains undone.
        Be precise — include exact key strings, endpoint paths, schema field names.

        <session>
        {content}
        </session>
    """),
    "B_handoff": textwrap.dedent("""
        Write a structured handoff document for the following vibe coding session using this exact format:

        # Handoff - recipe-collector - Session 1

        ## Current Goal
        [one line]

        ## Key Decisions
        - [decision] → [reasoning]

        ## Completed This Session
        - [bullet list with exact values]

        ## Safety Rules
        - [permanent constraints, exact key strings]

        ## Next Actions
        - [what to do next]

        ## Recon Notes
        - [specific values, endpoints, schema details]

        <session>
        {content}
        </session>
    """),
    "C_autocompact_sim": textwrap.dedent("""
        You are a context compaction system. Compress the following conversation to ~400 words.
        Preserve: locked constants/keys with exact values, permanent decisions, current build state, specific API endpoints.
        Drop: conversational filler, exploratory discussion, anything with no forward implication.
        Output ONLY the compressed text.

        <session>
        {content}
        </session>
    """),
}

# ── QA prompt ─────────────────────────────────────────────────────────────────
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

# ── Scoring prompt ────────────────────────────────────────────────────────────
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

# ── Run one condition ─────────────────────────────────────────────────────────
def run_condition(label: str, compress_tmpl: str) -> dict:
    print(f"\n{'='*55}", flush=True)
    print(f"CONDITION: {label}", flush=True)
    print("─"*55, flush=True)

    # Step 1: compress
    print("  [1/3] Compressing S1 (fresh Claude, blind to questions)...", flush=True)
    compressed = claude(compress_tmpl.format(content=S1_RAW))
    wc = len(compressed.split())
    print(f"        → {wc} words", flush=True)

    (OUT_DIR / f"STUDY5_REAL_{label}.md").write_text(
        f"# Real Compression — {label}\nWord count: {wc}\n\n---\n\n{compressed}"
    )

    # Step 2+3: QA + score
    print("  [2/3] Q1–Q10 (fresh Claude per question)...", flush=True)
    rows = []
    total = 0
    for qid, question in QUESTIONS:
        answer = claude(qa_prompt(compressed, question))
        raw_score = claude(score_prompt(GROUND_TRUTH[qid], answer))
        s = extract_score(raw_score)
        total += s
        rows.append({"q": qid, "score": s, "answer": answer[:120]})
        print(f"        {qid}: {s}/2", flush=True)

    print(f"  TOTAL: {total}/20", flush=True)
    return {"label": label, "word_count": wc, "total": total,
            "compressed_preview": compressed[:300], "rows": rows}

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Study 5 Real Experiment — claude --print as blind engine")
    print(f"S1: {len(S1_RAW.split())} words → compress → QA → score\n")

    all_results = {}
    for label, tmpl in COMPRESS_PROMPTS.items():
        all_results[label] = run_condition(label, tmpl)

    # ── Summary table ─────────────────────────────────────────────────────────
    print("\n" + "="*55)
    print("RESULTS SUMMARY")
    print("="*55)
    print(f"{'Method':<22} {'Compressed':>10} {'Score':>8}")
    print("─"*42)
    for label, r in all_results.items():
        bar = "█" * r["total"] + "░" * (20 - r["total"])
        print(f"{label:<22} {r['word_count']:>8}w  {r['total']:>3}/20  {bar}")

    print("\nPer-question breakdown:")
    print(f"{'Q':<5}", end="")
    for label in all_results:
        print(f"  {label[:6]:>6}", end="")
    print()
    for i, (qid, _) in enumerate(QUESTIONS):
        print(f"{qid:<5}", end="")
        for label in all_results:
            s = all_results[label]["rows"][i]["score"]
            print(f"  {'✓✓' if s==2 else ('✓·' if s==1 else '✗✗'):>6}", end="")
        print()

    # ── Save JSON ──────────────────────────────────────────────────────────────
    out = OUT_DIR / "STUDY5_REAL_RESULTS.json"
    out.write_text(json.dumps(all_results, indent=2, ensure_ascii=False))
    print(f"\nFull results → {out}")
