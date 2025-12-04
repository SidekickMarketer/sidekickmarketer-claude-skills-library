---
name: sidekick-linkedin-strategy-creator
description: Create comprehensive LinkedIn strategy including research, dual-channel approach, format strategy, and engagement guidelines. This skill should be used when (1) onboarding a new client who needs LinkedIn presence, (2) quarterly strategy refresh, (3) before creating LinkedIn content pillars or content, (4) client asks how to approach LinkedIn. Run AFTER profile-builder and BEFORE other LinkedIn skills.
---

# LinkedIn Strategy Creator

Create a comprehensive LinkedIn strategy document that serves as the persistent reference for all LinkedIn-related skills and content creation.

## When to Use This Skill

This skill activates when users want to:

**Primary Use Cases:**
- "Create a LinkedIn strategy for [client]"
- "How should [founder] approach LinkedIn?"
- "Build a LinkedIn plan for [company]"
- "We need a LinkedIn strategy before creating content"

**Integration Points:**
- This is the FOUNDATION skill for all LinkedIn work
- Run AFTER `sidekick-profile-builder` (required)
- Run BEFORE all other LinkedIn skills
- Quarterly refresh recommended

**What This Skill Produces:**
- Comprehensive strategy document (`00_LINKEDIN_STRATEGY.md`)
- Research findings on top performers in industry
- Dual-channel strategy (founder vs company page)
- Format strategy with benchmarks
- Engagement guidelines
- Success metrics with targets

**Skill Sequence:**
```
1. sidekick-profile-builder (prerequisite)
2. sidekick-linkedin-strategy-creator ← YOU ARE HERE
3. sidekick-linkedin-voice-capture
4. sidekick-linkedin-profile-optimizer
5. sidekick-linkedin-content-pillars
6. sidekick-linkedin-content-ideation
```

## Knowledge Base Reference

**Always load these files BEFORE generating any output:**

