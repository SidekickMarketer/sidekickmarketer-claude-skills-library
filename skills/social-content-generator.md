# Social Media Content Generator

**Skill Type:** Content Creation & Marketing Automation
**Version:** 1.0
**Created:** November 14, 2025
**Last Updated:** November 14, 2025
**Last Platform Audit:** November 14, 2025
**Next Platform Audit Due:** December 14, 2025 (30 days)

---

## Description

Generates monthly social media content calendars for Sidekick Marketer agency clients based on their brand strategy, monthly priorities, past performance, and SOW deliverables. This skill automates the Week 3 content planning workflow by analyzing client data and producing ready-to-publish social media posts.

---

## When to Use This Skill

Activate this skill when:
- User says "generate social content for [client]"
- User requests "create [month] social calendar for [client]"
- User needs monthly Instagram, Facebook, or GBP posts created
- It's Week 3 of the current month (content planning week)
- User says "social content generator" or references this skill by name

---

## Parameters

### Required:
- **client_name** (string): Full client name (e.g., "Cincinnati Music Academy")
- **month** (string): Target month for content (e.g., "December 2025")

### Optional:
- **platform** (string): Specific platform ("instagram", "facebook", "gbp", "all"). Default: "all"
- **count** (integer): Number of posts to generate. Uses SOW if not specified.
- **theme** (string): Special theme/focus for the month (e.g., "holiday enrollment", "back to school")

---

## Pre-Execution Freshness Check

**When skill activates, immediately perform freshness validation:**

### Step 0: Validate Skill Currency

1. **Calculate Skill Age**
   - Created: November 14, 2025
   - Last Updated: [CHECK FILE MODIFICATION DATE]
   - Today: [CURRENT_DATE]
   - Days since last update: [CALCULATE]

2. **Determine Freshness Status**

   **Trend Check (Always Required):**
   - ⏰ Last trend check: [LAST_UPDATE_DATE]
   - 🔍 Action: Always perform quick trend scan (2 min)

   **Feature Check:**
   - ✅ Green (0-30 days): Skip feature check, use existing knowledge
   - ⚠️ Yellow (31-60 days): Quick feature check recommended (5 min)
   - 🚨 Red (61-90 days): Feature audit required (10 min)
   - ❌ Critical (91+ days): STOP - Full platform audit required before use

   **Deep Audit:**
   - Recommended every 90 days
   - Includes: Algorithm changes, new best practices, workflow improvements

3. **Execute Required Checks**

   **If 0-30 days old:**
   ```
   ✅ Skill is current. Performing quick trend scan...
   → Web search: "[Platform] trends [current month] [year]"
   → Web search: "viral social media [current month]"
   → Proceed with generation
   ```

   **If 31-60 days old:**
   ```
   ⚠️ Skill is [X] days old. Running feature check...
   → Web search: "Instagram new features [year]"
   → Web search: "Facebook algorithm changes [year]"
   → Web search: "Google Business Profile updates [year]"
   → Update temporary feature notes
   → Proceed with generation
   ```

   **If 61-90 days old:**
   ```
   🚨 Skill is [X] days old. Platform audit required...
   → Comprehensive platform research (10 min)
   → Update all platform features sections
   → Document changes for permanent skill update
   → Ask user: "Audit complete. Continue with generation?"
   ```

   **If 91+ days old:**
   ```
   ❌ CRITICAL: Skill is [X] days old and may contain outdated practices.

   This skill should be manually updated before use. Options:
   1. Proceed anyway (not recommended - may use outdated features)
   2. Perform full platform audit now (15-20 min)
   3. Exit and schedule skill update

   User choice: [WAIT FOR INPUT]
   ```

---

## Data Sources

### From Google Drive:

1. **Client Strategy Document**
   - Path: `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-{slug}/{slug}_Social_Media_Strategy.md`
   - Alternative paths to check:
     - `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-{slug}/03 - Strategy Documents/`
     - `/My Drive/[CLIENT]_Social_Media_GBP_Strategy.md` (root level)
   - Contains: Content pillars, brand voice, posting frequency, templates
   - Fallback: Search for strategy docs in client folder

2. **Past Content Calendars**
   - Path: `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-{slug}/06_Social_Media/01_Content_Calendars/`
   - Alternative: Root level files like `CMA_Social_Content_Calendar_Sept2025.csv`
   - Purpose: Avoid duplicate content, understand what's been posted
   - Check last 3-6 months

3. **Client Intelligence Hub**
   - Path: `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-{slug}/cma notion audit/Client_Intelligence_Hub/CMA_CLIENT_HUB_POPULATED.md`
   - Contains: Target audience, brand voice, baseline metrics, competitive intel
   - Use for context and strategic alignment

