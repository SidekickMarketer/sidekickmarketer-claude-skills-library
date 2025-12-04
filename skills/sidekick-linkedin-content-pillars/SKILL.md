---
name: sidekick-linkedin-content-pillars
description: Define LinkedIn-specific content pillars with topics, formats, and posting strategy based on client profile and LinkedIn strategy. This skill should be used when (1) after linkedin-strategy-creator has defined goals and approach, (2) client profile has general content pillars but needs LinkedIn-specific themes, (3) before running linkedin-content-ideation to establish content foundation, (4) quarterly content pillar refresh.
---

# LinkedIn Content Pillars

Create LinkedIn-specific content pillars that map to business goals, audience needs, and the founder's expertise. These pillars guide all content ideation.

## When to Use This Skill

This skill activates when users want to:

**Primary Use Cases:**
- "Define content pillars for [client]'s LinkedIn"
- "What topics should [founder] post about on LinkedIn?"
- "Create a LinkedIn content framework for [company]"
- "We need to organize our LinkedIn content strategy"

**Integration Points:**
- After running `sidekick-linkedin-strategy-creator` (required)
- After running `sidekick-linkedin-voice-capture` (recommended)
- Before running `sidekick-linkedin-content-ideation`
- Quarterly refresh to optimize based on performance

**What This Skill Produces:**
- 4-6 distinct content pillars with specific topics
- Weekly content mix recommendation
- Performance tracking framework
- Guidance for both founder and company page

## Knowledge Base Reference

**ALWAYS load these files BEFORE creating pillars:**

### Required: Client Profile
**Location:** `{{client_folder}}/00_[CLIENT]_CLIENT_PROFILE.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| 3. Target Audience | Audience segments, psychographics | Pillars for each key audience |
| 4. Brand Voice | Tone, personality, what to avoid | Pillars that match their style |
| 5. Products & Services | Key offerings, differentiators | Authority/expertise pillars |
| 6. Content Pillars | Existing pillars (if defined) | **Check first** - may already exist |
| 8. KPIs & Goals | Business goals (leads? awareness?) | Weight pillars toward goals |
| 9. Competitors | Positioning, differentiators | Differentiation pillars |
| 10. Seasonality | Key events, campaigns, calendar | Timely content pillars |
| 15. Origin Story | Founder/owner background, the "why" | Personal/story pillars |

**⚠️ CHECK FIRST:** Some profiles already have Content Pillars defined in Section 6 (like CMA). If they exist:
- Review and validate they work for LinkedIn
- Expand with LinkedIn-specific topics and formats
- Don't duplicate work already done

### Required: LinkedIn Strategy
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| Primary Goal | Brand awareness / Leads / etc. | Weight pillars toward goal |
| Research Findings | Top performer patterns | Industry-relevant topics |
| Format Strategy | Preferred formats | Match pillar to format |

### Recommended: Founder Voice Guide
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/01_Founder_Voice_Guide.md`

| Element | How to Use It |
|---------|---------------|
| Topics they love | High-priority pillars |
| Hot takes | Thought leadership pillar topics |
| What frustrates them | Commentary pillar angles |

**⚠️ CRITICAL:** Pillars must be specific to THIS founder's expertise and THIS audience's needs. Generic pillars like "Industry News" are useless.

## Prerequisites

**Required (in order):**
1. `sidekick-profile-builder` - Client profile
2. `sidekick-linkedin-strategy-creator` - LinkedIn strategy (must exist)

**Recommended:** `sidekick-linkedin-voice-capture` (for founder-specific themes)

## Input Required

User provides:
1. **Client folder path** - To locate client profile
2. **Primary LinkedIn goal** - Choose 1-2:
   - Brand awareness
   - Thought leadership
   - Lead generation
   - Talent attraction
   - Community building
3. **Posting frequency** - Posts per week

## Workflow

### Step 1: Load Strategic Foundation

Extract from `00_[CLIENT]_CLIENT_PROFILE.md`:
- Target audience pain points and goals (Section 3)
- Brand voice and tone (Section 4)
- Products/services to promote (Section 5)
- General content pillars if exist (Section 6)
- Business KPIs (Section 8)
- Founder background and expertise (Section 15)
- Industry and competitors (Sections 1, 9)

If `[CLIENT]_FOUNDER_VOICE_GUIDE.md` exists, extract:
- Topics founder is passionate about
- Their hot takes
- Themes they gravitate toward

### Step 2: Load Strategy Context

**Read from `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`:**
- Primary LinkedIn goal (Section 1)
- Research findings and patterns (Section 3)
- Format strategy preferences (Section 6)
- Posting frequency (Section 7)

This research was already done by `linkedin-strategy-creator` - use it to inform pillar creation.

### Step 3: Map Goals to Content Types

| LinkedIn Goal | Content Types That Work |
|---------------|------------------------|
| Brand awareness | Industry commentary, behind-the-scenes, company milestones |
| Thought leadership | Original insights, contrarian takes, frameworks, predictions |
| Lead generation | Problem-aware content, case studies, how-to guides |
| Talent attraction | Culture posts, employee spotlights, values-driven content |
| Community building | Questions, polls, celebrating others, engagement posts |

