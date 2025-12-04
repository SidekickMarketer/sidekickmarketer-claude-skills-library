# Notion Structure Best Practices for Claude AI

## 📋 Overview

This guide shows you how to structure your Notion workspace to make it easy for Claude to query, search, and use your data via the Notion MCP server.

**Key Principle:** The clearer and more consistent your Notion structure, the easier it is for Claude to understand and use your data.

---

## 🎯 Core Principles

### 1. **Use Databases, Not Just Pages**
Claude works best with structured data in **databases**, not unstructured text in pages.

✅ **Good:**
```
Clients Database
├── Property: Client Name (Title)
├── Property: Status (Select)
├── Property: Industry (Select)
├── Property: Start Date (Date)
└── Property: Contact Email (Email)
```

❌ **Less Ideal:**
```
Clients Page
└── Bullet list of client names and info
```

### 2. **Use Consistent Property Names**
Make property names clear, consistent, and descriptive.

✅ **Good:**
- `Client Name`
- `Project Status`
- `Due Date`
- `Assigned To`

❌ **Avoid:**
- `name` (too generic)
- `stat` (abbreviation)
- `when is it due?` (question format)
- `Person Responsible for This Task` (too long)

### 3. **Use Standard Property Types**
Claude handles standard Notion property types best.

**Recommended Property Types:**
- ✅ **Title** - Main identifier
- ✅ **Text** - Short text fields
- ✅ **Select** - Single choice from options
- ✅ **Multi-select** - Multiple choices
- ✅ **Date** - Dates and date ranges
- ✅ **Number** - Numeric values
- ✅ **Checkbox** - Boolean values
- ✅ **Email** - Email addresses
- ✅ **Phone** - Phone numbers
- ✅ **URL** - Links
- ✅ **Relation** - Links to other databases
- ✅ **Rollup** - Calculated from relations

**Use Sparingly:**
- ⚠️ **Formula** - Can be queried but not always readable
- ⚠️ **Files & Media** - Can be accessed but harder to query

### 4. **Use Select Fields for Categories**
Use **Select** or **Multi-select** instead of free text for categories.

✅ **Good:**
```
Status: Active | Inactive | Pending
Priority: High | Medium | Low
Industry: Technology | Healthcare | Finance | Retail
```

❌ **Avoid:**
```
Status: (text field where users type "active", "Active", "ACTIVE", etc.)
```

---

## 🗂️ Database Structure Guidelines

### Ideal Database Setup

```
Database Name: Clients
├── 📌 Client Name (Title) - Required, unique identifier
├── 📧 Email (Email) - Contact information
├── 📞 Phone (Phone) - Contact information
├── 🏷️ Status (Select) - Active | Inactive | Pending
├── 🏭 Industry (Select) - Predefined categories
├── 📅 Start Date (Date) - When relationship began
├── 💰 Monthly Retainer (Number) - Revenue tracking
├── ✅ Onboarding Complete (Checkbox) - Boolean status
├── 👤 Account Manager (Person) - Who manages this client
├── 🔗 Active Projects (Relation) - Links to Projects database
└── 📊 Total Project Value (Rollup) - Sum from Active Projects
```

### Why This Works Well:

1. **Clear Title Field** - Every database needs a clear Title property
2. **Structured Categories** - Select fields instead of free text
3. **Standard Types** - Uses standard Notion property types
4. **Relations** - Connects to other databases logically
5. **Rollups** - Aggregates data from related databases

---

## 📊 Recommended Database Structures

### Example 1: Client Database

```
Database: Clients
Properties:
├── Client Name (Title)
├── Status (Select: Active, Inactive, Prospect)
├── Industry (Select: Tech, Finance, Healthcare, etc.)
├── Start Date (Date)
├── Contract Value (Number)
├── Account Manager (Person)
├── Primary Contact Email (Email)
├── Website (URL)
├── Active Projects (Relation → Projects)
├── Total Revenue (Rollup from Projects)
└── Notes (Text)
```

### Example 2: Projects Database

```
Database: Projects
Properties:
├── Project Name (Title)
├── Client (Relation → Clients)
├── Status (Select: Planning, In Progress, Completed, On Hold)
├── Priority (Select: High, Medium, Low)
├── Start Date (Date)
├── End Date (Date)
├── Budget (Number)
├── Project Lead (Person)
├── Tasks (Relation → Tasks)
├── Completion % (Rollup from Tasks)
└── Description (Text)
```

