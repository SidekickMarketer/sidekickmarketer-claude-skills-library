# Social Media Strategy Audit Skill

**Version:** 1.0
**Created:** November 21, 2025
**Purpose:** Analyze existing social media strategy and execution to identify gaps, patterns, and optimization opportunities
**Use Case:** Run before automating content generation to validate strategy is optimal
**Scope:** Social Media ONLY (Instagram, Facebook, TikTok, LinkedIn, GBP, etc.)

⚠️ **Note:** This skill audits ONLY social media channels. For paid ads, email, or SEO audits, use separate channel-specific skills.

---

## 📋 Description

This skill performs a comprehensive audit of a client's **social media strategy** by analyzing:
- Stated strategy vs actual execution
- Content pillar distribution
- Platform mix and posting frequency
- Template and format effectiveness
- Performance patterns (if analytics available)
- SOW compliance

**Output:** Data-driven audit report with specific recommendations and questions for the client.

---

## 🎯 When to Use This Skill

**Primary Use Cases:**
1. **New client onboarding** - Before creating first content calendar
2. **Strategy validation** - Before automating content generation
3. **Quarterly reviews** - Check if execution matches strategy
4. **Performance troubleshooting** - Understand what's not working
5. **Client handoff** - Audit inherited accounts

**Trigger Phrases:**
- "Audit [Client Name]'s social media strategy"
- "Social media strategy audit for [Client Name]"
- "Analyze [Client Name]'s social content performance"
- "Review [Client Name]'s social media execution"
- "Validate social strategy for [Client Name]"

---

## 📥 Required Inputs

### 1. Client Name (Required)
**Parameter:** `client_name`
**Example:** "Cincinnati Music Academy" or "CMA"

### 2. Data Sources (Auto-Located)

**Client Profile:**
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-[name]/00_[Client]_CLIENT_PROFILE.md
```
**Contains:** Brand voice, content pillars, SOW deliverables, KPIs

**Strategy Document:**
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-[name]/06_Social_Media/00_Strategy/Social_Strategy.md
```
**Contains:** Full social media strategy, templates, posting schedule

**Historical Content:**
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-[name]/06_Social_Media/01_Content_Calendars/
```
**Contains:** Past content calendars (CSV or markdown format)

**Performance Data (Optional):**
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-[name]/06_Social_Media/02_Performance_Data/
```
**Contains:** Analytics exports, engagement metrics

---

## 🔄 Workflow

### Step 1: Locate and Read Data (2-3 minutes)

**Actions:**
1. Find client folder using client name parameter
2. Read `00_[Client]_CLIENT_PROFILE.md`
   - Extract: Content pillars, SOW deliverables, posting schedule
3. Read strategy document(s) in `/00_Strategy/`
   - Extract: Templates, brand voice, platform focus
4. List all files in `/01_Content_Calendars/`
   - Identify date range of historical data
5. Check if performance data exists in `/02_Performance_Data/`

**Handle Missing Data:**
- If no Client Profile: Note as gap, proceed with available data
- If no Strategy: Flag as critical gap, analyze calendars only
- If no Historical Content: Cannot perform audit, exit gracefully
- If no Performance Data: Audit based on content only, note limitation

---

### Step 2: Analyze Strategy Documents (3-4 minutes)

**Extract from Client Profile & Strategy:**

**A. Intended Content Pillars:**
```
Example:
- Student Success: 30%
- Instructor Expertise: 25%
- Educational Value: 20%
- Community & Culture: 15%
- Promotional: 10%
```

**B. SOW Requirements:**
```
Example:
- Instagram: 12 posts/month
- Facebook: 4 posts/month
- GBP: 4 posts/month
- Reels: 1 per month
Total: 21 posts/month
```

**C. Brand Voice & Templates:**
- Voice description
- Available templates
- Content themes to emphasize

**D. Target KPIs:**
- Engagement rate targets
- Growth targets
- Conversion goals

---

### Step 3: Analyze Historical Content (5-7 minutes)

**Read all available content calendars** (typically 2-6 files)

**For each calendar, extract:**

**A. Post Count by Platform:**
```
May 2025:
- Instagram: 12 posts
- Facebook: 5 posts
- GBP: 4 posts
Total: 21 posts ✅ (matches SOW)
```

