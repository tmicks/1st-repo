# Phase 2 Roadmap — Economic Mobility Institute

Once the Economic Stability Service is proven (enrollment flowing, automations stable, first certificates issued, first outcome reports delivered to funders), expand the same Kajabi/Airtable architecture into a full **Economic Mobility Institute**, using the Economic Stability Service as the entry point and shared client portal for every academy below.

## Additional academies

- **Financial Stability Academy** — deeper/standalone version of Tier 1, sellable independently to employers or as a stand-alone offer
- **Homeownership Academy** — deeper version of Tier 2's homeownership track, likely paired with a lender/housing-counseling partner
- **Entrepreneur Academy** — deeper version of Tier 3 Modules 1-3
- **Construction Career Academy** — new vertical for construction-specific workforce pathways, feeding into the existing Construction Graduates community group
- **Clean Energy Contractor Academy (EEP → EEC)** — expands Tier 3 Modules 4-5 into a standalone credentialing academy
- **Business Capital Academy** — deeper version of Tier 3 Module 3, likely with lending-partner integration
- **Leadership & Executive Development Academy** — new vertical for participants who've completed Program Completion and want advancement/leadership tracks (also relevant to the "employers seeking retention and advancement support" audience)

## Why the current build supports this without re-platforming

- **Kajabi:** Each academy becomes another Product in the same site, gated by its own Offer/tag — the nav item `Programs` grows, the Client Portal/dashboard stays one shared surface (`03-client-dashboard.md` already keys widgets off tags, not off a single Tier structure)
- **Airtable:** `Participants` table already supports multiple linked tracks/outcomes per person — Phase 2 just adds new `Outcome Reporting` types and possibly new linked tables per academy, not a new base
- **Staff roles:** The role structure in `08-staff-portal-and-roles.md` extends by adding new scoped coach roles (e.g., "Construction Career Coach") following the same pattern as Housing/Business Coach

## Participant path

Participants begin in the Economic Stability Service (all three tiers) and, on Program Completion, are offered relevant Phase 2 academies based on their Completion Assessment's "next goal" answer (`09-certificates-and-assessments.md`) — this is the natural upsell/retention moment, not a separate marketing push.

## What to stand up when Phase 2 starts

1. Rename/re-theme the site from "Economic Stability Service" as the sole product to "Economic Stability Institute" as the umbrella brand, with ESS as one listed program among several
2. Add an Academy selector to the `/programs` page (mirrors `01-website-structure.md` structure, one section per academy)
3. Extend `Outcome Reporting` in Airtable with academy-specific outcome types
4. Recruit/assign academy-specific coaches
5. Build employer-facing partnership pages if pursuing employer contracts (retention/advancement support audience)
