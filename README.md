# Sidekick Marketer - Claude Skills Library

Monorepo for all Sidekick Marketer Claude Skills: Social media, paid ads, branding, SEO, and more.

## 📚 Skills Library

### ✅ Active Skills

#### 1. Strategy Audit
- **File:** `skills/strategy-audit.md`
- **Purpose:** Analyze existing social media strategy and execution to identify gaps and optimization opportunities
- **Status:** v1.0 - Ready for Testing
- **Created:** November 21, 2025
- **Last Updated:** November 21, 2025

**Features:**
- Compares stated strategy vs actual execution
- Analyzes content pillar distribution
- Checks SOW compliance
- Evaluates template effectiveness
- Performance pattern analysis (if analytics available)
- Generates actionable recommendations and client questions

**Usage:**
```
"Audit Cincinnati Music Academy's social media strategy"
"Analyze CMA's content performance and strategy"
"Strategy audit for [Client Name]"
```

**Use Before:** Running Social Content Generator for first time

---

#### 2. Social Content Generator
- **File:** `skills/social-content-generator.md`
- **Purpose:** Generate monthly social media content calendars for clients
- **Platforms:** Instagram, Facebook, Google Business Profile
- **Status:** v1.1 - Ready for Testing
- **Created:** November 14, 2025
- **Last Updated:** November 14, 2025

**Features:**
- Tiered freshness checking (auto-updates for trends)
- Brand voice alignment from client strategy docs
- Trend integration (viral formats, trending audio, local events)
- Enhanced creative direction (slide-by-slide specs, photo lists)
- CSV + markdown summary output
- Avoids content duplication (checks past 3-6 months)

**Usage:**
```
"Generate December social content for Cincinnati Music Academy"
"Create January Instagram posts for [Client]"
```

**Use After:** Running Strategy Audit to validate approach

---

### 🔄 In Development

#### 3. Performance Reporter (Planned)
- Monthly performance report generation
- Analytics integration
- Insights and recommendations

---

## 🚀 Installation

### Option 1: Symlink (Recommended)
Creates a link so edits to repo files instantly appear in Claude:

```bash
# Clone repo
cd ~/projects
git clone https://github.com/SidekickMarketer/sidekickmarketer-claude-skills-library.git

# Create symlinks
ln -s ~/projects/sidekickmarketer-claude-skills-library/skills/strategy-audit.md ~/.claude/skills/strategy-audit.md
ln -s ~/projects/sidekickmarketer-claude-skills-library/skills/social-content-generator.md ~/.claude/skills/social-content-generator.md

# Verify
ls -la ~/.claude/skills/
```

### Option 2: Manual Copy
Copy skills to Claude's skills directory:

```bash
cp skills/*.md ~/.claude/skills/
```

---

## 📁 Repository Structure

```
sidekickmarketer-claude-skills-library/
├── README.md                     ← You are here
├── CHANGELOG.md                  ← Version history
├── skills/                       ← Active skills
│   ├── strategy-audit.md
│   └── social-content-generator.md
├── docs/                         ← Documentation
│   ├── skill-development-guide.md
│   ├── testing-guide.md
│   └── testing-log.md
├── examples/                     ← Sample outputs
│   ├── sample-outputs/
│   └── sample-inputs/
└── templates/                    ← Skill templates
    └── new-skill-template.md
```

---

## 🧪 Testing

Before deploying a new skill version:

1. **Local Test:** Try the skill with real client data
2. **Document Results:** Add to `docs/testing-log.md`
3. **Iterate:** Fix issues, commit changes
4. **Version:** Update version number when stable
5. **Deploy:** Push to main branch

See `docs/testing-guide.md` for detailed testing procedures.

---

## 📝 Creating New Skills

1. Copy `templates/new-skill-template.md`
2. Follow the structure (Description, Parameters, Workflow, Output)
3. Include freshness checking for time-sensitive skills
4. Test with at least 2 clients before marking production-ready
5. Document in this README

---

## 🔄 Maintenance Schedule

### Strategy Audit
- **Skill Review:** Every 90 days - Next: February 21, 2026

### Social Content Generator
- **Trend Check:** Auto-performed on each run (7 days)
- **Feature Check:** Every 30 days - Next: December 14, 2025
- **Full Audit:** Every 90 days - Next: February 14, 2026

---

## 📚 Documentation

Full documentation available in Google Drive:
- **Location:** `/My Drive/01_Sidekick Marketer/3. AI_Automation/01_Claude_Skills/docs/`
- **Files:**
  - `CMA_CLAUDE_SKILLS_PLAN.md` - Project overview
  - `CMA_AUDIT_FINDINGS.md` - Client audit findings
  - `01_Quick_Start/`, `02_Reference_Guides/`, `03_Workflow_Templates/` - Detailed guides

---

## 🤝 Contributing

This is a private repo for Sidekick Marketer operations. Team members:

1. **Clone** the repo
2. **Create a branch** for new features: `git checkout -b feature/new-skill`
3. **Test thoroughly** before merging
4. **Update** README and CHANGELOG
5. **Submit PR** for review

---

## 📊 Skill Performance Tracking

Track skill effectiveness in `docs/testing-log.md`:
- Time saved vs manual creation
- Content quality scores
- Client adoption rate
- Performance of generated content

---

## 🆘 Support

Questions or issues? Contact:
- **Repo Maintainer:** Kyle Naughtrip
- **Documentation:** `/My Drive/02_Master_Documents_Hub/Claude_AI_Documentation/`

---

**Last Updated:** November 21, 2025
**Active Skills:** 2
**Skills in Development:** 1+
