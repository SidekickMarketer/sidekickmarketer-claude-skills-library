---
name: sidekick-strategy-creator
description: Creates comprehensive social media strategies with per-channel strategy docs aligned with Sidekick's photo-first model. Use when (1) onboarding new client needing social strategy, (2) quarterly strategy rebuild after audit reveals issues, (3) client requests strategic pivot or refresh. Requires CLIENT_PROFILE.md or manual business details.
---

# Sidekick Strategy Creator

Create client-specific social media strategy documents with a master strategy plus individual channel strategies for Instagram, Facebook, GBP, and LinkedIn.

## Output Structure

```
07_Marketing_Channels/
├── Social_Media/
│   ├── 00_MASTER_STRATEGY.md      # Brand voice, pillars, themes (cross-channel)
│   ├── STRATEGY_BRIEF.md
│   ├── Instagram/
│   │   ├── 00_IG_STRATEGY.md      # IG-specific tactics
│   │   ├── Content_Calendars/
│   │   └── Performance_Data/
│   ├── Facebook/
│   │   ├── 00_FB_STRATEGY.md      # FB-specific tactics
│   │   ├── Content_Calendars/
│   │   └── Performance_Data/
│   └── GBP/
│       ├── 00_GBP_STRATEGY.md     # GBP-specific tactics
│       ├── Content_Calendars/
│       └── Performance_Data/
├── LinkedIn/
│   ├── 00_LINKEDIN_STRATEGY.md    # LinkedIn master strategy
│   ├── 01_Founder_Voice_Guide.md
│   ├── 02_Profile_Specs.md
│   ├── 03_Content_Pillars.md
│   └── 04_Content_Archive/
├── SEO/                           # Future
├── Email/                         # Future
└── Paid_Ads/                      # Future
```

## Service Model Constraints

Sidekick operates a **photo-first** content strategy:
- High-quality designed graphics and carousels
- 1 monthly recap Reel (photo montage)
- No daily Stories or video-first strategy
- Focus on scalable, template-driven content

---

## Phase 1: Discovery & Research

### Step 1: Load Client Profile

```bash
Read 00_[CLIENT]_CLIENT_PROFILE.md
```

Extract:
- Business type, industry, location (Section 1)
- Target audience and pain points (Section 3)
- Services/products (Section 5)
- Existing brand voice (Section 4)
- Competitors (Section 9)
- Founder background (Section 15)

### Step 2: Load Audit Findings (If Available)

