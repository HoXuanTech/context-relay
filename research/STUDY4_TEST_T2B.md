# Study 4 — T2 Test Answers (Group B, after S2)
Agent: Claude Code (Sonnet 4.6)
Date: 2026-05-23
Context source: STUDY4_DATA_B.md — "Handoff2 — T2 Test Context (after S2)" only

---

**Q11**: What CSS constraint was established about the nav styling that must be respected in all future sessions?

**Answer**: Do not add new transition classes to fix the nav hover. The fix was cascade cleanup, not transition modification; the nav transition was correct the whole time.

**Score**: 2/2 — full — explicitly stated in Safety Rules of Handoff2.

---

**Q12**: What are the two core CSS color values that define the site's visual identity?

**Answer**: Cannot answer from Handoff2 alone. The Handoff2 section does not list any specific hex color values. (Handoff1 defines the full color system, but per strict rules I am reading only from Handoff2.)

**Score**: 0/2 — cannot answer — Handoff2 contains no hex color values; they are only in Handoff1.

---

**Q13**: What was the explicit decision about CSS animations for the hero section, and what caused it?

**Answer**: Hero animation was removed entirely. CSS `fadeInUp` keyframes with staggered delays were tried, but caused layout shift on iOS — `translateY` combined with `animation-fill-mode: both` triggers layout recalculation between the painted position and the end state. The user decided to remove the animation rather than patch it.

**Score**: 2/2 — full — decision, technical cause, and user's choice all documented in Handoff2 Key Decisions.

---

**Q14**: How was the circular photo effect achieved for the about section, and why wasn't border-radius: 50% on the img tag sufficient?

**Answer**: The circular photo uses a container approach: `border-radius: 50%` and `overflow: hidden` go on `.about-photo` (the container div, not the image). `border-radius: 50%` directly on the img tag failed because the grid assigns the container a non-square height, so `aspect-ratio: 1` on the image also failed. Explicit `width: 280px; height: 280px` on the container was the fix — it prevents the grid from stretching the container vertically, keeping the circle from becoming oval.

**Score**: 2/2 — full — both the solution and the reason img-tag approach failed are documented in Key Decisions and Recon Notes.

---

**Q15**: What is the final tagline used in the hero section after multiple iterations?

**Answer**: "Frontend engineer. The details are the whole point."

**Score**: 2/2 — full — exact tagline quoted in Handoff2 Key Decisions.

---

**Q16**: What is the current mobile layout status at the end of S2?

**Answer**: A `@media (max-width: 768px)` breakpoint collapses the about grid to a single column, with the photo resized to 200px and centered. The nav is not overflowing on mobile (3 links fit on one line). `clamp()` font sizes on the hero name and tagline behave correctly on mobile.

**Score**: 2/2 — full — all three mobile status points documented in Last Actions and Completed sections of Handoff2.

---

**Q17**: What were the two root causes of the nav hover flicker, and how was each addressed?

**Answer**:
1. A stale `.site-nav a { color: var(--color-text) }` rule — created ambiguity in the cascade's starting-state calculation. Fix: the stale rule was removed entirely.
2. Missing `color: inherit` on the global `a` reset — the browser UA stylesheet default link color was interfering. Fix: `color: inherit` was added to the `a` reset.

No new transition classes were added; the fix was purely cascade cleanup.

**Score**: 2/2 — full — both root causes and both fixes explicitly documented in Key Decisions of Handoff2.

---

**Q18**: What CSS property structure is required to make the about photo circular?

**Answer**: The `.about-photo` container (not the img tag) must have: `border-radius: 50%`, `overflow: hidden`, and explicit `width` AND `height` set to the same value (280px x 280px). Both dimensions are mandatory — removing either causes the grid to assign a non-square height to the container, turning the circle into an oval.

**Score**: 2/2 — full — all required properties documented in Key Decisions and Safety Rules of Handoff2.

---

**Q19**: What must NOT be done when fixing any future nav styling issues?

**Answer**: Do not add new transition classes to fix the nav hover. The nav transition was correct the whole time; the fix was cascade cleanup (removing the stale `.site-nav a` rule and adding `color: inherit` to the global reset). Adding transition classes would be the wrong approach.

**Score**: 2/2 — full — explicitly stated in Safety Rules of Handoff2.

---

**Q20**: What sections of the site are complete at the end of S2?

**Answer**: Nav (hover flicker fully resolved across all hover cycles), Hero (name + "Frontend engineer. The details are the whole point." + CTA button, statically rendered, no animation), and About section (circular photo via container-clip approach, bio placeholder, skill tags, responsive 768px breakpoint). Projects and contact sections are still empty skeletons with no active blockers.

**Score**: 2/2 — full — Completed This Session and In Progress sections of Handoff2 both confirm these details.

---

SCORES: Q11=2,Q12=0,Q13=2,Q14=2,Q15=2,Q16=2,Q17=2,Q18=2,Q19=2,Q20=2

**Total: 18/20**

**Note on Q12**: The question asks for "two core CSS color values" but Handoff2 contains no hex values — the color system was established in S1 and is documented only in Handoff1. Answering strictly from Handoff2 makes this unanswerable. If reading across the full document were permitted, the answer would be `--color-bg #1a1a2e` (dark navy background) and `--color-accent #e94560` (coral red).
