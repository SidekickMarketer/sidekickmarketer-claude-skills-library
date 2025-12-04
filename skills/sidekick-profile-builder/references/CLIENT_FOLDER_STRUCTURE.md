# Sidekick Marketer - Canonical Client Folder Structure
**Template Version:** 2.0
**Based On:** CMA (Cincinnati Music Academy) - Production Client
**Last Updated:** November 2025

---

## System Architecture

| System | Role | What Lives Here |
|--------|------|-----------------|
| **Notion** | Active Work | Reports, planning, tasks, dashboards, client-facing |
| **Google Drive** | File Storage | Exports, assets, documents, contracts, skill I/O |

**Key Principle:** Notion is the operational hub. Drive is the file backbone.

---

## Monthly Workflow

```
EXPORT DATA → DROP IN DRIVE → RUN SKILLS → ANALYZE → REPORT IN NOTION
     ↓              ↓              ↓           ↓              ↓
 Platforms    02_Performance_   reports/   Notion DB    Client Dashboard
              Data/ folders
```

---

## Complete Folder Structure

```
client-{{SHORT_CODE}}/
│
│ ─────────────────────────────────────────────────────────────
│ CONTROL CENTER
│ ─────────────────────────────────────────────────────────────
├── 00_{{CLIENT}}_CLIENT_PROFILE.md     ← Master profile (only control doc needed)
│
│ ─────────────────────────────────────────────────────────────
│ ADMIN & SETUP (rarely touched after onboarding)
│ ─────────────────────────────────────────────────────────────
├── 01_Admin_Legal/
│   ├── Agreement And SOW/
│   │   └── Signed Agreements/
│   ├── Proposal/
│   │   └── Old Proposal Versions/
│   └── ChatGPT Knowledge/              ← AI context docs
│
├── 02_Onboarding_Access/               ← Credentials, access notes
│
│ ─────────────────────────────────────────────────────────────
│ ASSETS & DELIVERABLES
│ ─────────────────────────────────────────────────────────────
├── 03_Brand_Assets/
│   ├── Assets/
│   │   ├── 01_Brand/                   ← Logos, colors, fonts
│   │   ├── 02_Photos/                  ← Organized library
│   │   └── 03_Graphics/                ← Templates, graphics
│   ├── Photos/
│   │   ├── Queue/                      ← DROP: New photos for content gen
│   │   ├── Processed/                  ← Already used
│   │   └── {{YEAR}}_Photos/            ← Yearly archives
│   └── Website Photos/
│
├── 04_Discovery_Research/
│   └── 01_Discovery Phase/             ← Initial audits, research (one-time)
│       └── CMA_GPT_Exports/            ← AI research outputs
│
│ ─────────────────────────────────────────────────────────────
│ SERVICE FOLDERS (same structure pattern across all)
│ ─────────────────────────────────────────────────────────────
├── 07_Marketing_Channels/Paid_Ads/
│   ├── 00_Strategy/                    ← Planning docs
│   ├── 01_Campaign_Data/               ← Setup, config
│   │   └── Discovery_Phase/
│   ├── 02_Performance_Data/            ← DROP: Platform exports
│   └── 03_Daily_Reports/               ← Working analysis
│
├── 07_Marketing_Channels/Social_Media/
│   ├── 00_MASTER_STRATEGY.md           ← Cross-channel strategy
│   ├── Instagram/
│   │   ├── 00_IG_STRATEGY.md           ← IG-specific tactics
│   │   ├── Content_Calendars/          ← Monthly calendars
│   │   │   └── {{YYYY}}-{{MM}}_IG_Calendar.csv
│   │   └── Performance_Data/           ← DROP: IG exports
│   ├── Facebook/
│   │   ├── 00_FB_STRATEGY.md           ← FB-specific tactics
│   │   ├── Content_Calendars/
│   │   │   └── {{YYYY}}-{{MM}}_FB_Calendar.csv
│   │   └── Performance_Data/           ← DROP: FB exports
│   ├── GBP/
│   │   ├── 00_GBP_STRATEGY.md          ← GBP-specific tactics
│   │   ├── Content_Calendars/
│   │   │   └── {{YYYY}}-{{MM}}_GBP_Calendar.csv
│   │   └── Performance_Data/           ← DROP: GBP exports
│   └── 04_Audit_Reports/               ← Skill outputs
│
├── 07_Marketing_Channels/LinkedIn/
│   ├── 00_LINKEDIN_STRATEGY.md         ← LinkedIn master strategy
│   ├── 01_Founder_Voice_Guide.md       ← Founder voice for ghostwriting
│   ├── 02_Profile_Specs.md             ← Profile optimization specs
│   ├── 03_Content_Pillars.md           ← LinkedIn content pillars
│   └── 04_Content_Archive/             ← Posted content archive
│
├── 07_Marketing_Channels/SEO/
│   ├── 00_Strategy/
│   ├── 01_Keywords_Research/
│   ├── 02_Performance_Data/            ← DROP: Tool exports
│   │   ├── BrightLocal/
│   │   └── SE Rankings/
│   └── 03_Technical_Audits/
│       └── Screaming Frog/
│
├── 09_Website/
│   ├── 00_Analytics/
│   │   └── Discovery_Phase/
│   ├── 01_Landing_Pages/
│   ├── 02_Conversion_Data/
│   └── 03_Performance_Data/            ← DROP: GA4/analytics exports
│
├── 07_Marketing_Channels/Email/
│   ├── 00_Strategy/
│   ├── 01_Subscriber_Lists/
│   ├── 02_Campaign_Data/               ← Campaign content
│   └── 03_Performance_Data/            ← DROP: Email platform exports
│
│ ─────────────────────────────────────────────────────────────
│ SYSTEM FOLDERS
│ ─────────────────────────────────────────────────────────────
├── 90_Archive/                         ← Old/deprecated files
│
└── notion_export/                      ← Skill input (profile builder)
```

