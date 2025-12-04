---
name: sidekick-linkedin-content-ideation
description: Generate 3 high-performing LinkedIn content ideas with dual-channel execution (founder/exec profile + company page) based on 2025 algorithm data. This skill should be used when (1) user asks for LinkedIn content ideas for a specific audience, (2) user wants to brainstorm LinkedIn posts for a client's founder/CEO, (3) user needs content strategy for LinkedIn engagement, (4) user mentions creating content for LinkedIn professionals.
---

# LinkedIn Content Ideation Engine

Generate 3 distinct, high-quality LinkedIn content ideas with dual-channel execution:
- **Founder/Exec Profile** = Primary channel (thought leadership, personal voice)
- **Company Page** = Supporting channel (institutional version or reshare)

**Before generating ideas, read:** `references/LINKEDIN_STRATEGY_2025.md`

## When to Use This Skill

This skill activates when users want to:

**Primary Use Cases:**
- "Generate LinkedIn content ideas for [client/founder]"
- "I need 3 LinkedIn post ideas for [topic/industry]"
- "Brainstorm LinkedIn content for [audience]"
- "What should [founder] post about on LinkedIn?"

**Integration Points:**
- After running `sidekick-linkedin-strategy-creator` (required)
- After running `sidekick-linkedin-content-pillars` (recommended)
- After running `sidekick-linkedin-voice-capture` (recommended for authenticity)
- During weekly/monthly content planning

**What This Skill Produces:**
- 3 distinct content ideas with full execution details
- Both founder post AND company page version for each idea
- Algorithm optimization notes
- Quick reference guide for prioritization

## Knowledge Base Reference

**ALWAYS load these files BEFORE generating ideas:**

### Required: Client Profile
**Location:** `{{client_folder}}/00_[CLIENT]_CLIENT_PROFILE.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| 3. Target Audience | Pain points, goals, audience segments | Content that resonates with THEIR specific audiences |
| 4. Brand Voice | Tone, personality, approved phrases, words to avoid | Match their voice exactly |
| 6. Content Pillars | Themes, purpose, topics, % mix | Map each idea to a pillar |
| 9. Competitors | Positioning, differentiators | Angles that set them apart |
| 13. Guidelines | Compliance, approval workflow, topics to avoid | What NOT to say |
| 15. Origin Story | Founder background, key milestones, the "why" | Source for authentic stories |
| 18. Content Bank | Photo library, testimonials, FAQs | Source material |

**Note:** Some profiles have subsections (4A/4B) for company vs. founder voice. If present, use the appropriate voice for the content type.

### Required: LinkedIn Strategy
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| Goal & Approach | Primary LinkedIn goal | Match content to goal (leads vs awareness) |
| Format Strategy | Preferred formats, % mix | Select appropriate formats |
| Research Findings | Top performers, patterns | Inform content angles |

### Highly Recommended: Founder Voice Guide
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/01_Founder_Voice_Guide.md`

| Element | How to Use It |
|---------|---------------|
| Signature phrases | Include naturally in content |
| Topics they love | Prioritize these in ideation |
| Hot takes | Source for contrarian content |
| Words to avoid | Never use these |

