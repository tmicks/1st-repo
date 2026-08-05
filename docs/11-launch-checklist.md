# Launch Checklist — Build Order

Follow in this order. Each phase references the doc that has the full spec.

## Phase 1 — Foundation (Airtable + Kajabi skeleton)
- [ ] Build Airtable base: all 8 tables, fields, and links (`06-airtable-backend-schema.md`)
- [ ] Build Airtable views: My Caseload, Needs Attention, Outstanding Documents, Pending Sync, Grant Capacity
- [ ] Create Kajabi site, connect domain
- [ ] Set up Kajabi nav: Home / About / Services / Programs / Client Portal / Success Stories / Resource Center / Book Consultation / Contact (`01-website-structure.md`)
- [ ] Build all public marketing pages with copy from `01-website-structure.md`

## Phase 2 — Curriculum
- [ ] Create Product 1 (Economic Stability Service / Orientation) with its 5 sections (`02-kajabi-curriculum.md`)
- [ ] Create Product 2 (Tier 1) — 4 modules, all lessons, each with the 6-item download template
- [ ] Create Product 3 (Tier 2) — 3 modules
- [ ] Create Product 4 (Tier 3) — 5 modules
- [ ] Produce downloads for every lesson: PDF, Worksheet, Checklist, Template, Example, Action Plan
- [ ] Build Beginning / Midpoint / Completion assessments (`09-certificates-and-assessments.md`)
- [ ] Build all 4 certificate templates and configure auto-issuance tags

## Phase 3 — Community & Coaching
- [ ] Create Kajabi Community groups: Financial Stability, Housing, Entrepreneur, Construction Graduates, EEC Participants — tag-gated
- [ ] Set up Weekly Live Call (program-wide)
- [ ] Set up Office Hours booking per track: Financial, Housing, Business, EEC
- [ ] Load Staff accounts and assign roles/permissions (`08-staff-portal-and-roles.md`)

## Phase 4 — Sales Funnel & HubSpot
- [ ] Build HubSpot eligibility assessment form with scoring logic (`05-sales-funnel-and-eligibility.md`)
- [ ] Build `/apply` and `/book-consultation` pages
- [ ] Set up Kajabi Offers/Checkout (grant-funded $0 path + self-pay path if applicable)
- [ ] Confirm admissions review step before final enrollment (no fully-blind auto-enrollment)

## Phase 5 — Automations & Integration
- [ ] Build the enrollment automation end-to-end in Kajabi (`04-automations-and-emails.md`)
- [ ] Write and load all 8 email templates
- [ ] Set up Zapier/Make connections for every trigger in `07-integration-architecture.md`'s table, testing each with a dummy participant before going live
- [ ] Build dashboard Option B (tag-based Airtable → Kajabi flags) for Documents Needed and Milestones widgets (`03-client-dashboard.md`)
- [ ] Confirm no Airtable links/branding are reachable from any participant-facing Kajabi page

## Phase 6 — Content & Proof
- [ ] Populate Success Stories page (even 2-3 to start; more added as first cohort completes)
- [ ] Populate Resource Center with 5-8 starter articles/guides tied to email-gated lead magnets
- [ ] Write SOPs listed in `08-staff-portal-and-roles.md`

## Phase 7 — Soft Launch
- [ ] Run 3-5 test participants through the full funnel: apply → assessment → payment/grant → enrollment → Kajabi access → first coaching call
- [ ] Confirm every automation trigger fired correctly and every Airtable sync landed
- [ ] Confirm coach notification and sign-off flow works end-to-end for at least one tier-gate
- [ ] Fix anything broken before opening enrollment publicly

## Phase 8 — Go Live
- [ ] Open public enrollment
- [ ] Turn on paid/organic traffic to Home and Resource Center
- [ ] Begin outcome tracking from day one (`00-overview.md` success metrics) so first funder report is a query, not a scramble
