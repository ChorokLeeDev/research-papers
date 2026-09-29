# Research communication materials

Chorok Lee, KAIST. Prepared 29 September 2026.

Seven source-grounded presentation sets: each includes an English 10-slide deck, an English A0 poster, and separate English and Korean A4 introductions. Each introduction is exactly one page.

[Download all 35 presentation files](research_materials_2026-09-29.zip)

| Paper | Slides (English, 10 pages) | Poster (English, A0) | Introduction (1 page each) |
| --- | --- | --- | --- |
| **How many labels make an audit informative?** | [PPTX](iclr2027/iclr2027_slides_en.pptx) · [PDF](iclr2027/iclr2027_slides_en.pdf) | [PDF](iclr2027/iclr2027_poster_en.pdf) | [English](iclr2027/iclr2027_introduction_en.pdf) · [한국어](iclr2027/iclr2027_introduction_ko.pdf) |
| **When drift does not identify coverage loss** | [PPTX](aistats2027/aistats2027_slides_en.pptx) · [PDF](aistats2027/aistats2027_slides_en.pdf) | [PDF](aistats2027/aistats2027_poster_en.pdf) | [English](aistats2027/aistats2027_introduction_en.pdf) · [한국어](aistats2027/aistats2027_introduction_ko.pdf) |
| **When conformal coverage fails** | [PPTX](uai2026/uai2026_slides_en.pptx) · [PDF](uai2026/uai2026_slides_en.pdf) | [PDF](uai2026/uai2026_poster_en.pdf) | [English](uai2026/uai2026_introduction_en.pdf) · [한국어](uai2026/uai2026_introduction_ko.pdf) |
| **Role support and KG error ranking** | [PPTX](kg-uncertainty/kg-uncertainty_slides_en.pptx) · [PDF](kg-uncertainty/kg-uncertainty_slides_en.pdf) | [PDF](kg-uncertainty/kg-uncertainty_poster_en.pdf) | [English](kg-uncertainty/kg-uncertainty_introduction_en.pdf) · [한국어](kg-uncertainty/kg-uncertainty_introduction_ko.pdf) |
| **Return-decay residuals and tail risk** | [PPTX](factor-regime/factor-regime_slides_en.pptx) · [PDF](factor-regime/factor-regime_slides_en.pdf) | [PDF](factor-regime/factor-regime_poster_en.pdf) | [English](factor-regime/factor-regime_introduction_en.pdf) · [한국어](factor-regime/factor-regime_introduction_ko.pdf) |
| **Source exclusion in regime-gated forecasts** | [PPTX](regime-predictability/regime-predictability_slides_en.pptx) · [PDF](regime-predictability/regime-predictability_slides_en.pdf) | [PDF](regime-predictability/regime-predictability_poster_en.pdf) | [English](regime-predictability/regime-predictability_introduction_en.pdf) · [한국어](regime-predictability/regime-predictability_introduction_ko.pdf) |
| **Predicting Factor Decay** | [PPTX](icaif2026/icaif2026_slides_en.pptx) · [PDF](icaif2026/icaif2026_slides_en.pdf) | [PDF](icaif2026/icaif2026_poster_en.pdf) | [English](icaif2026/icaif2026_introduction_en.pdf) · [한국어](icaif2026/icaif2026_introduction_ko.pdf) |

## Source versions

The materials follow the exact manuscript revisions below. They may be newer than the catalogue’s older one-minute speeches and one-pagers. The Factor Decay set follows the original ten-page TeX preprint, separately from the five-page submission record.

| Paper | Source revision |
| --- | --- |
| How many labels make an audit informative? | [38b792da07a1](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/38b792da07a174980303e6cb9272e5f5e3bd9bac/paper/body.tex) |
| When drift does not identify coverage loss | [76661fdf8629](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/76661fdf862959345ea22ea2ab5494a4171a6eab/paper_aistats2027/reliance_alignment.tex) |
| When conformal coverage fails | [96d9616961e5](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/96d9616961e5ae8607373181d35262cb21a2b0d1/paper/main.tex) |
| Role support and KG error ranking | [208f21270f44](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/208f21270f44cb5fe1e26a8b0e0b9dbab88f4a18/manuscript.tex) |
| Return-decay residuals and tail risk | [87dced921287](https://github.com/ChorokLeeDev/factor-regime-revision/blob/87dced92128746b8f7c82c5ad1a659e2ff9ad929/manuscript.tex) |
| Source exclusion in regime-gated forecasts | [ad08f1e2aeef](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/ad08f1e2aeef9e4ec667b787d8ae00430c60f65f/manuscript.tex) |
| Predicting Factor Decay | [a0bd43ea4789](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/a0bd43ea47898011d0661710975658a8969299d5/arxiv/original-source-20260929/main.tex) |

## Review and revision

Content authors and an independent reviewer exchanged source-located critiques before the final build. Review covered numerical denominators, timing assumptions, theoretical scope, interpretation of null results, and Korean wording. The design review inspected rendered slides, posters and introductions, then corrected spacing, missing mathematical glyphs and source-version labels.

The [review records](reviews/) document the discussions and resulting changes. This was an agent review of communication materials. It does not replace scientific peer review or a rerun of the underlying experiments.

## Editable sources and rebuilding

- PPTX text and tables are editable. Speaker notes include explanations and source references.
- The slide design uses Noto Sans. Install the bundled fonts for matching PowerPoint line wraps; the PDFs embed fonts and preserve the reviewed layout.
- English and Korean introduction Markdown files sit beside the PDFs. Shared content is in [content/](content/).
- Print PDFs use `python tools/build_print.py` with ReportLab, PyMuPDF and Pillow. Font files and their licenses are in `assets/fonts/`.
- Slides use `tools/build_decks.mjs` with the OpenAI artifact-tool runtime and LibreOffice. This builder requires that runtime and its presentation validation helpers; the editable PPTX files do not.
- Builders write into `output/`; `python tools/package_collection.py` stages prefixed final filenames and the ZIP under `publish/materials/`.
- [manifest.json](manifest.json) records source identities, page counts, file sizes and SHA-256 hashes.

The posters are A0 portrait (841 × 1189 mm). Print at actual size. Slides are 16:9. No conference acceptance or arXiv publication status is inferred from preparation of these materials.
