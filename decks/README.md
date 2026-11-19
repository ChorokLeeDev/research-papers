# Talk decks

One place collecting the presentation decks. The three conference decks are **git submodules** pinned to each paper's own repo (source of truth); e-prop is a copied PDF (no repo).

| Deck | Location | Source |
|------|----------|--------|
| UAI 2026 — Diagnosing Conformal Prediction Failures Under Distribution Shift | `uai2026/slides/main.pdf` | submodule → `ChorokLeeDev/conformal-covid-uai2026` |
| AISTATS 2027 — When Marginal Shift Magnitudes Cannot Identify Conformal Coverage Loss | `aistats2027/presentation/beamer/deck.pdf` | submodule → `ChorokLeeDev/conformal-coverage-identification-aistats2027` |
| ICLR 2027 — How Many More Labels Are Needed? Minimax Evaluation under Selective Labels | `iclr2027/presentation/beamer/deck.pdf` | submodule → `ChorokLeeDev/selective-labels-minimax-iclr2027` |
| e-prop (BCS541 course talk) | `eprop/eprop_presentation.pdf` | copied PDF |

Clone with `git clone --recursive`, or after cloning run `git submodule update --init`. Bump a deck to its latest with `git submodule update --remote decks/<name>`.
