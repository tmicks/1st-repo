# Sales Funnel & Eligibility Assessment

## Funnel

```
Landing Page (Home or paid-ad landing variant)
  ↓
Book Consultation  →  OR  →  Apply Today (direct to eligibility assessment)
  ↓
Eligibility Assessment  (HubSpot form)
  ↓
Recommended Service  (auto-scored track recommendation + admissions review)
  ↓
Payment  (Kajabi Checkout — or $0 if grant-funded, see below)
  ↓
Enrollment  (Airtable participant record created)
  ↓
Kajabi Access  (product granted, enrollment automation begins — see 04)
```

**HubSpot's job:** own everything left of "Enrollment." Once a lead is scored eligible and a track is recommended, HubSpot hands off by creating/updating the Airtable participant record (via Zapier/Make) and, on payment/grant-approval, triggers the Kajabi product grant. HubSpot should never be participant-facing after enrollment — coaching, community, and progress live in Kajabi only.

## Eligibility Assessment — question set

Use as a HubSpot form (or Kajabi-embedded form feeding HubSpot). Keep to ~12 questions max to protect completion rate; this set balances eligibility screening with track-recommendation scoring.

**Screening (funder/grant eligibility)**
1. What is your current employment/training status? (Employed / Apprentice / Job seeking / Enrolled in workforce program / Returning resident program / Veteran / Other)
2. Are you currently enrolled in, or a graduate of, a construction or workforce training program? (Y/N — which one)
3. Are you a justice-impacted individual or returning resident? (Y/N — optional disclosure, used for funder eligibility only, never surfaced to coaches as a label)
4. Are you a veteran? (Y/N)
5. What is your current housing situation? (Renting / With family or friends / Unstable or transitional / Own a home / Seeking to purchase)
6. What is your household income range? (ranges, for grant qualification)
7. What county/region do you live in? (service-area confirmation)

**Track recommendation scoring**
8. What's your primary goal right now? (Fix my credit and build savings / Get rent-ready or buy a home / Start or grow a business / Not sure — help me figure it out)
9. Do you currently have a business, or plan to start one? (Y/N — if Y, are you pursuing clean energy contractor work / Illinois Shines EEP-EEC?)
10. Have you reviewed your credit report in the past 12 months? (Y/N)
11. Are you working toward homeownership in the next 1-2 years? (Y/N)
12. How much time can you commit weekly? (<1 hr / 1-3 hrs / 3-5 hrs / 5+ hrs) — sets expectations, flags capacity risk to coach

**Auto-scoring logic:** Q8 primary answer sets the recommended starting Tier; Q9 secondary "yes" flags Entrepreneur/EEC track as a parallel or next track; Q5/Q11 flags Housing track priority. Admissions (HubSpot owner) reviews the auto-recommendation before confirming — this is a recommendation engine, not an autonomous gate.

## Payment / Enrollment logic

- **Grant/funder-covered participants:** $0 Kajabi Offer, gated by an admissions-approved tag rather than a card charge. Grant/funding source recorded in Airtable (`Grant Tracking` table) at enrollment, not left implicit.
- **Self-pay participants (if offered):** standard Kajabi Checkout Offer, tiered or full-program pricing set by the business, not covered here.
- Either path ends the same way: Airtable participant record created/confirmed → Kajabi product granted → enrollment automation (`04-automations-and-emails.md`) begins.

## Recommended Service — output shown to the applicant

After scoring, before payment/enrollment, show a simple confirmation screen: "Based on your answers, we recommend starting with **[Track Name]**." with a one-line description and a "Confirm & Continue" button — this is also where an admissions reviewer can override before enrollment finalizes, so the flow should support a short manual-review hold rather than fully instant auto-enrollment.