### Optional: Content Pillars
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/03_Content_Pillars.md`

**⚠️ CRITICAL:** Never generate ideas without reading client profile first. Generic content performs poorly.

## Prerequisites

**Required (in order):**
1. `sidekick-profile-builder` - Client profile
2. `sidekick-linkedin-strategy-creator` - LinkedIn strategy (must exist)
3. `sidekick-linkedin-content-pillars` - Content pillars (recommended)

**Optional but helpful:**
- `sidekick-linkedin-voice-capture` - Founder voice guide

## Input Required

User provides:
1. **Client folder path** - To locate client profile
2. **Target audience** (optional) - Override profile's audience if needed
3. **Specific topic** (optional) - If user has a topic in mind

## Workflow

### Step 1: Load Client Profile

Read `00_[CLIENT]_CLIENT_PROFILE.md` and extract:
- **Voice/Tone** from Section 4 (Brand Voice)
- **Content Pillars** from Section 6 (themes to write about)
- **Target Audience** from Section 3
- **Guidelines** from Section 13 (what to avoid, compliance needs)
- **Founder Story** from Section 15 (for personal perspective)
- **Primary Contact** from Section 2 (founder/exec name)

### Step 2: Research for Top 1% Execution

**Always use `WebSearch` to ensure ideas match current best practices:**

```
Required searches:
1. "[Industry] LinkedIn trending topics [current month] 2025"
2. "best [industry] LinkedIn posts this week"
3. "top [industry] thought leaders LinkedIn content"
4. "viral LinkedIn hook structures [current month] analysis"
```

**Analyze search results for:**
- What topics are getting engagement right now?
- What formats are top performers using?
- What angles haven't been covered yet?
- What industry news can be leveraged?

**Why this matters:**
- Trending topics yield **+50% additional reach**
- Industry-specific insights beat generic advice
- Ensures content is current, not recycled ideas
- Identifies differentiation opportunities

**Document in output:**
```
RESEARCH INSIGHTS:
- Trending topics found: [List]
- Top-performing content types: [List]
- Angle/gap identified: [Insight]
- Sources: [URLs]
```

### Step 3: Audience + Algorithm Analysis

**Audience Deep Dive:**
- Top 3-5 pain points/challenges
- Professional goals and aspirations
- What content formats do they engage with?

**Apply Algorithm Knowledge (from LINKEDIN_STRATEGY_2025.md):**

| Factor | Why It Matters |
|--------|----------------|
| Dwell time | Longer reads = more reach |
| Comments | #1 visibility driver |
| Saves/Reposts | Strongest reach signals |
| Expertise | Real knowledge, not generic advice |

**Format Selection Guide:**

| If Goal Is... | Use This Format |
|---------------|-----------------|
| Maximum reach | Poll (1.64x multiplier) |
| Deep engagement | Document/Carousel (5.85% ER) |
| Personal connection | Video 60-90 sec (5.60% ER) |
| Quick thought leadership | Text post 600-1,200 chars |
| Visual storytelling | Multi-image (6.60% ER) |

### Step 4: Generate 3 Content Ideas

**Requirements:**
- Each idea must align with one of the client's **Content Pillars** (Section 6)
- Use at least 2 different formats across the 3 ideas
- Respect **Guidelines** (Section 13) - especially for regulated industries (biotech, finance, healthcare)
- Write in the founder's voice using **Brand Voice** guidance (Section 4)
- **Visual Briefs:** For non-text posts (Carousels, Images), you MUST describe the visual.
  - ❌ "Format: Carousel"
  - ✅ "Visual: Minimalist pie chart on white background showing [Data point A] vs [Data point B]"

**Anti-Drift Check:**
Before finalizing content, scan for generic "LinkedIn speak".
- If you see: "delighted to share", "in today's landscape", "leverage", "synergy", "unlock"
- REPLACE with: Specific, conversational language as defined in the Founder Voice Guide.

**Quality Guardrails - AVOID:**
- ❌ Generic advice that could apply to any industry ("Be authentic!")
- ❌ Hooks that start with "I'm excited to share..." or "Thrilled to announce..."
- ❌ Yes/no CTAs ("Agree?", "Thoughts?")
- ❌ Overused formats ("5 tips for..." without unique angle)
- ❌ Vague statements without specific examples or data
- ❌ Content that sounds like ChatGPT wrote it (corporate, buzzword-heavy)
- ❌ **Inventing relationships** - Don't call someone a "mentor," "friend," or "close colleague" unless the client explicitly said so. Default to formal titles (e.g., "Senior Medical Advisor" not "my mentor")

**Quality Guardrails - REQUIRE:**
- ✅ Specific examples, numbers, or stories from the client's experience
- ✅ Hooks that create curiosity gap or pattern interrupt
- ✅ CTAs that spark discussion ("What's your unpopular take on X?")
- ✅ Content only THIS founder could write (industry-specific, experience-based)
- ✅ Clear POV - founder should have an opinion, not just share info
- ✅ One clear takeaway per post (not 7 points crammed together)

**Hook Quality Test:**
Before including a hook, ask: "Would I stop scrolling for this?" If no, rewrite.

For each idea, provide BOTH the founder post AND company page version:

```
## Idea [#]: [Catchy Title]

