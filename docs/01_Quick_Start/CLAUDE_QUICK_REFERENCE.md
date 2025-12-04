# Claude AI Data Integration - Quick Reference

**Fast syntax reference for Google Drive, Airtable, and Notion operations**

---

## Google Drive Quick Reference

### Base Path
```
/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/
```

### Common Operations

**Read a File**
```
"Read /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/file.md"
```

**Write a File**
```
"Create a file called 'report.md' in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/"
```

**Edit a File**
```
"In the file at [path], replace 'old text' with 'new text'"
```

**Find Files by Pattern**
```
"Find all .md files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/"
Pattern: **/*.md (all markdown files)
Pattern: **/client-*.csv (files starting with 'client-')
```

**Search Within Files**
```
"Search for 'keyword' in all files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/"
```

**List Directory**
```
"List all files in /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/"
```

---

## Airtable Quick Reference

### List Bases
```
Tool: mcp__airtable__list_bases
Example: "Show me all my Airtable bases"
```

### List Tables in Base
```
Tool: mcp__airtable__list_tables
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
Example: "Show tables in base appXXXXXXXXXXXXXX"
```

### Get Table Structure
```
Tool: mcp__airtable__describe_table
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name" or "tblXXXXXXXXXXXXXX"
Example: "Show me the structure of the Clients table"
```

### List All Records
```
Tool: mcp__airtable__list_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
Example: "List all records from the Clients table"
```

### List Records with Filter
```
Tool: mcp__airtable__list_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - filterByFormula: "{Status} = 'Active'"
Example: "Get all active clients from Airtable"
```

### List Records with Sorting
```
Tool: mcp__airtable__list_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - sort: [{"field": "Created", "direction": "desc"}]
Example: "Get clients sorted by creation date"
```

### List Records from View
```
Tool: mcp__airtable__list_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - view: "View Name"
Example: "Get records from the Active Clients view"
```

### Search Records
```
Tool: mcp__airtable__search_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - searchTerm: "keyword"
Example: "Search for 'website' in the Projects table"
```

### Get Single Record
```
Tool: mcp__airtable__get_record
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - recordId: "recXXXXXXXXXXXXXX"
Example: "Get record recXXXXXXXXXXXXXX from Clients"
```

### Create Record
```
Tool: mcp__airtable__create_record
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - fields: {"Field Name": "Value", "Another Field": 123}
Example: "Create a client record with name 'Acme Corp' and status 'Active'"
```

### Update Records (Batch)
```
Tool: mcp__airtable__update_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - records: [
      {"id": "recXXX", "fields": {"Status": "Complete"}},
      {"id": "recYYY", "fields": {"Status": "Complete"}}
    ]
Example: "Update record recXXX to set status to Complete"
```

### Delete Records
```
Tool: mcp__airtable__delete_records
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - recordIds: ["recXXX", "recYYY"]
Example: "Delete record recXXXXXXXXXXXXXX from Clients"
```

### Create Comment
```
Tool: mcp__airtable__create_comment
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - recordId: "recXXXXXXXXXXXXXX"
  - text: "Comment text"
Example: "Add a comment to record recXXX saying 'Review complete'"
```

### List Comments
```
Tool: mcp__airtable__list_comments
Parameters:
  - baseId: "appXXXXXXXXXXXXXX"
  - tableId: "Table Name"
  - recordId: "recXXXXXXXXXXXXXX"
Example: "Show comments on record recXXXXXXXXXXXXXX"
```

---

## Airtable Filter Formulas

### Basic Filters
```javascript
// Exact match
{Status} = 'Active'

// Not equal
{Status} != 'Archived'

// Greater than
{Revenue} > 5000

// Less than
{Created} < '2025-01-01'

// Empty field
{Email} = BLANK()

// Not empty
{Email} != BLANK()
```

### Multiple Conditions
```javascript
// AND (all conditions must be true)
AND({Status} = 'Active', {Revenue} > 5000)

// OR (any condition can be true)
OR({Status} = 'Active', {Status} = 'Pending')

// Complex combinations
AND(
  {Status} = 'Active',
  OR({Type} = 'Client', {Type} = 'Partner'}),
  {Revenue} > 1000
)
```

### Text Searches
```javascript
// Contains text (case-sensitive)
SEARCH('keyword', {Notes})

// Case-insensitive
SEARCH(LOWER('keyword'), LOWER({Notes}))

// Starts with
LEFT({Name}, 5) = 'Acme'

// Ends with
RIGHT({Name}, 4) = 'Corp'
```

### Date Filters
```javascript
// After specific date
IS_AFTER({Created}, '2025-01-01')

// Before specific date
IS_BEFORE({Deadline}, '2025-12-31')

// Between dates
AND(
  IS_AFTER({Created}, '2025-01-01'),
  IS_BEFORE({Created}, '2025-12-31')
)

// Last 30 days
IS_AFTER({Created}, DATEADD(TODAY(), -30, 'days'))

// This month
AND(
  IS_AFTER({Created}, DATETIME_FORMAT(TODAY(), 'YYYY-MM-01')),
  IS_BEFORE({Created}, DATEADD(DATETIME_FORMAT(TODAY(), 'YYYY-MM-01'), 1, 'month'))
)
```

