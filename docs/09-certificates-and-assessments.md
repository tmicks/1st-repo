# Certificates & Assessments

## Assessment structure

Three assessment points per participant journey, each gating the next stage. Build as Kajabi native quizzes/forms where possible; use a typeform-style embed if branching logic exceeds Kajabi's native quiz builder.

### Beginning Assessment (Product 1, Module 4 — gates track assignment and Tier access)
Purpose: baseline + coach-matching (in addition to the eligibility scoring already done pre-enrollment). **As actually built in Kajabi, this is 4 separate lessons/assessments, not one combined form** — see `docs/14-lesson-content-orientation.md` Module 4 for the full participant-facing copy. Question banks below map to each:

**Financial Assessment**
1. On a scale of 1-5, how confident are you in managing a monthly budget?
2. Have you reviewed a credit report in the last 12 months? (Y/N)
3. Do you currently have a checking/savings account in consistent use? (Y/N)

**Housing Assessment**
4. What is your current housing status? (repeat/confirm from intake)
5. Any current housing stability concerns? (open text)
6. Is homeownership a goal, and on what general timeline?

**Entrepreneur Assessment**
7. Do you have a business idea or existing business? (Y/N, describe)
8. Is your business already formed (LLC/EIN), or still just an idea?
9. Any interest in construction, clean energy, or contractor work (Illinois Shines EEP/EEC)?

**Economic Stability Goals** (synthesis lesson, completed after the above three)
10. What's the single biggest barrier standing between you and your goal today? (open text — coach reads this before first call)
11. What does success look like for you in 6 months? (open text)

This synthesis lesson is what the coach uses to confirm the recommended Tier — the output feeds directly into Module 5 (Participant Action Plan).

### Midpoint Assessment (administered at Tier transition, e.g. end of Tier 1 / start of Tier 2)
Purpose: confirm milestone completion, re-confirm readiness, catch anything that stalled.
Sample questions:
1. Have you completed your Financial Stability Plan (budget, savings target, financial calendar)? (Y/N)
2. Has your credit action plan been implemented? (Y/N, what's changed)
3. Are you banking consistently with your program-aligned account? (Y/N)
4. Rate your current confidence toward your next goal (Housing/Business), 1-5
5. What support do you still need from your coach?
6. Any changes to income, housing, or household status since enrollment?

### Completion Assessment (administered at Program Completion)
Purpose: outcome verification for funder reporting + testimonial capture.
Sample questions:
1. Which certificates have you earned? (confirm against Airtable record)
2. Describe the outcome(s) you achieved (financial stability / housing / business formation / capital access / EEP→EEC)
3. Would you be willing to share your story for Success Stories? (Y/N, release form link if Y)
4. What would you tell someone considering this program?
5. What's your next goal? (feeds Phase 2 interest — see `10-phase2-roadmap.md`)

## Certificate specs

| Certificate | Trigger | Issued via |
|---|---|---|
| Financial Stability Certificate | Tier 1 Module 4 complete + Coach sign-off in Airtable | Kajabi native certificate feature, auto-issued on tag |
| Housing Access Certificate | Tier 2 Module 3 complete + Housing Coach sign-off | Same |
| Entrepreneur & Economic Participation Certificate | Tier 3 Module 5 complete + Business Coach sign-off | Same |
| Economic Stability Certificate (Program Completion) | All three above earned | Kajabi native, triggered on all three certificate tags present |

Each certificate PDF should include: participant name, certificate name, date issued, program/institute branding, and a verification ID that maps back to the Airtable `Outcome Reporting` record — useful if a funder or employer ever needs to verify authenticity.
