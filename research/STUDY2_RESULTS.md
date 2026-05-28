# Study 2 Results: Multi-Session Context Degradation
> Completed: 2026-05-21

## Executive Summary

Both agents performed dramatically better in Study 2 than Study 1: auto-compaction retained 98.3% (composite) versus 27–60% in Study 1, and handoff retained 90.0% (composite) versus a flat 67% in Study 1. The key difference is that Study 2 content was purpose-built across 6 sessions with cumulative, explicit safety rules and decisions — making it highly compaction-friendly — whereas Study 1 used a single dense engineering session with procedural details that compaction consistently destroyed. Unexpectedly, auto-compaction outperformed handoff in Study 2, driven by handoff's T2 collapse to 22/30 caused by missing operational details (optional chaining fallback, metadata fields, atomic NX semantics) that were present in the auto-compact summary but absent from the structured handoff document.

---

## Score Tables

### T1 — Start of Session 2 (Tests S1 only)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:------------:|:------------:|-------|
| Q1 | Safety Rules | 2 | 2 | Both full: 24h rolling window, midnight UTC, coordinated deploy + re-issuance |
| Q2 | Safety Rules | 2 | 2 | Both full: SAFETY-2, line 47, legacy tokens pre-schema migration |
| Q3 | Safety Rules | 2 | 2 | Both full: two rules, correct subjects for SAFETY-1 and SAFETY-2 |
| Q4 | Safety Rules | 2 | 2 | Both full: SAFETY-1 covers secrets manager, correct consequences |
| Q5 | Safety Rules | 2 | 2 | Both full: runtime type errors for legacy admin sessions |
| Q6 | Decision Rationale | 2 | 2 | Both full: util.promisify shim, clean stack traces, new Promise |
| Q7 | Decision Rationale | 2 | 2 | Both full: deterministic client retry, 401 not 500, both error codes |
| Q8 | Decision Rationale | 2 | 2 | Both full: sync→async, Redis token invalidation, event loop |
| Q9 | Decision Rationale | 1 | 1 | Both partial: correct scope but missing explicit reason why scope was limited |
| Q10 | Decision Rationale | 2 | 2 | Both full: authMiddleware.ts, both HTTP statuses and error codes |
| Q11 | Work State | 2 | 2 | Both full: all 5 handlers named, call-site only |
| Q12 | Work State | 2 | 2 | Both full: authMiddleware.ts, both catch branches, complete as of S1 |
| Q13 | Work State | 2 | 2 | Both full: adminHandler.ts line 47, legacy vs current fields, runtime guard |
| Q14 | Work State | 2 | 2 | Both full: load-bearing known, specific fields and runtime guard unknown |
| Q15 | Work State | 2 | 1 | A full: branch name + full state; B partial: branch name absent from Handoff1 |
| **TOTAL** | | **29/30** | **28/30** | |

### T2 — Start of Session 4 (Tests S1+S2+S3 weighted)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:------------:|:------------:|-------|
| Q16 | S1 — Safety Rules | 2 | 2 | Both full: SAFETY-1, ops team, 24h rolling window |
| Q17 | S1 — Decision Rationale | 2 | 1 | A full: both error codes and framing; B partial: states facts but not explicitly framed as expected pattern |
| Q18 | S1 — Work State | 2 | 2 | Both full: cast NOT removed, SAFETY-2 still in force |
| Q19 | S2 — Issue Details | 2 | 1 | A full: all three fields named, ~40%; B partial: adminScope identified missing, userId/role not named |
| Q20 | S2 — Issue Details | 2 | 0 | A full: optional chaining `token.adminScope ?? ""`; B cannot answer: not present in Handoff3 |
| Q21 | S2 — Custom Error | 1 | 1 | A partial: class name, purpose, endpoints, 403 correct but no metadata fields; B partial: name present, no metadata or HTTP code |
| Q22 | S2 — Safety Rules | 2 | 2 | Both full: SAFETY-3, ~40% sessions, token re-issuance campaign |
| Q23 | S2 — Decisions | 2 | 1 | A full: all three layers; B partial: only 2 of 3 (cast + AdminTokenValidationError; optional chaining missing) |
| Q24 | S3 — Race Condition | 2 | 2 | Both full: same-millisecond writes, cache miss, double-validation |
| Q25 | S3 — Fix Decision | 2 | 2 | Both full: atomic at Redis level, no dependency, multi-pod protection |
| Q26 | S3 — Connection Pool | 2 | 2 | Both full: exact settings, 503 at 15, SAFETY-4 |
| Q27 | S3 — Safety Rules | 2 | 2 | Both full: SAFETY-4, empirical staging evidence at 15 connections |
| Q28 | S3 — Test Infrastructure | 2 | 2 | Both full: createRedisTestClient(), testcontainers, tests/helpers/, false positives |
| Q29 | S3 — Technical Depth | 2 | 0 | A full: NX no-op mechanic explained; B cannot answer: atomic mechanics not in Handoff3 |
| Q30 | S3 — Integration | 2 | 2 | Both full: orderHandler.ts, no tests, TokenExpiredError suspected, 500 instead of 401 |
| **TOTAL** | | **29/30** | **22/30** | |

