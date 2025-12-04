# Claude AI Workflow Templates

**25+ ready-to-use workflow templates for common tasks**

---

## Table of Contents

1. [Client Management Workflows](#client-management-workflows)
2. [Reporting & Analytics Workflows](#reporting--analytics-workflows)
3. [Content Production Workflows](#content-production-workflows)
4. [Data Management Workflows](#data-management-workflows)
5. [Project Management Workflows](#project-management-workflows)
6. [Automation & Monitoring Workflows](#automation--monitoring-workflows)

---

## Client Management Workflows

### Workflow 1: New Client Onboarding
**Purpose**: Complete onboarding process from Airtable data

**Steps:**
```
1. "Get the client record for [Client Name] from Airtable CRM"
2. "Read the onboarding template from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Templates/onboarding-template.md"
3. "Generate a customized onboarding document using the template and client data"
4. "Save the document to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/onboarding-[date].md"
5. "Update the Airtable client record with the onboarding document link"
6. "Add a comment to the Airtable record: 'Onboarding document generated - [date]'"
```

**Variables to Replace:**
- [Client Name] - Client name from Airtable
- [Client_Name] - Formatted for folder name
- [date] - Current date (YYYY-MM-DD)

**Tools Used:**
- mcp__airtable__search_records or get_record
- Read
- Write
- mcp__airtable__update_records
- mcp__airtable__create_comment

---

### Workflow 2: Client Health Check
**Purpose**: Audit client accounts for completeness

**Steps:**
```
1. "List all active clients from Airtable"
2. "For each client, check if these files exist in their Drive folder:
   - Contract
   - Onboarding document
   - Latest monthly report (within 45 days)"
3. "Check Airtable for:
   - At least one project in last 90 days
   - Billing record in last 60 days
   - Communication log updated in last 30 days"
4. "Generate a health check report listing:
   - Green (all items present)
   - Yellow (1-2 items missing)
   - Red (3+ items missing or critical items)"
5. "Save report to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/client-health-[date].md"
6. "For Red and Yellow clients, add a comment to their Airtable record with missing items"
```

**Frequency**: Weekly or Monthly

**Tools Used:**
- mcp__airtable__list_records
- Glob (find files)
- Write (report)
- mcp__airtable__create_comment

---

### Workflow 3: Quarterly Business Review Prep
**Purpose**: Prepare QBR materials from client data

**Steps:**
```
1. "Get all records for [Client Name] from the last 3 months:
   - Projects table (completed and in-progress)
   - Billing table (invoices and payments)
   - Metrics table (performance data)"
2. "Read previous QBR document from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/QBR-[previous-quarter].md"
3. "Read QBR template from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Templates/qbr-template.md"
4. "Generate QBR document with:
   - Executive summary
   - Quarter-over-quarter comparison
   - Project completions and outcomes
   - Key metrics and trends
   - Recommendations for next quarter"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/QBR-[current-quarter].md"
6. "Update client record in Airtable with QBR link and next review date"
```

**Variables:**
- [Client Name]
- [Client_Name]
- [previous-quarter] (e.g., 2025-Q3)
- [current-quarter] (e.g., 2025-Q4)

---

### Workflow 4: Client Folder Setup
**Purpose**: Create standardized folder structure for new client

**Steps:**
```
1. "Get client details from Airtable record [record ID]"
2. "Create folder structure in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/:
   - /Contracts
   - /Reports
   - /Projects
   - /Meeting_Notes
   - /Assets
   - /Communications"
3. "Copy template files:
   - README.md (client info)
   - meeting-notes-template.md
   - project-brief-template.md"
4. "Update Airtable client record with folder link"
5. "Add comment: 'Client folder structure created - [date]'"
```

---

## Reporting & Analytics Workflows

### Workflow 5: Monthly Analytics Report
**Purpose**: Generate comprehensive monthly performance report

**Steps:**
```
1. "Get all completed projects from [Month Year] from Airtable"
2. "Get revenue data for [Month Year]"
3. "Get new clients added in [Month Year]"
4. "Read previous month's report from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/[previous-month]-analytics.md"
5. "Generate new report with:
   - Month-over-month comparisons
   - Key metrics dashboard
   - Project highlights
   - Revenue analysis
   - Client acquisition metrics
   - Trends and insights
   - Action items for next month"
6. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/[current-month]-analytics.md"
7. "Update Notion analytics dashboard with summary metrics"
```

**Frequency**: First week of each month

---

### Workflow 6: Client Performance Dashboard
**Purpose**: Real-time view of client metrics

**Steps:**
```
1. "For [Client Name], get from Airtable:
   - All active projects
   - Revenue (current month, quarter, year)
   - Completed deliverables (last 30 days)
   - Upcoming deadlines (next 30 days)
   - Open tasks"
2. "Read historical metrics from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/metrics-history.csv"
3. "Generate dashboard with:
   - Current status summary
   - Active projects list
   - Revenue trends (3-month, 6-month, YTD)
   - Deliverables scorecard
   - Upcoming items
   - Health indicators"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/dashboard-[date].md"
5. "Update metrics history CSV with current data"
```

**Frequency**: As needed or weekly

---

### Workflow 7: Weekly Team Digest
**Purpose**: Summary of week's activity for team review

**Steps:**
```
1. "Get from Airtable (last 7 days):
   - New records created
   - Records with status changes
   - Comments added
   - Upcoming deadlines (next 7 days)"
2. "Read last week's digest from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/weekly-digest-[last-week-date].md"
3. "Generate digest with:
   - Week highlights
   - Key accomplishments
   - Status changes
   - Upcoming priorities
   - Items needing attention
   - Week-over-week trends"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/weekly-digest-[current-week-date].md"
```

**Frequency**: Every Monday morning

---

### Workflow 8: Revenue Forecasting
**Purpose**: Project revenue based on pipeline and trends

**Steps:**
```
1. "Get from Airtable:
   - All active clients (current MRR)
   - All prospects with proposals (value and probability)
   - Historical revenue data (last 12 months)"
2. "Read previous forecast from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/revenue-forecast-[last-month].md"
3. "Calculate:
   - Current MRR and ARR
   - Pipeline value (weighted by probability)
   - Trend analysis (3-month, 6-month, 12-month)
   - Projected revenue (next 3 months, 6 months, 12 months)"
4. "Generate forecast report with:
   - Current state
   - Pipeline analysis
   - Growth trends
   - Projections (conservative, likely, optimistic)
   - Risks and opportunities
   - Action items"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/revenue-forecast-[current-month].md"
```

**Frequency**: Monthly or quarterly

---

## Content Production Workflows

### Workflow 9: Blog Post Generation
**Purpose**: Create blog post from brief with brand voice

**Steps:**
```
1. "Read content brief from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Content/Briefs/[brief-name].md"
2. "Get brand guidelines from Airtable [Client Name] record"
3. "Read 2-3 example posts from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Content/Examples/"
4. "Generate blog post following brief and brand voice"
5. "Save draft to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Content/Drafts/[title]-[date]-draft.md"
6. "Create Airtable review record:
   - Title
   - Client
   - Type: Blog Post
   - Status: Draft
   - Link to document"
7. "Add comment with draft link and key SEO metadata"
```

---

### Workflow 10: Content Calendar Update
**Purpose**: Sync content status between Airtable and Drive

**Steps:**
```
1. "Read current calendar from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Content/content-calendar-[month].csv"
2. "Get all content records for [month] from Airtable Content table"
3. "Compare status between sources and identify:
   - Items in calendar but not in Airtable
   - Items in Airtable but not in calendar
   - Status mismatches"
4. "Generate updated calendar with current status from Airtable"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Content/content-calendar-[month].csv"
6. "If Airtable items need updating, update those records"
7. "Generate sync report with changes made"
```

**Frequency**: Weekly or as needed

---

### Workflow 11: Social Media Post Batch
**Purpose**: Generate week's worth of social posts

**Steps:**
```
1. "Get social media strategy from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/strategy-social.md"
2. "Get recent blog posts and news from Airtable"
3. "Read previous social posts from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Social/[previous-week].md"
4. "Generate 5-7 social posts for upcoming week:
   - Varied formats (tips, questions, announcements, etc.)
   - Platform-optimized (LinkedIn, Twitter, Facebook)
   - On-brand voice
   - Include hashtags and CTAs"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Social/week-[date].md"
6. "Create Airtable records for each post for scheduling"
```

**Frequency**: Weekly

---

## Data Management Workflows

### Workflow 12: CSV Import to Airtable
**Purpose**: Import data from CSV into Airtable

**Steps:**
```
1. "Read CSV file from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Data/import-[name].csv"
2. "Parse and validate data:
   - Check required fields
   - Validate data types
   - Check for duplicates"
3. "For each row, check if record already exists in Airtable (by unique identifier)"
4. "Create new records for items not in Airtable"
5. "Update existing records with new data"
6. "Generate import log with:
   - Total rows processed
   - Records created
   - Records updated
   - Errors/skipped
   - Details for each"
7. "Save log to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Data/import-log-[date].md"
```

---

### Workflow 13: Airtable Export and Backup
**Purpose**: Export Airtable data to Drive for backup

**Steps:**
```
1. "List all tables in Airtable base [Base Name]"
2. "For each table:
   - Get all records
   - Format as CSV
   - Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Backups/[Base_Name]/[table-name]-[date].csv"
3. "Generate backup summary with:
   - Backup date/time
   - Tables backed up
   - Record counts
   - File sizes"
4. "Save summary to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Backups/[Base_Name]/backup-summary-[date].md"
```

**Frequency**: Weekly or before major changes

---

### Workflow 14: Data Quality Audit
**Purpose**: Identify data quality issues in Airtable

**Steps:**
```
1. "Get all records from [Table Name] in Airtable"
2. "Check each record for:
   - Missing required fields
   - Invalid email formats
   - Empty linked records
   - Inconsistent formatting
   - Duplicate entries
   - Outdated information (based on last modified)"
3. "Categorize issues by severity:
   - Critical (missing required data)
   - High (invalid formats)
   - Medium (inconsistent formatting)
   - Low (minor issues)"
4. "Generate audit report with:
   - Summary statistics
   - Issues by severity
   - Specific records with problems
   - Recommended actions"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/data-quality-audit-[date].md"
6. "For critical issues, add comments to affected Airtable records"
```

**Frequency**: Monthly or quarterly

---

### Workflow 15: Duplicate Detection
**Purpose**: Find and flag duplicate records

**Steps:**
```
1. "Get all records from [Table Name]"
2. "Group records by key fields (email, company name, phone)"
3. "Identify potential duplicates (fuzzy matching for names)"
4. "For each group of duplicates:
   - Compare field values
   - Identify the most complete record
   - Note differences between records"
5. "Generate duplicate report with:
   - Total duplicates found
   - Grouped duplicates with comparison
   - Recommended primary record for each group
   - Merge strategy"
6. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/duplicates-[table-name]-[date].md"
7. "Add 'Potential Duplicate' tag to records in Airtable"
```

---

## Project Management Workflows

### Workflow 16: Project Kickoff Package
**Purpose**: Generate all project kickoff documents

**Steps:**
```
1. "Get project details from Airtable record [project ID]"
2. "Get client information from linked client record"
3. "Read templates:
   - Project brief template
   - Timeline template
   - Deliverables checklist
   - Communication plan"
4. "Generate customized documents:
   - Project brief with scope, goals, deliverables
   - Timeline with milestones
   - Deliverables checklist
   - Communication plan with stakeholders"
5. "Save all documents to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Projects/[Project_Name]/"
6. "Update Airtable project record with:
   - Status: In Progress
   - Kickoff date
   - Links to all documents"
7. "Add comment with summary and next steps"
```

---

### Workflow 17: Project Status Update
**Purpose**: Generate weekly project status report

**Steps:**
```
1. "Get project details from Airtable [project ID]"
2. "Get all tasks for project (completed this week, in progress, upcoming)"
3. "Read last week's status from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Projects/[Project_Name]/status-[last-week-date].md"
4. "Generate status report with:
   - Executive summary
   - Accomplishments this week
   - Current status (% complete, on track/at risk/behind)
   - Upcoming tasks
   - Blockers or issues
   - Next week's goals
   - Key decisions needed"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Projects/[Project_Name]/status-[current-week-date].md"
6. "Update Airtable project record with completion % and status"
```

**Frequency**: Weekly for active projects

---

### Workflow 18: Project Completion Report
**Purpose**: Final project summary and handoff

**Steps:**
```
1. "Get all project data from Airtable:
   - Project details
   - All tasks and completions
   - Timeline (planned vs actual)
   - All deliverables
   - Client feedback"
2. "Read all project status updates from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Projects/[Project_Name]/"
3. "Generate completion report with:
   - Executive summary
   - Original scope and goals
   - What was delivered
   - Timeline analysis (on time/delayed, reasons)
   - Key outcomes and metrics
   - Lessons learned
   - Client feedback
   - Recommendations for next phase"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Projects/[Project_Name]/completion-report-[date].md"
5. "Update Airtable project record:
   - Status: Completed
   - Completion date
   - Link to completion report
   - Success rating"
6. "Add final comment with summary"
```

---

## Automation & Monitoring Workflows

### Workflow 19: Daily Task Digest
**Purpose**: Morning summary of today's priorities

**Steps:**
```
1. "Get from Airtable:
   - Tasks due today
   - Overdue tasks
   - Meetings today
   - Urgent items flagged
   - Follow-ups due"
2. "Check Drive for:
   - Documents needing review (based on naming/status)
   - Pending approvals"
3. "Generate digest with:
   - Priority #1 items (urgent)
   - Today's schedule
   - Overdue items
   - Quick wins (easy completions)
   - Recommended focus areas"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/daily-digest-[date].md"
```

**Frequency**: Every morning

---

### Workflow 20: Deadline Monitor
**Purpose**: Alert on upcoming and missed deadlines

**Steps:**
```
1. "Get from Airtable:
   - Items due in next 7 days
   - Items due in next 24 hours
   - Overdue items"
2. "Categorize by urgency and project"
3. "Generate alert report with:
   - Red alerts (overdue or due today)
   - Orange alerts (due tomorrow)
   - Yellow alerts (due this week)
   - Details for each (project, deliverable, owner, status)"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/deadline-alerts-[date].md"
5. "For overdue items, add urgent comment to Airtable record"
```

**Frequency**: Daily

---

### Workflow 21: File Organization Audit
**Purpose**: Identify misplaced or unorganized files

**Steps:**
```
1. "List all files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/"
2. "Check for:
   - Files in root that should be in folders
   - Files with unclear naming
   - Old files (not accessed in 6+ months)
   - Duplicate files (same name, similar size)
   - Large files (over certain size threshold)"
3. "Generate organization report with:
   - Files to move (with suggested location)
   - Files to rename (with suggested name)
   - Files to archive
   - Files to review (potential duplicates)
   - Storage optimization suggestions"
4. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/file-organization-[date].md"
```

**Frequency**: Monthly

---

### Workflow 22: Client Communication Tracker
**Purpose**: Ensure regular client communication

**Steps:**
```
1. "Get all active clients from Airtable"
2. "For each client, check:
   - Last meeting date
   - Last email sent
   - Last status update
   - Last deliverable date"
3. "Identify clients with:
   - No contact in 30+ days (high priority)
   - No contact in 14-30 days (medium priority)
   - No contact in 7-14 days (low priority)"
4. "Generate touchpoint report with:
   - Clients needing immediate contact
   - Clients needing check-in soon
   - Recommended communication type
   - Last interaction summary
   - Suggested topics/talking points"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/client-touchpoints-[date].md"
6. "For high-priority clients, add comment to Airtable record"
```

**Frequency**: Weekly

---

### Workflow 23: Proposal Follow-up Tracker
**Purpose**: Monitor open proposals and schedule follow-ups

**Steps:**
```
1. "Get all proposals with status 'Sent' or 'Under Review' from Airtable"
2. "For each proposal:
   - Calculate days since sent
   - Check if follow-up has been done
   - Check for any client responses"
3. "Categorize:
   - Overdue follow-up (7+ days, no follow-up)
   - Due for follow-up (4-7 days)
   - Recently sent (0-3 days)"
4. "Generate follow-up report with:
   - Proposals needing immediate follow-up
   - Suggested follow-up approach
   - Win probability assessment
   - Historical context
   - Recommended next actions"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/proposal-follow-ups-[date].md"
6. "Add comments to Airtable records with follow-up reminders"
```

**Frequency**: Daily or every other day

---

## Specialized Workflows

### Workflow 24: Competitive Analysis Update
**Purpose**: Research and document competitive landscape

**Steps:**
```
1. "Get client details and industry from Airtable [Client Name]"
2. "Read previous competitive analysis from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Research/competitive-analysis-[previous-date].md"
3. "Read competitor data from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Research/competitor-data.csv"
4. "Generate updated analysis with:
   - Market overview
   - Top competitors (with recent changes)
   - Competitive positioning
   - Feature comparison
   - Pricing comparison
   - Marketing approach comparison
   - Opportunities identified
   - Threat assessment
   - Strategic recommendations"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/Research/competitive-analysis-[current-date].md"
6. "Update client record in Airtable with key findings"
```

**Frequency**: Quarterly or semi-annually

---

### Workflow 25: ROI Calculation Report
**Purpose**: Calculate and report client ROI

**Steps:**
```
1. "Get from Airtable for [Client Name]:
   - All services and costs
   - Client's reported revenue impact
   - Metrics improvements (traffic, leads, conversions)
   - Project costs and time invested"
2. "Read client's baseline metrics from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/baseline-metrics.md"
3. "Calculate:
   - Total investment (fees paid)
   - Quantifiable returns (revenue increase, cost savings)
   - Soft returns (efficiency gains, brand improvements)
   - ROI percentage
   - Payback period
   - Projected ongoing value"
4. "Generate ROI report with:
   - Executive summary
   - Investment breakdown
   - Returns analysis (direct and indirect)
   - ROI calculation with methodology
   - Before/after comparisons
   - Case studies of specific wins
   - Future value projection"
5. "Save to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client_Name]/roi-report-[date].md"
6. "Update client record with current ROI metric"
```

**Frequency**: Quarterly or for renewals

---

### Workflow 26: Meeting Notes Processing
**Purpose**: Structure and action raw meeting notes

**Steps:**
```
1. "Read raw meeting notes from /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Meetings/raw-notes-[date].md"
2. "Get attendee details from Airtable (client records, team members)"
3. "Process notes into structured format:
   - Meeting metadata (date, attendees, purpose)
   - Key discussion points
   - Decisions made
   - Action items (with owners and due dates)
   - Next steps
   - Follow-up needed"
4. "Save structured notes to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Meetings/[Client_Name]/meeting-notes-[date].md"
5. "Create Airtable task records for each action item"
6. "Add meeting summary comment to client record"
7. "If project-related, add notes to project record"
```

**Frequency**: After each meeting

---

## Tips for Using These Workflows

### Customization
- Replace [variables] with actual values
- Adjust file paths to match your structure
- Modify fields to match your Airtable schema
- Add or remove steps as needed

### Automation
- Save frequently used workflows as templates
- Create keyboard shortcuts or aliases
- Set up scheduled reminders for periodic workflows
- Use Make.com to trigger workflows automatically

### Iteration
- Start with basic version
- Test with real data
- Refine based on results
- Document any changes

### Documentation
- Keep a log of which workflows you use most
- Note any modifications you make
- Track time saved vs manual process
- Share successful patterns with team

---

**Last Updated**: November 2025
**Total Workflows**: 26
**Next Steps**: Copy a workflow template and customize for your needs