### Step 4: Generate Content Pillars

**Quality Guardrails for Pillars:**
- ❌ Avoid: Generic pillars that any company could use ("Industry News", "Tips & Tricks")
- ❌ Avoid: Pillars with no clear connection to business goals
- ❌ Avoid: Overlapping pillars (if you can't decide which pillar a topic fits, they overlap)
- ✅ Require: Each pillar reflects the founder's unique expertise or POV
- ✅ Require: Each pillar has 5+ SPECIFIC topics (not "industry trends" but "Why [specific trend] is overhyped")
- ✅ Require: Clear differentiation - could a competitor use this exact pillar framework? If yes, it's too generic

**The Specificity Test:**
For each topic idea, ask: "Could only THIS founder write this post?"
- ❌ "Tips for better leadership" - Anyone could write this
- ✅ "What I learned firing my first employee at [Company]" - Only they can write this

Create 4-6 LinkedIn-specific pillars:

```markdown
# [Company Name] - LinkedIn Content Pillars
**For:** [Founder Name]'s profile + [Company] page
**Generated:** [Date]
**Primary Goal:** [Goal from input]
**Posting Frequency:** [X posts/week]

---

## Pillar Overview

| # | Pillar Name | Purpose | % of Content | Best Format |
|---|-------------|---------|--------------|-------------|
| 1 | [Name] | [Purpose] | [X%] | [Format] |
| 2 | [Name] | [Purpose] | [X%] | [Format] |
| 3 | [Name] | [Purpose] | [X%] | [Format] |
| 4 | [Name] | [Purpose] | [X%] | [Format] |
| 5 | [Name] | [Purpose] | [X%] | [Format] |

**Total:** 100%

---

## Pillar 1: [Name]

**Purpose:** [What this pillar achieves for the business]

**Why It Works for [Audience]:**
[How this addresses their needs/interests]

**Content Themes:**
- [Theme 1]
- [Theme 2]
- [Theme 3]

**Example Topics (write as actual post titles, not categories):**
1. [Specific topic - "Why we stopped doing X and revenue doubled"]
2. [Specific topic - "The $50K mistake I made in year one"]
3. [Specific topic - "Unpopular opinion: [industry practice] is dead"]
4. [Specific topic - "I analyzed 100 [things]. Here's what I found"]
5. [Specific topic - "What [industry event] means for [audience]"]

**Best Formats:**
- Primary: [Format] - Why
- Secondary: [Format] - Why

**Founder vs Company Page:**
- Founder: [How to approach on personal profile]
- Company: [How to approach on company page, or "Skip"]

**Sample Hook:**
"[Example opening line for this pillar]"

---

## Pillar 2: [Name]
[Same structure as Pillar 1]

---

## Pillar 3: [Name]
[Same structure as Pillar 1]

---

## Pillar 4: [Name]
[Same structure as Pillar 1]

---

## Pillar 5: [Name]
[Same structure as Pillar 1]

---

## Weekly Content Mix

For [X] posts per week:

| Day | Pillar | Format | Channel |
|-----|--------|--------|---------|
| Monday | [Pillar] | [Format] | Founder |
| Wednesday | [Pillar] | [Format] | Founder |
| Thursday | [Pillar] | [Format] | Company |
| Friday | [Pillar] | [Format] | Founder |

**Monthly Breakdown:**
- Pillar 1: [X] posts
- Pillar 2: [X] posts
- Pillar 3: [X] posts
- Pillar 4: [X] posts
- Pillar 5: [X] posts

---

## Content Calendar Integration

### Recurring Content:
- **Weekly:** [Any weekly series or recurring format]
- **Monthly:** [Any monthly themes]
- **Quarterly:** [Any quarterly content like reviews, predictions]

### Tie to Business Calendar:
- [Event/date] → [Content opportunity]
- [Event/date] → [Content opportunity]
- [Event/date] → [Content opportunity]

---

## Pillar Performance Tracking

| Pillar | Track This Metric | Target |
|--------|-------------------|--------|
| [Pillar 1] | [Metric] | [Target] |
| [Pillar 2] | [Metric] | [Target] |
| [Pillar 3] | [Metric] | [Target] |
| [Pillar 4] | [Metric] | [Target] |
| [Pillar 5] | [Metric] | [Target] |

**Review Cadence:** Monthly

---

## Pillar Evolution

After 3 months, evaluate:
- Which pillars drive most engagement?
- Which pillars drive business results (leads, traffic)?
- What's missing that audience keeps asking about?
- What's underperforming and should be retired?

Adjust percentages and add/remove pillars based on data.
```

### Step 5: Validate Pillars

Before saving, verify:

**Pillar Quality:**
- [ ] 4-6 distinct pillars (not overlapping)
- [ ] Percentages add to 100%
- [ ] Each pillar has 5+ specific topic ideas
- [ ] Each pillar has clear purpose tied to business goal
- [ ] Each pillar has recommended formats
- [ ] Founder vs Company Page guidance included

**Strategic Alignment:**
- [ ] Maps to client's primary LinkedIn goal
- [ ] Reflects founder's expertise and interests
- [ ] Addresses audience pain points
- [ ] Balanced across brand awareness, engagement, and conversion

**Practical Usability:**
- [ ] Weekly mix is realistic for posting frequency
- [ ] Performance metrics are trackable
- [ ] Calendar integration suggestions included

### Step 6: Save Output

Save to: `[client_folder]/07_Marketing_Channels/LinkedIn/03_Content_Pillars.md`

### Step 7: Update LinkedIn Strategy

After saving pillars, update the existing strategy document with pillar summary.

**Add to `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md` Section 5:**
- Pillar overview table (from output)
- Pillar percentages
- Link to full `03_Content_Pillars.md`

This ensures the strategy doc stays current as a single reference point.

## Quality Standards

✅ 4-6 distinct pillars (not overlapping)
✅ Percentages add to 100%
✅ Each pillar has 5+ specific topic ideas
✅ Mapped to business goals
✅ Considers both founder and company page
✅ Includes weekly mix recommendation
✅ Has clear performance metrics

## Example Pillars by Industry

### Biotech/Pharma CEO:
1. Industry Trends (30%) - Market dynamics, regulatory landscape
2. Science Simplified (25%) - Making complex topics accessible
3. CEO Reflections (20%) - Leadership lessons, company journey
4. Team & Culture (15%) - Behind the scenes, hiring
5. Industry POV (10%) - Hot takes, predictions

### Marketing Agency:
1. Marketing Tactics (30%) - How-tos, tips, frameworks
2. Case Studies (25%) - Client wins, results
3. Industry Commentary (20%) - Trends, platform updates
4. Agency Life (15%) - Culture, team, behind the scenes
5. Thought Leadership (10%) - Contrarian takes, predictions

### Music Academy:
1. Student Success (30%) - Spotlights, achievements
2. Music Education Tips (25%) - Practice advice, learning insights
3. Community Connection (20%) - Local events, partnerships
4. Behind the Scenes (15%) - Teachers, studio life
5. Parent Resources (10%) - Guides, FAQs, enrollment info

## Time Estimate

| Step | Time |
|------|------|
| Load strategic foundation | 5-10 min |
| Load strategy context | 5 min |
| Map goals to content | 5 min |
| Generate pillars | 20-30 min |
| Validation | 5-10 min |
| Update strategy doc | 5 min |
| **Total** | **45-70 min** |

## Example Pillar Preview

**What a completed pillar looks like:**

```markdown
## Pillar 2: Industry Insights

**Purpose:** Establish thought leadership by sharing unique perspectives on industry trends

**Why It Works for [Audience]:**
They're overwhelmed by generic advice and crave perspectives from practitioners who've actually done the work.

**Content Themes:**
- Trend analysis and predictions
- Contrarian takes on "best practices"
- Lessons from industry shifts

**Example Topics:**
1. Why [common approach] is setting companies back
2. 3 predictions for [industry] in 2026
3. The metric everyone tracks that doesn't matter
4. What I learned from [specific industry event]
5. Why [emerging technology] won't replace [current approach]

**Best Formats:**
- Primary: Text post (hot takes, quick insights)
- Secondary: Carousel (frameworks, predictions)

**Founder vs Company Page:**
- Founder: Personal perspective, "I think...", contrarian takes
- Company: Data-backed insights, industry reports, formal analysis

**Sample Hook:**
"Everyone in [industry] is obsessed with [trend]. Here's why that's a problem:"
```

## Troubleshooting

**Issue: Pillars overlap too much**
- Solution: Merge similar pillars or create clearer boundaries
- Ask: "If I had to categorize this topic, which ONE pillar fits best?"
- Each pillar should have distinct keywords/themes

**Issue: Can't reach 5 topic ideas per pillar**
- Solution: Pillar may be too narrow—consider broadening
- Or pillar may need to be merged with another
- Check founder's hot takes and interests for inspiration

**Issue: Percentages don't align with goals**
- Solution: If goal is lead gen, increase problem-aware content %
- If goal is thought leadership, increase insights/commentary %
- Review `references/CONTENT_MIX_GUIDE.md` for guidance

**Issue: Company page doesn't fit some pillars**
- Solution: It's OK to mark some pillars as "Founder only"
- Company page can focus on 2-3 pillars that fit institutional voice
- Personal stories/vulnerability should stay on founder profile

**Issue: Client capacity is limited**
- Solution: Reduce to 3-4 core pillars
- Focus on highest-impact formats (text posts, carousels)
- Prioritize quality over quantity

## References

- `references/PILLAR_TEMPLATES.md` - Industry-specific pillar examples
- `references/CONTENT_MIX_GUIDE.md` - How to balance pillar percentages
- `references/INDUSTRY_ADAPTATION.md` - **Industry-specific content style, hooks, cadence, engagement drivers**
- `references/CONTENT_REPURPOSING.md` - **How to repurpose content across formats** (maximize each pillar)
