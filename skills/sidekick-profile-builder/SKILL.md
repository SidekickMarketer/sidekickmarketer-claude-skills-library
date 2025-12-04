---
name: sidekick-profile-builder
description: Build comprehensive 20-section client profiles from scattered data sources. This skill should be used when (1) onboarding a new client and need to consolidate discovery data, (2) auditing an existing client to rebuild profile from scattered sources, (3) preparing to run other skills that require a complete client profile (social audit, strategy, content, reporting). Extracts from Notion exports, Google Drive folders, and client websites.
---

# Sidekick Profile Builder

Extracts and consolidates client information into a single, authoritative 20-section Client Profile.

---

## When to Use This Skill

### Trigger Phrases
- "Set up a new client"
- "Build a profile for [client]"
- "I need to onboard [client]"
- "Create client profile from these files"
- "Consolidate client data"

### Prerequisites
- Client folder exists with source files (Notion exports, SOW, discovery notes)
- OR client website URL + manual input

### This Skill Creates
The **foundation for all other skills**. Run this FIRST before:
- LinkedIn skills (voice capture, profile optimizer, strategy, content)
- Social audit
- Content calendar
- Reporting

### Time Estimate
- **Phase 1 (Extract):** 2-5 minutes (automated)
- **Phase 2 (Review):** 15-30 minutes (with user)
- **Phase 3 (Validate):** 1 minute (automated)
- **Total:** 20-40 minutes for complete profile

---

## ⛔ MANDATORY WORKFLOW - NO SHORTCUTS

**Claude: You MUST follow this workflow exactly. Do not skip steps or make assumptions.**

1. **DO NOT** rewrite the profile yourself based on reading a few files
2. **DO NOT** resolve conflicts without asking the user
3. **DO NOT** skip Phase 2 (Review) - it is REQUIRED
4. **DO NOT** assume you know the correct values - ASK THE USER
5. **DO** walk through EVERY conflict one-by-one with the user
6. **DO** mention unprocessable files (PDFs, DOCXs) and ask if they contain critical info
7. **DO** ask about gaps in required fields before finalizing

**If you skip these steps, the profile will contain errors that break downstream skills.**

The automated extraction pulls garbage from ChatGPT exports and other messy files. The ONLY way to get accurate data is to verify with the user.

---

## Three-Phase Workflow

### Phase 1: Extract (Automated)
```bash
./scripts/run_profile_builder.sh "{{client_folder}}"
```

Or direct Python:
```bash
python3 scripts/build_profile.py --client-folder "{{client_folder}}" \
    --additional-folders "/path/to/contracts" \
    --urls "https://clientwebsite.com"
```

This scans all files and generates:
- `00_{{CLIENT}}_CLIENT_PROFILE.md` - The 20-section profile (draft)
- `90_Archive/Profile_Build/_extraction_audit.md` - Source tracking
- `90_Archive/Profile_Build/_conflicts.md` - Data conflicts found
- `90_Archive/Profile_Build/_gaps.md` - Missing fields

### Phase 2: Review (Claude-Assisted) - REQUIRED

**⛔ STOP: Do not proceed to Phase 3 without completing this phase with user input.**

```bash
python3 scripts/review_profile.py --client-folder "{{client_folder}}"
```

This generates `_review_checklist.json`. **Claude MUST then:**

1. **Read** `_review_checklist.json` AND `_conflicts.md` AND `_file_manifest.md`
2. **Tell the user** how many conflicts were found and how many files couldn't be processed
3. **Walk through EACH conflict one-by-one** - show the options, ask which is correct
4. **Ask about gaps** - for any required field marked `[NEEDS MANUAL INPUT]`, ask the user
5. **Ask about unprocessable files** - "There were X PDFs/DOCXs I couldn't read. Do any of these contain critical info?"
6. **Update the profile** only AFTER user confirms each section

**Example of correct behavior:**
```
Claude: Phase 1 found 58 conflicts and 1,154 files I couldn't auto-process.
        Let's go through the conflicts:

        **Conflict 1: Monthly Retainer**
        - Option A: $2,000 (from SOW document)
        - Option B: $1,250 (from ChatGPT export)
        - Option C: $500 (from another file)

        Which is correct?

User: $2,000

Claude: Got it. **Conflict 2: Primary Contact**...
```

**Example of WRONG behavior (do not do this):**
```
Claude: I read the files and wrote a clean profile for you. Here it is!
[WRONG - skipped user verification]
```

### Phase 3: Validate

```bash
python3 scripts/validate_profile.py --client-folder "{{client_folder}}"
```

Checks if profile is ready for downstream skills: social_audit, strategy, content, reporting.

## Example Session

```
User: Build the profile for client-acme

Claude: I'll run the profile builder in two phases.

[Runs build_profile.py]
[Runs review_profile.py]
[Reads _review_questions.json]

Claude: I found 15 conflicts that need your input. Let's go through them:

**Conflict 1: Client Name**
Found these values:
- "ACME Corp" (from contracts/sow.md)
- "Acme Corporation" (from website)
- "ACME" (from notion_export/overview.md)

Which is the correct legal name?

User: ACME Corporation

Claude: Got it.

**Conflict 2: Primary Contact Email**
...

[After all conflicts resolved]

Claude: Now I'll update the profile with your corrections.
[Makes edits to 00_ACME_CLIENT_PROFILE.md]

Claude: Profile updated. Running validation...
[Runs validate_profile.py]

All 4 skills ready. Profile is complete.
```

