---
name: sidekick-linkedin-profile-optimizer
description: Generate optimized LinkedIn profile copy and specifications for founder and company pages. This skill should be used when (1) onboarding a new LinkedIn client, (2) client's LinkedIn profiles need a refresh, (3) before starting content strategy to ensure profiles convert, (4) SOW includes LinkedIn profile optimization.
---

# LinkedIn Profile Optimizer

Generate optimized LinkedIn profile elements for both founder/exec personal profile and company page, based on client profile data.

## When to Use This Skill

This skill activates when users want to:

**Primary Use Cases:**
- "Optimize [founder name]'s LinkedIn profile"
- "Create LinkedIn profile copy for [company]"
- "Refresh our LinkedIn profiles - they need updating"
- "Generate LinkedIn profile specs for [client]"

**Integration Points:**
- After running `sidekick-profile-builder` (required)
- After running `sidekick-linkedin-strategy-creator` (recommended)
- Before starting LinkedIn content creation
- During client onboarding when SOW includes profile optimization

**What This Skill Produces:**
- Complete founder profile optimization (headline, about, banner specs, featured section)
- Complete company page optimization (tagline, about, banner specs, CTA)
- Ready-to-implement copy within LinkedIn character limits
- Designer briefs for banner images

## Knowledge Base Reference

**ALWAYS load these files BEFORE generating profile copy:**

### Required: Client Profile
**Location:** `{{client_folder}}/00_[CLIENT]_CLIENT_PROFILE.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| 1. Business Core | Company name, industry, website, founded year | Company page details, headline context |
| 2. Contacts | Founder/owner name, role | Founder profile headline |
| 3. Target Audience | Who they serve, pain points, segments | "Who I help" in About section |
| 4. Brand Voice | Tone, personality, taglines, approved phrases | Voice for all copy |
| 5. Products & Services | Offerings, key features | "What I do" value proposition |
| 9. Competitors | Differentiators, positioning | Unique angles for headlines |
| 11. Visual Brand | Colors, logo specs | Banner design brief |
| 15. Origin Story | The "why", founder background, milestones | "Why me" credibility |

**Note:** If Section 4 has company/founder voice split (4A/4B), use founder voice for personal profile, company voice for company page.

### Recommended: Founder Voice Guide
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/01_Founder_Voice_Guide.md`

If exists, use for:
- Specific phrases to include
- Tone and formality level
- Words/phrases to avoid

### Recommended: LinkedIn Strategy
**Location:** `{{client_folder}}/07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`

If exists, extract:
- Primary goal (what CTA should achieve)
- Research findings (competitor profile patterns)

**⚠️ CRITICAL:** Headlines and About sections must reflect the SPECIFIC client, not generic LinkedIn best practices. Always pull specific details from profile.

## Prerequisites

**Required (in order):**
1. `sidekick-profile-builder` - Client profile
2. `sidekick-linkedin-strategy-creator` - LinkedIn strategy (recommended to run first)

## Input Required

User provides:
1. **Client folder path** - To locate client profile
2. **Current LinkedIn URLs** (optional) - To audit existing profiles
3. **Primary CTA goal** - What action should profile visitors take?
   - Book a call
   - Visit website
   - Follow for content
   - Download resource
   - Apply for jobs

## Workflow

### Step 1: Load Client Profile

Extract from `00_[CLIENT]_CLIENT_PROFILE.md`:
- Company name, industry, website (Section 1)
- Founder name and role (Section 2)
- Target audience and their pain points (Section 3)
- Brand voice and tone (Section 4)
- Core services/products (Section 5)
- Founder background and origin story (Section 15)
- Key differentiators (Section 9 - vs competitors)

### Step 2: Research Top Profiles in Industry

**First, load `references/INDUSTRY_ADAPTATION.md` for industry-specific guidance:**
- Profile tone expectations for this industry
- Credibility signals that matter
- What to avoid (compliance, tone mismatches)
- Suggested research queries

**Then use `WebSearch` to find top 1% LinkedIn profiles in the client's industry:**

```
Search queries:
- "best [industry] CEO LinkedIn profiles"
- "top [industry] founders LinkedIn"
- "[industry] LinkedIn profile examples"
- "how to write [industry] LinkedIn headline"
```

**Analyze 3-5 top profiles for:**
- Headline formulas that work in this industry
- About section structures and hooks
- Featured section content types
- Banner messaging approaches
- How they communicate credibility

**Extract patterns for client:**
```
PROFILE RESEARCH FINDINGS:
- Top profiles analyzed: [Names/URLs]
- Headline patterns: [Common formulas used]
- About section hooks: [Opening lines that work]
- Featured content: [What top performers showcase]
- Industry-specific elements: [Certifications, metrics, language]
- Differentiation opportunity: [What client can do differently]
```