**Note:** Skills output to their respective service folders, not a generic reports folder:
- Social audit → `07_Marketing_Channels/Social_Media/04_Audit_Reports/`
- SEO audit → `07_Marketing_Channels/SEO/03_Technical_Audits/`
- Profile builder → `00_{{CLIENT}}_CLIENT_PROFILE.md` at root

---

## The Universal Data Drop Pattern

**Every service folder has `02_Performance_Data/` as the data drop zone.**

| Service | Drop Zone | What Goes Here |
|---------|-----------|----------------|
| 06_Paid_Ads | `02_Performance_Data/` | Google Ads exports, Meta exports |
| 07_Social_Media | `02_Performance_Data/` | Instagram insights, FB exports |
| 08_SEO | `02_Performance_Data/` | BrightLocal, SE Rankings exports |
| 09_Website | `03_Performance_Data/` | GA4 exports, heatmaps |
| 10_Email_Marketing | `03_Performance_Data/` | Klaviyo, Mailchimp exports |

**Mental model:** Export from platform → Drop in `02_Performance_Data/` → Skills read it

---

## Key Files Required by Skills

### For `sidekick-social-audit`
| File/Folder | Required | Purpose |
|-------------|----------|---------|
| `07_Marketing_Channels/Social_Media/02_Performance_Data/` | YES | CSV/Excel exports from platforms |
| `07_Marketing_Channels/Social_Media/04_Audit_Reports/` | Auto-created | Audit outputs + analysis files |

### For `sidekick-profile-builder`
| File/Folder | Required | Purpose |
|-------------|----------|---------|
| `00_{{CLIENT}}_CLIENT_PROFILE.md` | YES | Master profile output |
| `notion_export/` | Optional | Source docs if building from scratch |

### For `social-content-generator`
| File/Folder | Required | Purpose |
|-------------|----------|---------|
| `07_Marketing_Channels/Social_Media/00_Strategy/00_SOCIAL_STRATEGY.md` | YES | Voice, pillars, rules |
| `03_Brand_Assets/Photos/Queue/` | YES | Photos to use |
| `00_{{CLIENT}}_CLIENT_PROFILE.md` | YES | Client context |

---

## Naming Conventions

### Folders
- `{{NN}}_{{Name}}` format (e.g., `07_Social_Media`)
- Numbers ensure consistent sort order
- Use underscores, not spaces

### Monthly Folders
- Format: `{{YYYY}}-{{MM}}_{{Month}}` (e.g., `2025-11_November`)
- Ensures chronological sorting
- Always use this format, never `November 2025`

### Files
- Dates: `{{YYYY}}-{{MM}}-{{DD}}` (e.g., `2025-11-26`)
- Client prefix: `{{CLIENT}}_` (e.g., `CMA_`)
- Versions: `_v1`, `_v2`, `_FINAL`
- Skill outputs: `_COMPLETE.md`

---

## Setup Checklist for New Clients

```
AUTOMATED (run setup_client_folder.py):
[x] Create client-{{short_code}}/ folder
[x] Create all subfolders
[x] Create 00_{{CLIENT}}_CLIENT_PROFILE.md template
[x] Create 00_SOCIAL_STRATEGY.md template

MANUAL:
[ ] Fill out client profile with real data
[ ] Add SOW to 01_Admin_Legal/Agreement And SOW/
[ ] Complete social strategy doc
[ ] Add platform credentials to 02_Onboarding_Access/
[ ] Export initial performance data to service folders
```

---

## Service-Specific Notes

### Active Services (create full structure)
Only create service folders for services the client actually has:
- Social Media service → Full `07_Marketing_Channels/Social_Media/` structure
- Paid Ads service → Full `07_Marketing_Channels/Paid_Ads/` structure
- SEO service → Full `07_Marketing_Channels/SEO/` structure
- Website service → Full `09_Website/` structure
- Email service → Full `07_Marketing_Channels/Email/` structure

### Inactive Services
Don't create empty service folders. Add them when the service is sold.

---

## Quick Reference

| I need to... | Go to... |
|--------------|----------|
| Find client info | `00_{{CLIENT}}_CLIENT_PROFILE.md` |
| Drop platform exports | `{{SERVICE}}/02_Performance_Data/` (or `03_Performance_Data/`) |
| Find discovery research | `04_Discovery_Research/01_Discovery Phase/` |
| Get brand assets | `03_Brand_Assets/` |
| Run social audit | Skill reads from `07_Marketing_Channels/Social_Media/02_Performance_Data/` |
| Add photos for content | `03_Brand_Assets/Photos/Queue/` |

---

**This structure is the source of truth for all Sidekick Marketer clients.**