## Outputs Location

| File | Location |
|------|----------|
| Profile | `{{client_folder}}/00_{{CLIENT}}_CLIENT_PROFILE.md` |
| Audit files | `{{client_folder}}/90_Archive/Profile_Build/` |

## File Review Requirement

The manifest in `90_Archive/Profile_Build/` shows:
- **Files Processed** - Scanned for data
- **Unprocessable Files** - PDFs, DOCXs, etc. that need **manual review**
- **Skipped Files** - System files (safe to ignore)

## Script Options

### Basic Usage
```bash
python3 scripts/build_profile.py --client-folder "/path/to/client-xxx"
```

### With Website Scraping
```bash
python3 scripts/build_profile.py --client-folder "/path/to/client-xxx" \
    --urls "https://clientwebsite.com" "https://linkedin.com/company/xxx"
```

### With Additional Source Folders
```bash
python3 scripts/build_profile.py --client-folder "/path/to/client-xxx" \
    --additional-folders "/path/to/contracts" "/path/to/brand-assets"
```

### Full Options
```bash
python3 scripts/build_profile.py \
    --client-folder "/path/to/client-xxx" \
    --additional-folders "/path/to/contracts" \
    --urls "https://clientwebsite.com" "https://instagram.com/xxx"
```

---

## Section 4: Brand Voice Options

### Single Voice (Most Clients)
For clients with one unified voice (like CMA):
```markdown
## 4. Brand Voice

### Tone & Personality
[Single voice description]
```

### Dual Voice (Founder-Focused LinkedIn)
For clients with separate company + founder voice (like Reveal):
```markdown
## 4. Brand Voice

### 4A. Company Voice
**Use for:** Company LinkedIn page, website, press releases
[Company voice description]

### 4B. Founder's Personal Voice
**Use for:** Founder LinkedIn posts (primary deliverable)
[Founder voice description with specific examples, style references]
```

**When to use 4A/4B split:**
- Founder is the primary content channel (thought leadership)
- LinkedIn strategy has both company page + founder profile
- Founder's voice is distinctly different from company voice

**If 4B needs expansion:** Run `sidekick-linkedin-voice-capture` after profile is built.

---

## Downstream Skill Integration

### Skill Dependencies (what needs to be complete)

| Downstream Skill | Critical Sections | What to Check |
|------------------|-------------------|---------------|
| **sidekick-linkedin-voice-capture** | 2, 4, 15, 20 | Founder name, existing voice notes |
| **sidekick-linkedin-profile-optimizer** | 1, 2, 3, 4, 5, 9, 11, 15 | Business core, differentiators |
| **sidekick-linkedin-strategy-creator** | 1, 3, 4, 5, 7, 8, 9, 10, 13 | Full profile minus optional sections |
| **sidekick-linkedin-content-ideation** | 4, 6, 9, 13, 15, 18 | Voice, pillars, guidelines |
| **sidekick-linkedin-content-pillars** | 3, 4, 5, 8, 9, 15 | Audience, goals, differentiators |

### Recommended Workflow for New LinkedIn Client

```
1. Build Profile (this skill)
   ↓
2. Capture Founder Voice (if 4B needs expansion)
   ↓
3. Define Content Pillars (if Section 6 is incomplete)
   ↓
4. Create LinkedIn Strategy
   ↓
5. Optimize LinkedIn Profiles
   ↓
6. Generate Content Ideas
```

---

## Troubleshooting

### "Phase 1 found conflicts"
**Expected.** The automated extraction pulls from multiple sources which often disagree. That's why Phase 2 (Review) exists - to resolve conflicts with user input.

### "X files couldn't be processed"
PDFs and DOCXs can't be read automatically. Ask the user: "Do any of these files contain critical info I should know about?" If yes, they need to extract the text manually.

### "Section X is incomplete"
Run `validate_profile.py` to see which sections are blocking downstream skills. Focus on required sections (1-13) first.

### Profile doesn't match Reveal/CMA format
The generated profile is a template. The rich detail in Reveal/CMA comes from Phase 2 (Review) where you add client-specific information through conversation.

### Voice guide is too basic
This skill creates the foundation. For detailed founder voice (like Reveal's Section 4B), run `sidekick-linkedin-voice-capture` afterward with interview transcripts or voice samples.

---

## Example Outputs

See these completed profiles as reference:
- **Reveal Pharmaceuticals** - Biotech/pharma with dual voice (4A/4B), detailed founder voice guide, compliance constraints
- **Cincinnati Music Academy (CMA)** - Local business with single brand voice, detailed competitor analysis, seasonality calendar

Both follow the 20-section structure but differ in depth based on client needs.

---

## References

- **Section details**: See [references/PROFILE_SECTIONS.md](references/PROFILE_SECTIONS.md)
- **New client checklist**: See [references/NEW_CLIENT_INTAKE_CHECKLIST.md](references/NEW_CLIENT_INTAKE_CHECKLIST.md)
- **Folder structure**: See [references/CLIENT_FOLDER_STRUCTURE.md](references/CLIENT_FOLDER_STRUCTURE.md)
