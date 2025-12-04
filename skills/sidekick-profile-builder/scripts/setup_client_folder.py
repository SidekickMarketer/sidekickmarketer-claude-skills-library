#!/usr/bin/env python3
"""
Setup New Client Folder
Creates the canonical folder structure for a new Sidekick Marketer client.
Based on CMA (Cincinnati Music Academy) production template.
"""
import argparse
import os
from pathlib import Path
from datetime import datetime

# Canonical folder structure (based on CMA production template)
FOLDER_STRUCTURE = [
    "01_Admin_Legal/Agreement And SOW/Signed Agreements",
    "01_Admin_Legal/Proposal/Old Proposal Versions",
    "01_Admin_Legal/ChatGPT Knowledge",
    "02_Onboarding_Access",
    "03_Brand_Assets/Assets/01_Brand",
    "03_Brand_Assets/Assets/02_Photos",
    "03_Brand_Assets/Assets/03_Graphics",
    "03_Brand_Assets/Photos/Queue",
    "03_Brand_Assets/Photos/Processed",
    "03_Brand_Assets/Website Photos",
    "04_Discovery_Research/01_Discovery Phase",
    # Paid Ads
    "07_Marketing_Channels/Paid_Ads/00_Strategy",
    "07_Marketing_Channels/Paid_Ads/01_Campaign_Data/Discovery_Phase",
    "07_Marketing_Channels/Paid_Ads/02_Performance_Data",
    "07_Marketing_Channels/Paid_Ads/03_Daily_Reports",
    # Social Media - Per-channel structure
    "07_Marketing_Channels/Social_Media/Instagram/Content_Calendars",
    "07_Marketing_Channels/Social_Media/Instagram/Performance_Data",
    "07_Marketing_Channels/Social_Media/Facebook/Content_Calendars",
    "07_Marketing_Channels/Social_Media/Facebook/Performance_Data",
    "07_Marketing_Channels/Social_Media/GBP/Content_Calendars",
    "07_Marketing_Channels/Social_Media/GBP/Performance_Data",
    "07_Marketing_Channels/Social_Media/04_Audit_Reports",
    # LinkedIn
    "07_Marketing_Channels/LinkedIn/04_Content_Archive",
    # SEO
    "07_Marketing_Channels/SEO/00_Strategy",
    "07_Marketing_Channels/SEO/01_Keywords_Research",
    "07_Marketing_Channels/SEO/02_Performance_Data/BrightLocal",
    "07_Marketing_Channels/SEO/02_Performance_Data/SE Rankings",
    "07_Marketing_Channels/SEO/03_Technical_Audits/Screaming Frog",
    # Website
    "09_Website/00_Analytics/Discovery_Phase",
    "09_Website/01_Landing_Pages",
    "09_Website/02_Conversion_Data",
    "09_Website/03_Performance_Data",
    # Email
    "07_Marketing_Channels/Email/00_Strategy",
    "07_Marketing_Channels/Email/01_Subscriber_Lists",
    "07_Marketing_Channels/Email/02_Campaign_Data",
    "07_Marketing_Channels/Email/03_Performance_Data",
    # System
    "90_Archive",
    "notion_export",  # Skill input (profile builder)
]


