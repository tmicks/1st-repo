# Integration Architecture

How Kajabi, Airtable, HubSpot, and Credit Repair Cloud actually connect — and specifically how participants get the benefit of Airtable data without ever touching Airtable.

## System map

```
HubSpot (Admissions)
   │  eligibility form submitted, track scored
   ▼
Zapier/Make: create/update Airtable Participant record
   │
   ▼
Airtable "Participants" (source of truth for case data)
   │  on approval/payment
   ▼
Zapier/Make: grant Kajabi product + apply enrollment tag
   │
   ▼
Kajabi (participant's entire experience from here forward)
   │  progress events, tags, completions
   ▼
Zapier/Make: webhook back to Airtable (updates Milestones, Last Activity Date, tier status)
   │
   ▼
Airtable updates → (Option A) Softr/Stacker portal embedded in Kajabi
                 → (Option B) push flags back to Kajabi as tags/custom fields
```

Credit Repair Cloud sits off to the side as a coach/case-manager tool for Tier 1 Module 2 casework (disputes, bureau tracking) — it is not part of the participant-facing sync loop. Coaches log outcomes from CRC into Airtable `Case Notes`/`Milestones` manually or via CRC's own automations if available; do not attempt to expose CRC data directly to participants.

## Why participants never see Airtable

Two enforced boundaries:
1. **No direct links.** Nothing in Kajabi ever links to an airtable.com URL. Any Airtable-sourced content is either (a) rendered through a themed third-party portal (Softr/Stacker) embedded via iframe, or (b) flattened into Kajabi-native tags/custom fields before display.
2. **No Airtable credentials issued to participants.** Only `Staff` table members (Administrator, Coach, Case Manager, Housing Coach, Business Coach) get Airtable collaborator seats, permissioned per `08-staff-portal-and-roles.md`.

## Key automation triggers (build these first, in Zapier or Make)

| Trigger | Source | Action |
|---|---|---|
| Eligibility form submitted | HubSpot | Create/update Airtable Participant, set Status = Applied |
| Enrollment/payment confirmed | Kajabi or HubSpot | Set Airtable Status = Enrolled, grant Kajabi product, apply `enrolled` tag |
| Assessment submitted | Kajabi | Notify assigned-coach logic (round robin or manual), update Airtable |
| Coach assigned | Airtable (manual or automation) | Update Kajabi tag `coach:[name]`, fire Coach Assignment email |
| Lesson/module completed | Kajabi | Update Airtable Last Activity Date; if module is a Tier-gate, flag for coach sign-off |
| Coach sign-off on milestone | Airtable | Update Milestones table, sync flag set, push to Kajabi (tag or portal) |
| Tier certificate criteria met | Airtable + Kajabi | Issue Kajabi certificate, apply next-tier tag, unlock next product |
| 7 days no Kajabi activity | Kajabi | Update Airtable Last Activity Date, flag "Needs Attention" view, fire re-engagement email |
| Document requested by staff | Airtable | Push "Documents Needed" flag to participant dashboard |
| Document received | Kajabi upload or manual | Update Airtable Documents status, clear dashboard flag |

## Tooling recommendation

Use **Make** over Zapier if the team is comfortable with a slightly steeper learning curve — Make's per-operation pricing and branching logic handle this many conditional triggers more cheaply at scale. Zapier is the safer choice if whoever maintains this is non-technical; either works for the volume described here.

## Build order

Airtable base first (`06-airtable-backend-schema.md`) → Kajabi products/site (`01`, `02`) → Zapier/Make connections in the table above, one row at a time, testing each trigger with a dummy participant record before going live → dashboard integration (`03-client-dashboard.md`, Option B first) last.
