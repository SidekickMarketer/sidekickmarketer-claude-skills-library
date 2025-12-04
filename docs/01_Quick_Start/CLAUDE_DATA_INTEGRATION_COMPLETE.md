# Claude AI Data Integration - Complete Setup Summary

**Everything Claude AI can access and how to use it effectively**

---

## Overview

Claude AI has direct access to three primary data sources through different methods:

1. **Google Drive** - Local filesystem access (all synced files)
2. **Airtable** - MCP server with 15 specialized tools
3. **Notion** - MCP server (ready to configure)

This document provides a complete overview of capabilities, setup, and usage patterns.

---

## 1. Google Drive Access

### How It Works
Claude accesses Google Drive files through the local macOS filesystem. Google Drive Desktop syncs files to a local directory, making them accessible just like any other file on your Mac.

### Base Path
```
/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/
```

### What You Can Do

#### Read Files
```
Read any file from Google Drive using the absolute path
- Markdown files (.md)
- Text files (.txt)
- CSV files (.csv)
- JSON files (.json)
- And many other formats
```

#### Write Files
```
Create new files directly in Google Drive folders
Save reports, analyses, and generated content
```

#### Edit Files
```
Modify existing files with precise string replacements
Update documentation, data files, and content
```

#### Search Files
```
- Glob: Find files by pattern (*.md, *.csv, etc.)
- Grep: Search file contents with regex patterns
```

#### Navigate Structure
```
List directories, check file existence, explore folder hierarchies
```

### Key Folders Available

```
00_Personal/                    - Personal files and projects
01_Sidekick Marketer/          - Agency operations and client work
02_Master_Documents_Hub/       - Documentation and guides
04_Other Projects/             - Client projects and other work
```

### Common Operations

**Read a File:**
```
"Read the file at /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/02_Master_Documents_Hub/README.md"
```

**Create a New File:**
```
"Create a new markdown file called 'client-report.md' in the 01_Sidekick Marketer folder"
```

**Search for Files:**
```
"Find all markdown files in the Master Documents Hub folder"
```

**Search Within Files:**
```
"Search all files in 01_Sidekick Marketer for mentions of 'Integrity Greens'"
```

---

## 2. Airtable Integration

### How It Works
Airtable access is provided through an MCP (Model Context Protocol) server that gives Claude 15 specialized tools for database operations.

### Available Tools (15 Total)

#### Base & Table Management
1. **mcp__airtable__list_bases** - List all accessible Airtable bases
2. **mcp__airtable__list_tables** - List all tables in a specific base
3. **mcp__airtable__describe_table** - Get detailed table structure and field information

#### Record Operations
4. **mcp__airtable__list_records** - List records from a table (with filters, sorting, views)
5. **mcp__airtable__search_records** - Search for records containing specific text
6. **mcp__airtable__get_record** - Get a specific record by ID
7. **mcp__airtable__create_record** - Create a new record in a table
8. **mcp__airtable__update_records** - Update up to 10 records (batch operation)
9. **mcp__airtable__delete_records** - Delete records from a table

#### Table & Field Management
10. **mcp__airtable__create_table** - Create a new table in a base
11. **mcp__airtable__update_table** - Update table name or description
12. **mcp__airtable__create_field** - Create a new field in a table
13. **mcp__airtable__update_field** - Update field name or description

#### Collaboration
14. **mcp__airtable__create_comment** - Create a comment on a record
15. **mcp__airtable__list_comments** - List comments on a record

### Key Concepts

**Base ID**: Unique identifier for an Airtable base (e.g., "appXXXXXXXXXXXXXX")
**Table ID**: Table name or ID within a base
**Record ID**: Unique identifier for a record (e.g., "recXXXXXXXXXXXXXX")
**Field ID**: Field name or ID within a table

### Common Operations

**List All Your Bases:**
```
"Show me all my Airtable bases"
Uses: mcp__airtable__list_bases
```

**Get Table Structure:**
```
"Show me the structure of the Clients table in my CRM base"
Uses: mcp__airtable__describe_table
```

**Query Records:**
```
"Get all active clients from Airtable"
Uses: mcp__airtable__list_records with filterByFormula
```

**Create Record:**
```
"Add a new client to Airtable with name 'Acme Corp' and status 'Active'"
Uses: mcp__airtable__create_record
```

**Update Records:**
```
"Update the status of client record recXXX to 'Complete'"
Uses: mcp__airtable__update_records
```

**Search Across Records:**
```
"Find all records mentioning 'website redesign'"
Uses: mcp__airtable__search_records
```

### Filter Formula Syntax

Airtable uses formula syntax for filtering:

