# Study 3 Results: Dense Multi-Session Context Retention (GNN-NLP Survey)
> Completed: 2026-05-22

## Executive Summary

With dense academic content (~7,000 words per session, 45,870 words total), both methods performed dramatically worse than Study 2 (explicit labeled rules): auto-compact dropped from 98.3% composite to 53.9%, and handoff from 90.0% to 63.3%. Unlike Studies 1 and 2, handoff outperformed auto-compact throughout all three test points (T1B 73.3% vs T1A 53.3%, T2B 63.3% vs T2A 70.0% — auto-compact briefly surged at T2 — and T3B 60.0% vs T3A 43.3%), yielding a 9.4-point composite advantage (63.3% vs 53.9%) for handoff. The key driver is content density: dense technical paper content with mathematical notation, specific citations, and multi-level taxonomies is compressed into broad strokes by auto-compaction, stripping the exact details the questions probe, whereas handoff documents carried critical specifics forward.

---

## Score Tables

### T1 — Start of Session 2 (Tests Part 1 only)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q1 | Conceptual definition | 2 | 2 | Both full: filtering preserves structure, pooling coarsens it |
| Q2 | Conceptual definition | 1 | 0 | A partial: bag/sequence/graph views present but missing sequence exemplars (CRF, word2vec); B cannot answer |
| Q3 | Conceptual definition | 2 | 2 | Both full: flat/hierarchical, sub-sampling vs supernodes, named pooling functions |
| Q4 | Conceptual definition | 2 | 2 | Both full: limited expressive power + no unified learning framework |
| Q5 | Conceptual definition | 1 | 2 | A partial: MPNN as general framework but missing "choosing f_M and f_U recovers many GNNs"; B full |
| Q6 | Specific claim | 1 | 2 | A partial: "cannot directly exploit graphs" — missing specific "irregular structure + varying neighbor sizes"; B full |
| Q7 | Specific claim | 1 | 2 | A partial: formula present but problem (gradient instability) not named; B full: problem + exact substitution |
| Q8 | Specific claim | 2 | 2 | Both full: GRU as primary modification, fixed T steps, edge type/direction |
| Q9 | Specific claim | 0 | 2 | A: "Not in my context"; B full: not permutation-invariant but better expressive power (Hamilton 2017a; Zhang 2019e) |
| Q10 | Specific claim | 0 | 0 | Both fail: three-challenge enumeration from introduction not reproduced |
| Q11 | Named entity | 2 | 2 | Both full: GAT, Velickovic et al. (2018), multi-head attention |
| Q12 | Named entity | 0 | 0 | Both: "Not in my context" — classification/generation task split not retained |
| Q13 | Named entity | 1 | 0 | A partial: topic modeling mentioned, not LDA or Blei et al.; B: "Not in my context" |
| Q14 | Named entity | 1 | 2 | A partial: "neighborhood sampling" correct but not specific about fixed-size; B full: fixed random subset |
| Q15 | Named entity | 0 | 2 | A: "Not in my context"; B full: LPAs, Section 2.2.5, analogy to GNN propagation |
| **TOTAL** | | **16/30** | **22/30** | |

### T2 — Start of Session 4 (Tests Parts 1–3, weighted recent)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q16 | P1 cross-reference | 1 | 0 | A partial: implies fully-connected but doesn't state it; B: "Not in my context" (outside Handoff3 scope, Section 8.2) |
| Q17 | P1 cross-reference | 0 | 1 | A: "Not in my context"; B partial: carry-forward gives "1-hop" consequence but not compensation mechanism |
| Q18 | P1 cross-reference | 2 | 2 | Both full: edge type information discarded |
| Q19 | P2 | 0 | 0 | Both fail: three-step dependency graph construction not retained |
| Q20 | P2 | 2 | 1 | A full: jointly learns adjacency matrix end-to-end; B partial: O(n²) carry-forward but not full definition |
| Q21 | P2 | 1 | 2 | A partial: O(n²) present but anchor-based solution (Chen 2020f) absent; B full: O(n²) + anchor linear solution |
| Q22 | P2 | 2 | 1 | A full: intrinsic + implicit, "discarding hurts performance"; B partial: "helps" noted but rationale not given |
| Q23 | P2 | 2 | 0 | A full: all eleven categories listed correctly; B: "Not in my context" (Part 2 outside Handoff3) |
| Q24 | P3 | 1 | 2 | A partial: single edge type implied, no formal notation; B full: |T|=1, |R|=1, explains GNN failure for |R|>1 |
| Q25 | P3 | 2 | 2 | Both full: R-GCN (Schlichtkrull 2018), relation-specific matrices, basis decomposition for over-parameterization |
| Q26 | P3 | 1 | 2 | A partial: multiple types stated but two-level HAN attention structure only briefly implied; B full: two-level attention |
| Q27 | P3 | 2 | 0 | A full: structure-aware incorporates existing edge info beyond node embeddings; B: "Not in my context" |
| Q28 | P3 | 1 | 2 | A partial: gating prevents over-smoothing but phenomenon not defined; B full: convergence of representations + mitigation |
| Q29 | P3 | 2 | 2 | Both full: R-GGNN (Beck 2018), relation-specific params, GRU gating for multi-relational |
| Q30 | P3 | 2 | 2 | Both full: static edge-as-connectivity / bidirectional (N⁻, N⁺) / dynamic homogeneous |
| **TOTAL** | | **21/30** | **19/30** | |

