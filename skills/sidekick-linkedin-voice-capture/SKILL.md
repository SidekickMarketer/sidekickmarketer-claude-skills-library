---
name: sidekick-linkedin-voice-capture
description: Capture a founder/exec's personal voice for LinkedIn ghostwriting. This skill should be used when (1) onboarding a new client where you'll ghostwrite for their CEO/founder, (2) the brand voice in the profile isn't specific enough for personal LinkedIn posts, (3) ghostwritten content isn't sounding authentic, (4) preparing to run linkedin-content-ideation for a new client.
---

# LinkedIn Voice Capture

Create a founder voice guide for authentic LinkedIn ghostwriting. This captures how the specific person speaks, thinks, and presents themselves - distinct from the company's brand voice.

## When to Use This Skill

This skill activates when users want to:

**Primary Use Cases:**
- "Capture [founder name]'s voice for LinkedIn posts"
- "Create a voice guide for ghostwriting [exec]'s LinkedIn content"
- "Our ghostwritten posts don't sound authentic - help us capture their voice"
- "I need to write LinkedIn posts for [founder] but don't know their style"

**Integration Points:**
- After running `sidekick-profile-builder` (required)
- After running `sidekick-linkedin-strategy-creator` (recommended)
- Before running `sidekick-linkedin-content-ideation` (recommended)
- When brand voice (Section 4) isn't specific enough for personal posts

**What This Skill Produces:**
- Comprehensive voice guide with tone, language patterns, and preferences
- Ghostwriting checklist for quality control
- Sample posts demonstrating the voice
- Reference document for all future ghostwritten content

## Knowledge Base Reference

**ALWAYS load the client profile BEFORE voice analysis:**

### Required: Client Profile
**Location:** `{{client_folder}}/00_[CLIENT]_CLIENT_PROFILE.md`

| Section | What to Extract | How to Use It |
|---------|-----------------|---------------|
| 2. Contacts | Founder/exec name, role | Who we're capturing voice for |
| 4. Brand Voice | Existing tone, personality, approved phrases | Starting point for personal voice |
| 15. Origin Story | Background, milestones, the "why" | Source for personal themes |
| 20. Relationship Notes | Communication preferences, working style | How they actually communicate |
| 1. Business Core | Industry, company type | Context for industry-specific language |

### Check Existing Voice Documentation
**Before starting, check what already exists in Section 4:**

| What's There | Action |
|--------------|--------|
| Basic tone/personality only | Full voice capture needed |
| Detailed voice guide with examples | Extract and formalize into `01_Founder_Voice_Guide.md` |
| Company + Founder voice split (4A/4B) | Focus on expanding founder voice (4B) |

### Voice Samples to Request
Ask user to provide any of these:
- Existing LinkedIn posts from the founder
- Interview transcripts or call recordings
- Emails or Slack messages (with permission)
- Video/podcast appearances (URLs)
- Blog posts or articles they've written
- Previous content they've reviewed and approved

**⚠️ CRITICAL:** The profile's Brand Voice section describes the COMPANY voice. The voice guide we're creating captures how the FOUNDER personally talks - which may be different.

## Prerequisites

**Required (in order):**
1. `sidekick-profile-builder` - Client profile
2. `sidekick-linkedin-strategy-creator` - LinkedIn strategy (recommended to run first)

## Input Required

User provides:
1. **Client folder path** - To locate client profile
2. **Voice samples** - Any of:
   - Existing LinkedIn posts from the founder
   - Interview transcripts or call recordings
   - Emails or Slack messages from the founder
   - Previous content they've written
   - Video/podcast appearances (URLs)

## Workflow

### Step 1: Load Profile Foundation

Read client profile and extract:
- Founder name and role (Section 2)
- Brand voice baseline (Section 4)
- Origin story and background (Section 15)
- Industry context (Section 1)

### Step 2: Analyze Voice Samples

If voice samples provided, analyze for:

**⚠️ CRITICAL: Extract SPECIFIC phrases, not vague descriptions.**
- ❌ Bad: "Uses humor occasionally"
- ✅ Good: "Uses self-deprecating humor, often starting with 'I'll be honest, I completely failed at...'"

**Language Patterns:**
- Sentence length (short/punchy vs flowing) - Count actual average
- Vocabulary level (technical vs accessible) - List specific words they use
- Jargon usage (industry terms they use naturally) - List exact terms
- Transition phrases - Quote their actual phrases ("Here's the thing...", "What I've learned...")

