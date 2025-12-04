# Profile Sections Reference

## The 20 Profile Sections

### Core Sections (1-13) - Required
| # | Section | What's Extracted |
|---|---------|------------------|
| 1 | Business Core | Name, industry, website, address, founded, size |
| 2 | Contacts | Primary contact, decision maker, billing, preferences |
| 3 | Target Audience | Demographics, psychographics, segments, journey, objections |
| 4 | Brand Voice | Tone, personality, words to use/avoid, examples |
| 5 | Products & Services | Offerings, priority, seasonality, pricing |
| 6 | Content Pillars | Themes, purpose, % mix, topics, formats |
| 7 | SOW/Deliverables | Contract dates, retainer, platform deliverables |
| 8 | KPIs & Goals | Business goals, platform metrics, success definition |
| 9 | Competitors | Names, websites, strengths, weaknesses, differentiation |
| 10 | Seasonality | Business seasons, key events, holidays, blackouts |
| 11 | Visual Brand | Colors (hex), typography, logo usage, image style |
| 12 | Account Access | Platform handles, credentials location |
| 13 | Guidelines | Legal/compliance, approval workflow, topics to avoid |

### Strategic Sections (14-20) - Recommended
| # | Section | What's Extracted |
|---|---------|------------------|
| 14 | Business Model & Revenue | Revenue streams, transaction value, LTV, lead sources |
| 15 | Origin Story | Founder background, why started, milestones |
| 16 | Local Presence | Review ratings/counts, community involvement, partnerships |
| 17 | Marketing History | Past efforts, what worked, what flopped, previous agencies |
| 18 | Content Bank | Photo/video inventory, testimonials, FAQs, staff bios |
| 19 | Email & CRM | Email platform, list size, CRM system, integrations |
| 20 | Relationship Notes | Communication preferences, working style, key dates |

## Skill Readiness Requirements

### Core Skills
| Downstream Skill | Critical Sections Required |
|------------------|---------------------------|
| Social Audit | 4, 6, 7, 8, 12 (Brand Voice, Pillars, SOW, KPIs, Accounts) |
| Strategy | 1, 3, 4, 5, 6, 8, 9, 10 |
| Content | 4, 5, 6, 11 |
| Reporting | 1, 7, 8 |

### LinkedIn Skills
| Downstream Skill | Critical Sections Required |
|------------------|---------------------------|
| LinkedIn Voice Capture | 2, 4, 15 (Contacts, Brand Voice, Origin Story) |
| LinkedIn Profile Optimizer | 1, 2, 3, 4, 5, 9, 15 |
| LinkedIn Strategy Creator | 1, 3, 4, 5, 7, 8, 9, 10, 13 |
| LinkedIn Content Ideation | 4, 6, 9, 13, 15 |
| LinkedIn Content Pillars | 3, 4, 5, 8, 9 |

**Rule:** 70%+ of required sections must be complete to proceed.

### Section 4 Special Note
For LinkedIn-focused clients with founder thought leadership:
- **4A (Company Voice)** - Used for company page content
- **4B (Founder Voice)** - Used for founder posts (primary channel)

If Section 4B needs expansion, run `sidekick-linkedin-voice-capture` after profile is built.

## Data Sources

### Local Files
- `.md` (Markdown)
- `.txt` (Plain text)
- `.csv` (Structured data)
- `.json` (Notion database exports)

### Web Sources (when URLs provided)
- **Client website** - Home, About, Services, Contact, Team, Our Story pages
- **Facebook** - Page bio and info
- **Instagram** - Profile bio
- **LinkedIn** - Company info
- **Google Business Profile** - Listing details

## Deduplication Logic
1. Highest confidence score wins (based on pattern specificity)
2. All sources logged in extraction audit
3. Conflicts flagged for human review