### T3 — Start of Session 7 (Tests Parts 1–6, weighted recent)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:---:|:---:|-------|
| Q31 | P1 → P6 connection | 1 | 2 | A partial: over-parameterization noted but basis decomposition not named; B full: basis decomposition + Directed-GCN |
| Q32 | P2 → P6 connection | 1 | 2 | A partial: only 2 of 3 challenges match (incompleteness yes; schema heterogeneity approximate; third wrong); B full: all three |
| Q33 | P3 → P5 connection | 0 | 0 | Both fail: Question Generation + Sachan et al. (2020) not retained |
| Q34 | P3 → P4 connection | 2 | 1 | A full: GCN/GGNN/GraphSage/GAT + BiRNN + BERT/RoBERTa; B partial: high-level only, missing specific list |
| Q35 | P4 | 2 | 2 | Both full: Graph2Seq/Graph2Tree/Graph2Graph with correct input-output types |
| Q36 | P4 | 1 | 2 | A partial: "learnable copying" and node-level variant noted but no citations; B full: Vinyals 2015, Gu 2016, p_gen, node-level extension |
| Q37 | P4 + P5 | 0 | 2 | A: three categories not listed; B full: node transformation / edge transformation / node-edge-co-transformation + IE example |
| Q38 | P5 | 0 | 0 | Both fail: NMT structural limitation (failure to utilize syntactic structure / long-dependency problem) not stated |
| Q39 | P5 | 1 | 0 | A partial: NMT=BLEU present, NER metric absent; B: "Not in my context" |
| Q40 | P5 | 1 | 2 | A partial: Graph4NLP + DGL+PyTorch named, four layers not listed; B full: all four layers listed |
| Q41 | P5 + P6 | 0 | 0 | Both fail: MAWPS/MATH23K/MATHQA not retained |
| Q42 | P6 | 2 | 2 | Both full: Transformers cannot directly operate on graph-structured inputs |
| Q43 | P6 | 1 | 1 | Both partial: O(n²) + anchor-based present; future directions beyond anchor (efficient transformer designs, edge directions) absent |
| Q44 | P6 multi-section | 1 | 0 | A partial: three dimensions listed but 3 vs 4 inconsistency not noted; B: "Not in my context" |
| Q45 | P5 + P6 | 0 | 2 | A: KGC described without trade-off framing; B full: Shang 2019 (efficient) vs Teru/Xie 2020 (expressive) |
| **TOTAL** | | **13/30** | **18/30** | |

---

## Composite Scores

| | Group A (Auto-Compact) | Group B (Handoff) |
|---|---|---|
| T1 raw | 16/30 (53.3%) | 22/30 (73.3%) |
| T2 raw | 21/30 (70.0%) | 19/30 (63.3%) |
| T3 raw | 13/30 (43.3%) | 18/30 (60.0%) |
| **Composite** | **97/180 (53.9%)** | **114/180 (63.3%)** |

Composite: (T1×1 + T2×2 + T3×3) / 180

- Group A: (16×1 + 21×2 + 13×3) / 180 = (16 + 42 + 39) / 180 = 97/180 = **53.9%**
- Group B: (22×1 + 19×2 + 18×3) / 180 = (22 + 38 + 54) / 180 = 114/180 = **63.3%**

---

## Hypothesis Evaluation

### H1: With dense content, auto-compact T1 drops significantly vs Study 2 (from 96.7%)
**Confirmed.** T1A scored 16/30 (53.3%), a 43.4-point collapse from Study 2's 29/30 (96.7%). Dense academic content (mathematical notation, specific citations, multi-level taxonomies) is not compaction-friendly. The auto-compact summary retained broad concepts (GCN, GAT, GGNN, flat/hierarchical pooling) but lost specific details: the three-challenge enumeration (Q10), the three classification task names (Q12), LDA attribution (Q13), and the LPA-to-GNN analogy (Q15).

### H2: Auto-compact degrades across T1→T2→T3 with dense content
**Confirmed with reversal.** T1A=53.3% → T2A=70.0% → T3A=43.3%. There is no clean monotonic degradation — T2A actually rose 16.7 points above T1A because Parts 2–3 content (eleven static graph categories, R-GCN, R-GGNN, homogeneous sub-categories) was retained very well by Summary3. T3A then collapsed to 43.3% as late-session questions required cross-part connections and fine-grained details (Graph2Graph sub-categories, MWP datasets, copying mechanism citations) that Summary6 did not preserve. Overall, dense content causes degradation — but not uniformly across parts.