### Required: Client Profile
**Location:** `{{client_folder}}/00_[CLIENT]_CLIENT_PROFILE.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| 1. Business Core | Industry, company size, founded year | Research context |
| 3. Target Audience | Demographics, psychographics, segments | Audience-specific strategy |
| 4. Brand Voice | Tone, personality, approved phrases, words to avoid | Voice guidelines |
| 5. Products & Services | Offerings, priority, pricing | Content topics, value props |
| 7. SOW/Deliverables | Contract scope, posting frequency | Strategy constraints |
| 8. KPIs & Goals | Business goals, platform metrics, targets | Strategy KPIs |
| 9. Competitors | Names, strengths, differentiators | Positioning opportunities |
| 10. Seasonality | Key events, campaigns, calendar | Content timing |
| 12. Account Access | Platform handles, current metrics | Baseline data |
| 13. Guidelines | Compliance, approval workflow, topics to avoid | Constraints |
| 15. Origin Story | Founder background, milestones | Thought leadership angles |
| 17. Marketing History | What worked, what flopped | What to avoid repeating |

**Note:** Section 4 structure varies by client. Some have single brand voice, others split company/founder voice (4A/4B). Adapt accordingly.

### Optional: Prior Skill Outputs
If these exist, load them for context:
- `Social_Audit.md` - Historical performance data
- Previous strategy docs - What's worked before

**⚠️ CRITICAL:** Never generate strategy without reading the client profile first. Generic strategies are useless.

## Output Structure

```
07_Marketing_Channels/LinkedIn/
├── 00_LINKEDIN_STRATEGY.md      # Master LinkedIn strategy (created by this skill)
├── 01_Founder_Voice_Guide.md    # Created by linkedin-voice-capture
├── 02_Profile_Specs.md          # Created by linkedin-profile-optimizer
├── 03_Content_Pillars.md        # Created by linkedin-content-pillars
└── 04_Content_Archive/          # Historical content
```

## Prerequisites

**Required:** `sidekick-profile-builder` (client profile must exist)

Client must have `00_[CLIENT]_CLIENT_PROFILE.md` with:
- Section 1: Business Core (industry, company info)
- Section 3: Target Audience
- Section 4: Brand Voice
- Section 8: KPIs & Goals
- Section 15: Origin Story (for founder context)

## Input Required

User provides:
1. **Client folder path** - To locate client profile
2. **Primary LinkedIn goal** (choose 1-2):
   - Thought leadership
   - Lead generation
   - Brand awareness
   - Talent attraction
   - Community building
3. **Founder name** - Who will be the primary voice
4. **Posting frequency** - Posts per week (founder + company)

---

## Phase 1: Discovery & Research

### Step 1: Load Client Context

Extract from `00_[CLIENT]_CLIENT_PROFILE.md`:
- Industry and competitive landscape (Section 1)
- Target audience and pain points (Section 3)
- Brand voice and tone (Section 4)
- Business goals and KPIs (Section 8)
- Founder background (Section 15)
- Products/services (Section 5)

### Step 2: Load Audit Findings (If Available)

From previous `Social_Audit.md`, extract:
- LinkedIn-specific findings
- Current follower count and engagement baseline
- What's worked historically

### Step 3: Research Top Performers

**First, load `references/INDUSTRY_ADAPTATION.md` for industry-specific guidance:**
- Benchmark expectations for this industry
- Topics that work / topics to avoid
- Compliance requirements
- Suggested research queries

**Then use `WebSearch` to find top 1% LinkedIn execution in the client's industry:**

```
Search queries:
- "best [industry] LinkedIn creators 2025"
- "top [industry] thought leaders LinkedIn"
- "[industry] LinkedIn content strategy examples"
- "viral [industry] LinkedIn posts what works"
- "[industry] executives LinkedIn followers"
```

**Analyze 3-5 top performers for:**
- Content pillars they focus on
- Formats that get highest engagement
- Topics that resonate most
- Posting frequency and consistency
- Voice and personality traits
- Hook patterns they use
- **SPECIFIC phrases and patterns** (not generic observations)

**⚠️ CRITICAL: Don't just describe - DOCUMENT SPECIFICS:**
- ❌ Bad: "They post thought leadership content"
- ✅ Good: "Posts contrarian takes on [specific topic], uses 'Unpopular opinion:' hook pattern, averages 200+ comments by asking provocative questions"

**Identify opportunities:**
- Common themes across top performers (table stakes - must do)
- Gaps no one is filling (differentiation - unique angle)
- Industry-specific formats that work
- Engagement triggers for this audience

**The Differentiation Question:**
After research, answer: "What can [Founder] talk about that competitors CAN'T or WON'T?"
- Unique experience (founding story, failures, pivots)
- Contrarian POV (what do they believe that's unpopular?)
- Specific expertise (what do they know that others don't?)
- Access (customers, data, behind-the-scenes they can share)

**Document findings in strategy doc Section 3 with SPECIFIC examples, not general observations.**

---

## Phase 2: Strategy Development

### Step 4: Define Dual-Channel Strategy

LinkedIn requires a dual-channel approach:

**Founder Profile (Primary):**
- Thought leadership hub
- Personal stories and insights
- Hot takes and industry commentary
- Higher engagement potential
- Connection requests and DMs

**Company Page (Secondary):**
- Brand presence and legitimacy
- Job postings
- Company news and milestones
- Case studies (formal versions)
- Institutional content

**Create channel balance matrix:**
| Content Type | Founder | Company |
|--------------|---------|---------|
| Thought leadership | Primary | Reshare |
| Personal stories | Primary | Skip |
| Industry commentary | Primary | Adapted |
| Company news | Personal take | Primary |
| Case studies | Intro/story | Full version |
| Job posts | Skip | Primary |
| Culture/team | Personal angle | Primary |

### Step 5: Define Format Strategy

Load `references/LINKEDIN_BENCHMARKS.md` for performance data.

**Research-informed format mix:**

| Format | Target % | Best For | Performance Notes |
|--------|----------|----------|-------------------|
| Text posts | 50% | Stories, insights, hot takes | 600-1,200 chars optimal |
| Carousels/Docs | 25% | Frameworks, tips, how-tos | 6-10 slides, hook on slide 1 |
| Polls | 15% | Engagement, research, reach | 2-4 options, opinion-based |
| Video | 10% | Personal connection | 60-90s max, vertical, captions |

**Format guidelines per type:**
- Text: White space (+25% performance), strong closer
- Carousels: One idea per slide, CTA on final slide
- Polls: Avoid "other" option, make it opinion-based
- Video: Hook in first 3 seconds, always add captions

### Step 6: Create Posting Schedule

**Determine optimal frequency based on:**
- Client capacity (from SOW or input)
- Industry norms (from research)
- Competition saturation

**Optimal posting times for LinkedIn:**
- Tuesday-Thursday: Highest engagement
- 7-8am, 12pm, 5-6pm local time
- Avoid weekends (60% lower reach)

**Create weekly rhythm:**
| Day | Channel | Focus |
|-----|---------|-------|
| Monday | Founder | Week-opening insight |
| Tuesday | - | Engagement day (comments) |
| Wednesday | Founder | Educational content |
| Thursday | Company | Company/culture content |
| Friday | Founder | Reflective/story content |

### Step 7: Define Engagement Strategy

Load `references/ENGAGEMENT_TACTICS.md` for detailed tactics.

**Response protocol:**
| Interaction | Response Time | Action |
|-------------|---------------|--------|
| Comments on our posts | Within 1 hour | Reply to all |
| DMs | Within 24 hours | Personal response |
| Mentions | Within 24 hours | Engage appropriately |
| Connection requests | Within 48 hours | Accept if relevant |

**Proactive engagement (daily 10-15 min):**
- Comment on 5-10 posts from target audience
- Engage with industry thought leaders
- Respond to all comments on our content

**Comment quality rules:**
- Add value, not just "Great post!"
- Share perspective or experience
- Ask thoughtful questions

### Step 8: Set Success Metrics

**Primary KPIs:**
| Metric | Benchmark | Target |
|--------|-----------|--------|
| Engagement Rate | 2-4% (avg), 4-6% (good), >6% (excellent) | [Based on goal] |
| Follower Growth | 5-10% monthly | [Based on goal] |
| Profile Views | Varies by industry | Track baseline + growth |
| Inbound Leads | Varies | [Based on goal] |

**Tracking cadence:**
- Weekly: Engagement check, respond to comments
- Monthly: Full analytics review
- Quarterly: Strategy adjustment

---

## Phase 3: Document Generation

### Step 9: Generate Strategy Document

**Load template:** `references/LINKEDIN_STRATEGY_TEMPLATE.md`

**Fill all sections using:**
- Research findings (Step 3)
- Dual-channel strategy (Step 4)
- Format strategy (Step 5)
- Posting schedule (Step 6)
- Engagement strategy (Step 7)
- Success metrics (Step 8)
- Client profile context (Step 1)

**Placeholder sections (to be filled by other skills):**
- Section 4 (Voice Summary): Placeholder until linkedin-voice-capture runs
- Section 5 (Content Pillars): Placeholder until linkedin-content-pillars runs
- Section 8 (Profile Status): Placeholder until linkedin-profile-optimizer runs

### Step 10: Save Output

**Save to:** `[client_folder]/07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`

**Create folder structure if needed:**
```bash
mkdir -p "{{client_folder}}/07_Marketing_Channels/LinkedIn/04_Content_Archive"
```

---

## Phase 4: Validation

### Step 11: Strategy Validation

Check the strategy doc:
- [ ] All placeholders replaced with client-specific data
- [ ] Research findings documented with 3+ top performers
- [ ] Dual-channel strategy clearly differentiates founder vs company
- [ ] Format mix adds to 100%
- [ ] Posting schedule is realistic for stated capacity
- [ ] Metrics have specific numeric targets
- [ ] Placeholder sections clearly marked for other skills
- [ ] No generic advice

### Step 12: Create LinkedIn Brief (Optional)

**For quick reference, create LINKEDIN_BRIEF.md (1 page summary):**
- Platform Goals (ranked)
- Dual-Channel Split (Founder vs Company)
- Format Mix (percentages)
- 90-Day Focus (top 3 priorities)
- Key Metrics (3 KPIs with targets)

**Save to:** `07_Marketing_Channels/LinkedIn/LINKEDIN_BRIEF.md`

---

## Output Summary

| Document | Location |
|----------|----------|
| LinkedIn Strategy | `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md` |
| LinkedIn Brief (optional) | `07_Marketing_Channels/LinkedIn/LINKEDIN_BRIEF.md` |

---

## Quality Standards

Every strategy must include:
- Research findings with 3+ top performers analyzed
- Dual-channel strategy clearly differentiating founder vs company
- Format mix totaling 100%
- Engagement strategy with response protocols
- Specific KPI targets with benchmarks
- Realistic posting schedule for client capacity

Every strategy must avoid:
- Generic advice ("post consistently")
- Copy-paste content from templates
- Missing research documentation
- Unrealistic targets
- Ignoring client capacity/constraints

---

## Top 1% Execution Checklist

**What separates top 1% LinkedIn execution from average:**

### Content Quality
- [ ] Every post has a hook that creates curiosity (not "Excited to share...")
- [ ] Content is specific to THIS founder's expertise (not generic advice)
- [ ] Posts include specific numbers, stories, or examples
- [ ] Voice is distinctive (someone could identify it as this person)
- [ ] Each post has ONE clear takeaway (not 7 tips crammed together)

### Strategic Differentiation  
- [ ] Strategy identifies what founder can say that competitors CAN'T
- [ ] Content angles come from unique experience (failures, pivots, behind-the-scenes)
- [ ] Contrarian POV is identified and leveraged
- [ ] Industry gaps are documented (what no one else is talking about)

### Execution Consistency
- [ ] Response to comments within 1 hour of posting
- [ ] Proactive engagement on others' content daily (10+ comments)
- [ ] Format variety (not just text posts)
- [ ] Posting schedule matches actual capacity (realistic, not aspirational)

### Industry Adaptation
- [ ] Benchmarks are industry-specific (see `references/INDUSTRY_ADAPTATION.md`)
- [ ] Compliance requirements documented and followed
- [ ] Topics to avoid are clearly stated
- [ ] Best formats for this industry are prioritized

### Measurement
- [ ] KPIs have specific numeric targets
- [ ] Baseline metrics captured before starting
- [ ] Review cadence established (weekly engagement, monthly full review)

---

## Skill Sequence

**This skill is the foundation for LinkedIn work:**

```
1. sidekick-profile-builder (prerequisite)
2. sidekick-linkedin-strategy-creator ← YOU ARE HERE
3. sidekick-linkedin-voice-capture (updates Section 4)
4. sidekick-linkedin-profile-optimizer (updates Section 8)
5. sidekick-linkedin-content-pillars (updates Section 5)
6. sidekick-linkedin-content-ideation (uses strategy)
```

---

## Time Estimate

| Phase | Time |
|-------|------|
| Discovery & Research | 20-30 min |
| Strategy Development | 15-20 min |
| Document Generation | 10-15 min |
| Validation | 5-10 min |
| **Total** | **50-75 min** |

## Maintenance Schedule

| Cadence | Action | Template |
|---------|--------|----------|
| Weekly | Review engagement metrics | Quick check |
| Monthly | Full analytics review | `references/MONTHLY_REVIEW_TEMPLATE.md` |
| Quarterly | Strategy refresh (re-run this skill) | Re-run skill |
| Annually | Complete strategy overhaul | Full audit |

**Monthly Review Process:**
1. Use `references/MONTHLY_REVIEW_TEMPLATE.md` to structure the review
2. Identify top/bottom performing content
3. Adjust pillar weights if needed
4. Document lessons learned
5. Save to `07_Marketing_Channels/LinkedIn/05_Performance_Reviews/[Month]_Review.md`

**Trigger for early refresh:**
- Major algorithm change announced
- Significant business pivot
- New competitor enters space
- Current strategy underperforming 2+ months

## Troubleshooting

**Issue: Can't find top performers in industry**
- Solution: Broaden to adjacent industries or related roles
- Search for "[role] LinkedIn" not just "[industry] LinkedIn"
- Check LinkedIn's own "Top Voices" lists

**Issue: Research feels too generic**
- Solution: Focus on specific patterns (hooks, formats, topics)
- Document actual post examples, not just general advice
- Look for differentiation opportunities, not just best practices

**Issue: Format mix doesn't fit client capacity**
- Solution: Reduce to 2-3 core formats
- Prioritize text posts (lowest effort, solid performance)
- Add carousels once rhythm is established

**Issue: Engagement strategy is overwhelming**
- Solution: Start with post replies only (first hour)
- Add proactive engagement after 2-4 weeks
- Build habit gradually

**Issue: Metrics are hard to track**
- Solution: Focus on engagement rate (available on all profiles)
- Use LinkedIn's built-in analytics
- Track follower growth monthly (simple spreadsheet)

**Issue: Client has no LinkedIn presence yet**
- Solution: Focus on profile optimization first
- Start with 2 posts/week to build consistency
- Engagement strategy becomes critical (comment on others' content)

## References

- `references/LINKEDIN_STRATEGY_TEMPLATE.md` - Full strategy template
- `references/LINKEDIN_BENCHMARKS.md` - Industry benchmark data
- `references/ENGAGEMENT_TACTICS.md` - Engagement best practices
- `references/INDUSTRY_ADAPTATION.md` - **Industry-specific adaptation guide** (benchmarks, topics, compliance by industry)
- `references/MONTHLY_REVIEW_TEMPLATE.md` - **Monthly performance review template** (for ongoing optimization)
