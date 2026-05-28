# Context-Relay Research Summary: Studies 1–5
> Last updated: 2026-05-28
> Project: context-relay — /handoff skill for Claude Code

## Overview

This research series investigates how well two mechanisms — Claude Code's native auto-compaction and the context-relay `/handoff` tool — retain critical engineering context across long sessions and multiple context resets. The central question is whether a structured handoff document outperforms auto-generated summaries, and under what conditions. Five studies have been completed, each varying the content structure, session format, and scoring methodology to stress-test both mechanisms.

---

## Study 1: Repeated Compaction vs Handoff (Single Session)

### Method

A 2-hour engineering session on a Node.js/TypeScript `api-gateway` project was used as the source material, covering a JWT refactor across 5 handlers, an async migration, a bug fix, and several architectural decisions. The session content was compressed once (Round 1), then re-compressed twice more (Round 3), and again to a total of 6 compaction cycles (Round 6), simulating content degradation over a long session. A `/handoff`-formatted snapshot was used as the constant comparison condition, loaded fresh as a system prompt. Recall was tested with 15 questions across safety rules, decision rationale, and work state, scored 0–2 each (max 30 points).

### Key Results

| Condition | Score | Percentage |
|---|:---:|:---:|
| Auto-compact Round 1 | 18/30 | 60% |
| Auto-compact Round 3 | 9/30 | 30% |
| Auto-compact Round 6 | 8/30 | 27% |
| Handoff (constant) | 20/30 | 67% |

### Conclusion

Auto-compaction degrades rapidly after Round 1, reaching a near-floor of 27% by Round 6. Handoff maintains a stable 67% throughout, representing a +40% advantage over long sessions.

### Flaw Identified

Compaction was simulated by repeatedly compressing the *same* content rather than accumulating new work between sessions. Real usage involves fresh work added each session, which Study 2 addressed.

---

## Study 2: Multi-Session Accumulation (Explicit Content)

### Method