**Content Pillar:** [Which pillar from Section 6 this maps to]
**Compliance Check:** [Any guidelines from Section 13 to watch for, or "None"]

### FOUNDER/EXEC POST (Primary Channel)

**FORMAT:** [Poll / Document (X slides) / Video / Text / Multi-image]
- Length: [Character count or slide count or duration]
- Mobile-optimized: Yes (88% browse mobile)

**THE HOOK:**
[First 1-2 lines before "see more" - this is EVERYTHING]

Write the FULL hook text. Use one of these patterns:
- Curiosity gap: "I just [unexpected thing]. Here's what happened..."
- Bold claim: "Unpopular opinion: [contrarian take]"
- Story opener: "Three years ago, I [vulnerable moment]. Today..."
- Data surprise: "I analyzed [X]. The results surprised me..."
- Direct value: "The [framework] that [specific result]:"

**FULL POST COPY:**
Write the complete post, not just structure notes. Include:
- Opening (hook expanded into 2-3 more lines)
- Body (3-5 beats, each on its own line with white space)
- Close (strong statement that lands the point)
- CTA on its own line

Format with line breaks between sections (white space = +25% performance).

**ENGAGEMENT CTA:**
[Open-ended question that invites debate - NOT yes/no]
Good: "What's the most overrated advice in [industry]?"
Bad: "Agree?" or "Thoughts?"

---

### COMPANY PAGE VERSION (Supporting Channel)

**Approach:** [Institutional adaptation / Reshare with comment / Skip this one]

**If Institutional Adaptation:**
- Reframe from "I/my" to "Our team/We/[Company]"
- Shorter, more formal tone
- Focus on company credibility vs personal insight
- [Provide adapted hook and key points]

**If Reshare:**
- Suggested reshare comment: [1-2 sentences from brand voice]

**If Skip:**
- Reason: [e.g., "Too personal/vulnerable for brand page"]

---

### ALGORITHM OPTIMIZATION
- Primary trigger: [Dwell time / Comments / Saves / Shares]
- Expected engagement: [Based on format benchmarks]
- Why this audience will engage: [Specific reason]

### SOURCE (if trend-based)
[Citation for any external research]
```

### Step 5: Quick Reference Guide

```
## QUICK REFERENCE
- **Quick Win:** Idea #X - Easiest to execute
- **Highest Reach Potential:** Idea #X - Based on format multiplier
- **Comment Magnet:** Idea #X - Best discussion driver
- **Authority Builder:** Idea #X - Establishes expertise
- **Trend-Jacking:** Idea #X or "None" - Uses current topic (+50% reach)
```

### Step 6: Posting Recommendations

Include:
- **Best posting frequency:** 2-4x per week
- **Engagement reminder:** Reply to comments in first hour
- **Content lifespan:** Good posts stay in feed 2-3 weeks

### Step 7: First Hour Playbook

**⚠️ CRITICAL: The first hour after posting determines 80% of a post's total reach.**

Include this playbook with every content delivery:

```markdown
## FIRST HOUR PLAYBOOK

### Minute 0-5: Post Goes Live
- [ ] Post published at optimal time (see schedule)
- [ ] First comment added (if applicable - link, additional context)
- [ ] Post URL saved for tracking

### Minute 5-15: Seed Engagement
- [ ] Share post to relevant LinkedIn groups (if applicable)
- [ ] Send to 3-5 colleagues/friends who can leave thoughtful comments
- [ ] DM post to 2-3 people who would genuinely find it valuable

### Minute 15-60: Active Monitoring
- [ ] Reply to EVERY comment within 5 minutes of it appearing
- [ ] Reply length: At least 10-15 words (not just "Thanks!")
- [ ] Ask follow-up questions in replies (keeps thread going)
- [ ] Like every comment immediately

### Engagement Reply Framework
Instead of: "Thanks for sharing!"
Use: "[Name], that's a great point about [specific thing they said]. Have you found that [follow-up question]?"

### Hour 2-6: Continued Engagement
- [ ] Check back every 1-2 hours
- [ ] Continue replying to all new comments
- [ ] If engagement is low, engage on others' posts to increase visibility