### Step 3: Audit Current Profiles (If URLs Provided)

Use `WebFetch` to analyze current profiles for:
- Headline effectiveness
- About section completeness
- Featured section usage
- Banner alignment with brand
- CTA clarity

### Step 4: Generate Founder Profile Optimization

**Quality Guardrails for Headlines:**
- ❌ Avoid: Just job title ("CEO at Company")
- ❌ Avoid: Buzzwords ("Visionary thought leader")
- ❌ Avoid: Generic claims ("Helping businesses grow")
- ✅ Require: Specific audience ("Helping radiologists...")
- ✅ Require: Specific outcome or value prop
- ✅ Require: First 60 characters must hook (mobile cutoff)

**Quality Guardrails for About Sections:**
- ❌ Avoid: Third-person writing ("John is a leader who...")
- ❌ Avoid: Resume dump (list of achievements without story)
- ❌ Avoid: Generic opening ("I'm passionate about...")
- ✅ Require: First 2 lines must hook (visible before "see more")
- ✅ Require: Specific numbers, stories, or credentials
- ✅ Require: Clear CTA at the end
- ✅ Require: Written in founder's voice, not corporate speak

```markdown
# [Founder Name] - LinkedIn Profile Optimization
**Company:** [Company Name]
**Generated:** [Date]

## HEADLINE (220 characters max)

### Current:
[If audited, show current]

### Recommended:
[New headline - write the FULL headline, not a description]

**Formula used:** [Role] + [Who you help] + [Outcome/Result]

**Mobile Preview View (CRITICAL):**
> [Show EXACTLY what appears in the first 60 chars, including spaces]
> *Verify: Does the hook/value prop appear before this cutoff?*

**Why this works:**
- [Reason 1 - tied to audience needs]
- [Reason 2 - differentiation from competitors]

---

## ABOUT SECTION (2,600 characters max)

### Structure:
1. **Hook** (First 2 lines - visible before "see more") - Must create curiosity
2. **Who I help** (Target audience) - Be specific, not "businesses"
3. **What I do** (Services/expertise) - Focus on outcomes, not process
4. **Why me** (Credibility/origin story) - Personal, not resume
5. **CTA** (What to do next) - Single clear action

### Recommended Copy:

[Write the FULL About section - complete copy, not notes]

**Hook preview (first 300 chars):**
[Show exactly what appears before "see more"]

**Character count:** [X/2,600]

**Voice check:** Does this sound like [Founder Name] talking, or a corporate bio?

---

## BANNER IMAGE

### Specifications:
- Size: 1584 x 396 pixels
- Format: PNG or JPG
- File size: Under 8MB

### Recommended Content:
- [Primary element - e.g., tagline, value prop]
- [Secondary element - e.g., company logo, website]
- [Visual style - e.g., clean, professional, brand colors]

### Banner Brief for Designer:
[2-3 sentence brief]

---

## FEATURED SECTION

### Slot 1: [Type]
- **Title:** [Title]
- **What:** [Description]
- **Link:** [URL if applicable]

### Slot 2: [Type]
- **Title:** [Title]
- **What:** [Description]
- **Link:** [URL if applicable]

### Slot 3: [Type]
- **Title:** [Title]
- **What:** [Description]
- **Link:** [URL if applicable]

---

## EXPERIENCE SECTION

### Current Role Entry:
**[Title] at [Company]**
[Description focusing on impact and expertise, not just duties]

---

## PROFILE COMPLETENESS CHECKLIST

- [ ] Professional headshot (face visible, good lighting)
- [ ] Custom headline (not default job title)
- [ ] About section with clear CTA
- [ ] Banner image with branding
- [ ] Featured section with 2-3 items
- [ ] Current experience with description
- [ ] Contact info visible
- [ ] Custom URL (linkedin.com/in/[name])
```

### Step 5: Generate Company Page Optimization