### From Notion (when databases exist):

4. **Clients Database**
   - Fields needed: SOW deliverables, brand voice, strategy doc link
   - Query by client_name

5. **Monthly Priorities Database**
   - Fields needed: Events to promote, special offers, key dates
   - Filter by client + month

6. **Content Calendar Database**
   - Fields needed: Past posts, performance notes
   - Query last 3-6 months for client

7. **Performance Insights Database**
   - Fields needed: What worked, what didn't, top posts
   - Use to inform content strategy

---

## Workflow Steps

### Step 1: Gather Client Context (3-5 minutes)

**A. Load Strategy Document**
```
1. Try primary path: client-{slug}/{slug}_Social_Media_Strategy.md
2. If not found, check alternative paths
3. If still not found, search client folder for "*strategy*" or "*social*"
4. Extract:
   - Content pillars (with percentages)
   - Brand voice guidelines
   - Posting frequency per platform
   - Hashtag strategy
   - Content templates
   - Target audience segments
```

**B. Load Client Intelligence**
```
1. Check for CLIENT_HUB_POPULATED.md
2. If found, extract:
   - ICP/Target segments (WHO they're talking to)
   - Brand voice tone
   - What's currently working
   - Monthly priorities (if available)
3. If not found, rely on strategy doc only
```

**C. Review Past Content**
```
1. Check 06_Social_Media/01_Content_Calendars/ folder
2. Also check root Drive for scattered calendar files
3. Find last 2-3 months of content calendars
4. Identify:
   - Topics already covered (avoid duplication)
   - High-performing content types
   - Content gaps to fill
   - Seasonal patterns
```

---

### Step 1.5: Check Current Platform Best Practices (2-5 minutes)

**This step runs based on freshness check results from Step 0**

**A. Quick Trend Scan (ALWAYS - 2 minutes)**

Use WebSearch to identify:
```
1. "[Primary Platform] trends [current month] [year]"
   → Look for: Viral formats, trending audio, popular content types

2. "viral social media [current month] [year]"
   → Look for: Cross-platform trends, challenges, memes

3. "[Client Industry] social media trends [year]"
   → Look for: Industry-specific content that's working

4. "[Client Location] events [current month]"
   → Look for: Local happenings to reference
```

**B. Feature Check (IF NEEDED - 5 minutes)**

If skill >30 days old, verify current features:
```
Instagram:
- New post types or features?
- Reel length changes?
- Algorithm priority shifts?
- Hashtag best practices updated?

Facebook:
- Feed algorithm changes?
- New business tools?
- Video format updates?
- Group features?

Google Business Profile:
- New post types?
- Review features?
- Booking/messaging updates?
- Photo requirements?
```

**C. Integrate Findings Into Strategy**

Document discovered trends/features:
```
✅ Trending Format Found: [Description]
   → How to use: [Application for this client]
   → Examples: [2-3 post ideas]

✅ New Platform Feature: [Description]
   → Relevance: [High/Medium/Low]
   → Recommendation: [Use/Test/Skip]

✅ Algorithm Change: [Description]
   → Impact: [How it affects strategy]
   → Adjustment: [What to change]
```

**D. Set Content Strategy Adjustments**

Based on findings, note:
- Format priorities (e.g., "Prioritize Carousels this month - trending")
- Content types to increase/decrease
- New post ideas inspired by trends
- Platform-specific optimizations

---

### Step 2: Determine Monthly Priorities (2-3 minutes)

**Check for:**
- Upcoming events (recitals, workshops, open houses, classes)
- Seasonal themes (holidays, enrollment periods)
- Special promotions or offers
- New programs/services launching
- Industry-relevant dates

**Sources:**
- Monthly Priorities database (if exists)
- Past calendar patterns
- Client communications
- Industry calendar (back-to-school, holidays, etc.)
- **NEW:** Local events from trend scan

---

### Step 3: Calculate Post Distribution (1 minute)

**Based on SOW + Strategy:**

Example for CMA:
- 12 Instagram posts (3/week × 4 weeks)
- 4 Facebook posts (1/week × 4 weeks)
- 4 GBP posts (1/week × 4 weeks)

**Apply Content Pillar Percentages:**

For CMA (Instagram 12 posts):
- Student Success (30%): 4 posts
- Instructor Expertise (25%): 3 posts
- Educational Value (20%): 2 posts
- Community & Culture (15%): 2 posts
- Promotional (10%): 1 post

**Adjust for client-specific strategy if percentages differ**