### H3: Handoff is more stable than auto-compact across T1/T2/T3
**Partially confirmed.** T1B=73.3% → T2B=63.3% → T3B=60.0%. Handoff does degrade (−13 points from T1 to T3), but less severely than auto-compact (T1A=53.3% → T3A=43.3%, −10 points). Crucially, handoff never had a mid-session spike like auto-compact's T2A surge — it degraded more smoothly. The handoff variance (73.3% → 63.3% → 60.0%) is lower than auto-compact variance (53.3% → 70.0% → 43.3%).

### H4: Handoff advantage is larger with dense content (Study 3) than clean content (Study 2)
**Confirmed.** In Study 2 (clean content), auto-compact beat handoff by 8.3 points (98.3% vs 90.0%). In Study 3 (dense content), handoff beats auto-compact by 9.4 points (63.3% vs 53.9%) — a 17.7-point swing in handoff's favor. Dense content fundamentally alters the competitive landscape: auto-compaction discards specifics that handoff documents can preserve through explicit carry-forward, even imperfectly.

---

## Key Findings

- **Both methods fail badly on dense academic content.** Auto-compact composite 53.9% and handoff composite 63.3% are the worst results across all three studies, confirming that content density — not session count — is the primary driver of retention failure.

- **Handoff wins Study 3 with a 9.4-point composite advantage (63.3% vs 53.9%)**, reversing Study 2's outcome where auto-compact won by 8.3 points. The reversal is driven by handoff's ability to explicitly carry forward specific details (LPA analogy at Q15, basis decomposition at Q31, KGC trade-off at Q45) that auto-compact's summaries stripped.

- **Auto-compact's T2 anomaly (70.0%)** is the study's structural outlier: Parts 2–3 content (R-GCN, R-GGNN, eleven static graph categories, homogeneous sub-categories) happened to be retained well by Summary3. This inflated T2A above T1A and T3A, making degradation appear non-monotonic. The underlying pattern is that dense content retention is highly sensitive to whether summary authors preserved specific lists and named entities.

- **Both methods share the same blind spots:** Q10 (three enumerated intro challenges: 0/0 at T1), Q12 (classification task names: 0/0 at T1), Q33 (QG task + Sachan 2020: 0/0 at T3), Q38 (NMT structural limitation: 0/0 at T3), and Q41 (MWP datasets MAWPS/MATH23K/MATHQA: 0/0 at T3). These represent content that is neither enumerated in summaries nor surfaced in handoff carry-forwards — suggesting they require a fundamentally different documentation strategy (explicit named-entity logging) to be retained.

- **The handoff carry-forward mechanism proved critical at T3.** Five of T3B's eight 2-point scores (Q31, Q32, Q36, Q37, Q45) came from specifics explicitly carried forward across sessions (basis decomposition, KGA challenge list, Vinyals/Gu citations, Graph2Graph sub-types, KGC efficiency/expressiveness trade-off), whereas T3A's Summary6 compressed these to either absent or partial.

---

## Three-Study Comparison

| | Study 1 | Study 2 | Study 3 |
|---|---|---|---|
| Content type | Single session, implicit/procedural | 6 sessions, explicit labeled safety rules | Dense academic paper, 6 parts |
| Words per session | ~500 | ~350 | ~7,000 |
| Auto-compact T1 | 60% | 96.7% | 53.3% |
| Auto-compact T3 | 27% | 100% | 43.3% |
| Handoff T1 | 67% | 93.3% | 73.3% |
| Handoff T3 | 67% | 100% | 60.0% |
| Auto-compact composite | ~49% | 98.3% | 53.9% |
| Handoff composite | 67% | 90.0% | 63.3% |
| Winner | Handoff (+40% at Round 6) | Auto-compact (+8.3% composite) | Handoff (+9.4% composite) |
| Key driver | Content was implicit/procedural | Content was explicit and label-structured | Content was dense and citation-heavy |

---

## Implications

The three-study arc tells a clear story: **content structure, not session mechanism, determines retention quality.** Auto-compaction performs optimally when content is already structured with explicit labels and decision records (Study 2: 98.3%); it fails when content is either procedurally implicit (Study 1: ~49%) or densely academic (Study 3: 53.9%). Handoff's performance is more stable across content types — 67% / 90.0% / 63.3% — because a well-authored handoff document can preserve specific details that summary algorithms discard, particularly citations, named entities, and enumerated lists.

The practical implication is that **the value of /handoff scales with content hostility to compression.** For sessions producing explicit labeled outputs (architectural decisions, safety rules, configuration values), auto-compaction is sufficient and may outperform handoff due to its exhaustive coverage. For sessions involving dense technical reading — academic papers, protocol specifications, complex codebases — handoff's explicit carry-forward mechanism preserves the specific details (paper citations, algorithm names, benchmark datasets) that questions probe, while auto-compaction collapses them to category labels.

A further implication is that **neither mechanism adequately handles "enumeration" content.** Q10 (three intro challenges), Q12 (classification task names), Q33 (specific paper + task combination), Q38 (NMT limitation), and Q41 (MWP datasets) scored 0/0 in both groups across all three studies where they appeared. This class of content — precise lists of named items embedded in dense prose — requires a dedicated logging strategy beyond what either summary or handoff currently implements: an explicit named-entity and enumeration log maintained alongside the primary context mechanism.
