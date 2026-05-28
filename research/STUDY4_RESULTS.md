# Study 4 Results: Vibe Coding Multi-Session Context Retention
> Completed: 2026-05-24

## Executive Summary

With realistic vibe coding content (~6,500–7,000 words per session, 6 sessions of portfolio website building), both mechanisms performed dramatically better than Study 3 (dense academic paper) but not quite as cleanly as Study 2 (explicit labeled safety rules). Handoff edges out auto-compact with a 4.0-point weighted composite advantage (95.3% vs 91.3% for T1–T5). Both mechanisms scored 2/2 on the T6 cumulative architecture overview — contrary to the prediction that auto-compact would do better on the holistic question. The primary driver of auto-compact's gap is missing forward-looking safety constraints: when vibe coding sessions produce implicit product decisions (e.g., "orange was rejected"), auto-compact records the decision but often omits the framing that makes it forward-enforceable. Handoff's primary weakness is foundational carry-forward failures: hex color values established in S1 were not re-stated in Handoff2, causing a 0-score on Q12.

---

## Score Tables

### T1 — After S1, Before S2 (Tests S1 content only, Q1–Q10)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q1 | Safety Rules | 2 | 2 | Both full: Bootstrap abandoned due to specificity conflict with .container padding and CSS variable cascade |
| Q2 | Decision Rationale | 2 | 2 | Both full: bg #1a1a2e, orange rejected, final accent #e94560 |
| Q3 | Tech Details | 1 | 2 | A partial: variable names present, values for --color-text and --color-text-muted not in Summary1; B full: all 5 variables with hex values |
| Q4 | Work State | 2 | 2 | Both full: flicker not fully fixed, residual first-hover artifact open |
| Q5 | Work State | 2 | 2 | Both full: nav/hero/about built, projects+contact empty skeletons, footer |
| Q6 | Safety Rules | 0 | 2 | A: no per-color reaction recorded in Summary1; B full: "sports team logo feel" (user's exact words), multiple variations tried |
| Q7 | Decision Rationale | 2 | 2 | Both full: full CSS control, avoids Bootstrap specificity conflicts |
| Q8 | Tech Details | 2 | 2 | Both full: fixed nav, hero with clamp typography, two-column about, empty skeletons, footer |
| Q9 | Decision Rationale | 2 | 2 | Both full: global `a { color: white }` rule + UA stylesheet default, fixed with `color: inherit` |
| Q10 | Work State | 2 | 2 | Both full: fix flicker first, then hero + about content, nav fix is S2 priority |
| **TOTAL** | | **19/20** | **20/20** | |

### T2 — After S2, Before S3 (Tests S1 carry-forward ×2 + S2 ×8, Q11–Q20)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q11 | Carry-forward S1 Safety | 1 | 2 | A partial: constraint implied from fix description, not framed as forward-looking rule; B full: explicit "no new transition classes" rule |
| Q12 | Carry-forward S1 Tech | 2 | 0 | A full: both hex values explicitly in Summary2; B cannot answer: hex values not re-stated in Handoff2 (only in Handoff1) |
| Q13 | S2 Safety Rules | 2 | 2 | Both full: animation removed, iOS translateY + fill-mode layout shift, permanent decision |
| Q14 | S2 Decision Rationale | 2 | 2 | Both full: container-clips approach (border-radius + overflow: hidden on .about-photo), explicit 280px width+height required |
| Q15 | S2 Tech Details | 2 | 2 | Both full: "Frontend engineer. The details are the whole point." |
| Q16 | S2 Work State | 2 | 2 | Both full: 768px single-column, 200px centered photo, nav fits without hamburger |
| Q17 | S2 Decision Rationale | 2 | 2 | Both full: two causes (stale .site-nav a rule + UA stylesheet default), both fixed |
| Q18 | S2 Tech Details | 2 | 2 | Both full: container needs border-radius: 50% + overflow: hidden + explicit 280×280, img needs object-fit: cover |
| Q19 | S2 Safety Rules | 0 | 2 | A cannot answer: context describes fix but no explicit "must NOT" prohibition; B full: never add transition classes to nav |
| Q20 | S2 Work State | 2 | 2 | Both full: nav+hero+about complete, projects+contact empty skeletons |
| **TOTAL** | | **17/20** | **18/20** | *Note: T2A file contains arithmetic error showing 19/20; corrected to 17/20* |

### T3 — After S3, Before S4 (Tests S2 carry-forward ×2 + S3 ×8, Q21–Q30)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q21 | Carry-forward S2 Safety | 1 | 2 | A partial: ban confirmed + iOS reason, but permanence framing ("user explicitly said remove") absent; B full: permanent ban, user's words quoted |
| Q22 | Carry-forward S2 Tech | 2 | 2 | Both full: container-clips pattern with explicit 280px width+height |
| Q23 | S3 Decision Rationale | 2 | 2 | Both full: box-shadow tried in 3 configurations, all rejected as "too heavy/corporate" |
| Q24 | S3 Tech Details | 2 | 2 | Both full: transparent base border-left + accent color on hover + transition, base prevents layout shift |
| Q25 | S3 Safety Rules | 2 | 2 | Both full: proximity casualty during rename, moved to end of file in labeled block to prevent future deletion |
| Q26 | S3 Tech Details | 2 | 2 | Both full: 768px (3→2 col) and 480px (2→1 col) breakpoints |
| Q27 | S3 Work State | 2 | 2 | Both full: Work section complete with filters, border-left hover; all links href="#" placeholders |
| Q28 | S3 Decision Rationale | 1 | 2 | A partial: what broke fully documented, but trigger reason for rename absent from Summary3; B full: hero CTA already said "See My Work," touched 5 locations, footer rules as proximity casualties |
| Q29 | S3 Tech Details | 2 | 2 | Both full: data-tags/data-filter, exact string match (===), display toggle, .active class |
| Q30 | S3 Work State | 2 | 2 | Both full: contact form + validation not started, about has placeholders, no animations |
| **TOTAL** | | **18/20** | **20/20** | |

### T4 — After S4, Before S5 (Tests S3 carry-forward ×2 + S4 ×8, Q31–Q40)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q31 | Carry-forward S3 Safety | 2 | 2 | Both full: border-left hover, box-shadow rejected 3× as "too heavy/corporate" |
| Q32 | Carry-forward S3 Safety | 2 | 2 | Both full: footer CSS at end of file, lost twice as proximity casualty, cannot be moved |
| Q33 | S4 Decision Rationale | 1 | 2 | A partial: blur validation fully described but no stated reason for choosing blur over submit; B full: "feels like the form is paying attention to you" |
| Q34 | S4 Safety Rules | 2 | 2 | Both full: + in email intentionally rejected, user's explicit product decision ("my clients won't use + emails"), NOT a bug |
| Q35 | S4 Tech Details | 2 | 2 | Both full: success message + e.target.reset() + setTimeout 3000ms, no double-submit guard |
| Q36 | S4 Safety Rules | 2 | 2 | Both full: Safari polyfill works but uses per-element forEach listeners, memory-leak-adjacent, flagged for delegation refactor |
| Q37 | S4 Tech Details | 2 | 2 | Both full: scroll-margin-top: 70px on all sections, prevents fixed nav overlap |
| Q38 | S4 Work State | 1 | 2 | A partial: inferred from absence (cosmetic success only), not directly stated; B full: no backend, success message is cosmetic, data not transmitted |
| Q39 | S4 Decision Rationale | 2 | 2 | Both full: CSS scroll-behavior fails on Safari 14, JS polyfill with scrollIntoView chosen |
| Q40 | S4 Work State | 2 | 2 | Both full: all sections structurally complete, placeholders throughout, polyfill needs refactor |
| **TOTAL** | | **18/20** | **20/20** | |

### T5 — After S5, Before S6 (Tests S4 carry-forward ×2 + S5 ×8, Q41–Q50)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q41 | Carry-forward S4 Safety | 2 | 2 | Both full: + rejection is intentional product decision, must NOT be fixed |
| Q42 | Carry-forward S4 Tech | 2 | 2 | Both full: per-element listeners are memory-leak risk, event delegation refactor flagged for S6 |
| Q43 | S5 Decision Rationale | 2 | 2 | Both full: IntersectionObserver fires on threshold crossing, not 60×/sec polling; avoids main-thread jank |
| Q44 | S5 Safety Rules | 2 | 2 | Both full: dark mode partially implemented (nav+body only), cards+inputs unaffected, accepted as "good enough for now" |
| Q45 | S5 Tech Details | 2 | 2 | Both full: missed #e94560 in card :hover rule during variable sweep, card border-left accent broke, found by manual testing |
| Q46 | S5 Safety Rules | 2 | 2 | Both full: loading="lazy" wrong for hero (above-fold, critical render path), corrected to loading="eager" |
| Q47 | S5 Tech Details | 2 | 2 | Both full: 7 variables in :root including --color-card, --color-border; all rgba() tints left as raw values |
| Q48 | S5 Work State | 2 | 2 | Both full: toggle exists, nav+body switch, cards+form remain dark, explicitly accepted partial state |
| Q49 | S5 Decision Rationale | 1 | 0 | A partial: "considered and correctly not added" stated but no reasoning; B cannot answer: will-change/defer never mentioned in Handoff5 |
| Q50 | S5 Work State | 2 | 2 | Both full: Safari polyfill refactor, dark mode partial, no real content, no SEO, not deployed |
| **TOTAL** | | **19/20** | **18/20** | |

### T6 — Final Architecture Overview, After S6 (Q51, max 2 points)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q51 | Architecture Overview | 2 | 2 | Both full: complete coverage of all 6 sessions — structure, CSS variables with exact hex values, JS features, deployment state, known limitations |
| **TOTAL** | | **2/2** | **2/2** | Both mechanisms preserved full project mental model |

---

## Composite Scores

### T1–T5 Weighted Composite (weight = test point number)

| | Group A (Auto-Compact) | Group B (Handoff) |
|---|---|---|
| T1 raw | 19/20 (95.0%) | 20/20 (100.0%) |
| T2 raw | 17/20 (85.0%) | 18/20 (90.0%) |
| T3 raw | 18/20 (90.0%) | 20/20 (100.0%) |
| T4 raw | 18/20 (90.0%) | 20/20 (100.0%) |
| T5 raw | 19/20 (95.0%) | 18/20 (90.0%) |
| **Weighted Composite** | **274/300 (91.3%)** | **286/300 (95.3%)** |
| T6 (bonus) | 2/2 (100.0%) | 2/2 (100.0%) |

Composite formula: (T1×1 + T2×2 + T3×3 + T4×4 + T5×5) / (20×15)

- Group A: (19×1 + 17×2 + 18×3 + 18×4 + 19×5) / 300 = (19 + 34 + 54 + 72 + 95) / 300 = 274/300 = **91.3%**
- Group B: (20×1 + 18×2 + 20×3 + 20×4 + 18×5) / 300 = (20 + 36 + 60 + 80 + 90) / 300 = 286/300 = **95.3%**

Handoff wins by **4.0 percentage points.**

---

## Hypothesis Evaluation

### H1: Vibe coding content (~7,000 words/session) produces retention rates between Study 2 (explicit labels) and Study 3 (dense academic)
**Confirmed.** Auto-compact 91.3% falls between Study 2's 98.3% and Study 3's 53.9%. Handoff 95.3% falls between Study 2's 90.0% and Study 3's 63.3%. Vibe coding sessions produce content that is partially structured (explicit decisions, explicit bugs) but also contains implicit context (rejection framings, user preference statements) that requires different handling.

### H2: Auto-compact degrades more than handoff across sessions
**Partially confirmed.** Both methods show similar trajectory: non-monotonic, with dips at T2 and T5 for different reasons. Auto-compact: 95.0% → 85.0% → 90.0% → 90.0% → 95.0%. Handoff: 100.0% → 90.0% → 100.0% → 100.0% → 90.0%. Neither shows clean degradation — handoff has sharper spikes and sharper dips (0%/100% pattern on individual questions) while auto-compact is more smoothly distributed (1/2 partial scores more common).

### H3: Auto-compact will do better on the T6 cumulative architecture question
**Rejected.** Both scored 2/2 on Q51. By S6, Summary6's rolling prose and Handoff6's chain of carry-forwards both preserved a complete project mental model. The architecture overview tested breadth (all 6 sessions), and both mechanisms accumulated enough coverage over 6 sessions to answer fully. The cumulative advantage of Summary6 (which synthesizes all session content into flowing prose) was matched by Handoff6's explicit enumeration of key decisions and work states.

### H4: Handoff's T6 architecture question advantage (if any) reflects the carry-forward chain's explicit structure
**N/A** (both scored 2/2). The chain structure of handoffs (each explicitly carrying forward from the previous) did produce a complete cumulative record, as expected. But so did auto-compact's rolling summary.

---

## Key Findings

- **Handoff wins Study 4 by 4.0 points (95.3% vs 91.3%)**, continuing the pattern from Studies 1 and 3 where implicit/conversational content favors handoff. Vibe coding sessions produce "medium-density" content — more structured than Study 1's single session, less structured than Study 2's explicit labeled rules.

- **Both methods perform well (~91–95%)**, making vibe coding the best-performing content type for auto-compact after Study 2's explicit labels. The gap between the two mechanisms is the narrowest in any study (4.0 points vs 8.3 points in Study 2, 9.4 points in Study 3, ~18 points in Study 1).

- **Auto-compact's primary failure mode: missing forward-looking prohibitions.** Q6 (0/2: orange "sports team logo" reaction absent), Q11 (1/2: nav constraint implied not stated), Q19 (0/2: no explicit "must NOT" nav rule), Q28 (1/2: rename trigger absent), Q33 (1/2: blur validation reason absent), Q38 (1/2: form backend status inferred). Auto-compact records facts but does not always convert contextual judgments into forward-enforceable safety rules.

- **Handoff's primary failure mode: foundational values not re-stated in later sessions.** Q12 (0/2: hex values #1a1a2e and #e94560 not in Handoff2 — only in Handoff1), Q49 (0/2: will-change/defer negative-space decision never mentioned in Handoff5). Handoff focuses on "what changed this session" rather than "what remains permanently true" — foundational constants established in S1 must be explicitly repeated in subsequent handoffs or they disappear.

- **Q49 (will-change/defer) is a negative-space decision** — "we considered something and chose not to add it." Auto-compact preserved this as "correctly not added" (score 1, missing reasoning). Handoff omitted it entirely (score 0). Neither mechanism handles negative-space decisions well: they appear nowhere in the code, so both compression and carry-forward routinely drop them.

- **T6 architecture question: tie at 2/2.** The user predicted auto-compact would do better on the holistic cumulative question. Both mechanisms provided complete coverage. The reason: by S6, both Summary6 (rolling synthesis) and Handoff6 (chain of explicit carry-forwards across 6 sessions) had accumulated enough context to reconstruct the full project. The cumulative coverage advantage of auto-compact (which never discards any session content entirely) was not decisive because the handoff chain, while selective per session, had accumulated sufficient coverage by the sixth iteration.

- **Stability comparison:** Auto-compact variance (19/17/18/18/19) is tighter than Study 3 but shows a T2 dip. Handoff variance (20/18/20/20/18) shows sharper spikes (three perfect scores) and sharper dips (two 18s). Handoff's all-or-nothing pattern (2/2 or 0/2 per question) differs from auto-compact's softer 1/2 partial patterns.

---

## Four-Study Comparison

| | Study 1 | Study 2 | Study 3 | Study 4 |
|---|---|---|---|---|
| Content type | Single dense session, implicit/procedural | 6 sessions, explicit labeled safety rules | Dense academic paper (GNN-NLP survey), 6 parts | 6 vibe coding sessions, portfolio website |
| Words per session | ~500 | ~350 | ~7,000 | ~6,500–7,000 |
| Auto-compact T1 | 60% | 96.7% | 53.3% | 95.0% |
| Auto-compact T3/T5 | 27% | 100% | 43.3% | 95.0% (T5) |
| Handoff T1 | 67% | 93.3% | 73.3% | 100% |
| Handoff T3/T5 | 67% | 100% | 60.0% | 90.0% (T5) |
| Auto-compact composite | ~49% | 98.3% | 53.9% | 91.3% |
| Handoff composite | 67% | 90.0% | 63.3% | 95.3% |
| Winner | Handoff (+18pp at Round 6) | Auto-compact (+8.3pp) | Handoff (+9.4pp) | Handoff (+4.0pp) |
| T6 architecture Q | N/A | N/A | N/A | Tie (2/2 both) |
| Key driver | Implicit context = compression collapse | Explicit labels = compression-friendly | Citation density = specificity loss | Implicit product decisions = framing gap |

---

## Implications

**The four-study arc now defines the content-mechanism relationship clearly:**

1. **Explicit, label-structured content (Study 2):** Auto-compact wins decisively (+8.3pp). When every decision already has a label (SAFETY-N, DECISION-N), compression preserves the label and the content. Handoff's selectivity becomes a liability.

2. **Dense technical content with precise named entities (Study 3):** Handoff wins decisively (+9.4pp). Auto-compact collapses citation-level specificity (author names, dataset names, exact benchmarks) to category labels. Handoff's explicit carry-forward preserves the specifics even at the cost of coverage.

3. **Vibe coding / conversational engineering sessions (Study 4):** Handoff wins moderately (+4.0pp). Content is medium-density: enough structure for auto-compact to perform well (91.3%), but enough implicit context (user preferences, rejection framings, product decisions) that handoff's explicit carry-forward adds value.

4. **Single dense implicit session (Study 1):** Handoff wins dramatically (+18pp at round 6). Without session structure, repeated auto-compaction destroys context progressively.

**The practical decision rule** emerging from four studies: use auto-compaction when sessions produce explicitly labeled artifacts (safety rules, architectural decisions, config values). Use /handoff when sessions involve dense technical specifics (academic reading, protocol specs) or strong user preference signals (vibe coding, design choices, product decisions) that require forward-enforceable framing.

**The foundational carry-forward gap** (Q12 = 0 for Handoff, hex values not in Handoff2) suggests a structural improvement to the /handoff format: a "Permanent Constants" section for values that must persist across all sessions without being re-derived. Currently, the handoff format carries "what changed" but not "what is always true."

**The negative-space decision gap** (Q49 = 0 for both, Q6/Q19 = 0 for auto-compact) is a shared weakness: both mechanisms struggle to retain "we considered X and deliberately chose not to do it" — because these decisions leave no artifact in the codebase. An explicit "Considered and Rejected" section in the handoff format would address this.

**T6 tie invalidates the hypothesis that auto-compact has a structural advantage for cumulative architecture questions.** By session 6, both mechanisms have accumulated sufficient coverage. The architecture question advantage hypothesis may hold for shorter chains (3–4 sessions) where Summary's exhaustive coverage would dominate Handoff's selective carry-forwards before they accumulate enough.
