# Automations & Email Sequences

Build as a single Kajabi Automation triggered on "Offer Purchased / Product Granted" for the Economic Stability Service, using Kajabi Sequences for the timed emails and Kajabi Automations (trigger → tag → action) for the branching logic.

## Automation flow

```
Enrollment
  ↓ (trigger: product granted)
Welcome Email                    [immediate]
  ↓
Orientation                      [reminder if not started in 2 days]
  ↓
Assessment                       [Beginning Assessment — reminder if not completed in 3 days]
  ↓ (trigger: assessment submitted)
Coach Assignment                 [tag applied → notifies coach in Airtable/Slack, participant gets coach-intro email]
  ↓
Weekly Emails                    [ongoing nurture sequence, track-specific]
  ↓ (trigger: lesson/module marked complete)
Module Unlock                    [next module notification]
  ↓ (trigger: no activity in 7 days)
Progress Reminder                [re-engagement email]
  ↓ (trigger: tier requirements met + coach sign-off tag)
Certificate                      [certificate issuance email + dashboard update]
```

Each trigger above should be a Kajabi tag event so Airtable/Zapier can also listen for it (see `07-integration-architecture.md`) — e.g., applying tag `tier1-complete` both unlocks Tier 2 in Kajabi *and* fires a webhook that updates the participant's Airtable record.

---

## Email copy

### 1. Welcome Email (immediate on enrollment)
**Subject:** You're in — welcome to the Economic Stability Service
> Hi [First Name],
>
> Welcome to the Economic Stability Service. You're joining a program built to remove real barriers — financial, housing, and business — one step at a time, with a coach in your corner the whole way.
>
> Here's what happens next:
> 1. Log into your Client Portal
> 2. Complete Orientation (10 minutes)
> 3. Complete your Beginning Assessment so we can match you with the right coach and track
>
> [Log In to Get Started]
>
> We're glad you're here.
> — The Economic Stability Institute Team

### 2. Orientation Reminder (if not started within 2 days)
**Subject:** Quick step before we get started
> Hi [First Name], noticed you haven't started Orientation yet — it only takes about 10 minutes and unlocks your Beginning Assessment. [Continue Orientation]

### 3. Assessment Reminder (if not completed within 3 days of orientation)
**Subject:** Your Beginning Assessment is ready
> Hi [First Name], your Beginning Assessment helps us assign the right coach and confirm your starting track (Financial Stability, Housing, or Entrepreneur Pathway). It takes about 15 minutes. [Complete Assessment]

### 4. Coach Assignment
**Subject:** Meet your coach, [Coach Name]
> Hi [First Name],
>
> Based on your assessment, you've been matched with [Coach Name], your [Financial/Housing/Business] Coach. [Coach Name] will be with you through Tier [1/2/3] — including your weekly calls and office hours.
>
> Your first coaching call is on [date/time] — [Add to Calendar].
>
> [Message Your Coach] [View Your Dashboard]

### 5. Weekly Nurture (ongoing, track-specific — sample for Financial Stability track)
**Subject:** This week: [Module/Lesson name]
> Hi [First Name], this week's focus is [lesson topic]. Here's what to expect and why it matters for your Financial Stability Certificate: [1-2 sentence hook]. [Go to This Week's Lesson]
> Reminder: Weekly Live Call is [day/time] — [Join].

### 6. Module Unlock (on completion of prior module)
**Subject:** [Module name] is unlocked
> Nice work finishing [prior module]. [New module] is now open — here's what's inside: [1-line preview]. [Start Now]

### 7. Progress Reminder / Re-engagement (7 days no activity)
**Subject:** Picking back up — [First Name]?
> Hi [First Name], it's been a little while. Your progress is saved right where you left off: [Current Assignment]. If something's in the way, message your coach — that's what they're there for. [Return to Dashboard] [Message [Coach Name]]

### 8. Certificate Issued
**Subject:** 🎉 You earned your [Tier] Certificate
> Congratulations, [First Name] — you've completed [Tier Name] and earned your **[Certificate Name]**. [View/Download Certificate]
>
> [If not final tier:] Next up: [Next Tier Name] is now unlocked. [Start Next Tier]
> [If final tier:] You've completed the full Economic Stability Service and earned your **Economic Stability Certificate**. [View Program Completion Options →] (Phase 2 academies teaser)

---

## Coach-facing notification (internal, not participant email)

On each trigger above, fire a parallel internal notification (Slack/email) to the assigned coach via the Airtable automation layer: new enrollment assigned, assessment submitted and awaiting review, module completed and awaiting sign-off, 7-day inactivity flag. This keeps human follow-up attached to every automated trigger rather than letting automation replace the coach relationship.