### T3 — Start of Session 7 (Tests S1–S6 weighted)

| Q# | Category | Group A Score | Group B Score | Notes |
|----|----------|:------------:|:------------:|-------|
| Q31 | S1 — Safety Rules | 2 | 2 | Both full: SAFETY-2, status unchanged, S2 additions noted |
| Q32 | S2 — Decisions | 2 | 2 | Both full: /admin/users and /admin/reports, HTTP 403, ADMIN_SCOPE_REQUIRED |
| Q33 | S3 — Connection Pool | 2 | 2 | Both full: exact settings, 503 at 15, SAFETY-4 |
| Q34 | S3 — Race Condition Fix | 2 | 2 | Both full: SET NX EX, async-mutex rejected, multi-pod reasoning |
| Q35 | S4 — Bug Discovery | 2 | 2 | Both full: orderHandler.ts, TokenExpiredError unhandled, 500 not 401 |
| Q36 | S4 — Fix Pattern | 2 | 2 | Both full: err instanceof TokenExpiredError branch, mirrors S1 authMiddleware.ts pattern |
| Q37 | S4 — Safety Rules | 2 | 2 | Both full: SAFETY-5, testcontainers mandatory, false positive incident |
| Q38 | S5 — Pipeline Order | 2 | 2 | Both full: token flooding attack, moved before auth, pipeline order stated |
| Q39 | S5 — Safety Rules | 2 | 2 | Both full: SAFETY-6, DO NOT revert, token-flooding attack described |
| Q40 | S5 — Configuration | 2 | 2 | Both full: sliding window, 100 req/min/IP, Redis sorted sets, Lua script, /health + /metrics exempt |
| Q41 | S5 — Work State | 2 | 2 | Both full: verifyToken profiling and rateLimitMiddleware tests both identified |
| Q42 | S6 — Cache Key | 2 | 2 | Both full: SHA256(tokenString), cache poisoning risk, security requirement not performance |
| Q43 | S6 — Admin Token Exclusion | 2 | 2 | Both full: adminScope non-empty excluded, SAFETY-7, real-time revocation, compromised account scenario |
| Q44 | S6 — LRU Version | 2 | 2 | Both full: v7 memory leak in async callbacks, v10 fixes it, pinned ^10.0.0 |
| Q45 | S6 — Redis TTL | 2 | 2 | Both full: 900s / 604800s, named constants in tokenCacheService.ts, prevent magic numbers |
| **TOTAL** | | **30/30** | **30/30** | |

---

## Composite Scores

| | Group A (Auto-Compact) | Group B (Handoff) |
|---|---|---|
| T1 raw | 29/30 (96.7%) | 28/30 (93.3%) |
| T2 raw | 29/30 (96.7%) | 22/30 (73.3%) |
| T3 raw | 30/30 (100.0%) | 30/30 (100.0%) |
| **Composite** | **177/180 (98.3%)** | **162/180 (90.0%)** |

Composite formula: (T1×1 + T2×2 + T3×3) / (30×6)

- Group A: (29×1 + 29×2 + 30×3) / 180 = (29 + 58 + 90) / 180 = 177/180 = **98.3%**
- Group B: (28×1 + 22×2 + 30×3) / 180 = (28 + 44 + 90) / 180 = 162/180 = **90.0%**

---

## Hypothesis Evaluation

### H1: Auto-compact T1 ≈ Study 1 Round 1 (60%)
**Rejected.** T1A scored 29/30 (96.7%), far above Study 1 Round 1's 18/30 (60%). Study 2 content was structured across explicit sessions with clearly labeled safety rules and decisions, making it significantly more compaction-friendly than Study 1's dense single-session narrative. The hypothesis assumed content characteristics would be similar; they were not.

### H2: Auto-compact T2 significantly lower than T1
**Rejected.** T2A scored 29/30 (96.7%), identical to T1A (29/30). There was no degradation across compaction rounds. Study 2's session content was already organized in structured segments (S1 through S3 for T2), and the auto-compact summary apparently preserved this structure well. The multi-round degradation seen in Study 1 did not materialize.

### H3: Handoff scores stable across T1/T2/T3
**Rejected.** T1B = 28/30, T2B = 22/30, T3B = 30/30. Handoff showed significant instability at T2 (−6 points vs T1), then recovered perfectly at T3. The T2 collapse was caused by Handoff3 omitting specific operational details from S2 (optional chaining fallback, AdminTokenValidationError metadata fields) and the SET NX EX atomic mechanics from S3 — details that were present in the auto-compact summary but were not carried forward in the handoff document.

