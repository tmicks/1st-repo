# Airtable Backend Schema

This is the entire operational backend. Participants never see this base — access is staff-only (Admin/Coach/Case Manager permission groups, see `08-staff-portal-and-roles.md`). One base, one set of linked tables.

## Table: `Participants`
The hub table — every other table links back here.

| Field | Type | Notes |
|---|---|---|
| Full Name | Single line text | |
| Email | Email | Must match Kajabi login email — this is the join key for all integrations |
| Phone | Phone | |
| Enrollment Date | Date | |
| Status | Single select | Lead / Applied / Enrolled / Active / On Hold / Completed / Withdrawn |
| Current Track | Single select | Financial Stability / Housing / Entrepreneur |
| Current Tier | Single select | Orientation / Tier 1 / Tier 2 / Tier 3 / Complete |
| Assigned Coach | Link to `Staff` | |
| Funding Source | Link to `Grant Tracking` | |
| Eligibility Notes | Long text | From HubSpot handoff |
| Demographic flags | Single/multi select | Construction Grad / Apprentice / Returning Resident / Veteran / Justice-Impacted / Workforce Participant — used for outcome reporting only, never surfaced to Kajabi dashboard |
| Kajabi Member ID | Single line text | Populate via Zapier/Make on grant |
| Milestones | Link to `Milestones` | |
| Documents | Link to `Documents` | |
| Case Notes | Link to `Case Notes` | |
| Service Verifications | Link to `Service Verification` | |
| Last Activity Date | Date | Synced from Kajabi via automation, drives inactivity flags |

## Table: `Grant Tracking`
| Field | Type | Notes |
|---|---|---|
| Grant/Funder Name | Single line text | |
| Grant Period | Date range | |
| Funded Slots | Number | |
| Slots Used | Rollup/count | From linked Participants |
| Reporting Requirements | Long text | What this funder needs reported and how often |
| Participants | Link to `Participants` | |

## Table: `Service Verification`
Tracks that a service was actually delivered — required for most workforce/grant reporting.
| Field | Type | Notes |
|---|---|---|
| Participant | Link to `Participants` | |
| Service Type | Single select | Coaching Call / Assessment / Credit Review / Housing Counseling / Business Coaching / EEC Support |
| Date Delivered | Date | |
| Delivered By | Link to `Staff` | |
| Verification Method | Single select | Call log / Kajabi completion event / Coach attestation |
| Notes | Long text | |

## Table: `Case Notes`
| Field | Type | Notes |
|---|---|---|
| Participant | Link to `Participants` | |
| Date | Date | |
| Coach | Link to `Staff` | |
| Category | Single select | Financial / Housing / Business / General |
| Note | Long text | Internal only — never synced outward |
| Follow-up Needed | Checkbox | |
| Follow-up Date | Date | |

## Table: `Milestones`
Drives the "Milestones" widget on the Kajabi dashboard (via the sync described in `03-client-dashboard.md`).
| Field | Type | Notes |
|---|---|---|
| Participant | Link to `Participants` | |
| Milestone Name | Single line text | e.g. "Credit report reviewed," "Rent-ready packet submitted," "LLC formed" |
| Track | Single select | Financial / Housing / Entrepreneur |
| Status | Single select | Pending / In Progress / Complete |
| Date Completed | Date | |
| Sync to Kajabi | Checkbox | Flags this record for the outbound automation |

## Table: `Documents`
Drives the "Documents Needed" widget.
| Field | Type | Notes |
|---|---|---|
| Participant | Link to `Participants` | |
| Document Type | Single select | ID / Income Verification / Bank Statement / Credit Report / Lease / Business Formation Doc / Other |
| Status | Single select | Requested / Submitted / Approved / Rejected |
| Date Requested | Date | |
| Date Received | Date | |
| File | Attachment | Received copy, staff-only |
| Sync to Kajabi | Checkbox | |

## Table: `Outcome Reporting`
Aggregation table (or use views/rollups on `Participants`) built specifically to answer funder reporting without custom queries — mirrors the metrics in `00-overview.md`.
| Field | Type | Notes |
|---|---|---|
| Participant | Link to `Participants` | |
| Outcome Type | Single select | Financial Stability / Housing Stability / Business Formation / Capital Access / EEP→EEC Advancement |
| Date Achieved | Date | |
| Verified By | Link to `Staff` | |
| Reported To Funder | Checkbox | |
| Report Date | Date | |

## Table: `Staff`
| Field | Type | Notes |
|---|---|---|
| Name | Single line text | |
| Role | Single select | Administrator / Coach / Case Manager / Housing Coach / Business Coach |
| Email | Email | |
| Active Caseload | Rollup/count | From linked Participants |

## Views to build immediately
- `Participants` → "My Caseload" (filtered by Assigned Coach = current user)
- `Participants` → "Needs Attention" (Last Activity Date > 7 days, Status = Active)
- `Documents` → "Outstanding" (Status = Requested)
- `Milestones` → "Pending Sync" (Sync to Kajabi = true, not yet pushed)
- `Grant Tracking` → "Capacity" (Slots Used vs. Funded Slots, per grant)
