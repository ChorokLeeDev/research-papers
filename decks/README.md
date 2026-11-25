# Talk decks

One place collecting the presentation decks. The three conference decks are **git submodules** pinned to each paper's own repo (source of truth). The e-prop and time-series course decks are copied PDFs; the time-series folder also includes speaking notes and the requirements/source checks.

| Deck | Location | Source |
|------|----------|--------|
| UAI 2026 — Diagnosing Conformal Prediction Failures Under Distribution Shift | `uai2026/slides/main.pdf` | submodule → `ChorokLeeDev/conformal-covid-uai2026` |
| AISTATS 2027 — When Marginal Shift Magnitudes Cannot Identify Conformal Coverage Loss | `aistats2027/presentation/beamer/deck.pdf` | submodule → `ChorokLeeDev/conformal-coverage-identification-aistats2027` |
| ICLR 2027 — How Many More Labels Are Needed? Minimax Evaluation under Selective Labels | `iclr2027/presentation/beamer/deck.pdf` | submodule → `ChorokLeeDev/selective-labels-minimax-iclr2027` |
| e-prop (BCS541 course talk) | `eprop/eprop_presentation.pdf` | copied PDF |
| Time Series & AI Forecasting — Multi-horizon factor volatility | [timeseries/deck.pdf](timeseries/deck.pdf) | copied PDF; [notes and checks](timeseries/README.md), editable source in the course repo |
| PhD interview — nine-slide research introduction | [phd-interview/deck.pdf](phd-interview/deck.pdf) | copied exports; [speaker notes](phd-interview/speaking-notes.md), HTML and editable PowerPoint |
| CLS 2027 — four-minute research-video presentation | [cls2027/deck.pdf](cls2027/deck.pdf) | copied exports; [speaker notes](cls2027/speaking-notes.md), HTML and editable PowerPoint |

Clone with `git clone --recursive`, or after cloning run `git submodule update --init`. Bump a deck to its latest with `git submodule update --remote decks/<name>`.
