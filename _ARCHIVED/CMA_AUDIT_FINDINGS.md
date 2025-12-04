# Cincinnati Music Academy - System Audit Findings
**Date:** November 10, 2025
**Purpose:** Audit current setup to design Claude Skills for social media automation

---

## Executive Summary

Cincinnati Music Academy has a **partially organized** system with valuable data scattered across multiple locations. **Good foundation exists** but needs consolidation and standardization to enable Claude Skills automation.

### Key Findings:
✅ **What's Working:** Rich historical data, clear strategy document, detailed content calendars
⚠️ **Needs Work:** Data scattered across multiple locations, no centralized content repository
❌ **Missing:** Structured Notion databases, organized past post archive, performance tracking system

---

## 1. Current Google Drive Structure

### Main Client Folder
```
/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/
├── 01 - Admin & Legal/
│   ├── Agreement And SOW/
│   ├── ChatGPT Knowledge/
│   └── Proposal/
├── 02 - Onboarding & Access/
├── 03 - Brand & Assets/
│   ├── Assets/
│   │   ├── 01_Brand/
│   │   ├── 02_Photos/
│   │   └── 03_Graphics/
│   ├── Photos/
│   └── Website Photos/
├── 04 - Marketing Deliverables/
│   └── Ads Hub/ (Google Ads, Meta Ads)
├── 05 - Reports & Analytics/
│   ├── 01_Discovery Phase/
│   │   └── Social Media and GBP/ (Agency Analytics exports)
│   │       ├── 01_Jan 2025/
│   │       ├── 02_Feb 2025/
│   │       ├── 03_March 2025/
│   │       ├── 04_April 2025/
│   │       ├── 05_May 2025/
│   │       ├── 06_June 2025/
│   │       ├── 07_July 2025/
│   │       └── 08_August 2025/
│   └── 02_Monthly Reports/
│       ├── September 2025/
│       └── October 2025/
├── 06 - Extracted Data/
├── 08 - Handoff/
└── Archive/
```

### Root Drive Files (Scattered)
```
/My Drive/
├── CMA_Social_Content_Calendar_Sept2025.csv ⚠️ Should be in client folder
├── CMA_Social_Media_GBP_Strategy.md ⚠️ Should be in client folder
├── CMA_May2025_Content_Calendar.csv ⚠️ Should be in client folder
├── CMA_May2025_FinalContentCalendar_EmojiEnhanced.csv ⚠️ Should be in client folder
├── CMA_BulkCSV_May2025_Final.csv ⚠️ Should be in client folder
└── cma_may2025_bulk.csv ⚠️ Duplicate
```

---

## 2. Data Inventory

### ✅ What Exists

#### Social Media Strategy
**Location:** `/My Drive/CMA_Social_Media_GBP_Strategy.md`

**Contents:**
- Platform focus (Instagram, Facebook, GBP primary)
- Content pillars (Student Success 30%, Instructor Expertise 25%, Educational 20%, Community 15%, Promotional 10%)
- Posting schedule (IG 4-5/week, FB 3-4/week)
- Content templates
- Best posting times

**Status:** ✅ **Excellent foundation** - Very detailed and well-thought-out

#### Content Calendars
**Locations:**
- `CMA_Social_Content_Calendar_Sept2025.csv` (September 2025)
- `CMA_May2025_Content_Calendar.csv` (May 2025)
- `CMA_May2025_FinalContentCalendar_EmojiEnhanced.csv` (May 2025 Enhanced)

**Format:**
```csv
Date,Platform,Post Type,Content Theme,Caption,Hashtags,CTA,Visual Notes
2025-09-01,Instagram,Feed Post,Back to School,"...",".","..","..."
```

**Status:** ✅ **Good structure** - Clear format, detailed content

#### Agency Analytics Exports
**Location:** `/client-cma/05 - Reports & Analytics/01_Discovery Phase/Social Media and GBP/`

**Monthly folders:** Jan 2025 through August 2025

**File formats per month:**
- Facebook: PDF + XLSX
- Instagram: PDF + XLSX
- Google Business Profile: PDF + XLSX

**Status:** ✅ **Complete history** - 8 months of performance data available

#### SOW Documentation
**Location:** `/client-cma/01 - Admin & Legal/Agreement And SOW/`

**Documents:**
- Phase 1 Project Agreement
- Phase 2 Project Agreement
- Signed agreements (PDFs)