**B. Content Theme Distribution:**
Categorize each post into content pillars based on:
- Post title/content theme column
- Caption analysis
- Topic keywords

```
May 2025 Analysis:
- Student Success: 8 posts (38%) - Target: 30%
- Instructor Expertise: 6 posts (29%) - Target: 25%
- Educational: 3 posts (14%) - Target: 20%
- Community: 2 posts (10%) - Target: 15%
- Promotional: 2 posts (10%) - Target: 10%
```

**C. Post Type Distribution:**
```
- Feed posts: 15
- Reels: 1
- Stories: (not in calendar)
- Carousels: 4
```

**D. Template Usage:**
Identify which templates were used:
- Student Spotlight: 3 times
- Instructor Feature: 4 times
- Practice Tips: 2 times
- Event posts: 6 times
- Custom: 6 times

**E. Content Variety:**
- How many times was each theme repeated?
- Any over-saturation of specific topics?
- Balance of promotional vs value content?

---

### Step 4: Analyze Performance Data (3-5 minutes) [OPTIONAL]

**If analytics exports exist:**

**A. Top Performers:**
- Identify top 5-10 posts by:
  - Engagement rate
  - Reach
  - Click-through rate
  - Saves/shares

**B. Bottom Performers:**
- Identify lowest 5-10 posts
- Look for patterns (format, theme, time, platform)

**C. Pattern Recognition:**
```
High Engagement:
- Real student videos: 5.2% avg engagement
- Carousel posts: 4.1% avg
- Instructor spotlights: 2.8% avg

Low Engagement:
- Educational tips (text): 1.1% avg
- Promotional posts: 0.9% avg
- Generic quotes: 0.7% avg
```

**D. Platform Performance:**
- Which platform gets best engagement?
- Should allocation be adjusted?

**E. Timing Patterns:**
- Best performing days/times
- Compare to stated posting schedule

---

### Step 5: Compare Actual vs Intended (2-3 minutes)

**Create comparison tables:**

### Content Pillar Alignment
| Pillar | Target % | Actual % | Variance | Status |
|--------|----------|----------|----------|--------|
| Student Success | 30% | 38% | +8% | ⚠️ Over |
| Instructor | 25% | 29% | +4% | ✅ Close |
| Educational | 20% | 14% | -6% | ⚠️ Under |
| Community | 15% | 10% | -5% | ⚠️ Under |
| Promotional | 10% | 10% | 0% | ✅ Perfect |

### SOW Compliance
| Deliverable | Required | Actual | Status |
|-------------|----------|--------|--------|
| Instagram posts | 12/month | 12 | ✅ |
| Facebook posts | 4/month | 5 | ⚠️ Over |
| GBP posts | 4/month | 4 | ✅ |
| Reels | 1/month | 1 | ✅ |

### Platform Distribution
| Platform | Target % | Actual % | Variance |
|----------|----------|----------|----------|
| Instagram | 57% | 57% | ✅ Match |
| Facebook | 19% | 24% | ⚠️ +5% |
| GBP | 19% | 19% | ✅ Match |

---

### Step 6: Identify Patterns & Insights (3-4 minutes)

**Look for:**

**A. Over-saturations:**
- Topics repeated too frequently
- Same template used back-to-back
- Lack of content variety

**B. Gaps:**
- Pillars significantly under-represented
- Missing content types (e.g., no Reels despite SOW)
- Seasonal opportunities missed

**C. Inconsistencies:**
- Brand voice deviations
- Off-strategy content
- Platform mismatches (e.g., long captions on Facebook)

**D. Performance Patterns (if data available):**
- What works: "Student performance videos consistently get 5x engagement"
- What doesn't: "Educational carousel posts underperform by 60%"
- Platform insights: "Instagram Reels outperform static posts 3:1"

**E. Template Effectiveness:**
- Which templates are overused?
- Which are underutilized?
- Are templates still fresh or becoming stale?

---

### Step 7: Generate Recommendations (3-5 minutes)

**Create actionable recommendations in 3 categories:**

**1. Immediate Adjustments (This Month):**
```
- Reduce Student Success posts from 38% to target 30%
- Add 2 more Educational posts to reach 20% target
- Increase Community content (currently 10%, target 15%)
- Introduce new template to add variety
```