**Personality Markers:**
- Humor style (dry, self-deprecating, none)
- Confidence level (bold claims vs humble observations)
- Storytelling approach (data-driven, anecdotal, both)
- Formality (casual, professional, mix)

**Recurring Themes:**
- Topics they gravitate toward
- Values they emphasize
- Frustrations they express
- Wins they celebrate

**Distinctive Phrases - QUOTE DIRECTLY:**
- Catch phrases or signature expressions (exact quotes)
- How they start posts (list 3+ actual openers)
- How they close posts (list 3+ actual closers)
- Questions they tend to ask (exact phrasing)

**The Litmus Test:**
After analysis, you should be able to complete this sentence:
"If I read a post and it said '[specific phrase]' or started with '[specific opener]', I'd immediately know it was [Founder Name]."

If you can't identify these specifics, you need more samples or an interview.

### Step 3: Conduct Voice Interview (If No Samples)

If limited samples, ask user to gather answers to:

```
VOICE INTERVIEW QUESTIONS

1. How would you describe your communication style in 3 words?

2. What topics could you talk about for hours without getting bored?

3. What's a common industry belief you disagree with?

4. When you give advice, do you tend to be direct or diplomatic?

5. Do you prefer sharing data/research or personal stories?

6. What phrases do you catch yourself saying often?

7. Who are 2-3 people whose LinkedIn presence you admire? Why?

8. What do you never want to sound like on LinkedIn?

9. How do you feel about using emojis, humor, or vulnerability?

10. What's your hot take that might be controversial in your industry?
```

### Step 4: Generate Voice Guide

Create a `[CLIENT]_FOUNDER_VOICE_GUIDE.md` with:

```markdown
# [Founder Name] - LinkedIn Voice Guide
**For:** [Company Name]
**Created:** [Date]
**Based on:** [Sources analyzed]

## Voice Summary
[2-3 sentence overview of their voice]

## Tone Profile

| Dimension | Their Style | Notes |
|-----------|-------------|-------|
| Formality | [Casual / Professional / Mix] | |
| Confidence | [Bold / Humble / Balanced] | |
| Humor | [Frequent / Occasional / Rare] | |
| Storytelling | [Data-driven / Anecdotal / Both] | |
| Vulnerability | [Open / Guarded / Selective] | |

## Language Patterns

### Sentence Structure
- [Short and punchy / Longer and flowing / Mix]
- Average sentence length: [X words]

### Vocabulary
- Technical level: [High / Medium / Accessible]
- Industry jargon: [List terms they use naturally]
- Words they favor: [List]
- Words to avoid: [List - things that don't sound like them]

### Signature Phrases
- Opening hooks: "[Examples]"
- Transitions: "[Examples]"
- Closings: "[Examples]"
- Catch phrases: "[Examples]"

## Content Preferences

### Topics They Love
1. [Topic] - Why it resonates
2. [Topic] - Why it resonates
3. [Topic] - Why it resonates

### Their Hot Takes
- [Contrarian view they hold]
- [Industry norm they challenge]

### Topics to Avoid
- [Topic] - Why
- [Topic] - Why

## POV & Values

### Core Beliefs
- [Belief they frequently express]
- [Belief they frequently express]

### What Frustrates Them
- [Industry frustration]
- [Common mistake they see]

### What Excites Them
- [What they celebrate]
- [What they champion]

## Ghostwriting Checklist

Before publishing, verify:
- [ ] Sounds like something they'd actually say
- [ ] Uses their vocabulary, not generic business speak
- [ ] Reflects their level of formality
- [ ] Matches their storytelling style
- [ ] Aligns with their values and POV
- [ ] Avoids phrases/topics that don't fit them

## Example Voice Comparison

**Generic LinkedIn voice:**
"I'm excited to share that we've achieved significant growth this quarter."

**[Founder Name]'s voice:**
"[Rewritten in their actual voice based on analysis]"

## Sample Posts in Their Voice

### Sample 1: [Topic]
[Full post written in their voice]

### Sample 2: [Topic]
[Full post written in their voice]
```

### Step 5: Validate Voice Guide

Before saving, verify the voice guide includes:

