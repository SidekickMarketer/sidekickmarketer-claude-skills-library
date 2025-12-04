---
name: sidekick-monthly-recap
description: Generates monthly internal and external client reports using Looker Studio data. Use when (1) creating monthly performance reviews, (2) summarizing cross-channel metrics, (3) sharing wins/recommendations with clients. Requires Looker Studio data export and client context.
---

# Monthly Recap Generator

Generates a comprehensive **Internal Team Recap** and a polished **Client-Facing Report** based on aggregated metrics (from Looker Studio) and strategic context.

## When to Use This Skill

This skill activates when users want to:

**Primary Use Case:**
- "Create the November monthly recap for [Client]"
- "Generate monthly reports from this data"
- "Write the monthly summary for [Client]"

**Secondary Use Cases:**
- "Summarize our performance this month"
- "Draft the client email for the monthly report"

## Usage

### Step 1: Data Ingest

The user must provide:
1. **Metrics Data:** A copy-paste summary or CSV from Looker Studio.
2. **Context:** Answers to the "Narrative Context" questions (Wins, Challenges, Focus).

**If missing:** Prompt the user to provide the context using `references/CONTEXT_INPUT_TEMPLATE.md`.

### Step 2: Report Generation

**Generate Internal Report First:**
1. Load `references/INTERNAL_RECAP_TEMPLATE.md`.
2. Fill `{{INTERNAL_SUMMARY_PARAGRAPH}}` with a candid assessment of the data.
3. Include all "Red Flags" or "Challenges" mentioned in the context.
4. Calculate basic efficiencies if possible (e.g. CPA = Spend / Conversions).
5. **Output:** `[Client]_[Month]_INTERNAL_RECAP.md`

**Generate External Report Second:**
1. Load `references/EXTERNAL_RECAP_TEMPLATE.md`.
2. Fill `{{CLIENT_SUMMARY_PARAGRAPH}}` with a positive, forward-looking summary.
3. **Transformation Rules:**
   - **Wins:** Highlight metrics that improved or met goals.
   - **Losses:** Reframe as "Learnings" or "Optimization Opportunities".
   - **Tone:** Professional, confident, partnership-oriented.
   - **Data:** Use the same numbers as internal, but focus on *outcomes* (Conversions) over *inputs* (Spend) where possible.
4. **Output:** `[Client]_[Month]_CLIENT_RECAP.md`

## Example Interaction

**User:** "Create the recap for CMA. Data: [Pastes Looker Data]. Context: We had a great open house, but FB ads were pricey."

**Claude:**
1. Analyzes data + context.
2. Creates `CMA_Nov_INTERNAL_RECAP.md` (Notes high CPA on FB ads).
3. Creates `CMA_Nov_CLIENT_RECAP.md` (Highlights Open House success, frames FB ad costs as "competitive holiday market").

## Outputs

| File | Purpose |
|------|---------|
| `reports/YYYY-MM_INTERNAL_RECAP.md` | Honest team assessment, ROI analysis, internal todos. |
| `reports/YYYY-MM_CLIENT_RECAP.md` | Polished executive summary, wins, next steps. |

## References

- `references/CONTEXT_INPUT_TEMPLATE.md` - Questions to answer for the narrative.
- `references/INTERNAL_RECAP_TEMPLATE.md` - Template for the team report.
- `references/EXTERNAL_RECAP_TEMPLATE.md` - Template for the client report.
