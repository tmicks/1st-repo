# Economic Stability Institute — Kajabi Launch Package

This repo is the build-out package for launching the **Economic Stability Service** on Kajabi, with Airtable as the invisible operational backend. It's written to be handed directly to whoever builds the Kajabi site/products, the Airtable base, and the automations — no additional interpretation required.

**Positioning:** This is not marketed as a credit repair program. It is the front door to an **Economic Stability Institute**, serving workforce participants, apprentices, returning residents, homebuyers, entrepreneurs, and clean-energy contractors (EEP → EEC) under one platform that can scale into employer contracts and workforce board partnerships.

**Stack:**
- **Kajabi** = the University (learning, community, coaching, certificates, client-facing everything)
- **Airtable** = the Case Management System (participant records, grants, verification, outcomes — staff-only, participants never see it)
- **HubSpot** = the Admissions Office (lead capture, eligibility, CRM)
- **Credit Repair Cloud** = the Credit Operations Platform (dispute/credit-repair casework)

## Contents

| Doc | Purpose |
|---|---|
| [`docs/00-overview.md`](docs/00-overview.md) | Positioning, architecture, success metrics |
| [`docs/01-website-structure.md`](docs/01-website-structure.md) | Full site map + page-by-page copy, ready to paste into Kajabi |
| [`docs/02-kajabi-curriculum.md`](docs/02-kajabi-curriculum.md) | Full product/module/lesson build with objectives & downloads |
| [`docs/03-client-dashboard.md`](docs/03-client-dashboard.md) | Participant dashboard spec — what shows, where the data comes from |
| [`docs/04-automations-and-emails.md`](docs/04-automations-and-emails.md) | Enrollment automation + full email copy |
| [`docs/05-sales-funnel-and-eligibility.md`](docs/05-sales-funnel-and-eligibility.md) | Funnel, eligibility assessment questions, payment/enrollment logic |
| [`docs/06-airtable-backend-schema.md`](docs/06-airtable-backend-schema.md) | Airtable base: tables, fields, relationships, views |
| [`docs/07-integration-architecture.md`](docs/07-integration-architecture.md) | How Kajabi ↔ Airtable ↔ HubSpot ↔ CRC actually connect, and how participants never see Airtable |
| [`docs/08-staff-portal-and-roles.md`](docs/08-staff-portal-and-roles.md) | Roles, permissions matrix, SOPs |
| [`docs/09-certificates-and-assessments.md`](docs/09-certificates-and-assessments.md) | Assessment question banks + certificate specs |
| [`docs/10-phase2-roadmap.md`](docs/10-phase2-roadmap.md) | Economic Mobility Institute expansion academies |
| [`docs/11-launch-checklist.md`](docs/11-launch-checklist.md) | Step-by-step build order to go live |
| [`docs/12-kajabi-build-runbook.md`](docs/12-kajabi-build-runbook.md) | **Literal click-by-click instructions** — exact Kajabi menus, what to paste where |
| [`docs/13-lesson-content-template.md`](docs/13-lesson-content-template.md) | Lesson content template + the format used for every lesson below |
| [`docs/14-lesson-content-orientation.md`](docs/14-lesson-content-orientation.md) | Full content: Orientation, Program Expectations, Forms, Assessment |
| [`docs/15-lesson-content-tier1.md`](docs/15-lesson-content-tier1.md) | Full content: all 19 Tier 1 lessons (Financial Stability, Credit & Banking) |
| [`docs/16-lesson-content-tier2.md`](docs/16-lesson-content-tier2.md) | Full content: all 11 Tier 2 lessons (Housing Access & Stability) |
| [`docs/17-lesson-content-tier3.md`](docs/17-lesson-content-tier3.md) | Full content: all 24 Tier 3 lessons (Entrepreneur & Economic Participation, incl. Illinois Shines EEP→EEC) |
| [`airtable-import/`](airtable-import/) | **Ready-to-import CSVs** for all 8 Airtable tables, plus field-type setup instructions |

## Fastest path to execution

1. Read `docs/00-overview.md` for positioning.
2. Import the base: `airtable-import/README.md` → import all 8 CSVs → fix field types per that doc's reference.
3. Follow `docs/12-kajabi-build-runbook.md` phase by phase — it points to the exact content doc for each piece as you go, including `docs/14`-`docs/17` for pasting full lesson content directly into each Post.
4. Finish with `docs/11-launch-checklist.md` Phases 7-8 (soft launch → go live).

This kit assumes you or a teammate is logged into your own Kajabi/Airtable/HubSpot accounts and pasting directly — no credentials are needed by anyone else to execute it.