### Number Filters
```javascript
// Greater than
{Revenue} > 5000

// Between range
AND({Revenue} >= 1000, {Revenue} <= 10000)

// Top performers
{Revenue} > AVERAGE({Revenue})
```

### Checkbox Filters
```javascript
// Checked
{IsActive} = 1

// Unchecked
{IsActive} = 0
```

### Link Fields
```javascript
// Has linked records
{LinkedTable} != BLANK()

// No linked records
{LinkedTable} = BLANK()
```

---

## Notion Quick Reference

### List Available Resources
```
Tool: ListMcpResourcesTool
Example: "Show me all available Notion resources"
```

### Read Specific Resource
```
Tool: ReadMcpResourceTool
Parameters:
  - server: "notion"
  - uri: "notion://database/xxx"
Example: "Read the Notion database at notion://database/xxx"
```

---

## Common Workflows

### Workflow 1: Read Airtable, Save to Drive
```
1. "List all active clients from Airtable"
2. "Create a report from this data and save it to Google Drive"
```

### Workflow 2: Drive to Airtable
```
1. "Read the CSV file at [path]"
2. "Create Airtable records from this data"
```

### Workflow 3: Cross-Reference Data
```
1. "Get client list from Airtable"
2. "Check which clients have folders in Google Drive"
3. "Create a report of missing folders"
```

### Workflow 4: Update from Analysis
```
1. "Read the data file from Drive"
2. "Analyze the data"
3. "Update Airtable records with the findings"
```

---

## Quick Troubleshooting

### Google Drive
```
Issue: File not found
Fix: Check absolute path, verify sync

Issue: Permission denied
Fix: Check file permissions in Drive UI

Issue: Folder not accessible
Fix: Verify Google Drive Desktop is running
```

### Airtable
```
Issue: Base not found
Fix: Verify base ID starts with "app"

Issue: Invalid filter
Fix: Test formula in Airtable UI first

Issue: Record not updating
Fix: Check record ID starts with "rec"

Issue: Field not found
Fix: Verify field name matches exactly (case-sensitive)
```

### Notion
```
Issue: Resources not appearing
Fix: Check Notion integration is configured

Issue: Cannot read resource
Fix: Verify integration has page/database access
```

---

## ID Format Reference

### Airtable IDs
```
Base ID: appXXXXXXXXXXXXXX (17 characters, starts with "app")
Table ID: tblXXXXXXXXXXXXXX (17 characters, starts with "tbl")
Record ID: recXXXXXXXXXXXXXX (17 characters, starts with "rec")
Field ID: fldXXXXXXXXXXXXXX (17 characters, starts with "fld")
```

Note: Table names and field names can be used instead of IDs in most operations.

---

## Tips & Best Practices

### Google Drive
- Always use absolute paths
- Use Glob for file discovery before reading
- Batch read operations when possible
- Check file exists before operations

### Airtable
- List bases first to confirm access
- Use describe_table to check field names
- Use filters to limit results
- Test formulas in Airtable UI first
- Batch updates (up to 10 records)
- Use views for complex filtering

### Notion
- List resources first to see what's available
- Verify URIs before reading
- Check integration permissions

### General
- Test simple operations before complex workflows
- Handle errors gracefully
- Document common IDs and paths
- Use specific filters to limit data

---

## Environment Variables Reference

### Required for Airtable
```
AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX
```

### Required for Notion
```
NOTION_API_KEY=secret_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

These are configured in `.claude.json` MCP server settings.

---

## Quick Command Templates

### Google Drive
```
"Read [full path]"
"Create [filename] in [full path to folder]"
"Find all [pattern] in [full path]"
"Search for '[text]' in [full path]"
"List files in [full path]"
```

### Airtable
```
"List my Airtable bases"
"Show structure of [table] in [base]"
"Get all [table] records"
"Get [table] records where [field] = [value]"
"Create [table] record with [field]: [value]"
"Update record [ID] set [field] = [value]"
"Search [table] for '[text]'"
```

### Cross-Source
```
"Read [data] from Airtable and save to Drive"
"Get [file] from Drive and create Airtable records"
"Compare Airtable [table] with Drive [file]"
"Generate [report] from Airtable and save to Drive"
```

---

## Cheat Sheet

### Most Common Operations

1. **List Airtable Bases**: `mcp__airtable__list_bases`
2. **List Table Records**: `mcp__airtable__list_records` with baseId and tableId
3. **Read Drive File**: Use absolute path with Read tool
4. **Create Drive File**: Use absolute path with Write tool
5. **Search Airtable**: `mcp__airtable__search_records` with searchTerm
6. **Update Airtable**: `mcp__airtable__update_records` with records array
7. **Find Drive Files**: Glob with pattern like `**/*.md`

### Most Common Filters

1. **Active Status**: `{Status} = 'Active'`
2. **Recent Records**: `IS_AFTER({Created}, DATEADD(TODAY(), -30, 'days'))`
3. **Not Empty**: `{Field} != BLANK()`
4. **Text Search**: `SEARCH('keyword', {Field})`
5. **Multiple Status**: `OR({Status} = 'Active', {Status} = 'Pending')`

---

**Last Updated**: November 2025
**Quick Tip**: Bookmark this page for fast reference during workflows