def create_profile_template(client_folder: Path, client_name: str, short_code: str):
    """Create the comprehensive client profile template."""
    today = datetime.now().strftime('%Y-%m-%d')
    content = f"""# {client_name} - Client Profile
**For Use by Claude Skills & Automation**

| Field | Value |
|-------|-------|
| **Created** | {today} |
| **Last Updated** | {today} |
| **Status** | Active Client |
| **Short Code** | {short_code} |

---

## 1. Business Core

| Field | Value |
|-------|-------|
| **Legal Name** | {client_name} |
| **DBA / Brand Name** | [Same or different?] |
| **Industry** | [Be specific: "Music Education" not just "Music"] |
| **Website** | [https://...] |
| **Physical Address** | [Full address for local SEO] |
| **Service Area** | [Cities/regions served] |
| **Founded Year** | [YYYY] |
| **Business Size** | [# employees, # locations] |

---

## 2. Contacts

| Role | Name | Email | Phone | Notes |
|------|------|-------|-------|-------|
| **Primary Contact** | [Name] | [email] | [phone] | Day-to-day communication |
| **Decision Maker** | [Name] | [email] | [phone] | Content approval authority |
| **Billing Contact** | [Name] | [email] | [phone] | If different |

**Preferred Contact Method:** [Email / Slack / Text / Phone]
**Expected Response Time:** [Same day / 24-48 hours / etc.]

---

## 3. Target Audience

### Demographics
| Attribute | Value |
|-----------|-------|
| **Age Range** | [e.g., 25-55] |
| **Gender Split** | [e.g., 60% female, 40% male] |
| **Location** | [Local / Regional / National] |
| **Income Level** | [e.g., Middle to upper-middle class] |
| **Education** | [e.g., College educated] |
| **Occupation** | [e.g., Parents, professionals] |

### Psychographics
- **Values:** [What do they care about?]
- **Interests:** [Hobbies, activities]
- **Pain Points:** [Problems they need solved]
- **Motivations:** [What drives them to buy?]

### Customer Segments
| Segment | % of Business | Description |
|---------|---------------|-------------|
| Segment 1 | [X]% | [Description] |
| Segment 2 | [X]% | [Description] |
| Segment 3 | [X]% | [Description] |

### Customer Journey
- **How they find us:** [Google, referrals, social, ads]
- **Consideration period:** [Immediate / days / weeks]
- **Purchase trigger:** [What makes them act?]
- **Decision influencers:** [Spouse, reviews, price]

### Common Objections
1. [Objection 1] - **Response:** [How we address it]
2. [Objection 2] - **Response:** [How we address it]
3. [Objection 3] - **Response:** [How we address it]

---

## 4. Brand Voice

### Tone & Personality
| Attribute | Value |
|-----------|-------|
| **Overall Tone** | [Professional / Casual / Playful / Authoritative] |
| **Formality** | [Formal / Semi-formal / Casual] |
| **Personality Traits** | [3-5 adjectives: e.g., Warm, Expert, Encouraging, Approachable] |
| **Communication Style** | [Educational / Entertaining / Inspiring / Promotional] |

### Writing Style
| Element | Guideline |
|---------|-----------|
| **Sentence Length** | [Short & punchy / Medium / Longer flowing] |
| **Paragraph Length** | [1-2 sentences / 3-4 sentences] |
| **Emoji Usage** | [None / Minimal (1-2) / Moderate (3-5) / Heavy] |
| **Hashtag Count** | [X per post] |
| **Hashtag Types** | [Branded / Industry / Local / Trending] |

### Voice Examples
**This sounds like us:**
> [Example quote or post that captures the voice]

**This does NOT sound like us:**
> [Example of what to avoid]

### Words & Phrases
**Always Use:**
- [Word/phrase 1]
- [Word/phrase 2]
- [Word/phrase 3]

**Never Use:**
- [Word/phrase 1]
- [Word/phrase 2]
- [Word/phrase 3]

---

## 5. Products & Services

| Service | Description | Priority | Seasonality | Price Point | Landing Page |
|---------|-------------|----------|-------------|-------------|--------------|
| [Service 1] | [What it is] | High | [When to push] | $[X] | [URL] |
| [Service 2] | [What it is] | Medium | [When to push] | $[X] | [URL] |
| [Service 3] | [What it is] | Low | [When to push] | $[X] | [URL] |

### Key Selling Points (Universal)
1. [USP 1]
2. [USP 2]
3. [USP 3]

### Service-Specific Messaging
**[Service 1]:**
- Hook: [Attention grabber]
- Key benefit: [Main value prop]
- CTA: [Call to action]

---

## 6. Content Pillars

| Pillar | Purpose | % of Mix | Example Topics | Best Format |
|--------|---------|----------|----------------|-------------|
| **[Pillar 1]** | [Why this content] | [X]% | [Topics] | [Carousel/Reel/Static] |
| **[Pillar 2]** | [Why this content] | [X]% | [Topics] | [Carousel/Reel/Static] |
| **[Pillar 3]** | [Why this content] | [X]% | [Topics] | [Carousel/Reel/Static] |
| **[Pillar 4]** | [Why this content] | [X]% | [Topics] | [Carousel/Reel/Static] |
| **[Pillar 5]** | [Why this content] | [X]% | [Topics] | [Carousel/Reel/Static] |

---

## 7. SOW / Deliverables

### Contract Overview
| Field | Value |
|-------|-------|
| **Contract Start** | [YYYY-MM-DD] |
| **Contract End** | [YYYY-MM-DD] |
| **Monthly Retainer** | $[X] |
| **Payment Terms** | [Net 15 / Net 30 / etc.] |

### Social Media Deliverables
| Platform | Posts/Month | Post Types | Stories | Notes |
|----------|-------------|------------|---------|-------|
| **Instagram** | [X] | [Static X, Carousel X, Reel X] | [Y/N, X/week] | |
| **Facebook** | [X] | [Types] | | |
| **GBP** | [X] | [Updates/Offers/Events] | N/A | |
| **LinkedIn** | [X] | [Types] | | |
| **TikTok** | [X] | [Types] | | |

### Other Services
| Service | Scope | Notes |
|---------|-------|-------|
| **Paid Ads** | $[X]/month budget | [Platforms: Google, Meta, etc.] |
| **SEO** | [X] hours/month | [Focus areas] |
| **Email Marketing** | [X] campaigns/month | [Platform: Mailchimp, etc.] |
| **Website** | [X] hours/month | [Maintenance, updates, etc.] |
| **Reporting** | [Weekly/Biweekly/Monthly] | [Format: Email, Call, Dashboard] |

---

## 8. KPIs & Goals

### Primary Business Goals
1. [ ] Brand Awareness
2. [ ] Lead Generation
3. [ ] Website Traffic
4. [ ] Sales / Revenue
5. [ ] Customer Retention
6. [ ] Community Building

**#1 Priority Goal:** [What matters most?]

### Platform Metrics
| Platform | Metric | Baseline | Target | Stretch |
|----------|--------|----------|--------|---------|
| **Instagram** | Engagement Rate | [X]% | [X]% | [X]% |
| **Instagram** | Follower Growth | [X]/mo | [X]/mo | [X]/mo |
| **Facebook** | Reach | [X] | [X] | [X] |
| **Facebook** | Clicks | [X]/mo | [X]/mo | [X]/mo |
| **GBP** | Views | [X]/mo | [X]/mo | [X]/mo |
| **GBP** | Actions | [X]/mo | [X]/mo | [X]/mo |
| **Website** | Sessions | [X]/mo | [X]/mo | [X]/mo |
| **Leads** | Inquiries | [X]/mo | [X]/mo | [X]/mo |

### Success Definition
> [In one sentence, what does success look like? e.g., "10 new student signups per month from social/digital channels"]

---

## 9. Competitors

| Competitor | Website | IG Handle | FB Page | Notes |
|------------|---------|-----------|---------|-------|
| [Name 1] | [URL] | @[handle] | [page] | |
| [Name 2] | [URL] | @[handle] | [page] | |
| [Name 3] | [URL] | @[handle] | [page] | |

### Competitive Analysis
**[Competitor 1]:**
- What they do well: [Strengths]
- What they do poorly: [Weaknesses]
- How we differentiate: [Our advantage]

**[Competitor 2]:**
- What they do well: [Strengths]
- What they do poorly: [Weaknesses]
- How we differentiate: [Our advantage]

---

## 10. Seasonality & Calendar

### Business Seasons
| Season | Timing | Strategy |
|--------|--------|----------|
| **Peak Season** | [Months] | Push hard, increase ad spend |
| **Slow Season** | [Months] | Build awareness, nurture |
| **Shoulder Season** | [Months] | Balance approach |

### Key Annual Events
| Event | Date | Content Focus |
|-------|------|---------------|
| [Event 1] | [Date/Month] | [What to post] |
| [Event 2] | [Date/Month] | [What to post] |
| [Event 3] | [Date/Month] | [What to post] |

### Holidays That Matter
- [ ] New Year
- [ ] Valentine's Day
- [ ] Easter
- [ ] Mother's Day
- [ ] Father's Day
- [ ] Back to School
- [ ] Halloween
- [ ] Thanksgiving
- [ ] Christmas/Holidays
- [ ] Other: [Specify]

### Blackout Topics
- [Topic to avoid and why]
- [Topic to avoid and why]

---

## 11. Visual Brand

### Colors
| Type | Color | Hex Code |
|------|-------|----------|
| **Primary** | [Color name] | #[XXXXXX] |
| **Secondary** | [Color name] | #[XXXXXX] |
| **Accent** | [Color name] | #[XXXXXX] |
| **Background** | [Color name] | #[XXXXXX] |
| **Text** | [Color name] | #[XXXXXX] |

### Typography
| Use | Font | Weight |
|-----|------|--------|
| **Headlines** | [Font name] | [Bold/Regular] |
| **Body** | [Font name] | [Bold/Regular] |
| **Accent** | [Font name] | [Bold/Regular] |

### Logo Usage
- **Primary logo:** [When to use]
- **Alternate logo:** [When to use]
- **Minimum size:** [X px]
- **Clear space:** [X around logo]
- **What NOT to do:** [Stretch, recolor, etc.]

### Image Style
| Element | Guideline |
|---------|-----------|
| **Photo Style** | [Candid / Polished / Mix] |
| **Subjects** | [People, products, facility, etc.] |
| **Lighting** | [Bright & airy / Moody / Natural] |
| **Filters** | [None / Consistent filter / Brand preset] |
| **Graphics Style** | [Minimal / Bold / Playful] |

---

## 12. Account Access

| Platform | Account/Handle | Access Level | Credentials Location |
|----------|----------------|--------------|---------------------|
| **Instagram** | @[handle] | [Admin/Editor] | `02_Onboarding_Access/` |
| **Facebook Page** | [Page name] | [Admin/Editor] | `02_Onboarding_Access/` |
| **Meta Business Suite** | [Account] | [Admin] | `02_Onboarding_Access/` |
| **Google Business Profile** | [Business name] | [Owner/Manager] | `02_Onboarding_Access/` |
| **Google Analytics** | [Property] | [Editor/Viewer] | `02_Onboarding_Access/` |
| **Google Ads** | [Account ID] | [Admin/MCC] | `02_Onboarding_Access/` |
| **Meta Ads Manager** | [Account ID] | [Admin] | `02_Onboarding_Access/` |
| **Email Platform** | [Platform + account] | [Admin] | `02_Onboarding_Access/` |
| **Website CMS** | [Platform + URL] | [Admin/Editor] | `02_Onboarding_Access/` |
| **Scheduling Tool** | [Tool name] | [Admin] | `02_Onboarding_Access/` |

---

## 13. Guidelines & Constraints

### Legal & Compliance
- [ ] Photo release required for: [Students, minors, etc.]
- [ ] Privacy considerations: [HIPAA, FERPA, etc.]
- [ ] Testimonial rules: [FTC disclosure, etc.]
- [ ] Copyright: [Music licensing, image rights]

### Content Approval
| Content Type | Approver | Turnaround | Method |
|--------------|----------|------------|--------|
| **Regular Posts** | [Name] | [X hours/days] | [Email/Notion/Tool] |
| **Paid Ads** | [Name] | [X hours/days] | [Email/Notion/Tool] |
| **Blog/Website** | [Name] | [X hours/days] | [Email/Notion/Tool] |
| **Email Campaigns** | [Name] | [X hours/days] | [Email/Notion/Tool] |

### Topics to Avoid
- [Topic 1 and why]
- [Topic 2 and why]
- [Topic 3 and why]

### Competitors to Never Mention
- [Competitor 1]
- [Competitor 2]

### Other Constraints
- [Constraint 1]
- [Constraint 2]

---

## 14. Business Model & Revenue

### How They Make Money
| Revenue Stream | % of Revenue | Notes |
|----------------|--------------|-------|
| [Service/Product 1] | [X]% | [Primary driver] |
| [Service/Product 2] | [X]% | |
| [Service/Product 3] | [X]% | |

### Key Financial Metrics
| Metric | Value | Notes |
|--------|-------|-------|
| **Average Transaction Value** | $[X] | |
| **Customer Lifetime Value** | $[X] | |
| **Customer Acquisition Cost** | $[X] | [If known] |
| **Monthly Revenue Range** | $[X-Y] | [Optional] |

### Lead Sources (Current)
| Source | % of Leads | Quality | Notes |
|--------|------------|---------|-------|
| Referrals | [X]% | [High/Med/Low] | |
| Google Search | [X]% | [High/Med/Low] | |
| Social Media | [X]% | [High/Med/Low] | |
| Paid Ads | [X]% | [High/Med/Low] | |
| Walk-ins | [X]% | [High/Med/Low] | |
| Other: [specify] | [X]% | [High/Med/Low] | |

### Business Model Notes
- [Key insight about how business works]
- [Important context for marketing]

---

## 15. Origin Story

### Founder Background
| Field | Value |
|-------|-------|
| **Founder Name(s)** | [Name] |
| **Founder Background** | [Previous career, expertise] |
| **Year Founded** | [YYYY] |
| **Original Location** | [Where it started] |

### The "Why" Story
> [In their own words, why they started this business. What problem were they solving? What was the motivation?]

### Key Milestones
| Year | Milestone | Content Opportunity |
|------|-----------|---------------------|
| [YYYY] | Founded | Anniversary posts |
| [YYYY] | [Major event] | [How to leverage] |
| [YYYY] | [Growth milestone] | [How to leverage] |
| [YYYY] | [Award/recognition] | [How to leverage] |

### Human Interest Elements
- **Founder's personal story:** [What makes them relatable]
- **Family involvement:** [If relevant]
- **Community connection:** [Local ties]
- **Unique background:** [Interesting facts]

---

## 16. Local Presence & Reputation

### Review Status
| Platform | Rating | # Reviews | Last Updated |
|----------|--------|-----------|--------------|
| **Google** | [X.X] | [#] | [Date] |
| **Yelp** | [X.X] | [#] | [Date] |
| **Facebook** | [X.X] | [#] | [Date] |
| **Industry-specific** | [X.X] | [#] | [Platform:] |

### Review Strategy
- **Current review request process:** [How they ask for reviews now]
- **Review response policy:** [How/when they respond]
- **Negative review protocol:** [How to handle]

### NAP Consistency
| Directory | Name | Address | Phone | Status |
|-----------|------|---------|-------|--------|
| Google | [Exact name] | [Exact address] | [Exact phone] | [Correct/Needs fix] |
| Yelp | | | | |
| Facebook | | | | |
| Apple Maps | | | | |
| Bing Places | | | | |
| Industry directories | | | | |

### Community Involvement
| Activity | Description | Content Opportunity |
|----------|-------------|---------------------|
| [Sponsorship] | [Details] | [How to feature] |
| [Charity/cause] | [Details] | [How to feature] |
| [Local partnership] | [Details] | [Cross-promo opportunity] |
| [Events hosted] | [Details] | [Content ideas] |

### Local Partnerships
| Partner | Relationship | Cross-Promo Potential |
|---------|--------------|----------------------|
| [Business 1] | [Nature of partnership] | [Ideas] |
| [Business 2] | [Nature of partnership] | [Ideas] |

---

## 17. Marketing History

### Past Marketing Efforts
| Channel | Timeframe | What They Did | Result | Notes |
|---------|-----------|---------------|--------|-------|
| Social Media | [Dates] | [Description] | [Outcome] | |
| Paid Ads | [Dates] | [Platform, budget] | [Outcome] | |
| SEO | [Dates] | [Description] | [Outcome] | |
| Email | [Dates] | [Description] | [Outcome] | |
| Traditional | [Dates] | [Print, radio, etc.] | [Outcome] | |

### What's Worked Before
1. **[Tactic 1]:** [Why it worked, results]
2. **[Tactic 2]:** [Why it worked, results]
3. **[Tactic 3]:** [Why it worked, results]

### What Flopped
1. **[Tactic 1]:** [What went wrong, lessons learned]
2. **[Tactic 2]:** [What went wrong, lessons learned]

### Previous Agencies/Vendors
| Agency | Timeframe | Services | Why They Left |
|--------|-----------|----------|---------------|
| [Agency 1] | [Dates] | [What they did] | [Reason for leaving - important context] |
| [Agency 2] | [Dates] | [What they did] | [Reason for leaving] |

### Historical Ad Spend
| Period | Monthly Budget | Platforms | Notes |
|--------|----------------|-----------|-------|
| [Before us] | $[X] | [Platforms] | |
| [Current] | $[X] | [Platforms] | |

### Best Performing Content Ever
1. **[Content piece]:** [Metrics, why it worked]
2. **[Content piece]:** [Metrics, why it worked]
3. **[Content piece]:** [Metrics, why it worked]

---

## 18. Content Bank & Assets

### Photo Library
| Type | Location | Quantity | Quality | Notes |
|------|----------|----------|---------|-------|
| **Team/Staff Photos** | [Drive folder] | [#] | [Pro/Amateur] | |
| **Facility Photos** | [Drive folder] | [#] | [Pro/Amateur] | |
| **Product Photos** | [Drive folder] | [#] | [Pro/Amateur] | |
| **Event Photos** | [Drive folder] | [#] | [Pro/Amateur] | |
| **Customer Photos** | [Drive folder] | [#] | [Pro/Amateur] | Release on file? |
| **Stock Images** | [License/source] | [#] | | |

### Video Assets
| Type | Location | Duration | Quality | Notes |
|------|----------|----------|---------|-------|
| **Promo Videos** | [Location] | [Length] | [Pro/Amateur] | |
| **Testimonials** | [Location] | [Length] | [Pro/Amateur] | Release on file? |
| **How-to/Tutorial** | [Location] | [Length] | [Pro/Amateur] | |
| **Event Footage** | [Location] | [Length] | [Pro/Amateur] | |
| **B-roll** | [Location] | [Length] | [Pro/Amateur] | |

### Testimonials & Social Proof
| Source | Quote/Summary | Customer | Release? | Used? |
|--------|---------------|----------|----------|-------|
| [Google review] | [Key quote] | [Name] | [Y/N] | |
| [Direct testimonial] | [Key quote] | [Name] | [Y/N] | |
| [Case study] | [Summary] | [Customer] | [Y/N] | |

### FAQs & Common Questions
| Question | Answer | Content Opportunity |
|----------|--------|---------------------|
| [FAQ 1] | [Answer] | [Post type: carousel, reel, etc.] |
| [FAQ 2] | [Answer] | [Post type] |
| [FAQ 3] | [Answer] | [Post type] |
| [FAQ 4] | [Answer] | [Post type] |
| [FAQ 5] | [Answer] | [Post type] |

### Staff Bios
| Name | Role | Bio | Headshot? | Fun Fact |
|------|------|-----|-----------|----------|
| [Name] | [Title] | [Short bio] | [Y/N] | [For content] |
| [Name] | [Title] | [Short bio] | [Y/N] | [For content] |

### Existing Content to Repurpose
| Content | Original Format | Repurpose Ideas |
|---------|-----------------|-----------------|
| [Blog post] | Long-form | Carousel, quote graphics |
| [Video] | Long video | Clips, reels |
| [Brochure] | Print | Digital graphics |

---

## 19. Email & CRM

### Email Marketing
| Field | Value |
|-------|-------|
| **Platform** | [Mailchimp, Klaviyo, ActiveCampaign, etc.] |
| **List Size** | [# subscribers] |
| **Average Open Rate** | [X]% |
| **Average Click Rate** | [X]% |
| **Send Frequency** | [Weekly, monthly, etc.] |
| **Access Level** | [Admin, Editor, Viewer] |

### Email Segments
| Segment | Size | Description |
|---------|------|-------------|
| [Segment 1] | [#] | [Who's in it] |
| [Segment 2] | [#] | [Who's in it] |
| [Segment 3] | [#] | [Who's in it] |

### Email Automation in Place
- [ ] Welcome sequence
- [ ] Abandoned cart/inquiry
- [ ] Post-purchase follow-up
- [ ] Re-engagement campaign
- [ ] Birthday/anniversary
- [ ] Other: [Specify]

### CRM System
| Field | Value |
|-------|-------|
| **Platform** | [HubSpot, Salesforce, custom, spreadsheet, etc.] |
| **Lead Stages** | [List their pipeline stages] |
| **Integration with Marketing** | [How/if it connects] |
| **Access Level** | [Admin, User, Viewer] |

### Integration Opportunities
- [ ] Social → CRM lead capture
- [ ] Email → CRM sync
- [ ] Ads → CRM conversion tracking
- [ ] Website → CRM form integration

---

## 20. Relationship Notes

### Communication Preferences
| Preference | Detail |
|------------|--------|
| **Preferred Method** | [Email, phone, text, Slack] |
| **Best Times to Reach** | [Days/times] |
| **Meeting Cadence** | [Weekly call, monthly review, etc.] |
| **Response Style** | [Quick responses, batches emails, etc.] |
| **Communication Personality** | [Direct, detailed, casual, formal] |

### Working Style
- **Decision making:** [Quick decisions vs. needs time to consider]
- **Feedback style:** [Direct, diplomatic, detailed, brief]
- **Preferred deliverable format:** [Doc, video walkthrough, etc.]
- **Revision expectations:** [One round, unlimited, etc.]

### What Makes Them Happy
1. [Thing they've praised or appreciated]
2. [Thing that went well]
3. [How they prefer to be communicated with]

### Pet Peeves / Avoid
1. [Thing that frustrated them]
2. [Past issue to not repeat]
3. [Sensitivity to avoid]

### Key Dates
| Date | Occasion | Notes |
|------|----------|-------|
| [Date] | Client anniversary | [Send card/note?] |
| [Date] | Business anniversary | [Content opportunity] |
| [Date] | Founder birthday | [Optional relationship building] |
| [Date] | Contract renewal | [Important reminder] |

### Relationship History
| Date | Event | Notes |
|------|-------|-------|
| [Date] | Onboarded | [Context] |
| [Date] | [Issue/success] | [What happened, resolution] |
| [Date] | [Milestone] | [Context] |

### Internal Notes
> [Any context that helps the team work better with this client. Personality notes, preferences discovered over time, etc. This section is for internal reference only.]

---

## Profile Validation Checklist

Before using this profile, verify:

### Core Sections (Required)
- [ ] **1. Business Core** - All fields complete
- [ ] **2. Contacts** - Primary contact + decision maker identified
- [ ] **3. Target Audience** - At least 1 segment described in detail
- [ ] **4. Brand Voice** - Tone, personality, and do's/don'ts defined
- [ ] **5. Products/Services** - At least top 3 with priorities
- [ ] **6. Content Pillars** - 3-5 pillars with % mix
- [ ] **7. SOW** - All deliverables match signed contract
- [ ] **8. KPIs** - Baselines and targets set
- [ ] **9. Competitors** - At least 2 analyzed
- [ ] **10. Seasonality** - Peak/slow seasons identified
- [ ] **11. Visual Brand** - Colors and image style documented
- [ ] **12. Account Access** - All platforms with access confirmed
- [ ] **13. Guidelines** - Approval workflow and constraints clear

### Strategic Sections (Highly Recommended)
- [ ] **14. Business Model** - Revenue streams and lead sources documented
- [ ] **15. Origin Story** - Founder story and milestones captured
- [ ] **16. Local Presence** - Reviews and community involvement noted
- [ ] **17. Marketing History** - Past successes/failures recorded
- [ ] **18. Content Bank** - Available assets inventoried
- [ ] **19. Email & CRM** - Systems and integration status documented
- [ ] **20. Relationship Notes** - Communication preferences captured

---

## Quick Reference

| Need | Location |
|------|----------|
| Brand assets | `03_Brand_Assets/` |
| SOW document | `01_Admin_Legal/Agreement And SOW/` |
| Login credentials | `02_Onboarding_Access/` |
| Social strategy | `07_Marketing_Channels/Social_Media/00_Strategy/` |
| Performance data | `[Channel]/02_Performance_Data/` |
| Audit reports | `07_Marketing_Channels/Social_Media/04_Audit_Reports/` |

---

**This profile powers all Claude Skills. Keep it updated!**

*Last validated: [DATE]*
*Validated by: [NAME]*
"""
    profile_path = client_folder / f"00_{short_code}_CLIENT_PROFILE.md"
    with open(profile_path, 'w') as f:
        f.write(content)
    return profile_path


