# Study 4 — Test T4A (Agent answers based on Summary4 only)

Source context: Summary4 — T4 Test Context (after S4)
Date: 2026-05-23

---

**Q31**: What hover effect is currently used on project cards, and why was the alternative rejected?

The hover effect is a `border-left` accent line — a coupled pair of rules where the base state has `border-left: 3px solid transparent` (which pre-reserves the 3px space so the card does not shift sideways when the color appears) and the hover state changes the color to `var(--color-accent)`, with `transition: border-color 0.2s ease`. Box shadow was tried in three configurations (ring plus glow, glow alone, radial halo) and rejected each time because it reads as a UI "selected" state rather than a hover on dark backgrounds, and even at very low opacity it has an enterprise-dashboard heaviness that does not fit the site.

**Score**: 2 — full — complete answer with all specific details present in context.

---

**Q32**: What is unusual about the footer spacing CSS rule and why must it not be moved?

The footer's `margin-top: 4rem` was accidentally removed during S3 edits (a proximity casualty of CSS edits when renaming the Work section). As a result, both `.site-footer` and `.footer-inner p` were moved to the end of the file in a clearly labelled comment block to isolate them from the area that gets touched when sections are edited. They must not be moved because proximity to the section-editing area has already caused accidental damage once; keeping them isolated at the end prevents repeat proximity casualties.

**Score**: 2 — full — context explains both the unusual placement and the explicit reason.

---

**Q33**: Why does the contact form validate on blur rather than on form submit?

The context states that validation runs on `blur`, not on submit, and that each field has its own blur listener calling `validateField`, which calls `showFieldError` to set or clear the error text and `.input-error` border class. The submit handler runs all validations as a final gate. However, the context does not explicitly state *why* blur was chosen over submit — it describes how it works but gives no rationale for the timing choice.

**Score**: 1 — partial — implementation is described but the reason for choosing blur over submit is not stated in Summary4.

---

**Q34**: What is the rule about the email validation regex, and what is the explicit reason to keep it as-is?

The email regex is intentionally limited and should not be changed. It rejects plus-sign addresses like `name+tag@domain.com`. The fix was offered and explicitly declined. The explicit reason: clients reaching out through a portfolio contact form won't use plus addresses. This was characterized as a product decision, not an oversight.

**Score**: 2 — full — exact rule and explicit reason both present in context.

---

**Q35**: How does the contact form success message behavior work?

On valid submit, the form resets immediately via `e.target.reset()`. A success message is then shown, which uses a `setTimeout` at 3000ms to hide itself after three seconds. The user confirmed that clearing the form immediately and showing the success banner feels like the right order. No double-submit guard was added — it was considered and rejected as over-engineering for a contact form.

**Score**: 2 — full — all behavioral details present including the reset-first ordering and the 3000ms timeout.

---

**Q36**: What is the current status of the Safari smooth scroll implementation and why is it flagged as fragile?

The implementation uses a JavaScript polyfill with `document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', ...))` and `target.scrollIntoView({ behavior: 'smooth', block: 'start' })`. This per-element listener pattern was flagged at the time of writing as having a "memory-leak-adjacent quality" and was explicitly marked for refactor before deployment. At the end of S4, the polyfill is still in this per-element listener state — it has not yet been refactored to event delegation.

**Score**: 2 — full — current status and the exact fragility reason (memory-leak-adjacent per-element listeners) both present in context.

---

**Q37**: What CSS property was added to section headings and why?

`scroll-margin-top: 70px` was added to the `section` rule. The reason: to prevent the fixed nav from covering section headings when scrolling to them via anchor links. This property interacts with both the CSS `scroll-behavior` and the JS `scrollIntoView` polyfill.

**Score**: 2 — full — property, value, and reason all explicitly stated in context.

---

**Q38**: What is the status of form backend/submission at the end of S4?

The context does not mention any backend or form submission endpoint being wired up during S4. The form was built with fields, validation, and a success message, but no mention is made of Formspree or any other submission target. The "still open" list at the end of Summary4 does not include form backend as a noted item — it is absent from the discussion entirely.

**Score**: 1 — partial — the context implies no backend was connected (it is never mentioned) but does not explicitly state the backend is absent or deferred; it is an absence of information rather than an explicit statement.

---

**Q39**: What approach was chosen for smooth scrolling in Safari and what was the alternative?

The chosen approach is a JavaScript polyfill using per-element listeners: `document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', ...))` with `scrollIntoView({ behavior: 'smooth', block: 'start' })`. The context notes this approach was flagged for refactor to event delegation before deployment — so event delegation is identified as the intended replacement approach. CSS `scroll-behavior: smooth` on the `html` element alone is not supported on older Safari (added only in Safari 15.4 in 2022), which is why the polyfill was needed.

**Score**: 2 — full — chosen approach and the alternative (event delegation) both identified in context.

---

**Q40**: What sections are complete and what remains unbuilt at the end of S4?

Complete: nav, hero, about, Work section (six project cards with tag filtering and border-left hover), and the contact form section (fields, blur validation, success message).

Still open: the smooth scroll polyfill is marked for refactor to event delegation (flagged as memory-leak-adjacent). About section and hero still have placeholder content. Dark mode was not started. The explicitly listed open items in Summary4 are: smooth scroll polyfill refactor, placeholder content in about and hero.

**Score**: 2 — full — complete list of done and open items matches context exactly.

---

## Raw Scores

SCORES: Q31=2,Q32=2,Q33=1,Q34=2,Q35=2,Q36=2,Q37=2,Q38=1,Q39=2,Q40=2

**Total: 18 / 20**