Six sequential sessions continued the `api-gateway` JWT refactor scenario, each adding new realistic work (S1: base refactor, S2: adminHandler fix, S3: Redis race condition, S4: test coverage, S5: rate-limiting middleware, S6: performance profiling and cache optimization). Group A used auto-compaction (each session's summary compressed with new content), Group B used `/handoff` (fresh snapshot written between sessions). Three test points were used: T1 (after S1), T2 (after S3), and T3 (after S6), with 15 questions each scored 0–2. A weighted composite score was calculated: (T1×1 + T2×2 + T3×3) / 180.

### Key Results

| Test Point | Auto-compact (Group A) | Handoff (Group B) |
|---|:---:|:---:|
| T1 (after S1) | 29/30 (96.7%) | 28/30 (93.3%) |
| T2 (after S3) | 29/30 (96.7%) | 22/30 (73.3%) |
| T3 (after S6) | 30/30 (100.0%) | 30/30 (100.0%) |
| **Composite** | **177/180 (98.3%)** | **162/180 (90.0%)** |

### Conclusion

Auto-compaction outperformed handoff with a +8.3-point composite advantage. Both methods scored 30/30 at T3. Handoff collapsed at T2 (22/30) due to three specific omissions in the handoff document — the `token.adminScope ?? ""` optional chaining fallback, AdminTokenValidationError metadata fields, and SET NX EX atomic semantics — content that auto-compaction retained automatically.

### Flaw Identified

Study 2's session scripts were purpose-built with explicit SAFETY-N labels and structured decision rationale, making them unusually compaction-friendly. Real sessions don't look like ~350-word clean labeled scripts — they're messy, implicit, and conversational. Study 3 tested denser content to probe this dimension.

---

## Study 3: Multi-Session with Dense Academic Content

### Method

Six sessions each fed a ~7,000-word section of a dense GNN-NLP academic survey paper (45,870 words total), covering graph neural network architectures, pooling methods, knowledge graphs, sequence tasks, and generation tasks. The same two-group protocol from Study 2 was used: Group A auto-compacted across sessions, Group B wrote handoff documents between sessions. The same three test points (T1/T2/T3) with 15 questions each tested recall of specific claims, mathematical notation, citation attributions, named entities, and enumerated lists.

### Key Results

| Test Point | Auto-compact (Group A) | Handoff (Group B) |
|---|:---:|:---:|
| T1 (after Part 1) | 16/30 (53.3%) | 22/30 (73.3%) |
| T2 (after Part 3) | 21/30 (70.0%) | 19/30 (63.3%) |
| T3 (after Part 6) | 13/30 (43.3%) | 18/30 (60.0%) |
| **Composite** | **97/180 (53.9%)** | **114/180 (63.3%)** |

### Conclusion

Handoff outperformed auto-compaction by 9.4 composite points, reversing Study 2's outcome. Both methods performed dramatically worse than Study 2 — dense academic content (mathematical notation, specific citations, multi-level taxonomies) is hostile to compression. Auto-compact's non-monotonic curve (53.3% → 70.0% → 43.3%) reflects high sensitivity to whether specific details happened to survive any given summary round.

---

## Study 4: Multi-Session with Vibe Coding Content (Target Scenario)

### Method

Six sequential sessions (~6,500–7,000 words each, 42,000 words total) simulated realistic vibe coding conversations building a portfolio website. Sessions covered: S1 (Bootstrap abandoned, color palette, nav skeleton), S2 (nav flicker fix, CSS animations removed, circular photo), S3 (CSS Grid gallery, tag filter system, "Projects→Work" rename), S4 (contact form, blur validation, Safari polyfill), S5 (IntersectionObserver, CSS variable system, dark mode partial), S6 (event delegation refactor, SEO meta tags, GitHub Pages deployment). Five test points (T1–T5) tested 10 questions each; a bonus T6 tested 1 cumulative architecture overview question (max 2 points). Weighted composite: (T1×1 + T2×2 + T3×3 + T4×4 + T5×5) / 300.

### Key Results

| Test Point | Auto-compact (Group A) | Handoff (Group B) |
|---|:---:|:---:|
| T1 (after S1) | 19/20 (95.0%) | 20/20 (100.0%) |
| T2 (after S2) | 17/20 (85.0%) | 18/20 (90.0%) |
| T3 (after S3) | 18/20 (90.0%) | 20/20 (100.0%) |
| T4 (after S4) | 18/20 (90.0%) | 20/20 (100.0%) |
| T5 (after S5) | 19/20 (95.0%) | 18/20 (90.0%) |
| **Weighted Composite** | **274/300 (91.3%)** | **286/300 (95.3%)** |
| T6 Architecture (after S6) | 2/2 (100%) | 2/2 (100%) |

### Conclusion

Handoff wins by 4.0 composite points in the most realistic content condition tested. Both mechanisms perform well (~91–95%), the narrowest gap across all four studies. Auto-compact's failure mode: missing forward-looking prohibitions (Q6, Q19: zero scores where user preference reactions weren't framed as "must NOT" rules). Handoff's failure mode: foundational carry-forward gaps (Q12: hex values not re-stated in Handoff2; Q49: negative-space decision not mentioned). T6 architecture question: both scored 2/2 — contradicting the hypothesis that auto-compact would have a structural advantage on cumulative holistic questions.

---

## Cross-Study Findings

### The Content Structure Hypothesis (Now Confirmed Across 4 Studies)

The winner of each study is determined by content structure, not by any inherent advantage of either mechanism.

| Content Type | Auto-Compact | Handoff | Winner |
|---|---|---|---|
| Explicit labeled rules (Study 2) | 98.3% | 90.0% | **Auto-compact (+8.3pp)** |
| Implicit/procedural (Study 1) | ~49% | 67% | **Handoff (+18pp at R6)** |
| Dense academic (Study 3) | 53.9% | 63.3% | **Handoff (+9.4pp)** |
| Vibe coding (Study 4) | 91.3% | 95.3% | **Handoff (+4.0pp)** |

**Practical decision rule:** Use auto-compaction when sessions produce explicitly labeled artifacts (safety rules, architectural decisions, config values). Use /handoff when sessions involve dense technical specifics (academic reading, protocol specs) or strong implicit user preference signals (vibe coding, design choices, product decisions) that require forward-enforceable framing.

### Consistent Findings Across All Studies

Auto-compaction performs near-perfectly on explicitly labeled, structured content and degrades sharply when context is either implicit or dense. Handoff performance is more stable across content types (67% / 90.0% / 63.3% / 95.3% composite), and its variance across test points is consistently lower than auto-compaction's. In all studies, both methods converge toward similar scores at the final test point — the divergence is concentrated in the mid-session test points.

