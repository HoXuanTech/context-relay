# Study 5 Results: Multi-Session Vibe Coding (Recipe App)
> Completed: 2026-05-28
> Project: context-relay — /handoff skill for Claude Code

## Overview

Study 5 extended Study 4's vibe coding methodology with two key changes: (1) six sessions instead of five, and (2) a real API validation layer using `claude --print` subprocess calls to re-score all 51 questions with fresh, blind Claude sessions. This dual-scoring approach revealed a systematic inflation bias in the manual evaluation protocol used in Studies 1–4.

**Content**: Six sessions (~7,000 words each, 42,000 words total) building a vanilla JavaScript recipe collector app. Sessions covered: S1 (API selection, schema, project structure), S2 (favorites system, localStorage), S3 (recipe detail modal, serving scaler), S4 (compound filter, search history), S5 (custom recipe CRUD, export/import), S6 (Cache API, accessibility, deployment).

**Groups**: A = auto-compaction chain (Summary1–Summary6), B = handoff chain (Handoff1–Handoff6).

**Test points**: T1–T5 each had 10 questions (max 20pts); T6 had 1 architecture overview question (max 2pts). Weighted composite: (T1×1 + T2×2 + T3×3 + T4×4 + T5×5) / 300.

---

## Real API Scores (Primary Result)

*Scored by fresh Claude subprocess sessions, blind to ground truth during QA phase.*

| Test Point | Auto-compact (A) | Handoff (B) | Winner |
|---|:---:|:---:|:---:|
| T1 (after S1) | 18/20 (90.0%) | 17/20 (85.0%) | A |
| T2 (after S2) | 19/20 (95.0%) | 16/20 (80.0%) | A |
| T3 (after S3) | 17/20 (85.0%) | 15/20 (75.0%) | A |
| T4 (after S4) | 15/20 (75.0%) | 15/20 (75.0%) | tie |
| T5 (after S5) | 16/20 (80.0%) | 14/20 (70.0%) | A |
| **Weighted composite** | **247/300 (82.3%)** | **224/300 (74.7%)** | **A (+7.6pp)** |
| T6 architecture | 2/2 (100%) | 1/2 (50%) | A |

**Conclusion**: Auto-compact wins by 7.6 composite points in the real API test. Both methods perform well (75–95% per test point), with the gap widest at T2 (15pp) and T3 (10pp), narrowing to a tie at T4.

---

## Manual Scores (Reference — Inflation-Adjusted)

*Scored by the same model that wrote the answers, with full context available.*

| Test Point | Auto-compact (A) | Handoff (B) |
|---|:---:|:---:|
| T1 | 20/20 (100%) | 17/20 (85%) |
| T2 | 20/20 (100%) | 18/20 (90%) |
| T3 | 20/20 (100%) | 15/20 (75%) |
| T4 | 20/20 (100%) | 17/20 (85%) |
| T5 | 20/20 (100%) | 17/20 (85%) |
| **Weighted** | **300/300 (100%)** | **251/300 (83.7%)** |
| T6 | 2/2 | 1/2 |

Group A scored a perfect 300/300 manually — an implausible result that reveals a systematic evaluation flaw in the manual protocol. When the model evaluating Group A's answers has full access to the context document it is scoring against, it consistently awards 2/2 even for questions where the real API test reveals genuine recall failures. Group B was not immune (17/20 at T1 not inflated because the context was shorter and gaps more visible), but the inflation was less severe.

**Manual vs real API delta**:
- Group A: manual inflated by +53 points (+17.7pp) above real API score
- Group B: manual inflated by +27 points (+9.0pp) above real API score

This asymmetry explains why manual evaluations in Studies 1–4 systematically overstated auto-compact performance.

---

## Per-Question Breakdown