def create_strategy_template(client_folder: Path, client_name: str, short_code: str):
    """Create the social strategy template."""
    content = f"""# {client_name} - Social Media Strategy
**Version:** 1.0
**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

---

## Overview

This document contains platform-specific tactics and strategies.
For foundational brand info, see: `00_{short_code}_CLIENT_PROFILE.md`

---

## Platform Strategies

### Instagram
- **Primary Goal:** [Awareness / Engagement / Traffic]
- **Post Mix:** Carousel [X]%, Static [X]%, Reels [X]%
- **Best Posting Times:** [Days/times]
- **Hashtag Strategy:** [X branded, X industry, X local]
- **Stories Strategy:** [Frequency, content types]
- **Engagement Rules:** [Response time, tone]

### Facebook
- **Primary Goal:** [Awareness / Engagement / Traffic]
- **Post Mix:** [Types and percentages]
- **Best Posting Times:** [Days/times]
- **Group Strategy:** [If applicable]
- **Event Strategy:** [If applicable]

### Google Business Profile
- **Post Frequency:** [X per week]
- **Post Types:** Updates [X]%, Offers [X]%, Events [X]%
- **Keywords to Include:** [Local SEO terms]
- **Photo Strategy:** [What to upload, frequency]
- **Review Response:** [Template, timing]

---

## Content Calendar Framework

| Week | Pillar Focus | Platform Priority | Campaign/Theme |
|------|--------------|-------------------|----------------|
| 1 | [Pillar] | [Platform] | [Theme] |
| 2 | [Pillar] | [Platform] | [Theme] |
| 3 | [Pillar] | [Platform] | [Theme] |
| 4 | [Pillar] | [Platform] | [Theme] |

---

## Hashtag Library

### Branded
- #[BrandHashtag1]
- #[BrandHashtag2]

### Industry
- #[Industry1]
- #[Industry2]

### Local
- #[City]
- #[Neighborhood]

### Campaign-Specific
- #[Campaign1]

---

## Engagement Playbook

### Response Templates
**Positive Comment:**
> [Template response]

**Question:**
> [Template response]

**Complaint:**
> [Template response]

### Response Time Goals
- Comments: [X hours]
- DMs: [X hours]
- Reviews: [X hours]

---

**Review this strategy quarterly. Update based on performance data.**
"""
    strategy_path = client_folder / "07_Marketing_Channels/Social_Media/00_Strategy/00_SOCIAL_STRATEGY.md"
    with open(strategy_path, 'w') as f:
        f.write(content)
    return strategy_path