**2. Strategic Considerations (Next Quarter):**
```
- Performance data shows video outperforms static 3:1
  → Recommendation: Increase Reels from 1/month to 3/month
- Educational posts have low engagement but may serve SEO purpose
  → Question: Should we optimize for engagement or maintain for SEO?
- Adult learner content performing well
  → Recommendation: Consider dedicating 1 week/month to adult focus
```

**3. Questions for Client:**
```
1. Are you satisfied with current student spotlight frequency (38% vs 30% target)?
2. Do educational posts serve a purpose beyond engagement (e.g., SEO, authority)?
3. Should we shift resources from Facebook (over-delivering) to Instagram Reels?
4. Are there upcoming campaigns/events we should plan content around?
5. Has your target audience or business priorities shifted since strategy was created?
```

---

### Step 8: Output Audit Report (2-3 minutes)

**Generate comprehensive markdown report:**

---

## 📤 Output Format

```markdown
# [CLIENT NAME] - Social Media Strategy Audit
**Audit Date:** [Current Date]
**Analysis Period:** [Date Range of Historical Content]
**Data Sources:** [List what was analyzed]
**Analyst:** Claude via Strategy Audit Skill

---

## Executive Summary

**Overall Assessment:** [Green/Yellow/Red flag with 2-3 sentence summary]

**Key Findings:**
- [3-5 bullet points of most important discoveries]

**Top Recommendation:**
- [The #1 thing to change or focus on]

---

## 📊 Strategy vs Execution Analysis

### Content Pillar Distribution

**Intended Strategy:**
- Student Success: 30%
- Instructor Expertise: 25%
- Educational Value: 20%
- Community & Culture: 15%
- Promotional: 10%

**Actual Execution (Aggregated):**
| Pillar | Target | Actual | Variance | Status |
|--------|--------|--------|----------|--------|
| [Pillar] | [%] | [%] | [+/- %] | [✅/⚠️/🔴] |

**Analysis:**
[2-3 paragraphs explaining variances and what they mean]

---

### SOW Compliance

| Deliverable | Required | Actual Avg | Status | Notes |
|-------------|----------|------------|--------|-------|
| [Platform] | [#] | [#] | [✅/⚠️] | [Comment] |

**Analysis:**
[Is client getting what they're paying for? Any over/under delivery?]

---

### Platform Mix Analysis

| Platform | Target Posts | Actual Avg | % of Total | Recommendation |
|----------|--------------|------------|------------|----------------|
| [Platform] | [#] | [#] | [%] | [Action] |

**Analysis:**
[Is platform allocation optimal based on strategy and performance?]

---

## 🎭 Content Effectiveness

### Template Usage Analysis

| Template | Times Used | Avg Engagement* | Status | Recommendation |
|----------|------------|----------------|--------|----------------|
| [Template] | [#] | [% or N/A] | [Fresh/Stale] | [Keep/Refresh/Retire] |

*If performance data available

**Analysis:**
[Are templates working? Getting stale? Need new ones?]

---

### Content Variety & Freshness

**Topic Repetition:**
- [Topic]: Appeared [X] times in [Y] months
- [Topic]: Appeared [X] times in [Y] months

**Assessment:**
[Good variety / Getting repetitive / Needs more diversity]

**Format Distribution:**
- Feed posts: [%]
- Reels: [%]
- Carousels: [%]
- Stories: [%]

**Assessment:**
[Balanced / Over-reliant on [format] / Should experiment more with [format]]

---

## 📈 Performance Insights
[ONLY IF ANALYTICS DATA AVAILABLE]

### Top Performing Content

**Top 5 Posts:**
1. [Post theme] - [Platform] - [Engagement %] - [Date]
2. [Post theme] - [Platform] - [Engagement %] - [Date]
3. [etc.]

**Common Patterns in Top Performers:**
- [Pattern 1]
- [Pattern 2]
- [Pattern 3]

---

### Bottom Performing Content

**Bottom 5 Posts:**
1. [Post theme] - [Platform] - [Engagement %] - [Date]
2. [etc.]

**Common Patterns in Poor Performers:**
- [Pattern 1]
- [Pattern 2]
- [Pattern 3]

---

### Platform Performance Comparison

| Platform | Avg Engagement | Reach | Best Content Type | Recommendation |
|----------|----------------|-------|-------------------|----------------|
| [Platform] | [%] | [#] | [Type] | [Action] |

---

## 🎯 Brand Voice & Positioning

**Stated Brand Voice:** [From strategy document]

**Observed Execution:**
- [How well does actual content match intended voice?]
- [Any inconsistencies or deviations?]
- [Examples of on-brand vs off-brand content]

**Assessment:** [Strong alignment / Some drift / Needs recalibration]

---

## 🚩 Gaps & Over-Saturations

### Content Gaps Identified:
1. **[Gap Area]**
   - Current: [What's happening]
   - Should be: [What strategy says]
   - Impact: [Why this matters]
   - Fix: [Specific action]

2. [etc.]

### Over-Saturations Identified:
1. **[Over-saturated Area]**
   - Current: [What's happening]
   - Should be: [What strategy says]
   - Impact: [Why this matters]
   - Fix: [Specific action]

2. [etc.]

---

## 💡 Recommendations

### 🔴 High Priority (Implement This Month)
1. **[Recommendation]**
   - Why: [Reasoning]
   - Action: [Specific steps]
   - Impact: [Expected result]

2. [etc.]

### 🟡 Medium Priority (Next Quarter)
1. **[Recommendation]**
   - Why: [Reasoning]
   - Action: [Specific steps]
   - Impact: [Expected result]

2. [etc.]

### 🟢 Low Priority (Consider Long-Term)
1. **[Recommendation]**
   - Why: [Reasoning]
   - Action: [Specific steps]
   - Impact: [Expected result]

2. [etc.]

---

## ❓ Questions for Client

**Strategy Validation:**
1. [Question about strategic direction]
2. [Question about priorities]

**Execution Preferences:**
3. [Question about content mix]
4. [Question about posting frequency]

**Performance & Goals:**
5. [Question about success metrics]
6. [Question about audience feedback]

---

## 📋 Next Steps

**Before Generating New Content:**
1. [ ] Review this audit with client
2. [ ] Get answers to questions above
3. [ ] Update Client Profile document with any changes
4. [ ] Update Strategy document if needed
5. [ ] Document any new priorities in Notion

**Then:**
6. [ ] Run Social Content Generator skill with validated strategy
7. [ ] Review first month's output with client
8. [ ] Adjust based on feedback
9. [ ] Schedule next audit for [3 months from now]

---

## 📊 Audit Metadata

**Data Analyzed:**
- Client Profile: [Yes/No - File path]
- Strategy Document: [Yes/No - File path]
- Content Calendars: [List files analyzed]
- Performance Data: [Yes/No - If yes, list files]

**Analysis Period:**
- Start: [Earliest content date]
- End: [Latest content date]
- Total Months: [#]
- Total Posts Analyzed: [#]

**Limitations:**
- [Any missing data or constraints that affected analysis]

**Confidence Level:** [High/Medium/Low based on data availability]

---

**Generated by:** Claude Strategy Audit Skill v1.0
**Date:** [Timestamp]
```

---

## 🔍 Quality Checks

Before finalizing report:

1. ✅ **Data Accuracy:**
   - All percentages add to 100%
   - All counts match source data
   - No calculation errors

2. ✅ **Completeness:**
   - All sections filled out
   - No [TBD] or placeholder text
   - Specific examples provided

3. ✅ **Actionability:**
   - Recommendations are specific, not vague
   - Questions are open-ended and strategic
   - Prioritization is clear (High/Med/Low)

4. ✅ **Objectivity:**
   - Based on data, not assumptions
   - Notes limitations where data is missing
   - Provides balanced view (good + areas to improve)

---

## 💾 Save Output

**Save report to:**
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-[name]/06_Social_Media/[ClientName]_Strategy_Audit_[Date].md
```

**Also notify user:**
"Strategy audit complete! Report saved to: [file path]"

---

## 🔄 Maintenance

**Update Frequency:** Skill should be reviewed/updated every 90 days

**Next Review:** February 21, 2026

**Version History:**
- v1.0 (Nov 21, 2025) - Initial release

---

**END OF SKILL**