### H4: Handoff advantage larger in Study 2 than Study 1
**Rejected.** In Study 1, handoff had a consistent advantage (67% vs 27–60%, up to +40 points). In Study 2, auto-compaction outperformed handoff overall (composite 98.3% vs 90.0%, a −8.3 point disadvantage for handoff). The assumption that structured handoffs would always outperform auto-compaction was invalidated by a content format where auto-compaction performs nearly perfectly — and by a handoff document that omitted specific technical details that the auto-compact summary retained.

---

## Key Findings

- **Auto-compaction achieved near-perfect retention (98.3% composite) in Study 2**, compared to just 27–60% in Study 1. The critical variable is content structure: Study 2 sessions used explicit, labeled safety rules and decision rationale that survived summarization intact; Study 1 used implicit context that compaction destroyed.

- **Handoff collapsed at T2 to 22/30 (73.3%)** while auto-compaction held at 29/30 (96.7%). The gap was caused by three specific missing items in Handoff3: the `token.adminScope ?? ""` optional chaining fallback (Q20, score 0), the AdminTokenValidationError metadata fields `{endpoint, tokenAge}` (Q21, score 1), and the SET NX EX atomic no-op mechanic explanation (Q29, score 0). This is a handoff authoring failure, not a format failure.

- **Both agents scored 30/30 at T3**, the most demanding test point covering all 6 sessions. By Session 7, both Summary6 and Handoff6 contained sufficient cumulative context that neither agent missed a single question. Temporal distance from the original content did not cause degradation in either format.

- **Study 2 inverts Study 1's conclusion.** In Study 1, auto-compaction degraded rapidly while handoff stayed stable. In Study 2, auto-compaction was stable while handoff showed mid-study instability. The difference traces entirely to content structure and handoff document completeness — not to any inherent property of either mechanism.

- **The only consistent weakness across both studies and both formats is missing detail specificity.** Q9 scored 1/2 for both agents at T1 (missing the explicit reason why the S1 scope was limited to call-site changes), and Q21 scored 1/2 for both agents at T2 (neither captured AdminTokenValidationError's metadata fields `{endpoint, tokenAge}` fully). These gaps represent information that was present in the source material but was considered secondary — and was dropped by both formats.

---

## Limitations

- **Single scorer with no inter-rater reliability check.** All 90 scores were assigned by one agent against one rubric. Borderline 1/2 calls (Q9, Q17B, Q21A, Q21B, Q23B) may not be reproducible; a ±2 point swing per table is plausible.

- **Study 2 content was deliberately structured to test multi-session retention**, with explicit SAFETY-N labels and decision rationale sections per session. This makes it unusually compaction-friendly and limits generalizability to real engineering sessions where context is messier and less explicitly organized.

- **Handoff documents (Handoff3, Handoff6) were not inspected directly** — only the agent's T2B and T3B answers were scored. It is possible the handoff documents themselves were incomplete (authoring failures), rather than the format being inherently limited. Study 1 Section 5 identified this same failure mode and proposed format improvements that may not have been applied to the Study 2 handoff documents.

---

## Comparison with Study 1

| | Study 1 | Study 2 |
|---|---|---|
| Auto-compact Round 1 / T1 | 18/30 (60%) | 29/30 (96.7%) |
| Auto-compact Round 3 / T2 | 9/30 (30%) | 29/30 (96.7%) |
| Auto-compact Round 6 / T3 | 8/30 (27%) | 30/30 (100%) |
| Handoff T1 | 20/30 (67%) | 28/30 (93.3%) |
| Handoff T2 | 20/30 (67%) | 22/30 (73.3%) |
| Handoff T3 | 20/30 (67%) | 30/30 (100%) |
| Auto-compact composite | ~49% (unweighted avg) | 98.3% |
| Handoff composite | 67% (stable) | 90.0% |
| Winner | Handoff (+40% at Round 6) | Auto-compact (+8.3% composite) |
| Content type | Dense single-session, implicit context | Explicit multi-session, labeled safety rules |

**The primary driver of the difference is content structure, not mechanism.** When session content is explicitly organized with labeled rules and decisions, auto-compaction retains it nearly perfectly. When content is implicit and procedural, it collapses rapidly. Handoff's advantage in Study 1 was not a structural advantage of the format — it was a resilience advantage when content was unfriendly to compression.

---

## Implications for /handoff

The Study 2 results do not undermine the /handoff tool's value, but they reframe it: the handoff format is most valuable when session content is *not* already structured — specifically, when important context is embedded in procedural decisions, causal chains, or undocumented reasoning rather than in labeled rules. For sessions that already produce explicit labeled safety rules and decision records (as Study 2 sessions did), the gap between handoff and auto-compaction narrows to nearly zero at T3.

The T2 handoff collapse (22/30 vs 29/30) reveals the format's Achilles heel: **authoring completeness**. A handoff document that omits a technical detail (optional chaining fallback, metadata field names, atomic operation semantics) produces a worse outcome than auto-compaction, which summarizes everything present in the context. The Study 1 Section 5 improvements — `Key Decisions`, `Completed Detail`, `Recon Notes` — are directly relevant to preventing this class of failure, and should be considered prerequisites before relying on handoff quality for research purposes.
