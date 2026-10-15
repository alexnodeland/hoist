# arXiv submission sheet

What to enter, in the order arXiv's form asks for it. The source bundle is `make arxiv` in `paper/latex/`, which writes `arxiv.tar.gz`: `hoist.tex`, `hoist.bbl` (arXiv runs no BibTeX), `refs.bib`, `figure1.tex`, `algorithm1.tex` and `figures/*.pdf`. Do not upload `hoist.pdf`: arXiv builds its own from the source, and a PDF beside TeX source is dropped.

| Field | Entry |
|---|---|
| Title | Compile What the Environment Decides: Read-Only Speculation and Compiled Procedures for LLM Agents |
| Authors | Alex Nodeland |
| Primary category | cs.AI |
| Cross-lists | cs.LG, cs.SE |
| License | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) |
| Comments | 20 pages, 11 figures. Code, data and the claims ledger: https://github.com/alexnodeland/hoist |
| Report number, journal reference, DOI | none |

## Abstract

arXiv's field takes about 1,920 characters; the paper's abstract is 1719, so it is entered as it stands, word for word. arXiv shows the field as plain text; the `$...$` is TeX it renders.

An LLM agent pays a model turn for every decision, yet many of its decisions are fixed by what its tools returned, not by what the user said. We make this precise and use it in two regimes. While a user is present, a program learned from traces can take over only reads, speculatively. Because reads leave the state unchanged until the next write, the decision to speculate separates over reads: make each read whose probability of use before the next write exceeds $\delta/(\beta+\delta)$, for a detour's cost $\delta$ and a saved turn's value $\beta$. That probability, not the next-step probability speculative-action systems rank by, is the one to estimate, and counting estimates it with a calibration error of 0.01–0.08 (against 0.06–0.16). In replay across nine frontier agents it never saw, the speculator takes 86% of retail's read-only ceiling, 10 points more than the next-step speculator. Live on τ²-bench, with no model of its own, it cut GLM-5.3's LLM turns by 28% (95% CI 19–36%) and, in a pre-registered run of three trials, Claude Sonnet 5's by 21% (17–24%) and Claude Haiku 4.5's by 22% (16–29%), with passes no lower. Run live in AgentDojo's own environment with GLM-5.3 and Claude Haiku 4.5, it cut LLM turns by 10% (6–14%) in the suites where the replay found reads to take, with passes unchanged. Where no user speaks, a whole procedure, writes included, can be compiled once: on τ²-bench's solo telecom tasks, a cascade that hands a model only what the procedure's outcome check cannot confirm passes 39 of 40 held-out tasks at 0.48 LLM turns per ticket, against 15.9 for the model alone. Both run in Hoist, an open-source MCP proxy and procedure runtime that serves any agent and any MCP server.

## Before submitting

- [ ] A cs.AI submission by a first-time submitter may ask for an endorsement. Start the submission first: arXiv says at that point whether one is needed, and gives you the link to send to an endorser.
- [ ] Upload `arxiv.tar.gz`, wait for arXiv's compile, and read its PDF end to end. arXiv uses its own TeX Live, not this machine's.
- [ ] The paper's front matter still says *Draft, 2026-09-27*. Keep or change it before the PDF is the public one.
- [ ] Submit before 14:00 US Eastern on a weekday to be announced that evening. A moderator can hold or reclassify a cs.AI submission.

## After it is announced

- Put the arXiv ID in `CITATION.cff`, the BibTeX in `README.md` and `paper/hoist.md`.
- Fix mistakes as a new version (v2), not a new submission.
