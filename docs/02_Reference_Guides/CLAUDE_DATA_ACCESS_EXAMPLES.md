# Claude AI Data Access - Practical Examples

**Real-world examples for every data source and operation type**

---

## Table of Contents

1. [Google Drive Examples](#google-drive-examples)
2. [Airtable Examples](#airtable-examples)
3. [Notion Examples](#notion-examples)
4. [Cross-Source Workflow Examples](#cross-source-workflow-examples)
5. [Advanced Use Cases](#advanced-use-cases)

---

## Google Drive Examples

### Example 1: Read a Client Report
```
Task: Read the latest client report for Integrity Greens

Command:
"Read the file at /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/Integrity_Greens/Reports/2025-11-Report.md"

Result: File contents displayed for analysis
```

### Example 2: Create Monthly Report Template
```
Task: Create a new monthly report template

Command:
"Create a monthly report template file called 'monthly-report-template.md' in the /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Templates/ folder"

Result: New template file created with structure
```

### Example 3: Search for All Client Proposals
```
Task: Find all proposal documents across all clients

Command:
"Find all files matching the pattern '*proposal*.md' in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/"

Tool: Glob
Pattern: "*proposal*.md"

Result: List of all proposal files with full paths
```

### Example 4: Search for Specific Content
```
Task: Find all mentions of "SEO audit" in client documents

Command:
"Search for 'SEO audit' in all markdown files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/"

Tool: Grep
Pattern: "SEO audit"
Glob: "*.md"
Output: "content"

Result: All mentions with file paths and line numbers
```

### Example 5: Update Status Across Multiple Files
```
Task: Update project status from "In Progress" to "Completed" in all project files

Step 1: Find files with "In Progress"
"Search for 'Status: In Progress' in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Projects/"

Step 2: Read each file
"Read [file path]"

Step 3: Edit each file
"Replace 'Status: In Progress' with 'Status: Completed' in [file path]"

Result: All project statuses updated
```

### Example 6: Generate and Save Analysis
```
Task: Analyze marketing data and save insights to Drive

Step 1: Read data file
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Data/marketing-metrics.csv"

Step 2: Analyze (Claude processes)

Step 3: Save analysis
"Create a new file called 'marketing-analysis-2025-11.md' with the analysis results in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Analytics/"

Result: New analysis file saved to Drive
```

### Example 7: List Directory Contents
```
Task: See what's in the client folder

Command:
"List all files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/"

Tool: Bash
Command: ls -la "[path]"

Result: Directory listing with file details
```

### Example 8: Batch File Processing
```
Task: Read and summarize all project status files

Step 1: Find all status files
"Find all files named '*status*.md' in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/"

Step 2: Read each file (parallel)
"Read [file1]"
"Read [file2]"
"Read [file3]"

Step 3: Generate summary
"Create a summary of all project statuses"

Step 4: Save summary
"Save the summary to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/project-status-summary.md"

Result: Consolidated status report
```

---

## Airtable Examples

### Example 1: List All Bases
```
Task: See what Airtable bases I have access to

Command:
"Show me all my Airtable bases"

Tool: mcp__airtable__list_bases

Result:
- Base 1: "Client CRM" (appXXXXXXXXXXXXXX)
- Base 2: "Project Tracker" (appYYYYYYYYYYYYYY)
- Base 3: "Content Calendar" (appZZZZZZZZZZZZZZ)
```

### Example 2: Explore Table Structure
```
Task: Understand the Clients table structure

Command:
"Show me the detailed structure of the Clients table in my CRM base"

Tool: mcp__airtable__describe_table
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  detailLevel: "full"

Result: Complete field list with types:
- Name (Single line text)
- Status (Single select: Active, Inactive, Prospect)
- Revenue (Number)
- Start Date (Date)
- Services (Multiple select)
- etc.
```

### Example 3: Get All Active Clients
```
Task: List all clients with Active status

Command:
"Get all active clients from my Airtable CRM"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  filterByFormula: "{Status} = 'Active'"

Result: List of active client records with all fields
```

### Example 4: Get Recent Records
```
Task: Get clients added in the last 30 days

Command:
"Show me clients added in the last 30 days"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  filterByFormula: "IS_AFTER({Created}, DATEADD(TODAY(), -30, 'days'))"
  sort: [{"field": "Created", "direction": "desc"}]

Result: Recent clients sorted by creation date
```

### Example 5: Search for Specific Client
```
Task: Find all records mentioning "website redesign"

Command:
"Search Airtable for records containing 'website redesign'"

Tool: mcp__airtable__search_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Projects"
  searchTerm: "website redesign"

Result: All matching records
```

### Example 6: Create New Client Record
```
Task: Add new client to CRM

Command:
"Create a new client record in Airtable:
- Name: Acme Corporation
- Status: Prospect
- Revenue: 5000
- Services: SEO, Content Marketing"

Tool: mcp__airtable__create_record
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  fields: {
    "Name": "Acme Corporation",
    "Status": "Prospect",
    "Revenue": 5000,
    "Services": ["SEO", "Content Marketing"]
  }

Result: New record created with ID recXXXXXXXXXXXXXX
```

### Example 7: Update Multiple Records
```
Task: Mark several projects as complete

Command:
"Update these project records to Completed status:
- recAAAAAAAAAAAAAAA
- recBBBBBBBBBBBBBBB
- recCCCCCCCCCCCCCC"

Tool: mcp__airtable__update_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Projects"
  records: [
    {"id": "recAAAAAAAAAAAAAAA", "fields": {"Status": "Completed"}},
    {"id": "recBBBBBBBBBBBBBBB", "fields": {"Status": "Completed"}},
    {"id": "recCCCCCCCCCCCCCC", "fields": {"Status": "Completed"}}
  ]

Result: All three records updated
```

### Example 8: Complex Filter Query
```
Task: Get high-value active clients

Command:
"Get active clients with revenue over $10,000"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  filterByFormula: "AND({Status} = 'Active', {Revenue} > 10000)"
  sort: [{"field": "Revenue", "direction": "desc"}]

Result: High-value clients sorted by revenue
```

### Example 9: Add Comment to Record
```
Task: Add a note to a client record

Command:
"Add a comment to client record recXXXXXXXXXXXXXX saying 'Completed Q4 review - all metrics positive'"

Tool: mcp__airtable__create_comment
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  recordId: "recXXXXXXXXXXXXXX"
  text: "Completed Q4 review - all metrics positive"

Result: Comment added successfully
```

### Example 10: Query from Specific View
```
Task: Get records from "Active Projects" view

Command:
"Get all records from the Active Projects view"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Projects"
  view: "Active Projects"

Result: Records pre-filtered by view configuration
```

### Example 11: Check Empty Fields
```
Task: Find clients without email addresses

Command:
"Find all clients with empty email field"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Clients"
  filterByFormula: "{Email} = BLANK()"

Result: Clients missing email addresses
```

### Example 12: Date Range Query
```
Task: Get projects created in 2025

Command:
"Get all projects created in 2025"

Tool: mcp__airtable__list_records
Parameters:
  baseId: "appXXXXXXXXXXXXXX"
  tableId: "Projects"
  filterByFormula: "AND(IS_AFTER({Created}, '2024-12-31'), IS_BEFORE({Created}, '2026-01-01'))"

Result: 2025 projects
```

---

## Notion Examples

### Example 1: List Available Resources
```
Task: See what Notion resources are available

Command:
"Show me all available Notion resources"

Tool: ListMcpResourcesTool
Parameters:
  server: "notion"

Result: List of accessible Notion databases and pages
```

### Example 2: Read Notion Database
```
Task: Read project tracker database

Command:
"Read the Notion database at notion://database/abc123"

Tool: ReadMcpResourceTool
Parameters:
  server: "notion"
  uri: "notion://database/abc123"

Result: Database contents and structure
```

---

## Cross-Source Workflow Examples

### Example 1: Client Onboarding Report
```
Task: Generate comprehensive onboarding report

Step 1: Get client data from Airtable
"Get the record for client recXXXXXXXXXXXXXX from Airtable"

Tool: mcp__airtable__get_record

Step 2: Read onboarding template from Drive
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Templates/onboarding-template.md"

Step 3: Generate customized onboarding document
(Claude processes data and template)

Step 4: Save to client folder in Drive
"Save the onboarding document to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/[Client Name]/onboarding-2025-11.md"

Step 5: Update Airtable with document link
"Update the client record to add the onboarding document link"

Tool: mcp__airtable__update_records

Step 6: Add comment with completion note
"Add a comment to the record: 'Onboarding document generated and saved to Drive'"

Tool: mcp__airtable__create_comment

Result: Complete onboarding workflow automated
```

### Example 2: Monthly Analytics Report
```
Task: Generate monthly report from Airtable data

Step 1: Query metrics from Airtable
"Get all completed projects from November 2025"

Tool: mcp__airtable__list_records
Filter: AND({Status} = 'Completed', IS_AFTER({Completed Date}, '2025-11-01'), IS_BEFORE({Completed Date}, '2025-12-01'))

Step 2: Read previous month's report
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/2025-10-analytics.md"

Step 3: Generate comparison report
(Claude analyzes data and creates report)

Step 4: Save new report to Drive
"Save the November analytics report to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/2025-11-analytics.md"

Step 5: Update Notion dashboard
"Update the Notion analytics dashboard with November metrics"

Tool: ReadMcpResourceTool / Update (if write access available)

Result: Month-over-month analytics report generated
```

### Example 3: Content Calendar Management
```
Task: Update content calendar from Airtable status

Step 1: Read current calendar from Drive
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Content/content-calendar-2025-11.csv"

Step 2: Query content status from Airtable
"Get all content items from November with their current status"

Tool: mcp__airtable__list_records
Filter: IS_AFTER({Publish Date}, '2025-11-01')

Step 3: Cross-reference and identify updates
(Claude compares data sources)

Step 4: Generate updated calendar
(Claude creates new CSV with current status)

Step 5: Save updated calendar
"Save the updated content calendar to Drive"

Step 6: Update Airtable records if needed
"Update any out-of-sync records in Airtable"

Tool: mcp__airtable__update_records

Result: Synchronized content calendar
```

### Example 4: Client Health Check
```
Task: Automated client health assessment

Step 1: Get all active clients from Airtable
"Get all active clients"

Tool: mcp__airtable__list_records
Filter: {Status} = 'Active'

Step 2: Check for client folders in Drive
"For each client, check if folder exists in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/"

Tool: Glob or Bash (ls)

Step 3: Check for recent reports
"Find most recent report for each client"

Tool: Glob with pattern matching

Step 4: Identify missing items
(Claude analyzes and creates list)

Step 5: Generate health check report
"Create a report of client account health with missing items highlighted"

Step 6: Save to Drive
"Save health check report to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Reports/client-health-check-2025-11.md"

Step 7: Flag issues in Airtable
"For clients with issues, add comments to their Airtable records"

Tool: mcp__airtable__create_comment

Result: Comprehensive client health assessment
```

### Example 5: Proposal Generator
```
Task: Generate custom proposal from template and client data

Step 1: Get client details from Airtable
"Get client record for Acme Corporation"

Tool: mcp__airtable__search_records

Step 2: Read proposal template
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Templates/proposal-template.md"

Step 3: Read pricing data
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/Data/service-pricing.csv"

Step 4: Generate customized proposal
(Claude merges template with client data)

Step 5: Save proposal to client folder
"Save proposal to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Clients/Acme_Corporation/proposal-2025-11.md"

Step 6: Create proposal tracking record
"Create a proposal record in Airtable"

Tool: mcp__airtable__create_record
Fields: Client, Date Sent, Amount, Status

Step 7: Link proposal document
"Update the proposal record with Drive link"

Tool: mcp__airtable__update_records

Result: Proposal generated, saved, and tracked
```

### Example 6: Data Migration
```
Task: Migrate data from Drive CSV to Airtable

Step 1: Read CSV from Drive
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Data/import-clients.csv"

Step 2: Parse and validate data
(Claude processes CSV)

Step 3: Check for existing records
"Search Airtable for existing clients with these names"

Tool: mcp__airtable__search_records

Step 4: Create new records
"Create Airtable records for new clients"

Tool: mcp__airtable__create_record (multiple calls or batch)

Step 5: Update existing records
"Update records that already exist"

Tool: mcp__airtable__update_records

Step 6: Generate migration log
"Create a log of all migrated records"

Step 7: Save log to Drive
"Save migration log to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/Data/migration-log-2025-11.md"

Result: Data migrated with full audit trail
```

---

## Advanced Use Cases

### Use Case 1: Automated Weekly Digest
```
Workflow: Generate weekly digest of activity

1. Query Airtable for records created this week
2. Query Airtable for records updated this week
3. Query Airtable for upcoming deadlines
4. Read previous week's digest from Drive
5. Generate new digest with comparisons
6. Save to Drive with date stamp
7. Update Notion dashboard with summary
8. Add comments to key records

Tools Used:
- mcp__airtable__list_records (with date filters)
- Read (previous digest)
- Write (new digest)
- mcp__airtable__create_comment
- ReadMcpResourceTool (Notion)

Result: Automated weekly summary
```

### Use Case 2: Client Portfolio Analysis
```
Workflow: Analyze entire client portfolio

1. Get all active clients from Airtable
2. For each client:
   - Get all projects
   - Calculate total revenue
   - Get recent activity
3. Read previous quarter's analysis from Drive
4. Generate comprehensive portfolio report
5. Identify trends and patterns
6. Save analysis to Drive
7. Update Airtable with health scores
8. Flag at-risk clients

Tools Used:
- mcp__airtable__list_records (clients and projects)
- Read (previous analysis)
- Write (new analysis)
- mcp__airtable__update_records (health scores)
- mcp__airtable__create_comment (flags)

Result: Portfolio health assessment
```

### Use Case 3: Content Production Pipeline
```
Workflow: Manage content from brief to publication

1. Read content brief from Drive
2. Get content guidelines from Airtable
3. Query brand voice examples from Drive
4. Generate content draft
5. Save draft to Drive
6. Create Airtable review record
7. Add comment with draft link
8. Monitor for approval
9. Generate final version
10. Update Airtable status to Published

Tools Used:
- Read (brief, examples)
- mcp__airtable__list_records (guidelines)
- Write (draft, final)
- mcp__airtable__create_record (review tracking)
- mcp__airtable__update_records (status)
- mcp__airtable__create_comment (notes)

Result: End-to-end content production
```

### Use Case 4: Compliance Audit
```
Workflow: Audit all client deliverables

1. Get all clients from Airtable
2. For each client, check Drive for:
   - Contract
   - Onboarding doc
   - Monthly reports
   - Meeting notes
3. Check Airtable for:
   - Billing records
   - Project completion
   - Communication logs
4. Generate compliance matrix
5. Identify missing items
6. Save audit report to Drive
7. Create Airtable tasks for missing items
8. Add comments to client records

Tools Used:
- mcp__airtable__list_records (clients, projects)
- Glob (find files)
- Read (verify contents)
- Write (audit report)
- mcp__airtable__create_record (tasks)
- mcp__airtable__create_comment (notes)

Result: Compliance audit with action items
```

### Use Case 5: Performance Dashboard
```
Workflow: Generate real-time performance metrics

1. Query current month metrics from Airtable:
   - Revenue
   - Projects completed
   - New clients
   - Active projects
2. Read historical data from Drive
3. Calculate trends and projections
4. Generate dashboard markdown
5. Create visualizations (text-based)
6. Save dashboard to Drive
7. Update Notion with key metrics
8. Add insights as Airtable comments

Tools Used:
- mcp__airtable__list_records (with various filters)
- Read (historical data)
- Write (dashboard)
- ReadMcpResourceTool / Update (Notion)
- mcp__airtable__create_comment (insights)

Result: Live performance dashboard
```

---

## Tips for Success

### 1. Start Simple
- Test single operations first
- Verify data access
- Confirm IDs and paths
- Then build complex workflows

### 2. Use Descriptive Commands
- Be specific about data sources
- Include relevant filters
- Specify desired output format
- Mention any transformations needed

### 3. Chain Operations Logically
- Query → Analyze → Generate → Save
- Read → Transform → Create → Update
- Search → Verify → Modify → Log

### 4. Handle Errors Gracefully
- Check if records exist before updating
- Verify file paths before reading
- Test formulas in Airtable UI first
- Save progress at each step

### 5. Document Your Workflows
- Keep track of useful formulas
- Save common file paths
- Document base/table IDs
- Create workflow templates

---

**Last Updated**: November 2025
**Status**: Comprehensive example library
**Next**: Try these examples with your own data