def setup_client(base_path: str, short_code: str, client_name: str = None):
    """Create complete client folder structure."""
    short_code = short_code.upper()
    folder_name = f"client-{short_code.lower()}"

    if not client_name:
        client_name = short_code.replace('-', ' ').title()

    base = Path(base_path)
    client_folder = base / folder_name

    if client_folder.exists():
        print(f"Warning: Folder already exists: {client_folder}")
        print("   Use --force to overwrite (not recommended)")
        return None

    print(f"Setting up client: {client_name} ({short_code})")
    print(f"Location: {client_folder}")
    print("=" * 60)

    # Create all folders
    print("\nCreating folder structure...")
    for folder in FOLDER_STRUCTURE:
        folder_path = client_folder / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"   + {folder}")

    # Create template files
    print("\nCreating template files...")

    profile = create_profile_template(client_folder, client_name, short_code)
    print(f"   + {profile.name}")

    strategy = create_strategy_template(client_folder, client_name, short_code)
    print(f"   + 00_SOCIAL_STRATEGY.md")

    # Print checklist
    print("\n" + "=" * 60)
    print("CLIENT FOLDER CREATED SUCCESSFULLY")
    print("=" * 60)
    print("\nNEXT STEPS:")
    print(f"""
1. [ ] Fill out client profile: {profile}
2. [ ] Add signed SOW to: 01_Admin_Legal/Agreement And SOW/
3. [ ] Add credentials to: 02_Onboarding_Access/
4. [ ] Add brand assets to: 03_Brand_Assets/
5. [ ] Complete social strategy: 07_Marketing_Channels/Social_Media/00_Strategy/

Optional:
- Export Notion pages to: notion_export/
- Run: ./scripts/run_profile_builder.sh "{client_folder}"
""")

    return client_folder


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create canonical folder structure for new Sidekick Marketer client"
    )
    parser.add_argument(
        '--base-path',
        required=True,
        help="Base directory where client folder will be created"
    )
    parser.add_argument(
        '--short-code',
        required=True,
        help="Client short code (e.g., CMA, FMG)"
    )
    parser.add_argument(
        '--client-name',
        help="Full client name (optional, derived from short code if not provided)"
    )

    args = parser.parse_args()

    setup_client(
        args.base_path,
        args.short_code,
        args.client_name
    )
