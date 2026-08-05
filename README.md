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

Start with `docs/00-overview.md`, then build in the order listed in `docs/11-launch-checklist.md`.
