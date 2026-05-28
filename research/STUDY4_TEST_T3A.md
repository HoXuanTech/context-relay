# Study 4 — T3 Test Answers (Group A)
Source section: Summary3 — T3 Test Context (after S3)
Date: 2026-05-23

---

**Q21**: What type of CSS effect is permanently banned from the hero section?

A CSS entrance animation was tried and removed from the hero section because it caused a mobile layout shift. Summary3 states it was "removed entirely" — the hero now renders instantly with no motion.

**Score**: 1/2 — partial — Summary3 confirms the ban and the reason (mobile layout shift) but does not name the specific animation type (`fadeInUp`) in this summary. The direction is fully correct; the specific name is only in Summary2.

---

**Q22**: What is the correct implementation for the about section's circular photo?

The container-clips pattern with explicit `280×280` dimensions is required. `border-radius: 50%` and `overflow: hidden` go on the `.about-photo` container (not on the `<img>` element), and the container needs explicit `width: 280px; height: 280px`. Responsive stacking to single column occurs at 768px.

**Score**: 2/2 — full — all key details (container not img, explicit dimensions, border-radius, overflow:hidden, 768px breakpoint) are present in Summary3.

---

**Q23**: Why was box-shadow rejected as the card hover effect?

Box shadow was tried in three configurations (ring plus glow, glow alone, radial halo) and rejected each time because it reads as a UI "selected" state rather than a hover on dark backgrounds, and even at very low opacity it has an enterprise-dashboard heaviness that doesn't fit the site.

**Score**: 2/2 — full — exact reason, number of configurations, and all three configuration names are explicitly stated in Summary3.

---

**Q24**: What CSS properties create the card hover effect currently in use?

The card hover effect uses a `border-left` accent line. Base state: `border-left: 3px solid transparent` (pre-reserves the 3px space so the card doesn't shift sideways). Hover state: `border-left-color: var(--color-accent)`. Transition: `transition: border-color 0.2s ease`. These two rules are coupled and must both be present.

**Score**: 2/2 — full — all three CSS property values, the pre-reservation rationale, and the coupling requirement are explicitly stated in Summary3.

---

**Q25**: Why is the CSS rule for footer spacing located at the end of the stylesheet in an unusual position?

The footer's `margin-top: 4rem` was accidentally removed during the S3 session as a "proximity casualty" of the CSS edits made for the Projects → Work rename. To prevent recurrence, the footer CSS was moved to the end of the file in a clearly labelled comment block to isolate it from the area that gets touched when sections are edited.

**Score**: 2/2 — full — both the cause (proximity casualty) and the deliberate rationale for relocation (isolation from high-edit section area) are explicitly in Summary3.

---

**Q26**: What responsive breakpoint is used for the project card grid, and what does it change?

Two breakpoints apply to the project card grid:
- **768px**: changes from 3 columns to 2 columns (matching the about section breakpoint for consistency)
- **480px**: changes to 1 column; the filter bar also gets `flex-wrap: wrap` at this breakpoint as a safety net for narrow viewports

**Score**: 2/2 — full — both breakpoints, both column changes, the consistency rationale, and the filter bar wrap behavior are all present in Summary3.

---

**Q27**: What is the current state of the project section at the end of S3?

The Work section (formerly Projects) is fully built with six project cards in a CSS Grid (`grid-template-columns: repeat(3, 1fr)`, `gap: 1.5rem`), a tag filter system with three categories (Frontend, Backend, Design) plus All, a `border-left` hover effect, and responsive breakpoints at 768px and 480px. "View Project" links use `href="#"` as placeholders pending real URLs.

**Score**: 2/2 — full — the context explicitly says "The Work section was fully built in S3" and provides all structural details listed above.

---

**Q28**: What triggered the "Projects → Work" section rename, and what did it break?

The context does not state what triggered the decision to rename the section — it only documents that the rename happened and what it affected. What it broke: (1) the CSS selector was left at `#projects` after the HTML `id` was changed, causing a silent bug where the section collapsed and the nav link appeared to do nothing on click; (2) the footer's `margin-top: 4rem` was accidentally removed as a proximity casualty of the CSS edits made during the same session.

**Score**: 1/2 — partial — what the rename broke is fully answered; the trigger/reason for the rename decision is not stated in Summary3.

---

**Q29**: How does the tag filter system work in the Work section?

Filter buttons use `data-filter` attributes; project cards use `data-tags` attributes. JavaScript toggles `display: none/block` using exact string matching (`===`), so each card can only belong to one category. Filter state is managed by adding and removing an `.active` class on the buttons. The "All" button has the `.active` class hardcoded in the HTML to ensure the correct initial state on page load. Three filter categories exist: Frontend, Backend, Design — plus All.

**Score**: 2/2 — full — all mechanism details (data attributes on both sides, JS toggle, exact string match, .active class management, hardcoded initial state, category list) are present in Summary3.

---

**Q30**: What are the open items / next actions at the end of S3?

Per the "Still open" closing paragraph of Summary3:
1. The contact section is an empty skeleton (not yet built)
2. The about section has placeholder content
3. The hero has placeholder content
4. The footer rule `.footer-inner p` is confirmed present in the footer block (noted as verified)
5. No animations anywhere (confirmed state)

The implied primary next action is building the contact section.

**Score**: 2/2 — full — all items in the "Still open" paragraph are captured accurately.

---

## Raw Scores

SCORES: Q21=1,Q22=2,Q23=2,Q24=2,Q25=2,Q26=2,Q27=2,Q28=1,Q29=2,Q30=2

**Total: 18/20**

**Notes:**
- Q21 scored 1: the specific animation name (`fadeInUp`) and full mobile mechanism are only in Summary2; Summary3 abstracts to "A CSS entrance animation was tried and removed because it caused a mobile layout shift." Direction is correct, specific detail absent.
- Q28 scored 1: the trigger/reason for the rename decision is not stated in Summary3 — only the consequences and what broke are documented.
