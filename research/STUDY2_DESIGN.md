# Study 2 Design: Realistic Multi-Session Context Degradation
> Status: Design complete — pending execution

---

## Research Question

Study 1 had a flaw: we simulated multi-round compaction by compressing the *same* content repeatedly. Real usage is different — users *keep working* between compactions, accumulating new information. Each compaction event compresses the previous summary *plus new work*.

**Study 2 asks:** In a realistic 6-session project, how does context retention compare between auto-compaction and /handoff, when new work is added each session?

---

## Scenario: api-gateway (6 Sessions)

Continuation of the JWT refactor scenario from Study 1. Each session adds a new realistic task.

| Session | New Work Content |
|---|---|
| S1 | JWT refactor base (from Study 1) — authMiddleware, async verifyToken, 5 handlers |
| S2 | Attempt to fix adminHandler.ts unsafe cast; discover AdminTokenPayload structural issue |
| S3 | Redis race condition fix; evaluate async-mutex; add connection pooling |
| S4 | Test coverage for orderHandler async path; introduce integration test setup |
| S5 | New rate-limiting middleware added; conflicts discovered with authMiddleware pipeline |
| S6 | Performance profiling; verifyToken cache optimization; Redis TTL strategy |

Each session produces:
- 3–5 new decisions (with reasoning)
- 1–2 new safety rules or constraints
- New "in progress" items
- New "next actions"

---

## Two Groups

| | Group A: Auto-compact | Group B: /handoff |
|---|---|---|
| Between sessions | Compress (prev summary + new work) → continue | Write /handoff → open new session with handoff loaded |
| File access | Can read any project file (same as real Claude Code) | Can read any file listed in handoff's `→ read` pointers |
| Starting context | Accumulated compressed summary | Fresh handoff snapshot (55 lines max) |

**Fairness rule:** Handoff must include `→ read` pointers for any project files that auto-compact group can access. Neither group gets extra advantage from file system access.

---

## Test Points

Test happens at the **start** of the session — before any new work begins. This simulates "user returns to the project and Claude must resume work immediately."

| Test Point | When | What's tested |
|---|---|---|
| **T1** | Start of Session 2 | Retention of S1 content |
| **T2** | Start of Session 4 | Retention of S1+S2+S3 content (weighted) |
| **T3** | Start of Session 7 | Retention of S1–S6 content (weighted) |

Session 7 has no new work — it is the final test session only.

---

## Question Design

### Weighting by Recency

Newer content gets more questions. Ratio follows session recency:

| Test Point | Session weights | Question distribution |
|---|---|---|
| T1 | S1 only | 15 questions, all S1 |
| T2 | S1:S2:S3 = 1:2:3 | 15 questions: 2–3 S1, 4–5 S2, 6–7 S3 |
| T3 | S1:S2:S3:S4:S5:S6 = 1:2:3:4:5:6 | 15 questions: 1 S1, 1 S2, 2 S3, 3 S4, 4 S5, 4 S6 |

### Question Categories (5 per test point, same as Study 1)

Each test point has questions across three categories:
1. **Safety rules** — what must not be touched, and why
2. **Decision rationale** — why a specific approach was chosen
3. **Work state** — what is done, what is pending, exact next step

### Scoring

Same rubric as Study 1:
- **2**: Accurate and specific (includes reasoning and detail)
- **1**: Partially correct (right direction, missing specifics)
- **0**: Cannot answer

Max per test point: 30 points.
Weighted total across all test points: (T1 × 1) + (T2 × 2) + (T3 × 3) / 6 → single composite score.

---

## Agent Chain

### Phase 0: Setup (1 agent)
- Write all 6 session content scripts (S1–S6), each 300–400 words
- Write all ground truth questions for T1, T2, T3 (15 questions each = 45 total)
- Output: `STUDY2_CONTENT.md` (session scripts + ground truth)

### Phase 1: Group A — Build compaction chain (6 agents, sequential)
Each agent receives: previous summary + new session content → outputs new compressed summary

- Agent A1: Compress S1 → Summary1
- Agent A2: Compress (Summary1 + S2) → Summary2
- Agent A3: Compress (Summary2 + S3) → Summary3  ← T2 test uses Summary3
- Agent A4: Compress (Summary3 + S4) → Summary4
- Agent A5: Compress (Summary4 + S5) → Summary5
- Agent A6: Compress (Summary5 + S6) → Summary6  ← T3 test uses Summary6

T1 test uses Summary1.

### Phase 2: Group B — Build handoff chain (6 agents, sequential)
Each agent receives: previous handoff (if any) + session content → outputs new handoff file

- Agent B1: Write Handoff1 from S1 content
- Agent B2: Write Handoff2 from (Handoff1 context + S2 content)
- Agent B3: Write Handoff3 from (Handoff2 context + S3 content)  ← T2 test uses Handoff3
- Agent B4: Write Handoff4 from (Handoff3 context + S4 content)
- Agent B5: Write Handoff5 from (Handoff4 context + S5 content)
- Agent B6: Write Handoff6 from (Handoff5 context + S6 content)  ← T3 test uses Handoff6

T1 test uses Handoff1.

### Phase 3: Testing (6 agents, can run in pairs)
Each test agent receives ONLY its assigned context (summary OR handoff) — no other information.

- Agent T1A: Answer T1 questions using Summary1 only
- Agent T1B: Answer T1 questions using Handoff1 only
- Agent T2A: Answer T2 questions using Summary3 only
- Agent T2B: Answer T2 questions using Handoff3 only
- Agent T3A: Answer T3 questions using Summary6 only
- Agent T3B: Answer T3 questions using Handoff6 only

### Phase 4: Scoring + Analysis (me)
- Score all answers against ground truth
- Build comparison tables
- Write STUDY2_RESULTS.md

---

## Execution Notes

- Phases 0 is prerequisite for all others
- Phase 1 and Phase 2 are independent and can run in parallel after Phase 0
- Phase 3 pairs (T1A+T1B, T2A+T2B, T3A+T3B) can run in parallel within each pair
- Minimum sequential agent calls: Phase0 → [Phase1 chain] → T_A tests = 1 + 6 + 3 = 10
- Total agents: 1 + 6 + 6 + 6 = 19 agents

---

## Output Files

| File | Content |
|---|---|
| `research/STUDY2_DESIGN.md` | This document |
| `research/STUDY2_CONTENT.md` | Session scripts + ground truth (generated in Phase 0) |
| `research/STUDY2_DATA.md` | Raw agent outputs — all summaries, handoffs, test answers |
| `research/STUDY2_RESULTS.md` | Final analysis, scoring tables, conclusions |

---

## Hypotheses

Based on Study 1 findings:

1. **H1:** Auto-compact T1 score ≈ Study 1 Round 1 score (60%) — single compaction baseline holds
2. **H2:** Auto-compact T2 score will be significantly lower than T1, especially for S2–S3 content (new information more vulnerable than original content)
3. **H3:** Handoff T scores will remain stable across T1, T2, T3 — each handoff is a fresh snapshot, not an accumulation
4. **H4:** The handoff advantage over auto-compact will be larger in Study 2 than Study 1, because Study 2 tests *new* content (higher vulnerability) not just *original* content

---

## /goal Discussion

Deferred to after Study 2 completion. Key question noted: does /goal have its own context management, and is it compatible or in conflict with context-relay's new-window mechanism?

See: `research/FUTURE_WORK.md` (to be created)
