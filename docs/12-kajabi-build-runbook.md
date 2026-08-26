# Kajabi Build Runbook — Literal Click-by-Click

Execute in this order. Menu names match Kajabi's admin as of 2025/2026 — if a label has moved slightly in your account, it'll be the nearest equivalent under the same top-level section. Every piece of copy referenced below is already written in this repo — this doc is just "where to click and paste it."

Work through one numbered phase at a time. Don't start the next phase until the current one is done — automations in Phase 5 depend on tags/products that don't exist until Phases 2-3 are built.

---

## Phase 1 — Site shell

1. **Kajabi Dashboard → Website → Pages.**
2. For each nav item in `docs/01-website-structure.md`, click **+ New Page**, choose a blank/basic layout, and name it exactly as the nav label (Home, About, Services, Programs, Success Stories, Resource Center, Book Consultation, Contact). Client Portal is not a new page — skip it here (see Phase 3).
3. For each page, use the **Section/Block editor** to add a Text block per heading in `01-website-structure.md` and paste the copy in directly — H1/H2 as Heading blocks, body copy as Text blocks, buttons as Button blocks linking to the URLs noted in that doc (`/apply`, `/book-consultation`, `/programs#[tier]`).
4. **Website → Navigation** → drag the 9 pages into the exact order: Home, About, Services, Programs, Client Portal, Success Stories, Resource Center, Book Consultation, Contact.
5. **Website → Domain** → connect your custom domain if not already done.
6. On the Book Consultation page, add your scheduler embed (Kajabi's native scheduling or an embedded Calendly/Acuity block) per the "Embedded Kajabi/third-party scheduler" note in `01-website-structure.md`.

## Phase 2 — Products (curriculum)

Do this once per Product in `docs/02-kajabi-curriculum.md` (4 products total).

1. **Products → + New Product.** Name it exactly as listed (e.g., "Tier 1: Financial Stability, Credit & Banking").
2. Inside the product, **+ New Category** for each Module (e.g., "Module 1 — Financial Assessment").
3. Inside each Category, **+ New Post** for each Lesson listed under that module.
4. In each Post's editor: add a Text/Video block for the lesson content, then under **Downloads** attach the 6 files per the template in `02-kajabi-curriculum.md` (PDF, Worksheet, Checklist, Template, Example, Action Plan) — even placeholder PDFs are fine for launch; swap in final content as it's produced.
5. Repeat for all 4 products: Economic Stability Service (Orientation), Tier 1, Tier 2, Tier 3.
6. **Product Settings → Progress & Completion** — for each Tier product, set the completion rule (e.g., "all lessons in all categories must be marked complete") so Kajabi's native progress tracking works for the dashboard's Progress widget (`03-client-dashboard.md`).
7. **Product Settings → Certificates** → enable and design the certificate for each Tier product using the specs in `09-certificates-and-assessments.md` (Financial Stability Certificate, Housing Access Certificate, Entrepreneur & Economic Participation Certificate). For the Economic Stability Certificate (Program Completion), you'll gate it on all three tags being present — build that logic in Phase 5's Automations, not here.
8. **Product Settings → Drip/Access** → set each Tier product's default visibility to "hidden until tag applied" (`tier1-unlocked`, `tier2-unlocked`, `tier3-unlocked`) — these tags get applied by the automations in Phase 5, not manually.

## Phase 3 — Assessments, Community, Coaching, Client Portal

1. **Assessments:** Build the Beginning/Midpoint/Completion assessments (`09-certificates-and-assessments.md`) as Posts inside the relevant Product using Kajabi's native Quiz/Form block, or embed a Typeform if you need branching logic beyond what the native block supports.
2. **Community → + New Group**, create the 5 groups from `02-kajabi-curriculum.md`: Financial Stability, Housing, Entrepreneur, Construction Graduates, EEC Participants. Under each group's settings, restrict visibility to members with the matching track tag.
3. **Coaching:** Set up the Weekly Live Call as a recurring Kajabi Event (or embedded Zoom link on a Community post). Set up Office Hours booking per track (Financial/Housing/Business/EEC) — either Kajabi's native booking or an embedded scheduler per coach.
4. **Client Portal page (Website → Pages → the "Client Portal" nav item):** point this at Kajabi's native members-area login/dashboard rather than a custom blank page — Kajabi handles the logged-out → login redirect automatically once a visitor without an active session clicks it. Build the actual dashboard widgets described in `03-client-dashboard.md` as a custom **Member Dashboard** page inside the members area (Kajabi calls this the "Home" or "Dashboard" area of the member site) using conditional content blocks keyed to tags.

## Phase 4 — Offers, Pipelines & HubSpot handoff

1. **Offers → + New Offer** for the Economic Stability Service: one $0 offer gated by an `admissions-approved` tag (grant-funded path), and one paid offer if self-pay is being offered (`05-sales-funnel-and-eligibility.md`).
2. **Pipelines → + New Pipeline** for the `/apply` funnel: Landing → Eligibility Assessment (embed the HubSpot form) → Recommended Service confirmation page → Offer/Checkout → Enrollment confirmation.
3. Build the HubSpot eligibility form separately in HubSpot using the 12 questions in `05-sales-funnel-and-eligibility.md`, then embed it on the `/apply` step of the Pipeline via HubSpot's embed code.
4. Confirm HubSpot's workflow (built in HubSpot, not Kajabi) creates/updates the Airtable Participant record on form submission — this is the Zapier/Make connection from `07-integration-architecture.md`, built in Phase 5.

## Phase 5 — Automations & integrations

1. **Automations → + New Automation** in Kajabi for each row of the trigger table in `docs/07-integration-architecture.md`. Kajabi automations are Trigger → Action; use "Tag Applied," "Offer Purchased," "Lesson Completed," and "Assessment Submitted" as your available native triggers, and "Apply Tag," "Grant Offer," "Send Email" as actions.
2. **Sequences → + New Sequence** for the 8 emails in `04-automations-and-emails.md` — paste each subject/body directly, and set the sequence's trigger/delay logic to match the flow diagram at the top of that doc (immediate, +2 days, +3 days, on-completion triggers, 7-day inactivity, etc.).
3. Sign up for **Zapier or Make** (recommendation in `07-integration-architecture.md`) and build each Airtable ↔ Kajabi connection in the trigger table one row at a time. Test every single one with one dummy participant before connecting the next — this is the step most likely to have a silent failure if rushed.
4. Implement dashboard **Option B** from `03-client-dashboard.md`: the Zap/Make scenario that pushes Airtable's Documents/Milestones status back into Kajabi as member tags, and the conditional content blocks on the Member Dashboard page that read those tags.

## Phase 6 — Staff & permissions

1. **Kajabi → Settings → Team Members** → add each staff person, assign role/permission level per `08-staff-portal-and-roles.md`.
2. **Airtable → Share → Manage collaborators** → add the same staff people with the permission level from the matrix in `08-staff-portal-and-roles.md` (Administrator = full editor, Coach = editor scoped to their caseload view, Case Manager = full editor on operational tables, Housing/Business Coach = scoped like Coach).
3. Write and store the 7 SOPs listed in `08-staff-portal-and-roles.md` wherever your team keeps internal docs (Airtable itself, Notion, Google Docs — not Kajabi, since these are staff-only).

## Phase 7 — Content & proof

1. Add 2-3 Success Stories to that page (real or "coming soon" placeholders if none exist yet).
2. Add 5-8 Resource Center articles/guides, each with an email opt-in gate feeding the HubSpot nurture list.
3. Swap placeholder lesson downloads (Phase 2, step 4) for final PDFs/worksheets as they're produced — track this as an ongoing content-production backlog, not a launch blocker.

## Phase 8 — Soft launch & go live

Follow `docs/11-launch-checklist.md` Phases 7-8 exactly: run 3-5 test participants through the entire funnel end-to-end, confirm every automation and Airtable sync fired, fix what's broken, then open enrollment.

---

## If something in Kajabi's UI doesn't match a step above

Kajabi ships incremental UI changes fairly often. If a menu path here is stale, the content and logic in `docs/01` through `docs/11` are still the source of truth — find the nearest equivalent screen (Products/Courses, Automations/Workflows, Offers/Checkout, Community/Groups are the stable core concepts even when exact labels shift) and apply the same copy/logic.