**Required Elements:**
- [ ] Voice summary (2-3 sentences)
- [ ] Tone profile table (all dimensions filled)
- [ ] Language patterns (sentence structure, vocabulary, signature phrases)
- [ ] Content preferences (topics they love, hot takes, topics to avoid)
- [ ] POV & values (core beliefs, frustrations, excitements)
- [ ] Ghostwriting checklist
- [ ] Example voice comparison (generic vs. their voice)
- [ ] At least 2 sample posts in their voice

**Quality Checks:**
- [ ] Specific phrases included (not just "uses humor")
- [ ] Distinct from brand voice (personal vs. company)
- [ ] Based on actual samples or interview (not assumptions)
- [ ] Actionable for ghostwriters (clear do's and don'ts)

**Validation Test:**
Write a test post using the voice guide, then check:
- [ ] Sounds like something they'd actually say
- [ ] Uses their vocabulary, not generic business speak
- [ ] Matches their formality level
- [ ] Reflects their storytelling style
- [ ] Aligns with their values and POV

### Step 6: Save Output

Save to: `[client_folder]/07_Marketing_Channels/LinkedIn/01_Founder_Voice_Guide.md`

**File Structure:**
```markdown
# [Founder Name] - LinkedIn Voice Guide
**For:** [Company Name]
**Created:** [Date]
**Based on:** [Sources analyzed - e.g., "5 LinkedIn posts, 2 podcast transcripts"]

[Complete voice guide content]
```

**Integration:**
- Referenced by: `07_Marketing_Channels/LinkedIn/00_LINKEDIN_STRATEGY.md` (Section 4: Founder Voice Summary)
- Used by: All ghostwritten LinkedIn content
- Used by: `sidekick-linkedin-content-ideation` skill (if running)
- Used by: Content creators writing in founder's voice

## Quality Standards

✅ Distinct from generic brand voice (personal vs. company)
✅ Based on actual samples or direct input (not assumptions)
✅ Includes specific phrases and patterns (not vague descriptions)
✅ Provides clear ghostwriting checklist
✅ Contains sample posts demonstrating the voice
✅ Actionable for writers (specific do's and don'ts)

## Time Estimate

| Step | Time |
|------|------|
| Load profile foundation | 5 min |
| Analyze voice samples | 15-25 min |
| OR Conduct interview | 20-30 min |
| Generate voice guide | 15-20 min |
| Validation | 10 min |
| **Total** | **45-70 min** |

## Example Voice Guide Preview

**What a completed voice guide section looks like:**

```markdown
## Signature Phrases

- Opening hooks: "Here's the thing about...", "I used to believe...", "Let me tell you what actually works:"
- Transitions: "But here's where it gets interesting", "The real question is", "What nobody talks about:"
- Closings: "That's the game.", "Figure that out, and you're ahead of 90%.", Question to audience
- Catch phrases: "Let's be honest", "This is the part most people skip"

## Example Voice Comparison

**Generic LinkedIn voice:**
"I'm excited to share that our company has achieved significant growth this quarter through strategic initiatives and team collaboration."

**Sarah's voice:**
"We grew 40% last quarter. Want to know the unsexy truth? We stopped chasing every shiny object and doubled down on what was already working. Revolutionary, I know."
```

## Troubleshooting

**Issue: Limited voice samples available**
- Solution: Use `references/VOICE_INTERVIEW_TEMPLATE.md` to conduct interview
- Ask user for any written content (emails, Slack, previous posts)
- Request permission to analyze video/podcast transcripts

**Issue: Voice guide feels too similar to brand voice**
- Solution: Focus on personal communication style, not company messaging
- Emphasize how they speak vs. how the company speaks
- Include personal anecdotes and individual perspective

**Issue: Can't identify distinctive patterns**
- Solution: Analyze more samples (aim for 1,000+ words total)
- Look for subtle patterns (sentence length, transition phrases, closing styles)
- Compare against generic LinkedIn voice to highlight differences

**Issue: Founder doesn't have existing content**
- Solution: Conduct comprehensive interview using template
- Ask for examples of content they admire (what they want to sound like)
- Start with brand voice as baseline and refine through collaboration

**Issue: Voice guide too vague**
- Solution: Include specific phrases, not just descriptions
- Add concrete examples of "their voice" vs. "generic voice"
- Provide multiple sample posts showing the voice in action

## References

- `references/VOICE_INTERVIEW_TEMPLATE.md` - Full interview questions
- `references/VOICE_ANALYSIS_FRAMEWORK.md` - How to analyze samples
- `references/SAMPLE_VOICE_GUIDE.md` - Example completed voice guide (quality bar)