| Q | A (real) | B (real) | A (manual) | B (manual) | Both fail |
|---|:---:|:---:|:---:|:---:|:---:|
| Q1 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q2 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q3 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q4 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q5 | ✓✓ | ✓· | ✓✓ | ✓· | |
| Q6 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q7 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q8 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| **Q9** | **✗✗** | **✗✗** | ✓✓ | ✗✗ | **both fail** |
| Q10 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q11 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| **Q12** | ✓✓ | **✗✗** | ✓✓ | **✗✗** | B-specific |
| Q13 | ✓· | ✓✓ | ✓✓ | ✓✓ | |
| Q14 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q15 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q16 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q17 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q18 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q19 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| Q20 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q21 | ✓· | ✓· | ✓✓ | ✓· | |
| **Q22** | **✗✗** | **✗✗** | ✓✓ | **✗✗** | **both fail** |
| Q23 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q24 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q25 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q26 | ✓✓ | ✓· | ✓✓ | ✓· | |
| Q27 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q28 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q29 | ✓✓ | ✓✓ | ✓✓ | ✓· | |
| Q30 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| **Q31** | **✗✗** | **✗✗** | ✓✓ | **✗✗** | **both fail** |
| Q32 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q33 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q34 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q35 | ✗✗ | ✓✓ | ✓✓ | ✓✓ | A-specific |
| Q36 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q37 | ✓✓ | ✗✗ | ✓✓ | ✓· | B-specific |
| Q38 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q39 | ✓· | ✓✓ | ✓✓ | ✓✓ | |
| Q40 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| **Q41** | **✗✗** | **✗✗** | ✓✓ | ✓· | **both fail** |
| Q42 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q43 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q44 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| Q45 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q46 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q47 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| Q48 | ✓✓ | ✓✓ | ✓✓ | ✓✓ | |
| **Q49** | **✗✗** | **✗✗** | ✓✓ | **✗✗** | **both fail** |
| Q50 | ✓✓ | ✓· | ✓✓ | ✓✓ | |
| Q51 | ✓✓ | ✓· | ✓✓ | ✓· | |

---

## Failure Analysis

### Shared Failure Mode: "Why Not" Decisions

Questions Q9, Q22, Q31, Q41, Q49 all failed for both groups in the real API test. These share a common structure: **rationale for a road-not-taken**.

- **Q9**: Why localStorage over IndexedDB for favorites? (S1)
- **Q22**: How does the grid click handler access recipe data? (recipeCache, not localStorage — a deliberate architectural separation)
- **Q31**: Does the S3 modal-as-div rule carry into S4's chip UI? (It does, but only for modals — chips are not modal-like, so the rule applies differently)
- **Q41**: What S4 rule carries into S5? (The localStorage key permanence rule — abstract, not tied to a concrete artifact)
- **Q49**: Why localStorage over IndexedDB for custom recipes? (Same as Q9 but in a different session — neither context repeated the IndexedDB justification verbatim)

These questions require reasoning about absence or abstraction. Neither auto-compact nor handoff has a mechanism for preserving "we evaluated X and rejected it for reason Y." The rejection only survives if it was explicitly restated as a positive rule ("always use localStorage for small personal data") rather than a negative decision ("rejected IndexedDB because...").

### A-Specific Failure: Q35 (AND vs OR Filter Logic)

Q35 asks why AND logic was chosen for the compound filter. Auto-compact scored 0/2; handoff scored 2/2. The handoff document for T4 explicitly stated the user's rationale ("user wanted to narrow results — OR would expand"). The auto-compact summary described the filter's behavior correctly but dropped the design rationale. This is a known handoff advantage: user preference statements and design reasoning are more likely to be preserved in structured handoff sections.

### B-Specific Failures: Q12, Q37

- **Q12** (ingredients as objects vs flat strings): The handoff chain dropped this S1 decision at T2, consistent with the foundational carry-forward gap identified in Study 4.
- **Q37** (chip deselect mechanism): The handoff for T4 described the filter system broadly but omitted the specific "click active chip to deselect" interaction detail. Auto-compact preserved it because its rolling summary re-compressed both structural and interaction details.

### Manual Evaluation Bias

