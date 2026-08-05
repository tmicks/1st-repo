# Staff Portal, Roles & Permissions

The "Staff Portal" is not a separate platform — it's the staff-side view across Kajabi (admin) and Airtable (collaborator), permissioned by role. This doc defines who sees what and does what.

## Roles

### Administrator
- **Kajabi:** Full admin — site, products, automations, offers, community moderation, staff account management
- **Airtable:** Full base editor — schema changes, all tables, all views
- **Responsibilities:** Program oversight, funder/grant reporting (`Outcome Reporting`, `Grant Tracking`), staff onboarding, escalations

### Coach (general)
- **Kajabi:** Admin/staff role scoped to content delivery + community moderation for their track's group; can view (not edit) all participant progress
- **Airtable:** Editor on `Participants` (own caseload only via "My Caseload" view), `Case Notes`, `Milestones`, `Service Verification`; read-only on `Grant Tracking`
- **Responsibilities:** Weekly calls, office hours, module sign-offs for their assigned participants, case notes

### Case Manager
- **Kajabi:** Read-only progress visibility across all participants
- **Airtable:** Full editor on `Participants`, `Documents`, `Service Verification`, `Case Notes` across all caseloads (not just one coach's)
- **Responsibilities:** Document intake/tracking, cross-coach coordination, funder/grant compliance data entry, flags participants for admin escalation

### Housing Coach
- Scoped version of Coach role, Tier 2 (Housing Access) only — same Kajabi/Airtable permission pattern, filtered to Housing-track participants

### Business Coach
- Scoped version of Coach role, Tier 3 (Entrepreneur Pathway) only, including EEP → EEC Module 4/5 — same pattern, filtered to Entrepreneur-track participants

## Permissions matrix

| Capability | Administrator | Coach | Case Manager | Housing/Business Coach |
|---|---|---|---|---|
| Edit Kajabi products/site | ✅ | ❌ | ❌ | ❌ |
| Grant/revoke Kajabi products | ✅ | ❌ | ❌ | ❌ |
| View all participants (Airtable) | ✅ | ❌ (own caseload) | ✅ | ❌ (own track) |
| Edit Case Notes | ✅ | ✅ (own caseload) | ✅ | ✅ (own track) |
| Edit Milestones/sign off tier gates | ✅ | ✅ (own caseload) | ❌ | ✅ (own track) |
| Manage Documents | ✅ | ❌ | ✅ | ❌ |
| Edit Grant Tracking | ✅ | ❌ | ✅ (view/enter, not restructure) | ❌ |
| Run Outcome Reporting | ✅ | ❌ | ✅ | ❌ |
| Manage Zapier/Make automations | ✅ | ❌ | ❌ | ❌ |

## Core SOPs to write before launch (owners noted)

1. **New participant intake** (Case Manager) — from HubSpot handoff to Airtable record confirmed and Kajabi access granted
2. **Coach assignment** (Administrator/Case Manager) — assignment logic (caseload balance, track match), and how it's recorded
3. **Tier-gate sign-off** (Coach) — what "done" means for each module gate before applying the certificate/unlock tag
4. **Document chase** (Case Manager) — cadence for following up on outstanding `Documents` records
5. **Inactivity follow-up** (Coach) — what to do when a participant hits the "Needs Attention" view (call script, escalation point)
6. **Funder reporting cycle** (Administrator) — pulling `Outcome Reporting` + `Grant Tracking` into whatever cadence/format each funder requires
7. **Off-boarding** (Administrator) — process for Completed vs. Withdrawn participants, Kajabi access changes, final Airtable status
