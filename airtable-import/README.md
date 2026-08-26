# Airtable Import Files

Eight CSVs, one per table from `docs/06-airtable-backend-schema.md`. Each has the correct column headers and one `SAMPLE — DELETE ME` row so you can confirm the import worked, then delete that row.

## Import order (matters — link fields need the target table to exist first)

1. `Staff.csv`
2. `Grant_Tracking.csv`
3. `Participants.csv`
4. `Service_Verification.csv`
5. `Case_Notes.csv`
6. `Milestones.csv`
7. `Documents.csv`
8. `Outcome_Reporting.csv`

## How to import each one

1. In Airtable, create a new **Base** named "Economic Stability Institute — Operations."
2. For the first table, use **Add or import → CSV file** and select `Staff.csv`. Airtable creates the table with these columns as plain text.
3. Repeat for each remaining CSV **as its own new table** (don't merge into one table).
4. Delete the `SAMPLE — DELETE ME` row from every table once you've confirmed columns look right.

## After import: fix field types (CSV import makes everything plain text)

Airtable can't infer single-select, link, attachment, or checkbox fields from a CSV — you have to convert each column's type manually. For every table, click the column header dropdown → **Edit field** → change type. Use this reference:

### Staff
- `Role` → Single select: `Administrator`, `Coach`, `Case Manager`, `Housing Coach`, `Business Coach`

### Grant Tracking
- `Grant Period` → Date range (or two Date fields: Start/End)
- `Funded Slots` → Number
- `Participants` → this becomes a Link field automatically once you link it from the Participants table (see below)

### Participants
- `Enrollment Date`, `Last Activity Date` → Date
- `Status` → Single select: `Lead`, `Applied`, `Enrolled`, `Active`, `On Hold`, `Completed`, `Withdrawn`
- `Current Track` → Single select: `Financial Stability`, `Housing`, `Entrepreneur`
- `Current Tier` → Single select: `Orientation`, `Tier 1`, `Tier 2`, `Tier 3`, `Complete`
- `Assigned Coach` → Link to `Staff`
- `Funding Source` → Link to `Grant Tracking`
- `Demographic Flags` → Multiple select: `Construction Grad`, `Apprentice`, `Returning Resident`, `Veteran`, `Justice-Impacted`, `Workforce Participant`

### Service Verification
- `Participant` → Link to `Participants`
- `Date Delivered` → Date
- `Service Type` → Single select: `Coaching Call`, `Assessment`, `Credit Review`, `Housing Counseling`, `Business Coaching`, `EEC Support`
- `Delivered By` → Link to `Staff`
- `Verification Method` → Single select: `Call log`, `Kajabi completion event`, `Coach attestation`

### Case Notes
- `Participant` → Link to `Participants`
- `Coach` → Link to `Staff`
- `Date`, `Follow-up Date` → Date
- `Category` → Single select: `Financial`, `Housing`, `Business`, `General`
- `Follow-up Needed` → Checkbox

### Milestones
- `Participant` → Link to `Participants`
- `Date Completed` → Date
- `Track` → Single select: `Financial`, `Housing`, `Entrepreneur`
- `Status` → Single select: `Pending`, `In Progress`, `Complete`
- `Sync to Kajabi` → Checkbox

### Documents
- `Participant` → Link to `Participants`
- `Date Requested`, `Date Received` → Date
- `Document Type` → Single select: `ID`, `Income Verification`, `Bank Statement`, `Credit Report`, `Lease`, `Business Formation Doc`, `Other`
- `Status` → Single select: `Requested`, `Submitted`, `Approved`, `Rejected`
- `File` → Attachment
- `Sync to Kajabi` → Checkbox

### Outcome Reporting
- `Participant` → Link to `Participants`
- `Date Achieved`, `Report Date` → Date
- `Outcome Type` → Single select: `Financial Stability`, `Housing Stability`, `Business Formation`, `Capital Access`, `EEP→EEC Advancement`
- `Verified By` → Link to `Staff`
- `Reported To Funder` → Checkbox

## After field types are fixed, build the views

See `docs/06-airtable-backend-schema.md` → "Views to build immediately" for the 5 filtered views (My Caseload, Needs Attention, Outstanding Documents, Pending Sync, Grant Capacity).

## Permissions

Once the base is built, go to **Share → Manage collaborators** and add each Staff person per `docs/08-staff-portal-and-roles.md` — do not add participants as collaborators under any circumstance.
