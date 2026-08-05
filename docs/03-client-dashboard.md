# Client Dashboard Specification

What a participant sees the moment they log into the Client Portal, and — critically — where each piece of data actually comes from. Kajabi does not natively support a fully custom per-user dashboard, so this spec splits widgets into **native Kajabi** (build directly) vs. **Airtable-sourced** (requires the integration layer in `07-integration-architecture.md`).

## Dashboard layout (top to bottom)

| Widget | Content | Data source | Build method |
|---|---|---|---|
| **Welcome** | "Welcome back, [First Name]" + track badge (Financial / Housing / Entrepreneur) | Kajabi member name + a tag set at enrollment | Native Kajabi custom page with liquid/merge tag |
| **Progress** | % complete of current Tier, visual bar | Kajabi native course/product progress | Native Kajabi product progress widget |
| **Current Tier** | Which of the 3 tracks they're active in | Tag applied when a Tier product is granted | Native Kajabi (tag-based conditional content block) |
| **Current Assignment** | Name of the next incomplete lesson/module | Kajabi native "continue where you left off" | Native Kajabi |
| **Next Coaching Call** | Date/time of their next scheduled 1:1 or group call | Scheduler (Kajabi or embedded 3rd-party booking tool) | Native/embed — pull from booking tool's participant view |
| **Documents Needed** | Outstanding items case manager needs (ID, income verification, etc.) | Airtable `Documents` table, filtered to this participant, status = "Requested" | Airtable-sourced — see below |
| **Milestones** | Checklist of milestones hit/pending (e.g., "Credit report reviewed," "Rent-ready packet submitted") | Airtable `Milestones` table, filtered to this participant | Airtable-sourced |
| **Certificate Progress** | Which certificates earned, which are next, % toward Program Completion | Combination: Kajabi certificate issuance (native) + Airtable outcome verification for gated certificates that require coach sign-off | Hybrid |

## How Airtable data reaches the dashboard without exposing Airtable

Participants must never see Airtable's UI, login, or branding. Two supported approaches — pick one and standardize:

**Option A (recommended): Airtable → Softr/Stacker portal, embedded in Kajabi**
Build a lightweight, read-only participant portal in Softr or Stacker on top of the Airtable base, themed to match Kajabi's branding, filtered per-user by matching login email to the Airtable Participant record. Embed that portal's relevant views (Documents Needed, Milestones) into the Kajabi dashboard page via a secure iframe, gated behind Kajabi membership so only logged-in participants can load it. This gives real per-participant filtering and a clean UI with zero Airtable branding visible.

**Option B (lighter-weight, no third tool): Push-only via Kajabi tags/custom fields**
Use Zapier/Make automations to push a small set of status flags from Airtable back into Kajabi as member tags or custom fields (e.g., `docs-needed:ID` , `milestone:rent-ready-complete`), and build the dashboard content blocks in Kajabi to conditionally display based on those tags. This avoids a third tool but is limited to simple flags/checklists, not free-text case notes.

**Recommendation:** Start with Option B for launch (faster, no new tool), and layer in Option A once volume justifies build time — it's a straight upgrade path since Airtable stays the single source of truth either way.

## What never appears on the participant dashboard

Case notes, internal outcome-reporting fields, grant/funding-source financials, and coach-only flags stay in Airtable and are visible only through the Staff Portal (`08-staff-portal-and-roles.md`).