Group A's manual score of 300/300 (100%) is methodologically invalid. The model scoring A's answers had access to the same Summary document it was being asked to recall from — effectively an open-book test. Questions Q9, Q22, Q31, Q41, Q49 all scored 2/2 manually despite failing completely in real API conditions. The bias is strongest on "why not" questions because the model can infer the rationale from the context it is reading, even if the context doesn't directly state it.

Group B's manual scores were less inflated (+9pp delta vs +17.7pp for A) because handoff documents are shorter and more structured — missing information is more visually obvious when the document is 300 words and uses explicit headers.

---

## Cross-Study Comparison (Updated)

| Study | Content | Auto-compact | Handoff | Winner | Scoring method |
|---|---|:---:|:---:|:---:|:---:|
| Study 1 | Clean session log (re-compressed) | ~49% at R6 | 67% | Handoff (+18pp) | Manual |
| Study 2 | Clean labeled script | 98.3% | 90.0% | Auto-compact (+8.3pp) | Manual |
| Study 3 | Dense academic text | 53.9% | 63.3% | Handoff (+9.4pp) | Manual |
| Study 4 | Vibe coding (portfolio site) | 91.3% | 95.3% | Handoff (+4.0pp) | Manual |
| **Study 5** | **Vibe coding (recipe app)** | **82.3%** | **74.7%** | **Auto-compact (+7.6pp)** | **Real API** |

Study 5 is the only study evaluated with real API scoring. The Study 4 result (handoff wins) must be re-interpreted given the manual inflation finding: if manual scoring inflated A by ~18pp and B by ~9pp, adjusting Study 4's scores would shift A from 91.3% to ~73% and B from 95.3% to ~86%, maintaining handoff's advantage but narrowing the gap. Study 5's real API result (auto-compact wins) may reflect genuine content-type differences between a portfolio site and a more technically structured recipe app — or it may reflect the fact that Study 5's auto-compact chain produced more complete summaries due to the recipe app content being better-structured (explicit Safety Rules, numbered lists, named constants).

---

## Key Findings

### New Finding: Manual Evaluation Bias Confirmed

The real API test reveals that self-scoring (model evaluates its own answers with access to the source context) inflates Group A by ~18pp and Group B by ~9pp. This asymmetry is because longer, denser auto-compact summaries make it easier for the scoring model to infer correct answers by re-reading the source, while shorter structured handoff documents expose gaps more visibly. All Study 1–4 results using manual scoring should be read with this inflation caveat — conclusions about relative advantage hold directionally but the magnitude of advantage for auto-compact was likely overstated.

### Confirmed Finding: Both Methods Are Viable

Both methods score 70%+ across all valid test points in real API conditions. For vibe coding content with explicit Safety Rules and named constants, both mechanisms preserve critical implementation details well enough for a successor session to continue without major regressions.

### Confirmed Finding: T4 (Compound Features) Is a Tie

T4 (compound filter + search history) was tied at 15/15 in real API scoring. Compound feature sessions — where multiple independent features are built in parallel — appear to be equally tractable for both mechanisms. Neither mechanism has a structural advantage at the mid-session accumulation point for this content type.

### Confirmed Finding: Architecture Questions Are Near-Parity

T6 architecture question: A=2/2, B=1/2. Handoff lost one point because the B chain's later documents dropped specific persistence layer details (Cache API TTL mechanism). This partially confirms the Study 4 hypothesis about auto-compact having a holistic synthesis advantage for late-session cumulative questions — but the margin is small.

---

## Methodological Note: Real API vs Manual Scoring

Study 5 introduces a two-tier scoring design:
1. **Manual**: model evaluates its own answers with source context available (open-book, prone to inflation)
2. **Real API**: fresh blind subprocess calls per question — the QA model has only the compressed context, not the original session (closed-book, structurally equivalent to actual usage)

For future studies, real API scoring should be the primary evaluation method. Manual scoring is faster but systematically inflated for auto-compact groups, making cross-group comparisons unreliable.