**Expected Deliverables (from SOW):**
- 12 Instagram posts/month
- 4 Facebook posts/month
- 4 Google Business Profile posts/month
- 1 Reel/month

**Status:** ✅ **Documented** - Clear scope of work

#### Brand Assets
**Location:** `/client-cma/03 - Brand & Assets/`

**Contents:**
- Logos (multiple formats)
- Brand guide
- Photos (student photos, website photos)
- Graphics
- Stock assets

**Status:** ✅ **Well organized** - Assets available for content creation

---

### ❌ What's Missing

#### 1. **Centralized Social Media Content Folder**
**Problem:** Content calendars are in root Drive, not in client folder
**Impact:** Hard to find, not organized with other CMA materials
**Needed:** `/client-cma/Social_Media_Content/` folder structure

#### 2. **No September+ Analytics Exports**
**Problem:** Agency Analytics exports end at August 2025
**Impact:** Can't analyze recent performance (Sept-Nov)
**Needed:** Continue monthly exports OR transition to Looker Studio

#### 3. **Past Posts Archive**
**Problem:** No archive of what was actually posted with performance data
**Impact:** Can't easily reference what worked/didn't work
**Needed:** Database linking posts to performance

#### 4. **Monthly Priorities/Promotions Tracking**
**Problem:** No clear place where "what to promote this month" is documented
**Impact:** Have to hunt for this information
**Needed:** Monthly priorities document or database

#### 5. **Content Performance Insights**
**Problem:** Raw analytics exist, but no synthesis of "what we learned"
**Impact:** Can't feed learnings back into content creation
**Needed:** Performance notes/insights document

