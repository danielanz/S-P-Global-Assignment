# Project Walkthrough Roadmap (Not Slides)

Use this as your **live presentation order** for interviewers. The goal is to tell a clean story: problem → method → evidence → conclusion → limitations.

## Recommended order (what to open first)

1. **Start with the assignment PDF** (`S_P_Global_Assignment_DanielAnzures.pdf`) — 1-2 min
2. **Then open the README** (`README.md`) — 2-3 min
3. **Show final outputs first** (`output/figures/`) — 5-7 min
4. **Then show how you built it** (`notebooks/01`, `02`, `03`) — 6-8 min
5. **Close with limitations and next steps** — 2 min

---

## Why this order works

- Starting with the **PDF** proves you understood the business/research ask.
- Moving to the **README** frames your hypothesis and key finding quickly.
- Showing **results before code** keeps interviewers engaged and gives context.
- Then showing **notebooks/code** demonstrates implementation depth only after the audience knows why it matters.

---

## Exact walkthrough script by section

## 1) Assignment PDF (start here)
**File:** `S_P_Global_Assignment_DanielAnzures.pdf`

### What to explain
- What question the assignment is asking.
- The success criteria you decided to optimize for (equity signal detection + defensible methodology).
- The scope decisions you made (NYC, 2024 sampled months, HVFHV).

### Key sentence to use
> “I started by translating the assignment into a testable equity question: are lower-income neighborhoods underserved, after controlling for structural demand drivers?”

### Insight to highlight
- You approached this as a **causal-ish fairness diagnostic problem**, not just a descriptive dashboard.

---

## 2) README (project framing)
**File:** `README.md`

### What to explain
- Problem statement and post-subsidy motivation.
- Data sources and geographic unit.
- Final answer in one sentence.

### Insights to highlight
- The project combines **TLC trip behavior + Census context**.
- Main finding: no systematic underservice signal in 2024 at zone level after modeling.

### Keep this short
Spend ~2 minutes here. Don’t read line-by-line; summarize the narrative.

---

## 3) Show outputs/figures before notebooks (evidence first)
**Folder:** `output/figures/`

Pick 4-5 figures only. Suggested order:
1. Trip volume distribution/map (where demand exists)
2. Service quality proxy map (wait/fare)
3. Demographic relationship chart (poverty vs service)
4. Temporal chart (hourly/borough/poverty bins)
5. Residual analysis chart (core fairness test)

### What to explain in this section
- “This is the descriptive picture.”
- “This is where naive interpretations can be misleading.”
- “This final residual view is the stronger equity diagnostic.”

### Insights to highlight
- Raw geographic differences exist, but not all are inequity.
- Structural mobility factors explain most variance.
- Residuals don’t show a strong systematic poverty/race pattern.

---

## 4) Notebooks/code walkthrough (how you built it)

## 4.1 `notebooks/01_data_cleaning.ipynb`
### What to explain
- Filtering logic (HVFHV focus).
- Zone exclusions (airports/parks/non-residential effects).
- Spatial join design (tract-to-zone via centroid approach).
- Final aggregated dataset outputs.

### Insight to highlight
- Your data engineering choices were made to reduce noise and make fairness comparisons meaningful.

## 4.2 `notebooks/02_data_exploration.ipynb`
### What to explain
- Why each EDA view exists (not just “I plotted this”).
- Which hypotheses were weak/unsupported in bivariate form.

### Insight to highlight
- Poverty alone has weak explanatory power for trips per capita in this dataset.

## 4.3 `notebooks/03_ml_underservice_detection.ipynb`
### What to explain
- Target: trips per capita.
- Feature groups: ownership, transit usage, labor/commute, density.
- Model choices: Ridge (interpretable) + Random Forest (nonlinear).
- Residual correlation checks with equity variables.

### Insight to highlight
- The strongest explanation is transport fundamentals; residual equity signal is weak at this level of aggregation.

---

## 5) How to close (important)

### 3-part close
1. **Answer:** “At zone level in 2024, I found no systematic underservice signal by poverty/race.”
2. **Caveat:** “This does not rule out micro-level or event-level inequities.”
3. **Next step:** “I would extend to full-year + finer spatial granularity + external controls (weather/transit disruptions).”

---

## High-probability interviewer questions and concise responses

### “Why not start with code?”
Because decision-makers care first about the question and answer; code is credibility after context.

### “Why trust residual analysis?”
It isolates unexplained shortfalls after accounting for legitimate demand structure.

### “Could aggregation hide inequity?”
Yes—zone-level analysis can mask block-level or rider-segment disparities.

### “What would you do next with more time?”
Full-year panel, event controls, and alternative spatial units for robustness.

---

## 15-minute time budget (practical)

- PDF framing: 2 min
- README + approach: 2 min
- Key figures (results): 5 min
- Notebook logic/code depth: 4 min
- Conclusion + limitations: 2 min

If time is cut to 10 minutes: skip most code cells and focus on figures + residual conclusion.

---

## Final prep checklist for tomorrow

- Keep PDF, README, figures folder, and all 3 notebooks pre-opened.
- Pre-select exactly 4-5 figures (avoid browsing during interview).
- Prepare 1 sentence each for: objective, method, result, caveat, next step.
- Rehearse once with a timer (15 min hard cap).