### Example 3: Tasks Database

```
Database: Tasks
Properties:
├── Task Name (Title)
├── Project (Relation → Projects)
├── Status (Select: To Do, In Progress, Done)
├── Priority (Select: High, Medium, Low)
├── Assigned To (Person)
├── Due Date (Date)
├── Completed (Checkbox)
├── Estimated Hours (Number)
├── Actual Hours (Number)
└── Notes (Text)
```

### Example 4: Content Calendar Database

```
Database: Content Calendar
Properties:
├── Title (Title)
├── Type (Select: Blog Post, Social Media, Email, Video)
├── Platform (Multi-select: LinkedIn, Twitter, Instagram, etc.)
├── Status (Select: Draft, Review, Scheduled, Published)
├── Author (Person)
├── Publish Date (Date)
├── Target Audience (Multi-select: Prospects, Clients, Partners)
├── Topic Tags (Multi-select: SEO, Marketing, Sales, etc.)
├── URL (URL)
└── Performance Notes (Text)
```

---

## 🔗 Using Relations Effectively

### Best Practices for Relations

1. **Create Logical Connections**
   - Clients → Projects (one-to-many)
   - Projects → Tasks (one-to-many)
   - Tasks → People (many-to-many)

2. **Use Descriptive Relation Names**
   - ✅ `Active Projects` (not just "Projects")
   - ✅ `Assigned Team Members` (not just "People")
   - ✅ `Related Documents` (not just "Links")

3. **Set Up Bi-directional Relations**
   - When you create a relation, Notion automatically creates the reverse
   - Name both sides clearly:
     - Clients DB: "Active Projects"
     - Projects DB: "Client"

### Example Relation Structure

```
Clients Database
└── Active Projects (Relation → Projects)
    ↓
Projects Database
├── Client (Relation → Clients)
└── Tasks (Relation → Tasks)
    ↓
Tasks Database
├── Project (Relation → Projects)
└── Assigned To (Person)
```

---

## 🏷️ Select Field Best Practices

### Standardize Your Select Options

**Status Fields** - Use consistent status naming across databases:
```
To Do → In Progress → Done
Draft → Review → Approved → Published
Active → Inactive → Archived
```

**Priority Fields** - Keep it simple:
```
High | Medium | Low
or
P0 | P1 | P2 | P3
```

**Category Fields** - Create comprehensive but manageable lists:
```
✅ Good: 5-15 options (Industry: Tech, Finance, Healthcare, Retail, etc.)
❌ Too Many: 50+ options (hard to manage)
❌ Too Few: 2 options (use checkbox instead)
```

### Color Coding for Visual Clarity

Use Notion's color options consistently:
- 🔴 Red - Urgent, High Priority, Overdue
- 🟡 Yellow - In Progress, Pending
- 🟢 Green - Completed, Active, Approved
- 🔵 Blue - Information, Low Priority
- ⚪ Gray - Archived, Inactive

---

## 📝 Page Organization

### Database Pages vs. Regular Pages

**For structured data Claude needs to query:**
- ✅ Use databases
- Make pages templates within databases
- Fill out properties consistently

**For documentation Claude needs to read:**
- ✅ Use regular pages
- Use clear headings (H1, H2, H3)
- Break content into sections
- Use bullet points and numbered lists

### Page Content Best Practices

When Claude reads page content, structure helps:

✅ **Good Structure:**
```markdown
# Project Overview

## Objectives
- Objective 1
- Objective 2

## Timeline
Start Date: Jan 1, 2025
End Date: Mar 31, 2025

## Team
- Project Lead: John Doe
- Developer: Jane Smith

## Key Deliverables
1. Deliverable 1
2. Deliverable 2
```

❌ **Less Structured:**
```
just a bunch of text describing the project without clear sections
or headings and it's hard to extract specific information quickly
when querying programmatically
```

---

## 🔍 Making Data Queryable

### Use Filters Effectively

Claude can query with filters. Make your data filterable:

**Example Queries Claude Can Run:**

1. **Get all active clients:**
   - Filter: `Status = "Active"`

2. **Get high-priority tasks due this week:**
   - Filter: `Priority = "High" AND Due Date is this week`

3. **Get completed projects in Q1 2025:**
   - Filter: `Status = "Completed" AND End Date is in Q1 2025`

### Properties That Make Data Easy to Filter