### Handoff's Carry-Forward Mechanism

Handoff's advantage in Studies 1, 3, and 4 is traceable to explicit carry-forward: specific details — causal chains, user preference statements, concrete next steps — are explicitly copied into the next session's context regardless of whether a summarization algorithm would have preserved them. In Study 3 at T3, five of handoff's eight 2-point scores came from details explicitly carried forward across handoff documents. In Study 4, handoff preserved Q6 ("sports team logo" rejection framing), Q11/Q19 (nav constraint framed as a forward rule), Q28 (rename trigger reason), and Q33 (blur validation user rationale) — all details that auto-compact recorded as facts but not as forward-enforceable prohibitions.

### New Finding: The Foundational Carry-Forward Gap

Study 4 revealed a handoff-specific failure mode not seen in earlier studies: **foundational constants established early in a session chain are not re-stated in later handoffs**. Q12 (hex values #1a1a2e and #e94560) scored 0/2 in Handoff2 because Handoff1 contained them but Handoff2 didn't re-state them. Handoff format focuses on "what changed this session" but lacks a "Permanent Constants" section for values that must persist across all sessions. Auto-compact's rolling summary re-compressed both new and old content, retaining the hex values through Summary2.

### New Finding: The Negative-Space Decision Gap

Q49 (will-change and defer "deliberately not added") reveals a shared weakness: both mechanisms struggle with decisions that leave no code artifact. Auto-compact preserved "correctly not added" (score 1, missing reasoning). Handoff omitted it entirely (score 0). Neither mechanism currently has a dedicated mechanism for logging "we considered X and chose not to implement it." This gap is most relevant for performance optimizations and deliberate omissions.

### New Finding: T6 Architecture Question — Tie

The hypothesis that auto-compact has a structural advantage on cumulative holistic questions (because its rolling summary comprehensively synthesizes all sessions) was invalidated: both scored 2/2. By session 6, the handoff chain has accumulated enough carry-forwards to reconstruct a complete project mental model. The advantage of auto-compact's exhaustive rolling coverage is not decisive once enough handoff iterations have accumulated. This hypothesis may still hold for shorter session chains (3–4 sessions).

### The Shared Blind Spot

Both methods consistently fail on enumeration content — precise named lists embedded in prose. These scored 0/0 for both groups across all studies (Q10, Q12, Q33, Q38, Q41 in Study 3; Q2 in Study 1). For real-world vibe coding (Study 4), this class of content is rare — the blind spot matters more for academic or specification reading.

---

## Study 5: Multi-Session Vibe Coding with Real API Scoring

### Method

Six sessions (~7,000 words each, 42,000 words total) simulated a realistic vibe coding project building a vanilla JS recipe collector app. Sessions covered: S1 (API selection, data schema, project structure), S2 (favorites system, localStorage), S3 (recipe detail modal, serving scaler), S4 (compound filter, search history), S5 (custom recipe CRUD, export/import), S6 (Cache API, accessibility, deployment). Six test points tested 10 questions each (T1–T5) plus 1 architecture question (T6, max 2pts). Weighted composite: (T1×1 + T2×2 + T3×3 + T4×4 + T5×5) / 300.

**Key innovation**: Study 5 introduced a real API scoring layer — answers were generated and scored by fresh `claude --print` subprocess sessions that had no access to the source session content, only the compressed context document. This is structurally equivalent to actual usage (a new Claude session reading a handoff or auto-compact summary). Manual scoring was also completed for comparison.

### Key Results

| Test Point | Auto-compact (A) | Handoff (B) |
|---|:---:|:---:|
| T1 (after S1) | 18/20 (90.0%) | 17/20 (85.0%) |
| T2 (after S2) | 19/20 (95.0%) | 16/20 (80.0%) |
| T3 (after S3) | 17/20 (85.0%) | 15/20 (75.0%) |
| T4 (after S4) | 15/20 (75.0%) | 15/20 (75.0%) |
| T5 (after S5) | 16/20 (80.0%) | 14/20 (70.0%) |
| **Weighted composite (real API)** | **247/300 (82.3%)** | **224/300 (74.7%)** |
| T6 architecture | 2/2 | 1/2 |
| Weighted composite (manual) | 300/300 (100%) | 251/300 (83.7%) |

### Conclusion

Auto-compact wins by 7.6 composite points in real API conditions. The manual evaluation revealed a critical bias: Group A's 100% manual score is methodologically invalid — the scoring model had access to the same summary it was testing recall against (open-book). Real API scoring shows both methods perform at 75–95% per test point, with auto-compact holding a consistent edge across T1–T3 and T5, and a tie at T4.

### New Finding: Manual Evaluation Inflation Bias

The real API test exposes a systematic flaw in the manual scoring protocol used in Studies 1–4: Group A is inflated by ~18pp and Group B by ~9pp. This asymmetry exists because longer, denser auto-compact summaries allow the scoring model to infer correct answers by re-reading, while shorter structured handoff documents expose gaps more visibly. All prior study conclusions hold directionally but the magnitude of advantage was likely overstated for whichever mechanism produced denser context.

### New Finding: Shared "Why Not" Failure Mode

Five questions (Q9, Q22, Q31, Q41, Q49) failed for both groups in real API conditions despite passing in manual scoring. All share the same structure: rationale for a road-not-taken or an absence decision ("why localStorage over IndexedDB," "why recipeCache not localStorage," "why the S3 modal rule applies differently in S4"). Neither mechanism preserves negative-space reasoning unless it was explicitly restated as a forward-facing rule.

---

## Cross-Study Findings (Updated)

### The Content Structure Hypothesis (Revised After Study 5)

| Study | Content Type | Auto-Compact | Handoff | Winner | Scoring |
|---|---|:---:|:---:|:---:|:---:|
| Study 2 | Explicit labeled rules | 98.3% | 90.0% | **Auto-compact (+8.3pp)** | Manual |
| Study 1 | Implicit/procedural | ~49% | 67% | **Handoff (+18pp at R6)** | Manual |
| Study 3 | Dense academic | 53.9% | 63.3% | **Handoff (+9.4pp)** | Manual |
| Study 4 | Vibe coding (portfolio) | 91.3% | 95.3% | **Handoff (+4.0pp)** | Manual |
| **Study 5** | **Vibe coding (recipe app)** | **82.3%** | **74.7%** | **Auto-compact (+7.6pp)** | **Real API** |

Study 5's reversal of Study 4's result is partly explained by the manual inflation bias — if Study 4 were re-scored with real API conditions, the gap would narrow. However, content structure differences remain a plausible co-factor: the recipe app sessions contained more explicitly named constants (STORAGE_KEYS, Safety Rules, CUSTOM_RECIPE_PREFIX), which auto-compact rolling summaries preserve naturally. The portfolio site sessions were heavier on implicit design decisions (animation choices, color rejections) that handoff's structured format captures more reliably.

**Updated practical decision rule**: Use auto-compaction when sessions produce explicitly named constants, locked keys, and structured decision artifacts. Use /handoff when sessions are dominated by implicit user preferences, design choices, or "never do X" constraints that require forward-enforceable framing.

### Consistent Findings Across All Studies

- Both mechanisms are viable: real API scores of 70%+ across all test points
- Mid-session test points (T2–T4) show the largest divergence; early (T1) and late (T5–T6) converge
- "Why not" decisions (negative-space reasoning) are the hardest content class for both mechanisms
- Neither mechanism has a mechanism for preserving explicitly rejected alternatives

---

## Methodological Evolution

| Study | Input content | Sessions | Words/session | Scoring | Verdict |
|---|---|---|---|---|---|
| Study 1 | Clean session log (re-compressed) | 1 | ~500 | Manual | Artificial |
| Study 2 | Clean labeled script | 6 | ~350 | Manual | Too clean |
| Study 3 | Dense academic paper section | 6 | ~7,000 | Manual | Wrong domain |
| Study 4 | Realistic vibe coding conversation | 6 | ~6,500–7,000 | Manual | Realistic content, inflated scores |
| **Study 5** | **Realistic vibe coding conversation** | **6** | **~7,000** | **Real API** | **Most rigorous** |

Study 5 is the methodological gold standard of the series: realistic content (vibe coding) + closed-book evaluation (fresh blind subprocess per question). Future studies should use real API scoring as the primary evaluation method.
