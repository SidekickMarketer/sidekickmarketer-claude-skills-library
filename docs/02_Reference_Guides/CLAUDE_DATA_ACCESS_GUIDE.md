# Claude AI Data Access - Technical Reference Guide

**Comprehensive technical documentation for all data access methods**

---

## Table of Contents

1. [Google Drive Local Filesystem Access](#google-drive-local-filesystem-access)
2. [Airtable MCP Server](#airtable-mcp-server)
3. [Notion MCP Server](#notion-mcp-server)
4. [Cross-Source Integration Patterns](#cross-source-integration-patterns)
5. [Performance Optimization](#performance-optimization)
6. [Error Handling](#error-handling)
7. [Security Considerations](#security-considerations)

---

## Google Drive Local Filesystem Access

### Architecture

Claude accesses Google Drive through macOS filesystem integration. Google Drive Desktop creates a local mount point that syncs files bidirectionally.

**Mount Point:**
```
/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/
```

**Sync Mechanism:**
- Files are synced in real-time by Google Drive Desktop
- Changes made locally sync to cloud automatically
- Claude operations are standard filesystem operations
- No special API or authentication required

### Available Tools

#### 1. Read Tool
**Purpose**: Read file contents

**Parameters:**
- `file_path` (required): Absolute path to file
- `offset` (optional): Line number to start reading from
- `limit` (optional): Number of lines to read

**Supported File Types:**
- Text files (.txt, .md, .csv, .json, .xml, .yml, .log)
- Images (PNG, JPG, etc.) - visual display
- PDFs - text and visual extraction
- Jupyter notebooks (.ipynb) - all cells with outputs

**Line Limit:**
- Default: 2000 lines from beginning
- Lines >2000 characters are truncated
- Use offset/limit for large files

**Example:**
```
Read file at /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/file.md
```

#### 2. Write Tool
**Purpose**: Create new files or overwrite existing files

**Parameters:**
- `file_path` (required): Absolute path for new file
- `content` (required): Full file content

**Behavior:**
- Overwrites existing files completely
- Creates parent directories if needed
- Must Read existing files before overwriting
- Syncs to Google Drive automatically

**Best Practices:**
- Always Read before Write for existing files
- Use Edit tool for modifications instead
- Verify path before writing
- Check if file exists first

**Example:**
```
Write new file to /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/reports/analysis.md
```

#### 3. Edit Tool
**Purpose**: Make precise modifications to existing files

**Parameters:**
- `file_path` (required): Absolute path to file
- `old_string` (required): Exact text to replace
- `new_string` (required): Replacement text
- `replace_all` (optional): Replace all occurrences (default: false)

**Requirements:**
- Must Read file first in conversation
- old_string must be unique (unless replace_all = true)
- Preserves exact indentation and formatting
- Line numbers in Read output are for reference only

**Example:**
```
Edit file to replace "Draft" with "Final" in status field
```

#### 4. Glob Tool
**Purpose**: Find files matching patterns

**Parameters:**
- `pattern` (required): Glob pattern to match
- `path` (optional): Directory to search (default: current working directory)

**Pattern Syntax:**
- `*.md` - All markdown files in current directory
- `**/*.md` - All markdown files recursively
- `**/client-*.csv` - Files starting with "client-"
- `folder/**/*.{md,txt}` - Multiple extensions

**Returns:**
- List of matching file paths
- Sorted by modification time
- Works with any codebase size

**Example:**
```
Find all markdown files: pattern "**/*.md"
Find client reports: pattern "**/client-report-*.md"
```

#### 5. Grep Tool
**Purpose**: Search file contents with regex

**Parameters:**
- `pattern` (required): Regex pattern to search
- `path` (optional): Directory or file to search
- `output_mode` (optional): "content" | "files_with_matches" | "count"
- `-i` (optional): Case insensitive
- `-A`, `-B`, `-C` (optional): Context lines
- `glob` (optional): Filter by file pattern
- `type` (optional): Filter by file type
- `multiline` (optional): Enable multiline matching

**Output Modes:**
- `files_with_matches`: List files containing pattern (default)
- `content`: Show matching lines with context
- `count`: Show match counts per file

**Example:**
```
Search for "client" in all markdown files
pattern: "client"
glob: "*.md"
output_mode: "content"
```

#### 6. Bash Tool
**Purpose**: Execute filesystem commands

**Use Cases:**
- List directory contents (ls)
- Check file existence (test -f)
- Get file info (stat)
- Navigate directory structure

**Important:**
- DO NOT use for file reading (use Read instead)
- DO NOT use for file writing (use Write instead)
- DO NOT use grep/find commands (use Grep/Glob instead)
- Use for git, npm, docker, etc.

**Example:**
```bash
ls -la "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/"
```

### Path Handling

#### Absolute Paths Required
```
✅ /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/folder/file.md
❌ ~/Google Drive/folder/file.md
❌ folder/file.md
❌ ./file.md
```

#### Special Characters in Paths
When using Bash tool, quote paths with spaces:
```bash
✅ ls "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/"
❌ ls /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/
```

For Read/Write/Edit tools, no quotes needed.

### Sync Considerations

**Real-time Sync:**
- Changes sync within seconds typically
- Large files may take longer
- Check sync status in Google Drive Desktop

**Conflict Resolution:**
- Google Drive handles conflicts automatically
- Creates conflict copies if needed
- Monitor sync status for issues

**Offline Mode:**
- Files must be synced locally to access
- Check "Available offline" in Drive settings
- Verify sync before critical operations

---

## Airtable MCP Server

### Architecture

Airtable access is provided through a Model Context Protocol (MCP) server that exposes specialized tools as Claude functions.

**Configuration Location:**
`.claude.json` (MCP servers section)

**Authentication:**
Environment variable: `AIRTABLE_API_KEY`

**Base URL:**
https://api.airtable.com/v0/

### Tool Reference

#### Base & Schema Discovery

##### 1. list_bases
**Purpose**: List all accessible Airtable bases

**Parameters:** None

**Returns:**
```json
{
  "bases": [
    {
      "id": "appXXXXXXXXXXXXXX",
      "name": "Base Name",
      "permissionLevel": "create"
    }
  ]
}
```

**Use Cases:**
- Discover available bases
- Confirm API access
- Get base IDs for other operations

##### 2. list_tables
**Purpose**: List tables in a base

**Parameters:**
- `baseId` (required): Base ID (appXXX...)
- `detailLevel` (optional): "tableIdentifiersOnly" | "identifiersOnly" | "full"

**Returns:**
```json
{
  "tables": [
    {
      "id": "tblXXXXXXXXXXXXXX",
      "name": "Table Name",
      "description": "Table description",
      "primaryFieldId": "fldXXXXXXXXXXXXXX",
      "fields": [...],
      "views": [...]
    }
  ]
}
```

**Detail Levels:**
- `tableIdentifiersOnly`: Just table IDs and names
- `identifiersOnly`: Includes field IDs but not full schema
- `full`: Complete schema with field types, views, etc.

##### 3. describe_table
**Purpose**: Get detailed table structure

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `detailLevel` (optional): Same as list_tables

**Returns:**
```json
{
  "id": "tblXXXXXXXXXXXXXX",
  "name": "Table Name",
  "fields": [
    {
      "id": "fldXXXXXXXXXXXXXX",
      "name": "Field Name",
      "type": "singleLineText",
      "options": {...}
    }
  ],
  "views": [...]
}
```

**Use Cases:**
- Discover field names and types
- Check available views
- Understand table structure before operations

#### Record Operations

##### 4. list_records
**Purpose**: Query records from a table

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `filterByFormula` (optional): Airtable formula for filtering
- `maxRecords` (optional): Limit number of results
- `sort` (optional): Array of sort objects
- `view` (optional): View name or ID

**Sort Object Structure:**
```json
{
  "field": "Field Name",
  "direction": "asc" | "desc"
}
```

**Returns:**
```json
{
  "records": [
    {
      "id": "recXXXXXXXXXXXXXX",
      "createdTime": "2025-01-01T00:00:00.000Z",
      "fields": {
        "Field Name": "Value",
        "Another Field": 123
      }
    }
  ],
  "offset": "recXXX/tblXXX" // For pagination
}
```

**Pagination:**
- Returns up to 100 records by default
- Use `offset` from response for next page
- Or use `maxRecords` to limit

**Performance Tips:**
- Use `filterByFormula` to limit results
- Use `view` parameter for pre-filtered data
- Use `maxRecords` to prevent large responses

##### 5. search_records
**Purpose**: Full-text search across records

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `searchTerm` (required): Text to search for
- `fieldIds` (optional): Limit search to specific fields
- `maxRecords` (optional): Limit results
- `view` (optional): Search within specific view

**Returns:** Same structure as list_records

**Search Behavior:**
- Searches all text and number fields by default
- Case-insensitive
- Partial matches included
- Use `fieldIds` to focus search

##### 6. get_record
**Purpose**: Retrieve single record by ID

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `recordId` (required): Record ID (recXXX...)

**Returns:**
```json
{
  "id": "recXXXXXXXXXXXXXX",
  "createdTime": "2025-01-01T00:00:00.000Z",
  "fields": {
    "Field Name": "Value"
  }
}
```

**Use Cases:**
- Verify record exists before update
- Get current values before modification
- Fetch specific record details

##### 7. create_record
**Purpose**: Create new record in table

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `fields` (required): Object with field names and values

**Fields Object:**
```json
{
  "Field Name": "Value",
  "Number Field": 123,
  "Checkbox Field": true,
  "Multiple Select": ["Option 1", "Option 2"],
  "Linked Records": ["recXXX", "recYYY"]
}
```

**Returns:**
```json
{
  "id": "recXXXXXXXXXXXXXX",
  "createdTime": "2025-01-01T00:00:00.000Z",
  "fields": {...}
}
```

**Field Type Guidelines:**
- Single line text: String
- Long text: String
- Number: Number
- Checkbox: Boolean (true/false)
- Single select: String
- Multiple select: Array of strings
- Date: ISO 8601 string
- Linked records: Array of record IDs
- Attachments: Array of attachment objects

##### 8. update_records
**Purpose**: Update multiple records (batch operation)

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `records` (required): Array of update objects (max 10)

**Records Array:**
```json
[
  {
    "id": "recXXXXXXXXXXXXXX",
    "fields": {
      "Field Name": "New Value"
    }
  },
  {
    "id": "recYYYYYYYYYYYYYY",
    "fields": {
      "Field Name": "Another Value"
    }
  }
]
```

**Returns:**
```json
{
  "records": [
    {
      "id": "recXXXXXXXXXXXXXX",
      "createdTime": "2025-01-01T00:00:00.000Z",
      "fields": {...}
    }
  ]
}
```

**Limitations:**
- Maximum 10 records per call
- Only specified fields are updated
- Other fields remain unchanged
- Returns updated records

##### 9. delete_records
**Purpose**: Delete records from table

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `recordIds` (required): Array of record IDs to delete

**Returns:**
```json
{
  "records": [
    {
      "id": "recXXXXXXXXXXXXXX",
      "deleted": true
    }
  ]
}
```

**Caution:**
- Permanent deletion (no undo)
- Verify record IDs before deleting
- Consider archiving instead (status field)

#### Table Management

##### 10. create_table
**Purpose**: Create new table in base

**Parameters:**
- `baseId` (required): Base ID
- `name` (required): Table name
- `fields` (required): Array of field definitions
- `description` (optional): Table description

**Field Definition:**
```json
{
  "name": "Field Name",
  "type": "singleLineText",
  "options": {...} // Type-specific options
}
```

**Common Field Types:**
- `singleLineText`: Simple text
- `multilineText`: Long text
- `number`: Numeric values
- `checkbox`: Boolean
- `singleSelect`: Dropdown
- `multipleSelects`: Multi-select
- `date`: Date field
- `linkedRecords`: Link to another table

##### 11. update_table
**Purpose**: Update table metadata

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `name` (optional): New table name
- `description` (optional): New description

**Note:** Cannot modify fields or records, only table metadata

##### 12. create_field
**Purpose**: Add new field to table

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `nested` (required): Object containing field definition

**Nested Object:**
```json
{
  "field": {
    "name": "New Field",
    "type": "singleLineText",
    "description": "Field description",
    "options": {...}
  }
}
```

##### 13. update_field
**Purpose**: Modify field metadata

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `fieldId` (required): Field ID
- `name` (optional): New field name
- `description` (optional): New description

**Note:** Cannot change field type, only name and description

#### Collaboration

##### 14. create_comment
**Purpose**: Add comment to record

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `recordId` (required): Record ID
- `text` (required): Comment text
- `parentCommentId` (optional): For threaded replies

**Returns:**
```json
{
  "id": "comXXXXXXXXXXXXXX",
  "text": "Comment text",
  "createdTime": "2025-01-01T00:00:00.000Z",
  "author": {...}
}
```

##### 15. list_comments
**Purpose**: Get comments on record

**Parameters:**
- `baseId` (required): Base ID
- `tableId` (required): Table name or ID
- `recordId` (required): Record ID
- `pageSize` (optional): Results per page (max 100)
- `offset` (optional): Pagination offset

**Returns:**
```json
{
  "comments": [
    {
      "id": "comXXXXXXXXXXXXXX",
      "text": "Comment text",
      "createdTime": "2025-01-01T00:00:00.000Z",
      "author": {...}
    }
  ],
  "offset": "comXXX"
}
```

### Formula Reference

#### Operators
```javascript
// Comparison
=, !=, <, >, <=, >=

// Logical
AND(), OR(), NOT()

// Arithmetic
+, -, *, /

// String
&, CONCATENATE()
```

#### Common Functions
```javascript
// Text
SEARCH(string, text)
LOWER(text)
UPPER(text)
LEFT(text, count)
RIGHT(text, count)
MID(text, start, count)
LEN(text)

// Logic
IF(condition, ifTrue, ifFalse)
SWITCH(expression, pattern1, result1, ...)

// Date
TODAY()
NOW()
DATEADD(date, count, units)
IS_AFTER(date1, date2)
IS_BEFORE(date1, date2)
DATETIME_FORMAT(date, format)

// Check
BLANK()
ERROR()

// Aggregation
COUNT(values)
SUM(numbers)
AVERAGE(numbers)
MAX(numbers)
MIN(numbers)
```

#### Field References
```javascript
{Field Name}  // Reference field value
```

### Error Codes

**Common Errors:**
- `INVALID_REQUEST_BODY`: Malformed parameters
- `INVALID_FILTER_FORMULA`: Formula syntax error
- `MODEL_ID_NOT_FOUND`: Base/table/record doesn't exist
- `NOT_AUTHORIZED`: Permission denied
- `RATE_LIMIT_EXCEEDED`: Too many requests

---

## Notion MCP Server

### Architecture

Notion access through MCP server for reading workspace resources.

**Configuration Location:**
`.claude.json` (MCP servers section)

**Authentication:**
Environment variable: `NOTION_API_KEY`

### Available Tools

#### 1. ListMcpResourcesTool
**Purpose**: Discover available Notion resources

**Parameters:**
- `server` (optional): Filter by server name

**Returns:**
List of resources with:
- URI
- Name
- Type
- Description
- Server

#### 2. ReadMcpResourceTool
**Purpose**: Read specific Notion resource

**Parameters:**
- `server` (required): Server name ("notion")
- `uri` (required): Resource URI

**URI Format:**
```
notion://database/{database_id}
notion://page/{page_id}
```

### Setup Requirements

1. Create Notion integration
2. Grant integration access to pages/databases
3. Set NOTION_API_KEY environment variable
4. Configure MCP server in .claude.json

---

## Cross-Source Integration Patterns

### Pattern 1: Airtable → Analysis → Drive
```
1. Query data from Airtable
2. Analyze in Claude
3. Generate report
4. Save to Google Drive
5. Update Airtable with report link
```

### Pattern 2: Drive → Transform → Airtable
```
1. Read CSV from Drive
2. Transform/clean data
3. Create Airtable records
4. Log results to Drive
```

### Pattern 3: Multi-Source Reporting
```
1. Read template from Drive
2. Query metrics from Airtable
3. Read previous reports from Drive
4. Generate comparison report
5. Save to Drive
6. Update Notion tracker
```

### Pattern 4: Monitoring & Updates
```
1. Monitor Drive folder for new files
2. Process file contents
3. Create/update Airtable records
4. Generate summary
5. Save to Drive
6. Add Airtable comment
```

---

## Performance Optimization

### Google Drive
- Use Glob before Read to verify files exist
- Read multiple files in parallel when possible
- Use Edit instead of Read + Write for modifications
- Cache frequently accessed data

### Airtable
- Use `filterByFormula` to limit results
- Use `maxRecords` to cap response size
- Use views for complex filtering
- Batch updates (up to 10 records)
- Cache base/table IDs
- Use `describe_table` once, cache field names

### General
- Minimize API calls
- Batch operations
- Cache static data
- Use specific filters
- Limit result sets

---

## Error Handling

### Google Drive Errors

**File Not Found:**
```
Check: Path is absolute
Check: File exists in Drive
Check: Google Drive is synced
```

**Permission Denied:**
```
Check: File permissions in Drive UI
Check: Google Drive Desktop has access
Check: File isn't locked by another process
```

**Sync Issues:**
```
Check: Google Drive Desktop is running
Check: Internet connection
Check: Sync status in Drive UI
Wait: Large files may take time to sync
```

### Airtable Errors

**Invalid Base ID:**
```
Verify: ID starts with "app"
Verify: Base exists and is accessible
Check: API key has base access
```

**Invalid Formula:**
```
Test: Formula in Airtable UI first
Check: Field names are exact (case-sensitive)
Check: Syntax (curly braces for fields)
Simplify: Break complex formulas into parts
```

**Record Not Found:**
```
Verify: Record ID starts with "rec"
Check: Record wasn't deleted
Verify: Table name is correct
```

**Rate Limiting:**
```
Airtable: 5 requests per second per base
Solution: Add delays between calls
Solution: Batch operations
Solution: Use caching
```

### Notion Errors

**Integration Not Configured:**
```
Check: NOTION_API_KEY is set
Verify: Integration exists in Notion
Check: MCP server configuration
```

**Access Denied:**
```
Check: Integration added to page/database
Verify: Correct permissions granted
Check: Resource URI is valid
```

---

## Security Considerations

### API Keys
- Never expose in conversations
- Store in environment variables
- Rotate regularly
- Limit permissions to needed scopes

### Data Access
- Claude can access all data API key allows
- Be explicit about what to access
- Use filters to limit exposure
- Review outputs before saving

### File Operations
- Claude can read/write/delete files in Drive
- Verify paths before operations
- Check outputs before saving
- Keep backups of important files

### Best Practices
1. Use least-privilege API keys
2. Verify operations before executing
3. Review generated content
4. Keep audit logs
5. Monitor API usage
6. Use specific filters
7. Limit data exposure

---

**Last Updated**: November 2025
**Status**: Complete Technical Reference