✅ **Filterable:**
- Select fields (Status, Priority, Category)
- Date fields (Start Date, Due Date)
- Checkbox fields (Completed, Active)
- Number fields (Budget, Revenue)
- Person fields (Assigned To, Owner)

⚠️ **Less Filterable:**
- Long text fields
- Formula fields (depends on complexity)
- Rich text content

---

## 🎨 Template Best Practices

### Create Database Templates

For consistent data entry, create templates:

**Client Onboarding Template:**
```
Properties Pre-filled:
- Status: "Prospect"
- Onboarding Complete: Unchecked
- Start Date: [empty]

Page Content:
# Welcome [Client Name]

## Onboarding Checklist
- [ ] Contract signed
- [ ] Initial meeting scheduled
- [ ] Access granted
- [ ] Kickoff complete

## Key Contacts
- Primary:
- Secondary:

## Notes
[Space for notes]
```

This ensures every new client entry has:
- Consistent structure
- Required fields
- Standard checklist

---

## 🚫 Common Pitfalls to Avoid

### 1. **Inconsistent Naming**
❌ Don't use:
- "Client Name", "client_name", "clientName" in different databases
- "In Progress", "In-Progress", "InProgress" in select fields

✅ Do use:
- Consistent casing: "Client Name" everywhere
- Consistent select values: "In Progress" (with space) everywhere

### 2. **Overly Complex Formulas**
❌ Avoid complex nested formulas that are hard to parse
✅ Use simple formulas or rollups instead

### 3. **Free Text Instead of Select Fields**
❌ Text field where users type status
✅ Select field with predefined options

### 4. **No Clear Identifier**
❌ Database without a clear Title field
✅ Every database has a clear, unique Title property

### 5. **Nested Databases**
❌ Databases inside pages inside databases (too deep)
✅ Flat structure with relations connecting them

### 6. **Duplicate Information**
❌ Same data stored in multiple places
✅ Use relations and rollups to reference data

---

## 🔐 Granting Access to Claude

### Required Steps for Notion MCP

1. **Create/Verify Integration**
   - Go to: https://www.notion.so/profile/integrations
   - Create internal integration or verify existing
   - Copy integration token

2. **Grant Page Access**
   For each database or page Claude needs to access:
   - Open the database/page
   - Click "•••" (three dots) in top right
   - Click "Connections"
   - Select your integration
   - Click "Confirm"

3. **Grant Access to Parent Pages**
   - If database is inside a page, grant access to parent page too
   - Integration inherits access to child pages/databases

### Access Permissions Best Practices

✅ **Do:**
- Grant access to specific databases Claude needs
- Start with read-only access (default)
- Test with one database first
- Expand access as needed

⚠️ **Be Careful:**
- Don't grant access to personal/sensitive pages
- Don't give access to entire workspace initially
- Review what's shared regularly

---

## 📊 Recommended Workspace Structure

### Organized Workspace for Claude Access

```
Notion Workspace
│
├── 📁 Clients & Projects (Share with Claude)
│   ├── Clients Database
│   ├── Projects Database
│   └── Tasks Database
│
├── 📁 Content & Marketing (Share with Claude)
│   ├── Content Calendar Database
│   ├── Campaign Tracker Database
│   └── Marketing Assets Database
│
├── 📁 Operations (Share with Claude)
│   ├── SOPs Database
│   ├── Meeting Notes Database
│   └── Documentation Database
│
├── 📁 Personal (Don't Share)
│   └── Personal notes, private info
│
└── 📁 Archive (Optional Share)
    └── Historical data
```

### Why This Works:

1. **Clear Boundaries** - Easy to control what Claude accesses
2. **Logical Grouping** - Related databases together
3. **Easy Permissions** - Grant access by folder
4. **Scalable** - Easy to add new databases

---

## 🎯 Quick Setup Checklist

Use this checklist when creating a new Notion database for Claude:

### Database Setup
- [ ] Clear, descriptive database name
- [ ] Title property is meaningful and unique
- [ ] Status field uses Select (not text)
- [ ] Category fields use Select/Multi-select
- [ ] Date fields for temporal data
- [ ] Relations to other relevant databases
- [ ] Rollups for aggregated data
- [ ] Properties have clear, consistent names

### Access & Integration
- [ ] Integration created in Notion settings
- [ ] Database shared with integration
- [ ] Parent pages (if any) shared with integration
- [ ] Tested access with simple query

