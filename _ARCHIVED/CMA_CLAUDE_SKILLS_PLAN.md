# CMA Claude Skills Project Plan

**Created:** November 12, 2025
**Status:** In Progress - Notion MCP Just Configured
**Client:** Cincinnati Music Academy (CMA)

---

## Project Overview

Building Claude Skills to automate monthly social media content generation and performance reporting for Sidekick Marketer clients, starting with Cincinnati Music Academy as the pilot client.

### Key Decision: Generalized Skills Approach
- Build ONE skill that works for ALL clients by taking client name as parameter
- NOT client-specific skills (avoids having to build separate skills for each client)
- Skills will pull client data from Notion + Google Drive dynamically

---

## Two Workflows Identified

### Workflow 1: Monthly Social Content Generation
**Timing:** Week 3 of current month (for next month's content)

**Process:**
1. Review what client wants to promote next month
2. Check past posts to avoid duplicates + understand performance
3. Generate content per SOW requirements
4. Follow social media strategy document
5. Align with business goals

**CMA Deliverables (per SOW):**
- 12 Instagram posts
- 4 Facebook posts
- 4 Google Business Profile posts
- 1 Reel (montage of month's images)

### Workflow 2: Monthly Performance Report
**Timing:** Week 1 of current month (recap previous month)

**Process:**
1. Pull performance data from analytics platform
2. Analyze what worked/didn't work
3. Generate insights and recommendations
4. Create client-facing report

**Analytics Transition:**
- Currently using Agency Analytics (exports available)
- Transitioning to Looker Studio (more cost-effective)

---

## Current Setup Status

### ✅ Completed

**Google Drive Access:**
- Direct filesystem access working
- Path: `/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/`

**Airtable MCP:**
- Configured and working in Claude Code
- 15 tools available

**Notion MCP:**
- Just added to `.claude.json` (lines 65-74)
- User needs to restart Claude Code to activate
- Integration token: `[REDACTED]`
- Page access granted by user

**Documentation Created:**
7 comprehensive documentation files in `/My Drive/01_Sidekick Marketer/3. AI_Automation/01_Claude_Skills/docs/`:
1. README.md - Navigation guide
2. CLAUDE_DATA_INTEGRATION_COMPLETE.md - Complete setup summary (if exists)
3. CLAUDE_QUICK_REFERENCE.md - Cheat sheet (if exists)
4. CLAUDE_DATA_ACCESS_GUIDE.md - Technical reference (if exists)
5. CLAUDE_DATA_ACCESS_EXAMPLES.md - Practical examples (if exists)
6. NOTION_STRUCTURE_BEST_PRACTICES.md - Notion optimization guide (if exists)
7. CMA_AUDIT_FINDINGS.md - Complete audit of CMA current setup
8. **CMA_CLAUDE_SKILLS_PLAN.md** (this document)

---

## CMA Audit Findings Summary

### What We Found

**Google Drive Structure:**
- Main folder: `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/`
- Strategy doc exists: `/My Drive/CMA_Social_Media_GBP_Strategy.md`
- Content calendars: May 2025 and September 2025 (scattered in root Drive)
- Agency Analytics exports: January-August 2025 (in `/05 - Reports & Analytics/01_Discovery Phase/Social Media and GBP/`)

**Content Strategy (from strategy doc):**
- Primary platform: Instagram
- Content pillars: Student Success 30%, Instructor Expertise 25%, Educational 20%, Community 15%, Promotional 10%
- Brand voice: Encouraging, knowledgeable, community-focused
- Posting schedule: IG 4-5/week, FB 3-4/week

**Current Gaps:**
- No centralized `/06_Social_Media/` folder
- Sept-Nov 2025 analytics missing (or need transition to Looker Studio)
- No monthly priorities tracking document
- No organized archive of past posts
- Content calendars scattered across Drive root

### Recommended Folder Structure

```
/client-cma/
├── 01 - Client Details/
├── 02 - Branding & Assets/
├── 03 - Strategy Documents/
├── 04 - Contracts & SOW/
├── 05 - Reports & Analytics/
│   ├── 01_Discovery Phase/
│   └── 02_Ongoing Analytics/
│       ├── 2025-01_January/
│       ├── 2025-02_February/
│       └── [etc...]
└── 06_Social_Media/            ← NEW
    ├── 00_Strategy/
    ├── 01_Content_Calendars/
    │   ├── 2025-05_May/
    │   ├── 2025-09_September/
    │   └── [etc...]
    ├── 02_Monthly_Priorities/
    ├── 03_Past_Posts_Archive/
    └── 04_Performance_Insights/
```

### Recommended Notion Databases

**5 Databases for CMA:**
1. **CMA Client Profile** - Basic info, contacts, SOW details, strategy links
2. **Monthly Priorities** - What to promote each month (events, programs, offers)
3. **Content Calendar** - Master calendar with all posts
4. **Performance Data** - Monthly metrics from analytics
5. **Performance Insights Log** - What worked/didn't work for future reference

---

## Notion Workspace Status

**Current State (per user):**
- "Kind of a mess with different drafts"
- Need to audit and consolidate after restart

**Access Granted:**
- Integration created in Notion settings
- User granted page access to integration
- Waiting for Claude Code restart to test connectivity

---

## Next Steps (After Restart)

### Phase 1: Audit & Organize
1. ✅ Restart Claude Code
2. Test Notion MCP connection
3. List all Notion databases and pages
4. Audit what exists for CMA in Notion
5. Review and consolidate "messy drafts"
6. Provide specific recommendations for organization

### Phase 2: Structure Setup
7. Create/organize 5 recommended Notion databases for CMA
8. Reorganize CMA Google Drive folder structure
9. Move scattered content calendars to proper locations
10. Set up monthly priorities tracking
11. Create past post archive system

### Phase 3: Data Gaps
12. Address missing Sept-Nov 2025 analytics
13. Transition to Looker Studio (if ready)
14. Document monthly priorities for upcoming months
15. Ensure all strategy documents are in one place

### Phase 4: Build First Skill
16. Create `SKILL.md` for monthly social content generator
17. Define skill structure:
    - Name, description, parameters
    - Data sources it needs (Notion DBs, Drive files)
    - Workflow steps
    - Output format
18. Test with December 2025 content generation
19. Refine based on results

### Phase 5: Build Second Skill
20. Create `SKILL.md` for monthly performance report
21. Test with November 2025 report
22. Refine and document learnings

### Phase 6: Generalize & Scale
23. Document patterns for adapting to other clients
24. Create template/checklist for new client setup
25. Test with second client

---

## Key Technical Details

### Claude Skills Structure
Skills are defined in `SKILL.md` files that Claude auto-discovers. They use progressive disclosure (30-50 tokens until activated).

**Skill File Components:**
- Name and description
- When to use this skill
- Parameters it accepts
- Data sources it accesses
- Step-by-step workflow
- Output format/deliverables

### Data Integration Architecture
- **Google Drive:** Local filesystem access via Google Drive for Desktop
- **Airtable:** MCP stdio server via npx
- **Notion:** MCP stdio server via node (just configured)
- All three will be queryable from within Claude Skills

### File Paths Reference
- **Google Drive root:** `/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/`
- **CMA folder:** `/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/`
- **Documentation:** `/My Drive/01_Sidekick Marketer/3. AI_Automation/01_Claude_Skills/docs/`
- **CMA strategy:** `/My Drive/CMA_Social_Media_GBP_Strategy.md`

---

## Important Context

### What We're NOT Doing
- ❌ NOT using the 117-agent Conductor.build system (old project, can revisit later)
- ❌ NOT building client-specific skills for each client
- ❌ NOT using Make.com initially (just Claude Skills first)

### What We ARE Doing
- ✅ Building generalized Claude Skills that work for all clients
- ✅ Starting with ONE client (CMA) to fine-tune process
- ✅ Using Notion + Google Drive as primary data sources
- ✅ Building in small, testable steps
- ✅ Creating hybrid approach: clean up folders first, then build skills

### User Preferences
- Wants to build in small steps to fine-tune
- Wants to see real working automation, not just documentation
- Using Notion and Google Drive for marketing agency operations
- Transitioning from Agency Analytics to Looker Studio
- Wants content ready by Week 3, reporting done Week 1

---

## Resume Instructions

**To continue this project after restarting Claude Code, say:**

> "Continue the CMA Claude Skills project. We just configured Notion MCP. Reference the plan at `/My Drive/01_Sidekick Marketer/3. AI_Automation/01_Claude_Skills/docs/CMA_CLAUDE_SKILLS_PLAN.md`"

**Or simply:**

> "Test Notion MCP and audit my workspace for CMA"

All context is preserved in:
- This plan document
- The 7 other documentation files in same folder
- CMA audit findings document
- Your `.claude.json` configuration (Notion MCP now configured)

---

## Questions to Answer Next Session

1. What Notion databases already exist for CMA?
2. What's in the "messy drafts" that need consolidation?
3. Are there any existing workflows or templates in Notion?
4. What format does user prefer for content calendars in Notion?
5. Where should Claude Skills files be stored? (`.claude/skills/` directory?)

---

**Status:** Ready to restart Claude Code and test Notion MCP connectivity. All documentation and planning complete. Next action: Audit Notion workspace.