From previous `Social_Audit.md`, extract:
- Hall of Fame posts (what worked)
- Red flags (what's broken)
- Current metrics baseline
- Format performance data

### Step 3: Research Top Performers by Channel

**Use `WebSearch` for each platform the client will use:**

```
Instagram:
- "best [industry] Instagram accounts 2025"
- "[industry] Instagram content strategy"

Facebook:
- "best [industry] Facebook pages 2025"
- "[industry] Facebook marketing examples"

GBP:
- "[industry] Google Business Profile best practices"
- "local [industry] GBP examples [city]"

LinkedIn:
- "best [industry] LinkedIn creators 2025"
- "[industry] thought leaders LinkedIn"
```

**For each channel, document:**
- Top 3 performers analyzed
- Content patterns that work
- Formats getting engagement
- Gaps/differentiation opportunities

---

## Phase 2: Master Strategy

### Step 4: Define Cross-Channel Elements

**Platform Priority:**
| Platform | Priority | Role | Frequency |
|----------|----------|------|-----------|
| Instagram | [1/2/3] | [Role] | [X/week] |
| Facebook | [1/2/3] | [Role] | [X/week] |
| GBP | [1/2/3] | [Role] | [X/week] |
| LinkedIn | [1/2/3] | [Role] | [X/week] |

**Content Pillars (apply across channels):**
Load `references/pillar_frameworks.md` for industry templates.

| Pillar | % | Purpose |
|--------|---|---------|
| [Pillar 1] | [X]% | [Goal] |
| [Pillar 2] | [X]% | [Goal] |
| [Pillar 3] | [X]% | [Goal] |
| [Pillar 4] | [X]% | [Goal] |
| [Pillar 5] | [X]% | [Goal] |

**Brand Voice:**
Load `references/voice_framework.md` for options.

### Step 5: Build Master Strategy Doc

Load `references/MASTER_STRATEGY_TEMPLATE.md`

Fill all sections with client-specific data:
- Business overview
- Target audience
- Brand voice (shared across channels)
- Content pillars
- Platform overview
- Format mix
- Quarterly themes
- Visual guidelines
- Success metrics

**Save to:** `07_Marketing_Channels/Social_Media/00_MASTER_STRATEGY.md`

---

## Phase 3: Channel-Specific Strategies

### Step 6: Instagram Strategy

Load `references/IG_STRATEGY_TEMPLATE.md`

Fill with:
- IG-specific research findings
- Format mix for Instagram
- Posting schedule and times
- Hashtag strategy and sets
- Caption approach
- Stories/Reels approach
- IG-specific KPIs

**Save to:** `07_Marketing_Channels/Social_Media/Instagram/00_IG_STRATEGY.md`

### Step 7: Facebook Strategy

Load `references/FB_STRATEGY_TEMPLATE.md`

Fill with:
- FB-specific research findings
- Format mix for Facebook
- Posting schedule and times
- Link strategy
- Groups strategy (if applicable)
- FB-specific KPIs

**Save to:** `07_Marketing_Channels/Social_Media/Facebook/00_FB_STRATEGY.md`

### Step 8: GBP Strategy

Load `references/GBP_STRATEGY_TEMPLATE.md`

Fill with:
- GBP-specific research findings
- Post types and frequency
- Photo strategy
- Review management approach
- Q&A strategy
- Local SEO integration
- GBP-specific KPIs

**Save to:** `07_Marketing_Channels/Social_Media/GBP/00_GBP_STRATEGY.md`

### Step 9: LinkedIn Strategy (If Applicable)

**Note:** For comprehensive LinkedIn strategy, use the dedicated LinkedIn skill suite:
1. `sidekick-linkedin-strategy-creator` - Master LinkedIn strategy (start here)
2. `sidekick-linkedin-voice-capture` - Founder voice guide
3. `sidekick-linkedin-profile-optimizer` - Profile specs
4. `sidekick-linkedin-content-pillars` - Content pillars
5. `sidekick-linkedin-content-ideation` - Content ideas

The LinkedIn strategy skill creates `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md`

Skip this step if using the LinkedIn skill suite (recommended for clients with LinkedIn in SOW).

---

## Phase 4: Folder Setup

### Step 10: Create Folder Structure

```bash
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/Instagram/Content_Calendars"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/Instagram/Performance_Data"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/Facebook/Content_Calendars"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/Facebook/Performance_Data"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/GBP/Content_Calendars"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Social_Media/GBP/Performance_Data"
mkdir -p "{{client_folder}}/07_Marketing_Channels/LinkedIn/04_Content_Archive"
mkdir -p "{{client_folder}}/07_Marketing_Channels/SEO"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Email"
mkdir -p "{{client_folder}}/07_Marketing_Channels/Paid_Ads"
```

---

## Phase 5: Validation

### Step 11: Strategy Validation

Check each strategy doc:
- [ ] All placeholders replaced with client-specific data
- [ ] Research findings documented with sources
- [ ] No generic advice
- [ ] Within photo-first constraints
- [ ] KPIs have specific targets
- [ ] Quarterly themes defined

### Step 12: Create Strategy Brief

**STRATEGY_BRIEF.md (1 page summary):**
- Platform Priority (ranked)
- Content Pillars (names + percentages)
- Brand Voice (3-word summary)
- 90-Day Focus (top 3 priorities)
- Key Metrics (3 KPIs with targets)

**Save to:** `07_Marketing_Channels/Social_Media/STRATEGY_BRIEF.md`

---

## Output Summary

| Document | Location |
|----------|----------|
| Master Strategy | `07_Marketing_Channels/Social_Media/00_MASTER_STRATEGY.md` |
| Strategy Brief | `07_Marketing_Channels/Social_Media/STRATEGY_BRIEF.md` |
| Instagram Strategy | `07_Marketing_Channels/Social_Media/Instagram/00_IG_STRATEGY.md` |
| Facebook Strategy | `07_Marketing_Channels/Social_Media/Facebook/00_FB_STRATEGY.md` |
| GBP Strategy | `07_Marketing_Channels/Social_Media/GBP/00_GBP_STRATEGY.md` |
| LinkedIn Strategy | `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md` |

---

## Quality Standards

Every strategy must include:
- Research findings with top performers analyzed
- Specific platform priorities with rationale
- 4-6 content pillars totaling 100%
- Photo-first format mix
- Brand voice with examples
- Channel-specific tactics (not copy-paste)
- Quarterly seasonal themes
- Concrete KPI targets per channel

Every strategy must avoid:
- Generic advice ("post consistently")
- Recommendations outside photo-first model
- Copy-paste content across channels
- Missing research documentation
- Unrealistic targets

---

## References

- `../_shared/channel_benchmarks.md` - Research-backed engagement data (2024-2025)
- `references/MASTER_STRATEGY_TEMPLATE.md` - Master strategy template
- `references/IG_STRATEGY_TEMPLATE.md` - Instagram strategy template
- `references/FB_STRATEGY_TEMPLATE.md` - Facebook strategy template
- `references/GBP_STRATEGY_TEMPLATE.md` - GBP strategy template
- `references/pillar_frameworks.md` - Industry-specific content pillars
- `references/platform_matrix.md` - Platform selection guidance
- `references/voice_framework.md` - Brand voice attribute options