### Data Quality
- [ ] Sample entries created
- [ ] Select field options defined
- [ ] Templates created (if needed)
- [ ] Duplicate entries removed
- [ ] Required fields filled

---

## 💡 Pro Tips

### 1. **Use Database Views for Claude**

Create filtered views for common queries:
- "Active Clients" view (Status = Active)
- "This Week's Tasks" view (Due Date = This Week)
- "High Priority Projects" view (Priority = High)

Claude can query specific views: "Get records from 'Active Clients' view"

### 2. **Keep Property Lists Manageable**

Too many properties make databases hard to query:
- ✅ 5-15 properties per database (ideal)
- ⚠️ 20-30 properties (manageable)
- ❌ 50+ properties (too complex)

### 3. **Use Rollups for Calculations**

Instead of formulas, use rollups from related databases:
- Total project value from related projects
- Number of completed tasks
- Average task completion time

### 4. **Document Your Structure**

Create a "Database Schema" page documenting:
- What each database contains
- How databases relate to each other
- What select field options mean
- Naming conventions used

### 5. **Regular Cleanup**

- Archive old entries
- Remove unused properties
- Consolidate duplicate select options
- Update outdated relations

---

## 🚀 Example: Well-Structured Database

Here's a complete example of a well-structured database:

### Agency Client Database

```
Database Name: Agency Clients

Properties:
├── 📌 Client Name (Title)
│   Example: "Acme Corporation"
│
├── 🏷️ Status (Select)
│   Options: Active | Inactive | Prospect | Churned
│   Colors: Green | Gray | Yellow | Red
│
├── 🏭 Industry (Select)
│   Options: Technology | Finance | Healthcare | Retail | Manufacturing
│
├── 📅 Start Date (Date)
│   When client relationship began
│
├── 💰 Monthly Retainer (Number)
│   Format: Currency (USD)
│
├── 👤 Account Manager (Person)
│   Assigned team member
│
├── 📧 Primary Contact Email (Email)
│   Main point of contact
│
├── 📞 Phone (Phone)
│   Client phone number
│
├── 🌐 Website (URL)
│   Client website
│
├── 🔗 Active Projects (Relation)
│   Links to: Projects Database
│   Relation name in Projects DB: "Client"
│
├── 📊 Total Project Value (Rollup)
│   From: Active Projects
│   Property: Budget
│   Calculate: Sum
│
├── ✅ Onboarding Complete (Checkbox)
│   Boolean status
│
└── 📝 Notes (Text)
    Additional context
```

### Why This Works:

1. ✅ Clear title field (Client Name)
2. ✅ Select fields for categories (Status, Industry)
3. ✅ Proper field types (Date, Number, Email, etc.)
4. ✅ Logical relations (to Projects)
5. ✅ Useful rollups (Total Project Value)
6. ✅ Consistent naming conventions
7. ✅ Manageable number of properties (12)

### Sample Query Claude Can Run:

```
"Claude, get all active clients in the Technology industry with
monthly retainer over $5,000 and show me their account managers"
```

Claude will query:
- Database: Agency Clients
- Filter: Status = "Active" AND Industry = "Technology" AND Monthly Retainer > 5000
- Show: Client Name, Account Manager, Monthly Retainer

---

## 📚 Summary

### Key Takeaways

1. **Use databases** for structured data, not just pages
2. **Use Select fields** instead of free text for categories
3. **Name properties clearly** and consistently
4. **Create logical relations** between databases
5. **Keep structure simple** - don't over-complicate
6. **Grant access intentionally** - start small, expand as needed
7. **Document your structure** for future reference

### Quick Wins

Start with these actions:
1. Audit your top 3 most-used databases
2. Convert text fields to Select fields where appropriate
3. Standardize property names across databases
4. Grant integration access to one test database
5. Try a simple query with Claude

---

## 🆘 Need Help?

### Common Questions

**Q: Should I restructure my entire Notion workspace?**
A: No! Start with one database, test it, then expand.

**Q: Can Claude read page content or just database properties?**
A: Both! But databases are easier to query systematically.

**Q: What if I have existing data that's messy?**
A: Clean it up gradually. Start with new entries following best practices.

**Q: How do I know if my structure is working?**
A: Try querying it with Claude. If you get expected results, it's working!

---

**Created:** November 10, 2025
**Version:** 1.0
**Purpose:** Guide for structuring Notion for optimal Claude AI integration