```javascript
// Single condition
{Status} = 'Active'

// Multiple conditions (AND)
AND({Status} = 'Active', {Revenue} > 1000)

// Multiple conditions (OR)
OR({Type} = 'Client', {Type} = 'Prospect')

// Text search
SEARCH('keyword', {Notes})

// Date comparisons
IS_AFTER({Created}, '2025-01-01')
```

---

## 3. Notion Integration

### How It Works
Notion access is provided through an MCP server that allows reading and querying Notion workspace resources.

### Current Status
The Notion MCP server is configured and ready to use. Tools are available for:
- Listing available resources
- Reading specific resources by URI
- Accessing Notion databases and pages

### Available Tools

1. **ListMcpResourcesTool** - List all available Notion resources
2. **ReadMcpResourceTool** - Read a specific Notion resource by URI

### Setup Requirements

To use Notion integration, you need:
1. Notion API key (NOTION_API_KEY environment variable)
2. Notion integration configured in your workspace
3. Database/page permissions granted to the integration

### Common Operations

**List Available Resources:**
```
"Show me all available Notion resources"
```

**Read a Specific Resource:**
```
"Read the Notion database at notion://database/xxx"
```

---

## Cross-Source Workflows

One of the most powerful capabilities is combining data from multiple sources in a single workflow.

### Example Workflow 1: Client Onboarding
```
1. Read client information from Airtable
2. Generate onboarding document using Claude
3. Save document to Google Drive in client folder
4. Update Notion project tracker
```

### Example Workflow 2: Report Generation
```
1. Query analytics data from Airtable
2. Pull previous reports from Google Drive for comparison
3. Generate new report with insights
4. Save to Google Drive
5. Add comment to Airtable record with link
```

### Example Workflow 3: Content Calendar
```
1. Read content calendar from Google Drive CSV
2. Check Airtable for content status
3. Update calendar with current status
4. Save updated version to Drive
5. Update Notion content tracker
```

---

## Best Practices

### 1. Always Use Absolute Paths for Google Drive
```
✅ Good: /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/file.md
❌ Bad: ~/Google Drive/folder/file.md
❌ Bad: folder/file.md
```

### 2. Test Connections Before Complex Workflows
```
1. List Airtable bases to confirm access
2. Read a simple file from Drive
3. Check Notion resources
4. Then proceed with complex operations
```

### 3. Use Filters to Limit Airtable Results
```
✅ Good: List records with {Status} = 'Active'
❌ Bad: List all records then filter in Claude
```

### 4. Handle Errors Gracefully
```
- Check if files exist before reading
- Verify record IDs before updating
- Confirm base/table names before operations
```

### 5. Document Base IDs and Paths
Keep a reference document with:
- Frequently used Airtable base IDs
- Common Google Drive paths
- Notion database URIs
- Standard filter formulas

### 6. Batch Operations When Possible
```
✅ Good: Update 10 records in one call
❌ Bad: 10 separate update calls
```

### 7. Use Views in Airtable
```
Create views in Airtable UI with pre-configured filters
Reference view name in list_records calls
More maintainable than complex formulas
```

---

## Quick Reference Commands

### Google Drive
```
"Read [file path]"
"Create a file called [name] in [folder]"
"Find all [pattern] files in [folder]"
"Search for '[text]' in [folder]"
"List files in [folder]"
```

### Airtable
```
"List my Airtable bases"
"Show the structure of [table] in [base]"
"Get all records from [table]"
"Find records where [field] = [value]"
"Create a record in [table] with [fields]"
"Update record [ID] to set [field] = [value]"
"Search [table] for '[text]'"
```

### Notion
```
"List available Notion resources"
"Read the Notion resource at [URI]"
```

---

## Troubleshooting

### Google Drive Issues

**Problem**: File not found
- Verify Google Drive Desktop is running and synced
- Check file path is absolute and correct
- Confirm file exists in Google Drive web UI

**Problem**: Permission denied
- Check file permissions in Drive
- Verify Google Drive Desktop has filesystem access
- Try reading a different file to isolate issue

### Airtable Issues

**Problem**: Base not found
- Verify base ID is correct (starts with "app")
- Check API key has access to base
- Confirm base isn't deleted or renamed

**Problem**: Invalid filter formula
- Test formula in Airtable UI first
- Check field names are exact matches
- Verify formula syntax (use curly braces for field names)

**Problem**: Record not updating
- Verify record ID is correct (starts with "rec")
- Check field names match exactly
- Confirm field types match data being sent

### Notion Issues

**Problem**: Resources not appearing
- Check Notion API key is configured
- Verify integration has access to pages/databases
- Confirm MCP server is running

**Problem**: Cannot read resource
- Verify URI format is correct
- Check resource permissions
- Confirm integration has been added to page/database

---

## Advanced Features

### 1. Airtable Formula Filtering

Complex filtering examples:

