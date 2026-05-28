# Study 4 — T4B Test Results (Agent answers based on Handoff4 context only)

Source section used: "## Handoff4 — T4 Test Context (after S4)" from STUDY4_DATA_B.md

---

**Q31**: What hover effect is currently used on project cards, and why was the alternative rejected?

The current hover effect is a `border-left` accent line: `border-left: 3px solid transparent` in the base state (space pre-reserved), and `border-left-color: var(--color-accent)` on hover, with `transition: border-color 0.2s ease`. The alternative — box-shadow — was tried in three configurations (ring+shadow, shadow-only, and radial halo) and rejected each time. The reasons given were: "too UI-y like a form input," "too corporate/enterprise dashboard," and the final verdict "the glowing thing doesn't fit this design." The border-left was described as more editorial.

**Score**: 2/2 — full and specific answer

---

**Q32**: What is unusual about the footer spacing CSS rule and why must it not be moved?

The footer CSS (including `margin-top: 4rem` spacing) lives at the end of `style.css` inside a labelled comment block. This is unusual because it is deliberately isolated from the rest of the section rules. The reason it must not be moved: it was accidentally displaced during the "Work" rename edits in S3, which caused it to be lost as a proximity casualty — not from the logic of the rename itself, but simply from being adjacent to heavily-edited CSS. Physically isolating it at the end of the file prevents future proximity casualties.

**Score**: 2/2 — full and specific answer

---

**Q33**: Why does the contact form validate on blur rather than on form submit?

Blur-triggered validation was the user's explicit preference. The reason stated in the context is the user's own framing: "feels like the form is paying attention to you as you fill it out." It was chosen over submit-only or live (per-keystroke) validation.

**Score**: 2/2 — full and specific answer

---

**Q34**: What is the rule about the email validation regex, and what is the explicit reason to keep it as-is?

The regex is `/^[a-zA-Z0-9._%\-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`. It intentionally rejects `name+work@gmail.com` style addresses (plus-sign addresses). The explicit reason to keep it as-is: the user was offered the fix, tested the form with their own work email `name+work@gmail.com`, saw the error, and explicitly declined the fix, saying: "my clients won't use plus addresses, it's a contact form not a mission-critical system." This is documented as a product decision, not a bug.

**Score**: 2/2 — full and specific answer

---

**Q35**: How does the contact form success message behavior work?

When a valid form is submitted: (1) the form resets immediately via `e.target.reset()`, which fires at the same time as the success message display — the form clears right away; (2) the `#form-success` div is shown; (3) after 3 seconds (a `setTimeout`), the success message hides. The user tested and confirmed the 3-second duration as "quick enough but enough time to read it," and confirmed clearing the form immediately: "the form is done, clear it right away."

**Score**: 2/2 — full and specific answer

---

**Q36**: What is the current status of the Safari smooth scroll implementation and why is it flagged as fragile?

The smooth scroll polyfill is implemented and working in Safari (verified at end of S4). However, it is flagged as fragile / memory-leak-adjacent because it uses per-element event listeners attached via `querySelectorAll('a[href^="#"]').forEach()`. Each anchor element gets its own listener, which is a memory-leak-adjacent pattern. The context notes it "should be refactored to event delegation before deployment." It is listed under "In Progress" rather than fully complete.

**Score**: 2/2 — full and specific answer

---

**Q37**: What CSS property was added to section headings and why?

`scroll-margin-top: 70px` was added to all sections (on the section rule). The reason: after the Safari smooth scroll polyfill was implemented, the user discovered that section headings were being clipped/hidden under the fixed nav when smooth scroll fired. The `scroll-margin-top` value of 70px offsets the scroll target so the heading appears below the fixed nav instead of behind it.

**Score**: 2/2 — full and specific answer

---

**Q38**: What is the status of form backend/submission at the end of S4?

There is no backend on the form. The success message is cosmetic only — no data is transmitted when the form is submitted. This is explicitly noted under "In Progress" at the end of S4.

**Score**: 2/2 — full and specific answer

---

**Q39**: What approach was chosen for smooth scrolling in Safari and what was the alternative?

The chosen approach is a JS polyfill: `querySelectorAll('a[href^="#"]').forEach()` with `scrollIntoView({ behavior: 'smooth' })`. The alternative that was not used: CSS `scroll-behavior: smooth` alone. The reason for rejecting the CSS-only approach: it doesn't work on older Safari — `scroll-behavior: smooth` was only added in Safari 15.4, whereas the JS polyfill provides coverage from Safari 14.

**Score**: 2/2 — full and specific answer

---

**Q40**: What sections are complete and what remains unbuilt at the end of S4?

**Complete:** nav, hero, about section (with placeholder photo/bio), work/projects section (six-card grid with filter), contact form (with blur validation and success message), Safari smooth scroll polyfill, `scroll-margin-top` nav offset.

**Still in progress / unbuilt:**
- About section: still has placeholder photo and bio (not real content)
- Form backend: no data transmission, success message is cosmetic only
- Smooth scroll polyfill: functional but flagged for refactor (per-element listeners to event delegation) before deployment

**Score**: 2/2 — full and specific answer

---

SCORES: Q31=2,Q32=2,Q33=2,Q34=2,Q35=2,Q36=2,Q37=2,Q38=2,Q39=2,Q40=2