---

### Step 4: Generate Content (10-15 minutes)

**For each post, create:**

1. **Date** - Spread evenly across month, respecting platform schedule
2. **Platform** - Instagram, Facebook, GBP
3. **Post Type** - Feed Post, Reel, Story, Carousel, Live, Event, etc.
4. **Content Theme** - Which pillar (Student Success, etc.)
5. **Caption** - 100-150 words, brand voice aligned, with emojis
6. **Hashtags** - 3-5 relevant hashtags (current best practice)
7. **CTA** - Clear call-to-action (link in bio, call now, DM us, etc.)
8. **Visual Notes** - Description of image/video needed

**Trend Integration:**

As you generate content, actively incorporate findings from Step 1.5:

```
✓ Trending format found?
  → Adapt 2-3 posts to use this format
  → Example: If "photo carousels" trending → Create "This Month at [Client]" carousel

✓ Viral audio found?
  → Suggest Reel using this audio
  → Example: Trending sound → "Get ready with me" instructor content

✓ Local event found?
  → Create timely post referencing it
  → Example: Cincinnati festival → "Festival prep tips from our instructors"

✓ Industry trend found?
  → Educational post opportunity
  → Example: New study on music education → Share insights + client perspective

✓ New platform feature?
  → Test it with 1-2 posts
  → Example: Instagram Notes → Quick practice tip of the day
```

**Quality Standards:**
- ✅ Match brand voice exactly (from strategy doc)
- ✅ Include specific details (instructor names, student stories)
- ✅ Vary post types (not all feed posts)
- ✅ Balance promotion with value content
- ✅ Use emojis naturally (not excessively)
- ✅ Include strong CTAs
- ✅ Make posts seasonally relevant
- ✅ NO duplicate topics from past 3 months
- ✅ Incorporate at least 2-3 current trends
- ✅ Use current best practices (3-5 hashtags, etc.)

---

### Step 5: Format Output (2 minutes)

**Generate CSV table with columns:**
```csv
Date,Platform,Post Type,Content Theme,Caption,Hashtags,CTA,Visual Notes,Trend Note
```

**Example Row:**
```csv
2025-12-01,Instagram,Carousel,Student Success,"🌟 STUDENT SPOTLIGHT: Emma's 6-month journey! Swipe to see her progress from first lesson to first recital. 'I was so nervous but Ms. Chen helped me feel confident!' Your journey starts here too! 🎹","#CMAStudents #PianoProgress #CincinnatiMusic","Link in bio to book your trial lesson","5-photo carousel: lesson 1, practice, rehearsal, performance, certificate","Carousel format trending - high engagement"
```

**Note the "Trend Note" column** - documents WHY this post format/topic was chosen based on current trends.

---

## Output Format

### Primary Deliverable: CSV Content Calendar

**Filename:** `{CLIENT_SLUG}_{MONTH}_{YEAR}_Social_Content_Calendar.csv`

**Example:** `CMA_December_2025_Social_Content_Calendar.csv`

**Save to:** `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-{slug}/06_Social_Media/01_Content_Calendars/`

**If folder doesn't exist:** Create it first, or save to root Drive and notify user

---

### Secondary Deliverable: Summary Document

**Create markdown summary including:**

```markdown
# [Client Name] - [Month Year] Social Content Calendar

**Generated:** [Date]
**Generated By:** Claude Social Content Generator v1.0
**Skill Last Updated:** [Skill update date]
**Trend Scan Performed:** Yes ([Date])
**Posts Created:** [Count by platform]

## Freshness & Trend Analysis

**Platform Updates Checked:**
- ✅ Quick trend scan performed
- ✅ Current best practices verified
- [List any new features/trends incorporated]

**Trending This Month:**
1. [Trend 1] - [How we used it]
2. [Trend 2] - [How we used it]
3. [Trend 3] - [How we used it]

## Calendar Overview

[Brief description of the month's content strategy, including how trends were incorporated]

## Platform Breakdown

### Instagram ([X] posts)
- Feed Posts: [Count]
- Reels: [Count]
- Carousels: [Count]
- Stories: [Count]

### Facebook ([X] posts)
- Photo Posts: [Count]
- Video Posts: [Count]
- Events: [Count]

### Google Business Profile ([X] posts)
- What's New: [Count]
- Offers: [Count]
- Events: [Count]

## Content Pillar Distribution

- [Pillar 1]: [X] posts ([X]%)
- [Pillar 2]: [X] posts ([X]%)
- [Pillar 3]: [X] posts ([X]%)
- [Pillar 4]: [X] posts ([X]%)
- [Pillar 5]: [X] posts ([X]%)

## Key Themes This Month

1. [Theme 1] - [Dates] - [Why relevant]
2. [Theme 2] - [Dates] - [Why relevant]
3. [Theme 3] - [Dates] - [Why relevant]

## Trend Integration Strategy

**Format Innovations:**
- [New format 1]: Used in posts [X, Y, Z]
- [New format 2]: Used in posts [A, B, C]

**Timely Content:**
- [Local event]: Post on [date]
- [Trending topic]: Post on [date]

**Platform Optimizations:**
- [Optimization 1]: Applied to [posts]
- [Optimization 2]: Applied to [posts]

## Next Steps

1. Review and approve calendar
2. Begin content creation (photos/videos)
   - Priority: [List trending format content first]
3. Schedule posts in [scheduling tool]
4. Monitor engagement and adjust
5. Note which trend-based posts perform best

## Notes for Content Team

### Must-Have Visuals:
[List specific photo/video requirements, prioritizing trending formats]

### Trending Audio/Music:
[If Reels included, list specific trending audio to use]

### Special Considerations:
[Any unique requirements for this month's content]

## Performance Tracking

**Track These Specifically:**
- Engagement on trend-based posts vs standard posts
- Carousel performance (if trending format)
- Reel performance with trending audio
- New feature adoption (if tested)

Compare to previous months to validate trend integration effectiveness.
```

