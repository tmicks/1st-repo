# Overview & Positioning

## The front door, not the whole building

The **Economic Stability Service (ESS)** is the entry program. It is marketed as the front door to an **Economic Stability Institute** — not as a credit repair product. Credit work is one module inside Tier 1, not the headline. This framing is what lets the same platform serve workforce participants, apprentices, returning residents, CDC clients, homebuyers, entrepreneurs, EEPs pursuing EEC opportunities, and employers seeking retention/advancement support, without re-platforming later.

## Why this framing matters commercially

A "credit program" caps you at one funding source and one audience. An "Economic Stability Institute" is fundable by workforce boards, housing initiatives, clean energy programs, and employer contracts simultaneously — and every one of those funding sources can point participants at the *same* Kajabi front door and the *same* Airtable case record.

## Platform architecture (who does what)

| Platform | Role | Participant-facing? |
|---|---|---|
| **Kajabi** | Learning (courses/products), community, coaching/calls, certificates, client dashboard, marketing emails, checkout | **Yes — this is the entire participant experience** |
| **Airtable** | Participant record, grant tracking, service verification, case notes, milestones, document intake, outcome reporting | **No — staff/case-manager only** |
| **HubSpot** | Lead capture, eligibility intake, CRM/pipeline, marketing attribution | Partially (forms only, pre-enrollment) |
| **Credit Repair Cloud** | Dispute letters, bureau tracking, credit-repair casework | No — coach/case-manager tool |

Participants live entirely inside Kajabi. Anything that looks like "your documents," "your milestones," or "your case notes" on their dashboard is actually Airtable data reflected into Kajabi through the integration layer described in `07-integration-architecture.md` — they never see an Airtable interface, login, or branding.

## The three service tracks (Tiers)

1. **Financial Stability** — budgeting, credit, banking alignment
2. **Housing Access** — rent-ready, housing stability, homeownership pathway
3. **Entrepreneur Pathway** — business formation, business banking, capital pathways, Illinois Shines EEP → EEC, EEC Incubator

## Who this serves

Construction graduates, apprentices, returning residents, justice-impacted individuals, veterans, workforce participants, future entrepreneurs.

## Outcomes tracked

Financial stability, housing stability, business formation, capital pathways, EEP → EEC support/advancement.

## Success metrics to instrument from day one

Build these into Airtable reporting (`06-airtable-backend-schema.md`) so outcome reporting to funders is a query, not a project:

- Enrollment → Beginning Assessment completion rate
- Tier completion rate (1, 2, 3) and time-to-completion
- Certificate issuance count by type
- Coaching call attendance rate
- Housing outcome: rent-ready → housed → stable at 6/12 months
- Business outcome: entity formed → banked → capital accessed
- EEP → EEC conversion rate
- Document turnaround time (requested → received)

## What "ready to launch" means for this package

Every doc in this repo is written so a Kajabi builder and an Airtable builder could execute it without further clarification: exact nav structure, exact product/module/lesson tree, exact email copy, exact Airtable fields, exact automation triggers, and a build-order checklist. Copy is a strong first draft meant to be reviewed against the actual grant/funder language you're operating under before publishing.
