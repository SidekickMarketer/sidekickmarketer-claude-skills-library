# Content Calendar CSV Template

## Required Columns

| Column | Description | Example |
|--------|-------------|---------|
| Date | YYYY-MM-DD format | 2025-02-03 |
| Day | Day of week (must match Date!) | Monday |
| Platform | Target platform | Instagram |
| Format | Content type | Carousel |
| Pillar | Content pillar | Educational |
| Topic | Specific angle | "5 Practice Tips for Beginners" |
| Caption_Outline | Hook + Body + CTA | "Hook: Most beginners... \| Body: 5 tips \| CTA: Save this" |
| Visual_Direction | Photo/graphic guidance | "Student practicing, warm lighting" |
| Alt_Text | Accessibility description | "Piano student practicing scales with instructor guidance" |
| Hashtags | Platform-specific | #musiclessons #pianolearning |
| Status | Draft/Scheduled/Posted | Draft |

> ⚠️ **Day Column:** Must match the actual calendar day for the Date. Always validate programmatically before export.

## CSV Format

```csv
Date,Day,Platform,Format,Pillar,Topic,Caption_Outline,Visual_Direction,Alt_Text,Hashtags,Status
2025-02-03,Monday,Instagram,Carousel,Educational,"5 Practice Tips for Beginners","Hook: Most beginners waste their practice time | Body: 5 specific tips with examples | CTA: Save for your next session","Student at piano, instructor pointing, friendly atmosphere","Piano student receiving instruction on practice techniques at Cincinnati Music Academy","#musiclessons #pianolearning #practicetips #musicstudent #learnpiano",Draft
2025-02-03,Monday,Facebook,Single Image,Educational,"5 Practice Tips for Beginners","Hook: Quick tips for better practice | Body: Summary of key points | CTA: Learn more at link","Same image as IG, square crop","Practice tips infographic for music students","#musiclessons #cincinnati",Draft
```

## Caption Outline Formats

### Single Image Posts
```
Hook: [attention-grabber] | Body: [2-3 sentences of value/story] | CTA: [specific action]
```

Example:
```
Hook: This moment changed everything for Marcus | Body: After 3 months of consistent practice, he played his first complete song | CTA: Ready for your moment? Link in bio
```

### Carousel Posts
```
Hook: [curiosity driver] | Slides: 1-[intro], 2-X-[content points], Final-[CTA] | Body: [context] | CTA: [save/share]
```

Example:
```
Hook: 5 mistakes killing your practice time | Slides: 1-Hook, 2-5-Each mistake, 6-7-Solutions, 8-Save reminder | Body: We see these daily | CTA: Which one are you guilty of? Save this!
```

### Monthly Recap Reel
```
Hook: [month summary] | Highlights: [key moments] | CTA: [follow/engage]
```

Example:
```
Hook: February was EVERYTHING | Highlights: New students, recital moments, breakthrough lessons | CTA: March is going to be even better—stay tuned!
```

## Visual Direction Examples

### Student/Customer Focus
- "Student at piano, smiling, instructor in background, warm lighting"
- "Before/after split image, same student 6 months apart, progress clear"
- "Group class wide shot, diverse ages, engaged students"

### Educational Content
- "Clean graphic with numbered list, brand colors, easy to read"
- "Instructor demonstrating technique, hands visible, professional"
- "Infographic style, icons for each tip, minimal text"

### Testimonial/Quote
- "Quote graphic, brand colors, testimonial text overlay"
- "Customer photo with quote bubble, candid shot"
- "Star rating graphic with review excerpt"

### Behind-the-Scenes
- "Candid shot of team working, natural lighting"
- "Setup/preparation shot, showing process"
- "Fun team moment, personality showing"

## Calendar Brief Template

```markdown
# [CLIENT] Content Calendar - [MONTH YEAR]

## Month Overview
- **Total Posts:** [X]
- **Primary Theme:** [Monthly focus]
- **Key Dates:** [List special dates]

## Weekly Themes
- Week 1: [Theme]
- Week 2: [Theme]
- Week 3: [Theme]
- Week 4: [Theme]

## Pillar Distribution
| Pillar | Target | Actual | Status |
|--------|--------|--------|--------|
| [Pillar 1] | X% | X% | ✅/⚠️ |
| [Pillar 2] | X% | X% | ✅/⚠️ |

## Platform Breakdown
| Platform | Posts | Carousels | Singles | Reels |
|----------|-------|-----------|---------|-------|
| Instagram | X | X | X | X |
| Facebook | X | X | X | - |
| GBP | X | - | X | - |

## Special Content Notes
- [Date]: [Special content for event/holiday]
- [Date]: [Promotional push]

## Action Items
- [ ] [Specific asset needed]
- [ ] [Photo to schedule]
```