**Filename:** `{CLIENT_SLUG}_{MONTH}_{YEAR}_Content_Summary.md`

---

## Current Platform Features & Best Practices

**Last Platform Audit:** November 14, 2025
**Next Audit Due:** December 14, 2025 (30 days)

### Instagram (as of November 2025)

**Priority Features:**
- Reels: Max 90 sec, trending audio crucial, highest reach
- Carousels: 1.4x more engagement than single images
- Stories: 24hr, use polls/questions/quizzes for engagement
- Broadcast Channels: Creator-to-follower updates (test with VIP audiences)
- Notes: Quick text updates (60 chars) - good for quick tips

**Algorithm Priorities (Nov 2025):**
- Watch time & completion rate (Reels)
- Saves > likes (indicates valuable content)
- Shares (highest signal of quality)
- Original content over reposts
- Consistent posting schedule
- Early engagement (first hour crucial)

**Current Best Practices:**
- Post 3-5 Reels/week for maximum reach
- Use 3-5 hashtags only (down from 30 - algorithm change)
- Carousel posts get highest engagement
- Post when audience most active (check Insights)
- Mix feed posts with Reels (70/30 split)
- First 3 seconds of Reels = hook or skip
- Use closed captions on all video

**Hashtag Strategy:**
- 3-5 hashtags maximum
- Mix: 1 broad, 2 niche, 1-2 branded
- Avoid banned/spam hashtags
- Test different combos, track which drive discovery

---

### Facebook (as of November 2025)

**Priority Features:**
- Native video (prioritized in feed)
- Groups for community building
- Events (essential for local businesses)
- Live video (reach boost)

**Algorithm Priorities (Nov 2025):**
- Meaningful interactions (comments > reactions > likes)
- Content from friends/family > pages (harder for businesses)
- Video completion rate
- Local content for local businesses
- Group activity

**Current Best Practices:**
- Native video > YouTube links
- Ask questions to drive comments
- Go Live monthly for algorithmic boost
- Create/use Groups for community
- All events should be Facebook Events
- Post when parents/decision-makers online
- Longer captions work (people expect depth)

---

### Google Business Profile (as of November 2025)

**Priority Features:**
- Posts (updates, offers, events, products)
- Q&A section
- Messaging
- Product/service catalog
- Review management

**Ranking Factors (Nov 2025):**
- Review quantity & recency (most important)
- Review response rate & speed (100% within 24hrs)
- Photo uploads (minimum 3 every 7 days)
- Post frequency (minimum weekly)
- Profile completeness (100%)

**Current Best Practices:**
- Post 2-4x/week minimum
- Respond to ALL reviews within 24 hours
- Upload 3+ photos weekly
- Answer all Q&A questions publicly
- Enable messaging, respond quickly
- Complete every field in profile

---

## Quality Checklist

Before delivering content, verify:

**Content Quality:**
- [ ] All posts align with client's brand voice
- [ ] Content pillar percentages match strategy
- [ ] No duplicate topics from past 3 months
- [ ] All posts have strong CTAs
- [ ] Hashtags follow current best practices (3-5)
- [ ] Visual notes are specific and actionable
- [ ] Platform posting frequencies match SOW
- [ ] Seasonal/monthly priorities addressed
- [ ] Posts spread evenly across month
- [ ] Mix of post types (not just feed posts)
- [ ] Grammar and spelling are perfect
- [ ] CSV format is clean and importable