```markdown
# [Company Name] - LinkedIn Company Page Optimization
**Generated:** [Date]

## TAGLINE (120 characters max)

### Recommended:
[Tagline]

**Why this works:**
- [Reason]

---

## ABOUT SECTION (2,000 characters max)

### Structure:
1. **What we do** (Clear value proposition)
2. **Who we serve** (Target audience)
3. **What makes us different** (Differentiators)
4. **CTA** (Website, contact, follow)

### Recommended Copy:

[Full About section copy]

**Character count:** [X/2,000]

---

## BANNER IMAGE

### Specifications:
- Size: 1128 x 191 pixels
- Format: PNG or JPG

### Recommended Content:
[Brief for designer]

---

## COMPANY DETAILS

- **Industry:** [Correct industry category]
- **Company size:** [Range]
- **Headquarters:** [Location]
- **Type:** [Public/Private/etc.]
- **Founded:** [Year]
- **Specialties:** [Comma-separated list, up to 20]

---

## CALL-TO-ACTION BUTTON

**Recommended:** [Visit website / Contact us / Learn more / Sign up / Register]
**URL:** [Landing page URL]

---

## PAGE COMPLETENESS CHECKLIST

- [ ] Logo uploaded (300 x 300 pixels)
- [ ] Banner image with branding
- [ ] Tagline filled in
- [ ] About section complete
- [ ] All company details accurate
- [ ] Website URL added
- [ ] CTA button configured
- [ ] Specialties listed (for SEO)
```

### Step 6: Validate Outputs

Before saving, verify:

**Founder Profile:**
- [ ] Headline ≤ 220 characters (check mobile preview - only ~60 visible)
- [ ] About section ≤ 2,600 characters
- [ ] About section has hook in first 2 lines
- [ ] About section includes clear CTA
- [ ] Featured section has 2-3 items specified
- [ ] Banner specs include dimensions (1584 x 396)

**Company Page:**
- [ ] Tagline ≤ 120 characters
- [ ] About section ≤ 2,000 characters
- [ ] About section includes CTA
- [ ] Banner specs include dimensions (1128 x 191)
- [ ] Company details are accurate
- [ ] CTA button URL is specified

**Alignment:**
- [ ] Copy matches brand voice from client profile
- [ ] Headlines use formulas from `references/HEADLINE_FORMULAS.md`
- [ ] Content addresses target audience pain points
- [ ] CTA aligns with primary goal specified by user

### Step 7: Save Outputs

Save to: `[client_folder]/07_Marketing_Channels/LinkedIn/02_Profile_Specs.md`

**File Structure:**
```markdown
# [Client Name] - LinkedIn Profile Optimization
**Generated:** [Date]
**Founder:** [Name]
**Company:** [Name]

[Founder Profile Section]

[Company Page Section]
```

**Integration:**
- Referenced by: `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md` (Section 8: Profile Optimization Summary)
- Used by: Content creators implementing the profiles
- Used by: Designers creating banner images

## Quality Standards

✅ All copy within character limits (validate before saving)
✅ Headlines follow proven formulas from references
✅ About sections have clear structure and CTA
✅ Banner specs ready for designer (dimensions + brief)
✅ Aligned with brand voice from profile
✅ Optimized for target audience
✅ SEO keywords naturally integrated

## Time Estimate

| Step | Time |
|------|------|
| Load client profile | 5 min |
| Research top profiles | 15-20 min |
| Audit current profiles | 10-15 min (if URLs provided) |
| Generate founder optimization | 15-20 min |
| Generate company optimization | 10-15 min |
| Validation | 5-10 min |
| **Total** | **60-85 min** |

## Example Output Preview

**What a completed headline recommendation looks like:**

```markdown
## HEADLINE (220 characters max)

### Current:
CEO at Reveal Diagnostics

### Recommended:
CEO @ Reveal | Helping radiologists ditch gadolinium contrast agents | Building the future of MRI diagnostics

**Formula used:** Role + Who you help + Outcome/Mission

**Why this works:**
- Immediately clear what she does (MRI diagnostics)
- Speaks to specific audience (radiologists)
- Addresses their pain point (gadolinium concerns)
- Shows mission, not just title

**Character count:** 118/220 ✓
**Mobile preview (first 60 chars):** "CEO @ Reveal | Helping radiologists ditch gadolinium..." ✓
```

## Troubleshooting

**Issue: Headline too long**
- Solution: Prioritize first 60 characters (mobile visibility)
- Use shorter formula or remove non-essential elements

**Issue: About section feels generic**
- Solution: Include specific metrics, stories, or differentiators from client profile
- Reference origin story (Section 15) for authenticity

**Issue: Can't find industry examples**
- Solution: Search broader industry terms or related industries
- Use competitor analysis if top profiles aren't available

**Issue: Missing client profile sections**
- Solution: Run `sidekick-profile-builder` first to ensure all required sections exist
- Ask user to provide missing information if profile is incomplete

## References

- `references/HEADLINE_FORMULAS.md` - Proven headline structures
- `references/PROFILE_BENCHMARKS.md` - What good profiles include
- `references/INDUSTRY_ADAPTATION.md` - **Industry-specific profile guidance** (tone, credibility signals, compliance)
