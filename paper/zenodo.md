# Zenodo upload sheet

For the paper's own record on Zenodo (https://zenodo.org/uploads/new), which gives it a DOI and a stable link to use while the arXiv submission waits for an endorser. Upload `paper/latex/hoist.pdf`. The software has a separate record, made from a GitHub release (below).

| Field | Entry |
|---|---|
| Resource type | Publication, then Preprint |
| Title | Compile What the Environment Decides: Read-Only Speculation and Compiled Procedures for LLM Agents |
| Authors | Nodeland, Alex. Affiliation: Independent researcher. Add the ORCID if there is one. |
| Publication date | the day it is published |
| Version | 1 |
| Language | English |
| License | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| Keywords | LLM agents; Model Context Protocol; speculative execution; tool use; probabilistic programming |
| Related works | *is supplemented by* https://github.com/alexnodeland/hoist (resource type: Software) |

## Description

The paper's abstract, word for word. (The same text goes in arXiv's field, `arxiv.md`.)

An LLM agent pays a model turn for every decision, yet many of its decisions are fixed by what its tools returned, not by what the user said. We make this precise and use it in two regimes. While a user is present, a program learned from traces can take over only reads, speculatively. Because reads leave the state unchanged until the next write, the decision to speculate separates over reads: make each read whose probability of use before the next write exceeds $\delta/(\beta+\delta)$, for a detour's cost $\delta$ and a saved turn's value $\beta$. That probability, not the next-step probability speculative-action systems rank by, is the one to estimate, and counting estimates it with a calibration error of 0.01–0.08 (against 0.06–0.16). In replay across nine frontier agents it never saw, the speculator takes 86% of retail's read-only ceiling, 10 points more than the next-step speculator. Live on τ²-bench, with no model of its own, it cut GLM-5.3's LLM turns by 28% (95% CI 19–36%) and, in a pre-registered run of three trials, Claude Sonnet 5's by 21% (17–24%) and Claude Haiku 4.5's by 22% (16–29%), with passes no lower. Run live in AgentDojo's own environment with GLM-5.3 and Claude Haiku 4.5, it cut LLM turns by 10% (6–14%) in the suites where the replay found reads to take, with passes unchanged. Where no user speaks, a whole procedure, writes included, can be compiled once: on τ²-bench's solo telecom tasks, a cascade that hands a model only what the procedure's outcome check cannot confirm passes 39 of 40 held-out tasks at 0.48 LLM turns per ticket, against 15.9 for the model alone. Both run in Hoist, an open-source MCP proxy and procedure runtime that serves any agent and any MCP server.

## After the arXiv paper is announced

Edit the Zenodo record and add a related work, *is identical to* arXiv:ID. Zenodo and arXiv then point at each other.

## The software record

Zenodo archives a GitHub release when the repository's switch is on (https://zenodo.org/account/settings/github). It does not go back for releases made before the switch, so v0.2.0 is not archived. The next release (v0.2.1 or later) will be, and Zenodo reads `CITATION.cff` for its metadata. Nothing here asks for a release now: turn the switch on, and the DOI comes with the next one.