**Trend Integration:**
- [ ] Trend scan performed and documented
- [ ] At least 2-3 current trends incorporated
- [ ] Trending formats included (if relevant)
- [ ] Local/timely content included
- [ ] New platform features tested (if applicable)
- [ ] Trend notes documented for each trend-based post

**Technical:**
- [ ] File saved to correct Google Drive location
- [ ] Summary document created
- [ ] Trend analysis included in summary
- [ ] Performance tracking recommendations provided

---

## Skill Maintenance Schedule

### Every 7 Days (Trend Check):
- Performed automatically when skill runs
- Quick web search for current trends
- 2-3 minutes per execution
- No manual update needed

### Every 30 Days (Feature Check):
- [ ] Review Instagram/Facebook/GBP for new features
- [ ] Update "Current Platform Features" section if changes found
- [ ] Test skill with real client
- [ ] Document any issues

**Next Feature Check:** December 14, 2025

### Every 90 Days (Full Platform Audit):
- [ ] Comprehensive platform research
- [ ] Update algorithm priorities section
- [ ] Update all best practices
- [ ] Review workflow efficiency
- [ ] Gather user feedback
- [ ] Version number update if major changes

**Next Full Audit:** February 14, 2026

### Trigger Immediate Update If:
- ⚠️ Major platform algorithm change announced
- ⚠️ New critical feature launched
- ⚠️ Skill producing consistently outdated recommendations
- ⚠️ User reports pattern of issues

---

## Example Usage

### Basic Usage:
```
User: "Generate December social content for Cincinnati Music Academy"

Skill executes:
→ Step 0: Freshness check (performs trend scan)
→ Step 1: Reads CMA_Social_Media_GBP_Strategy.md
→ Step 1: Reads CMA_CLIENT_HUB_POPULATED.md
→ Step 1: Reviews Sept/Oct/Nov content calendars
→ Step 1.5: Web searches for December trends, holiday content ideas
→ Step 2: Identifies December priorities (holidays, winter enrollment)
→ Step 3: Calculates 12 IG + 4 FB + 4 GBP = 20 posts
→ Step 4: Generates all 20 posts, incorporating trends
→ Step 5: Creates CSV file + summary doc
→ Saves to Google Drive

Output:
"✅ Generated December 2025 content calendar for CMA:
- 12 Instagram posts (4 Reels, 5 Carousels, 3 Feed)
- 4 Facebook posts
- 4 GBP posts

Trend Integration:
✓ Holiday countdown carousel (trending format)
✓ Year-in-review Reel (seasonal trend)
✓ Gift guide for musicians (holiday theme)

Saved to: [path]"
```

---

## Error Handling

**Missing client folder:**
```
Error: Client folder not found for "{client_name}"

Suggestions:
- Check client name spelling
- Verify client slug format
- Available clients: [list folders in 01_Clients]
```

**No strategy data:**
```
Warning: No strategy document found. Proceeding with limited context.

Recommendations:
1. Review output carefully
2. Provide monthly priorities manually
3. Create strategy document for future

Continue? (y/n)
```

**Skill too old:**
```
⚠️ This skill was last updated [X] days ago.

Options:
1. Perform platform audit now (10-15 min)
2. Proceed with current knowledge
3. Exit and update manually

Your choice: [1/2/3]
```

---

## Notes for Claude

**When this skill is activated:**

1. **Always start with Step 0** - Freshness check is mandatory
2. **Be thorough** - Gather all context before generating
3. **Be current** - Always perform trend scan
4. **Be creative** - Craft engaging stories, not just templates
5. **Be specific** - Use real names, programs, events
6. **Be strategic** - Align with business goals
7. **Be consistent** - Match brand voice precisely
8. **Ask questions** - Clarify before proceeding

**Remember:**
- Balance trending content (reach) with evergreen content (value)
- Don't force trends that don't fit the brand
- Document trends used for performance tracking
- Save outputs to proper locations
- Update "Last Platform Audit" date if you perform checks

---

**Skill Status:** ✅ Ready for Testing
**Version:** 1.0
**Created:** November 14, 2025
**Maintained By:** Sidekick Marketer Operations Team

---

## Version History

### v1.0 (November 14, 2025)
- Initial release
- Tiered freshness checking (7/30/90 days)
- Automatic trend scanning
- Platform best practices (Instagram, Facebook, GBP)
- CMA-tested workflow
- CSV + markdown summary output