### Day 2-3: Follow-up
- [ ] Reply to any overnight comments
- [ ] If post performed well, plan related follow-up content
- [ ] Screenshot engagement for reporting
```

**Why This Matters:**
- LinkedIn's algorithm heavily weights early engagement velocity
- Posts that get 10+ comments in first hour get 3x more reach
- Author replies signal "active conversation" to algorithm
- This is the difference between 500 views and 50,000 views

### Step 8: Validate Output

Before delivering, verify:

**For Each Idea:**
- [ ] Aligns with one of client's Content Pillars (Section 6)
- [ ] Respects Guidelines/Compliance (Section 13)
- [ ] Hook is compelling (would you click "see more"?)
- [ ] CTA is open-ended (not yes/no)
- [ ] Character/slide/duration counts are specified
- [ ] Both founder AND company page versions provided

**Across All 3 Ideas:**
- [ ] At least 2 different formats used
- [ ] No overlapping topics (each idea is distinct)
- [ ] Quick reference guide included
- [ ] Research findings documented
- [ ] First Hour Playbook included

## Quality Standards

✅ Based on 2025 algorithm data (not outdated advice)
✅ Aligned with client's Content Pillars (Section 6)
✅ Written in founder's voice (Section 4)
✅ Respects compliance/guidelines (Section 13)
✅ Format matches goal (reach vs engagement vs authority)
✅ Mobile-optimized (88% of users)
✅ Strong hook (determines if anyone reads further)
✅ Open-ended CTA (comments > likes for algorithm)
✅ Distinct formats across the 3 ideas
✅ Both founder + company page versions provided

## Time Estimate

| Step | Time |
|------|------|
| Load client profile | 2-3 min |
| Research trending topics | 10-15 min |
| Audience + algorithm analysis | 5-10 min |
| Generate 3 ideas | 15-20 min |
| Validation | 5 min |
| **Total** | **35-55 min** |

## Example Output Preview

**What a completed idea looks like:**

```markdown
## Idea 1: The Uncomfortable Truth About [Industry Trend]

**Content Pillar:** Thought Leadership
**Compliance Check:** None

### FOUNDER POST (Primary)

**FORMAT:** Text post
- Length: 1,100 characters
- Mobile-optimized: Yes

**THE HOOK:**
Everyone's talking about [trend].
But here's what nobody mentions:

**CONTENT STRUCTURE:**
- Opening: Acknowledge the hype
- Body: 3 counterpoints with evidence
- Close: "The companies winning aren't chasing [trend]. They're..."
- White space throughout

**ENGAGEMENT CTA:**
"What's one industry 'best practice' you think is actually holding companies back?"

---

### COMPANY PAGE VERSION

**Approach:** Reshare with comment
**Comment:** "Our CEO shares a contrarian perspective on [trend]. What do you think?"
```

## Troubleshooting

**Issue: Can't find trending topics**
- Solution: Broaden search to adjacent industries
- Use general LinkedIn trending topics as backup
- Check what competitors are posting about

**Issue: Ideas feel generic**
- Solution: Reference founder's voice guide for authentic angle
- Include specific client stories, metrics, or examples
- Add contrarian perspective from their hot takes

**Issue: Compliance restrictions limit topics**
- Solution: Focus on educational content vs promotional
- Share industry trends without product claims
- Highlight team expertise instead of product features

**Issue: Company page version feels forced**
- Solution: Some posts are better as "Skip" for company page
- Personal/vulnerable content should stay on founder profile only
- Company page works best for reshares with brief comment

## References

- `references/LINKEDIN_STRATEGY_2025.md` - Algorithm data, benchmarks, format performance
- `references/LINKEDIN_BEST_PRACTICES.md` - Formatting and structure tips
- `references/HOOK_EXAMPLES.md` - Strong hook templates by type
- `references/CTA_BANK.md` - LinkedIn-specific calls-to-action by goal
- `references/CONTENT_PITFALLS.md` - Common mistakes to avoid
- `references/INDUSTRY_ADAPTATION.md` - **Industry-specific guidance** (topics, compliance, what works by industry)
- `references/CONTENT_REPURPOSING.md` - **How to turn one idea into multiple formats**