#### 6. **Structured Notion Databases**
**Problem:** Unknown if CMA data exists in Notion (can't access via MCP)
**Impact:** Can't query/update Notion programmatically
**Needed:** Verify Notion setup and create databases if needed

---

## 3. Current Workflow (Inferred)

### Content Creation Process
1. Review strategy document
2. Check SOW deliverables (12 IG + 4 FB + 4 GBP + 1 reel)
3. Identify what to promote this month (source unclear)
4. Create content calendar CSV manually
5. Enhance with emojis and refinements
6. Generate bulk CSV for scheduling
7. Post content to platforms

### Reporting Process
1. Export from Agency Analytics (monthly)
2. Save PDFs + XLSX by platform
3. Create monthly report (stored in `/02_Monthly Reports/`)
4. Present to client

---

## 4. Gap Analysis

### For Content Generation Skill

| Required Input | Current Status | Location | Issue |
|----------------|----------------|----------|-------|
| **Strategy/Goals** | ✅ Exists | CMA_Social_Media_GBP_Strategy.md | In root Drive (should move) |
| **SOW Requirements** | ✅ Exists | Agreement documents | Documented (12 IG, 4 FB, 4 GBP, 1 reel) |
| **Monthly Priorities** | ❌ Missing | Unknown | Need structured input |
| **Past Posts** | ⚠️ Partial | Content calendar CSVs | Only May & Sept available |
| **Performance Data** | ✅ Exists | Agency Analytics exports | Jan-Aug 2025 |
| **Brand Voice** | ✅ Exists | Strategy doc + past posts | Available |
| **Visual Assets** | ✅ Exists | Brand & Assets folder | Well organized |

### For Reporting Skill

| Required Input | Current Status | Location | Issue |
|----------------|----------------|----------|-------|
| **Platform Metrics** | ⚠️ Partial | Agency Analytics exports | Ends Aug 2025 |
| **Posted Content** | ⚠️ Partial | Content calendar CSVs | Not all months |
| **Goals/Benchmarks** | ❓ Unknown | Unknown | Need to verify |
| **Previous Insights** | ❌ Missing | None | No running log |

---

## 5. Recommended Folder Structure

### Proposed New Structure
```
/client-cma/
├── 01_Admin_Legal/ (keep as-is)
├── 02_Onboarding_Access/ (keep as-is)
├── 03_Brand_Assets/ (keep as-is)
├── 04_Marketing_Deliverables/ (keep as-is)
├── 05_Reports_Analytics/
│   ├── Agency_Analytics_Exports/ (rename from Discovery Phase)
│   │   └── [Monthly folders by YYYY-MM format]
│   ├── Monthly_Reports/
│   │   └── [Monthly folders]
│   └── Performance_Insights/
│       └── insights_log.md (NEW - cumulative learnings)
├── 06_Social_Media/ (NEW)
│   ├── 01_Strategy/
│   │   ├── CMA_Social_Media_GBP_Strategy.md (move from root)
│   │   └── monthly_priorities/ (NEW)
│   │       ├── 2025-09_September_Priorities.md
│   │       ├── 2025-10_October_Priorities.md
│   │       └── 2025-11_November_Priorities.md
│   ├── 02_Content_Calendars/
│   │   ├── 2025-05_May_Content_Calendar.csv (move from root)
│   │   ├── 2025-09_September_Content_Calendar.csv (move from root)
│   │   ├── 2025-10_October_Content_Calendar.csv (CREATE)
│   │   ├── 2025-11_November_Content_Calendar.csv (CREATE)
│   │   └── 2025-12_December_Content_Calendar.csv (CREATE)
│   ├── 03_Generated_Content/
│   │   ├── 2025-11_November/ (bulk CSVs, formatted posts)
│   │   └── 2025-12_December/
│   ├── 04_Posted_Content_Archive/
│   │   ├── 2025-09_September_Posted.csv (what actually went live)
│   │   └── 2025-10_October_Posted.csv
│   └── 05_Templates/
│       ├── student_spotlight_template.md
│       ├── instructor_feature_template.md
│       └── promotion_template.md
├── 07_Extracted_Data/ (keep as-is)
└── 08_Archive/ (keep as-is)
```

---

## 6. Notion Database Recommendations

### Database 1: CMA Client Profile

**Purpose:** Store strategy, SOW, and client-specific information

**Properties:**
- Client Name (Title): "Cincinnati Music Academy"
- Brand Voice (Text): "Friendly, educational, community-focused"
- Target Audience (Text): "Parents of children 5-18, adult learners"
- Primary Platforms (Multi-select): Instagram, Facebook, GBP
- SOW - IG Posts (Number): 12
- SOW - FB Posts (Number): 4
- SOW - GBP Posts (Number): 4
- SOW - Reels (Number): 1
- Strategy Document Link (URL): Link to strategy doc
- Drive Folder Path (Text): Path to client folder
- Account Manager (Person): Your name
- Status (Select): Active, Paused, Inactive

### Database 2: Monthly Priorities

**Purpose:** Track what to promote each month

**Properties:**
- Month (Title): "2025-11 November"
- Client (Relation): → CMA Client Profile
- Priority Items (Text): "Fall enrollment, Thanksgiving recital, Holiday gift certificates"
- Special Events (Text): "Nov 15 - Open House, Nov 28 - Recital"
- Seasonal Themes (Multi-select): Thanksgiving, Fall, Holiday prep
- Key Messages (Text): Focus areas for the month
- Status (Select): Planning, In Progress, Complete

### Database 3: Content Calendar

**Purpose:** Track all social media posts (planned + posted)

**Properties:**
- Post Title (Title): Brief description
- Client (Relation): → CMA Client Profile
- Month (Relation): → Monthly Priorities
- Date (Date): Post date
- Platform (Select): Instagram, Facebook, GBP
- Post Type (Select): Feed Post, Reel, Story, Event, etc.
- Content Theme (Select): Student Success, Instructor Feature, Tip, Promotion, etc.
- Caption (Text): Full post copy
- Hashtags (Text): Hashtags used
- CTA (Text): Call to action
- Visual Notes (Text): Description of image/video needed
- Status (Select): Draft, Scheduled, Posted, Archived
- Performance Link (Relation): → Performance Data (optional)

### Database 4: Performance Data

**Purpose:** Track post performance and learnings

**Properties:**
- Post (Relation): → Content Calendar
- Platform (Select): Instagram, Facebook, GBP
- Post Date (Date): When it was posted
- Impressions (Number): Total reach
- Engagement (Number): Likes + comments + shares
- Engagement Rate (Formula): Engagement / Impressions
- Link Clicks (Number): CTA performance
- Top Performing (Checkbox): Mark winners
- Performance Notes (Text): What worked/didn't work
- Month (Relation): → Monthly Priorities

### Database 5: Performance Insights Log

**Purpose:** Cumulative learnings to inform future content

**Properties:**
- Month (Title): "2025-10 October"
- Client (Relation): → CMA Client Profile
- Top Performers (Relation): → Performance Data (top posts)
- What Worked (Text): Successful patterns
- What Didn't Work (Text): Underperformers
- Recommendations (Text): Apply to next month
- Key Metrics Summary (Text): Overall performance
- Report Link (URL): Link to monthly report

---

## 7. Critical Questions

Before designing the Claude Skills, I need to know:

### About Notion:
1. ❓ Do you have CMA data in Notion already?
2. ❓ If yes, what databases exist?
3. ❓ If no, are you open to creating the 5 recommended databases?
4. ❓ Should we set up Notion MCP access so Claude can query/update?

### About Data:
5. ❓ Where do you currently track "what to promote this month"?
   - Email from client?
   - Meeting notes?
   - Your head?
6. ❓ How do you want to transition from Agency Analytics to Looker Studio?
   - Timeline?
   - Who sets up Looker Studio?
7. ❓ Do you have September, October, November analytics anywhere?
   - Different format?
   - Not exported yet?

### About Workflow:
8. ❓ How do you currently approve content with CMA?
   - Share Google Doc?
   - Email with attachments?
   - Notion page?
9. ❓ What's your timeline for December content?
   - Need to create by Nov 21 (week 3)?
   - Already started?
10. ❓ Do you track what was actually posted vs. what was planned?
    - If yes, where?
    - If no, should we start?

---

## 8. Immediate Next Steps

### Option A: Clean Up Current Structure First
**Timeline:** 2-4 hours

**Tasks:**
1. Move scattered CMA files from root Drive to `/client-cma/06_Social_Media/`
2. Create missing folder structure
3. Rename folders for consistency (YYYY-MM format)
4. Create monthly priorities documents for remaining 2025 months
5. Export Sept-Nov analytics (or set up Looker Studio)

**Pro:** Clean foundation before building skills
**Con:** No immediate automation value

### Option B: Build Skills Now, Clean As We Go
**Timeline:** Start today

**Tasks:**
1. Build content generator skill using current structure
2. Have skill output to proper organized location
3. Clean up old files over time
4. Improve as we use it

**Pro:** Immediate value, learn by doing
**Con:** Working with messy data initially

### Option C: Hybrid Approach (RECOMMENDED)
**Timeline:** Start today, refine continuously

**Phase 1 (Today):**
1. Create `/client-cma/06_Social_Media/` folder structure
2. Move critical files (strategy, content calendars)
3. Create December priorities document

**Phase 2 (This Week):**
4. Build first version of content generator skill
5. Test with December content generation
6. Identify what additional data/structure is needed

**Phase 3 (Next Week):**
7. Set up Notion databases based on learnings
8. Build reporting skill
9. Refine and optimize

---

## 9. Success Metrics

### For Content Generation Skill
- ✅ Generate 12 IG + 4 FB + 4 GBP + 1 reel in < 30 minutes
- ✅ Follow brand voice and strategy automatically
- ✅ Avoid duplicate topics from previous months
- ✅ Incorporate monthly priorities
- ✅ Output in client-approved format
- ✅ Save time: 4-6 hours → 30 minutes + review

### For Reporting Skill
- ✅ Pull performance data automatically
- ✅ Identify top/bottom performers
- ✅ Generate insights and recommendations
- ✅ Create formatted monthly report
- ✅ Save time: 3-4 hours → 20 minutes + review

---

## 10. Estimated Value

### Time Savings Per Month
- **Current:** 8-10 hours (content creation + reporting)
- **With Skills:** 2-3 hours (review + refinement)
- **Savings:** 5-7 hours/month per client

### Scalability
- **Current:** Can handle ~5-8 clients max
- **With Skills:** Can handle 20+ clients
- **Multiplier:** 3-4x capacity

### Quality Improvements
- **Consistency:** Same high quality every month
- **Data-driven:** Automatic incorporation of performance insights
- **Brand alignment:** Always follows strategy
- **Reduced errors:** No missed deliverables or duplicate posts

---

## 11. Recommended Decision

**I recommend Option C: Hybrid Approach**

**Start with:**
1. Quick folder reorganization (1 hour)
2. Create December priorities doc (15 minutes)
3. Build content generator skill for December (3-4 hours)
4. Test and refine with real use
5. Add Notion + reporting skill after learning from first skill

**Why this approach:**
- Get value immediately
- Learn what works through real use
- Don't over-engineer before knowing needs
- Can adjust structure as we discover requirements
- Builds momentum and confidence

---

## Next Actions

Please answer the 10 Critical Questions (Section 7) so I can:
1. Design the exact Notion database structure you need
2. Understand your current workflow pain points
3. Build skills that match how you actually work
4. Avoid building features you won't use

Once you answer, I'll create:
- Detailed implementation plan
- First skill specification
- Setup instructions

Ready when you are!