```javascript
// Active clients with revenue over $5000
AND({Status} = 'Active', {Revenue} > 5000)

// Records created in last 30 days
IS_AFTER({Created}, DATEADD(TODAY(), -30, 'days'))

// Records with empty email
{Email} = BLANK()

// Case-insensitive search
SEARCH(LOWER('keyword'), LOWER({Notes}))
```

### 2. Airtable Sorting

```javascript
// Sort by multiple fields
sort: [
  {field: "Status", direction: "asc"},
  {field: "Created", direction: "desc"}
]
```

### 3. Google Drive Pattern Matching

```bash
# Find all markdown files
**/*.md

# Find files in specific subfolder
01_Sidekick Marketer/**/*.csv

# Find files with specific name pattern
**/client-report-*.md
```

### 4. Google Drive Content Search

```bash
# Case insensitive search
-i flag

# Search with context lines
-C 3 (shows 3 lines before and after)

# Search specific file types
--type md (only markdown files)
```

---

## Security & Privacy

### What Claude Can Access
- All files in synced Google Drive folders
- All Airtable bases associated with API key
- All Notion resources with integration access

### What Claude Cannot Do
- Access files outside Google Drive sync folder
- Access Airtable bases without proper API key
- Access Notion without integration permissions
- Make changes without explicit instruction
- Access the internet or external services (except configured MCP servers)

### Best Practices for Security
1. Never share API keys in conversations
2. Be explicit about which data to access
3. Review outputs before saving to Drive
4. Use specific filters to limit data exposure
5. Regularly audit MCP server configurations

---

## Performance Tips

### 1. Limit Airtable Query Results
```
Use maxRecords parameter to limit results
Default: Returns all records (can be slow)
Better: maxRecords: 100 or use views
```

### 2. Use Airtable Views
```
Pre-configure filters in Airtable UI
Reference view name in queries
Faster than formula filtering
```

### 3. Batch Google Drive Operations
```
Read multiple files in parallel
Use Glob to find files first
Then read only needed files
```

### 4. Cache Frequently Used Data
```
Store Airtable base IDs in a reference file
Keep common paths in documentation
Reuse filter formulas across queries
```

---

## Example Use Cases

### Use Case 1: Weekly Client Report
```
1. Query client metrics from Airtable
2. Pull last week's report from Drive for comparison
3. Generate new report with week-over-week analysis
4. Save to Drive with date-stamped filename
5. Update Airtable record with report link
```

### Use Case 2: Content Production Pipeline
```
1. Read content brief from Drive
2. Query audience data from Airtable
3. Generate content draft
4. Save to Drive in drafts folder
5. Create Airtable record for review tracking
6. Add initial comment with draft status
```

### Use Case 3: Data Migration
```
1. Export records from one Airtable base
2. Transform data format
3. Import to new base
4. Save migration log to Drive
5. Update Notion migration tracker
```

### Use Case 4: Automated Analysis
```
1. Monitor Drive folder for new CSV files
2. Read and analyze data
3. Generate insights document
4. Save analysis to Drive
5. Create Airtable record with findings
6. Add comment with key takeaways
```

---

## Getting Help

### For Setup Issues
- Check MCP server configuration in `.claude.json`
- Verify API keys are set correctly
- Confirm Google Drive Desktop is synced

### For Usage Questions
- See CLAUDE_QUICK_REFERENCE.md for syntax
- See CLAUDE_DATA_ACCESS_GUIDE.md for technical details
- See CLAUDE_DATA_ACCESS_EXAMPLES.md for examples

### For Workflow Ideas
- See CLAUDE_WORKFLOW_EXAMPLES.md for 25+ templates
- Start with simple single-source workflows
- Gradually combine multiple sources

---

## Next Steps

1. **Test Basic Access**
   - Read a file from Google Drive
   - List your Airtable bases
   - Check Notion resources

2. **Try Simple Workflows**
   - Create a file in Drive
   - Query Airtable records
   - Generate a simple report

3. **Build Cross-Source Workflows**
   - Combine data from multiple sources
   - Automate repetitive tasks
   - Create custom reporting pipelines

4. **Optimize Performance**
   - Use filters and views
   - Batch operations
   - Cache common data

5. **Document Your Patterns**
   - Keep track of useful formulas
   - Save common file paths
   - Document workflow sequences

---

## Summary

Claude AI can access and work with:

- **Google Drive**: Direct filesystem access to all synced files
- **Airtable**: 15 specialized tools for complete database operations
- **Notion**: MCP server for workspace resources

This creates powerful possibilities for:
- Automated reporting
- Cross-source data analysis
- Content generation pipelines
- Client management workflows
- Data migration and transformation

Start simple, test connections, then build increasingly sophisticated workflows that combine multiple data sources.

---

**Last Updated**: November 2025
**Status**: Complete and Ready to Use
**Next Steps**: Review Quick Reference guide and try example workflows
