# Claude Skills - Sidekick Marketer

**Automated marketing workflows powered by Claude Code**

---

## 📚 Active Skills

### 1. Social Content Generator
- **File:** `skills/social-content-generator.md` (symlinked to GitHub)
- **Purpose:** Generate monthly social media content calendars for clients
- **Platforms:** Instagram, Facebook, Google Business Profile
- **Status:** ✅ v1.0 - Ready for Testing
- **Last Updated:** November 14, 2025

**Usage:**
```
"Generate December social content for Cincinnati Music Academy"
"Create January Instagram posts for [Client]"
```

**Features:**
- Auto trend scanning (stays current with social media changes)
- Brand voice alignment from client strategy docs
- Content pillar distribution based on SOW
- Avoids duplicate content (checks past 3-6 months)
- CSV + markdown summary output

---

## 📁 Folder Structure

```
01_Claude_Skills/
├── README.md                          ← You are here
├── skills/                            ← Symlinked to GitHub repo
│   └── social-content-generator.md
├── docs/                              ← Documentation
│   ├── 01_Quick_Start/
│   ├── 02_Reference_Guides/
│   ├── 03_Workflow_Templates/
│   ├── CMA_CLAUDE_SKILLS_PLAN.md     ← Main project plan
│   ├── CMA_AUDIT_FINDINGS.md         ← Client audit
│   └── README.md                      ← Docs index
└── examples/                          ← Sample outputs
    └── sample-outputs/
```

---

## 🔗 GitHub Integration

**Skills are managed in GitHub:**
- **Repo:** https://github.com/SidekickMarketer/sidekickmarketer-claude-skills-library
- **Local Path:** `~/projects/sidekickmarketer-claude-skills-library/`

**How it works:**
```
GitHub Repo (source of truth)
    ↓ (symlink)
~/.claude/skills/ (Claude reads from here)
    ↓ (symlink)
Google Drive (backup/team access)
```

**To edit a skill:**
1. Open in your editor: `~/projects/sidekickmarketer-claude-skills-library/skills/[skill].md`
2. Save changes
3. Changes instantly available to Claude (via symlink)
4. Commit to GitHub when ready

---

## 🚀 Quick Start

### Using a Skill

Just say what you want:
```
"Generate December social content for Cincinnati Music Academy"
```

Claude will:
1. Activate the skill
2. Load client data from Drive
3. Scan current social media trends
4. Generate content calendar
5. Save CSV + summary to client folder

### Creating a New Skill

1. Copy template from GitHub repo
2. Follow structure (Description, Parameters, Workflow, Output)
3. Test with real client data
4. Document in `docs/`
5. Commit to GitHub (symlink makes it available automatically)

---

## 📊 Skill Performance

Track effectiveness in `docs/testing-log.md`:
- Time saved vs manual creation
- Content quality scores
- Client adoption rate
- Performance of generated content

---

## 🔄 Maintenance

### Social Content Generator
- **Trend Check:** Auto-performed on each run
- **Feature Check:** Every 30 days - Next: December 14, 2025
- **Full Audit:** Every 90 days - Next: February 14, 2026

### Adding Skills
When you add a new skill to GitHub:
1. Symlink automatically appears in `~/.claude/skills/`
2. Also appears here in Drive (via second symlink)
3. Update this README
4. No manual copying needed!

---

## 📖 Documentation

**Main Docs:**
- `docs/CMA_CLAUDE_SKILLS_PLAN.md` - Full project plan and setup
- `docs/CMA_AUDIT_FINDINGS.md` - Client setup analysis
- `docs/README.md` - Detailed documentation index

**Quick References:**
- `docs/01_Quick_Start/` - Getting started guides
- `docs/02_Reference_Guides/` - Detailed how-tos
- `docs/03_Workflow_Templates/` - Process templates

---

## 💡 Tips

**For Best Results:**
1. Keep client strategy docs up to date
2. Run skills during Week 3 of month (content planning week)
3. Review generated content before publishing
4. Track what works and update skill based on results

**Troubleshooting:**
- Skill not found? Check symlink: `ls -la ~/.claude/skills/`
- Old trends? Skill auto-updates, but check last update date
- Wrong output? Verify client data in Drive is current

---

## 🎯 Roadmap

### v1.1 (Coming Soon)
- Performance Reporter skill
- Client Onboarding Helper skill
- Integration with Notion databases

### v2.0 (Future)
- Auto-post to scheduling tools
- Performance prediction based on past data
- Multi-language support

---

**Maintained By:** Kyle Naughtrip
**GitHub:** https://github.com/SidekickMarketer/sidekickmarketer-claude-skills-library
**Questions?** See `docs/CMA_CLAUDE_SKILLS_PLAN.md` for full context
