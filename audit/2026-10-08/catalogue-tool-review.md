# Independent catalogue-tool review — 2026-10-08

Reviewed the working diff against `a04e9fdd062133dd8c4c44cefc8e828e76409c65` in `materials/tools/build_decks.mjs`, `materials/tools/check_deck_pdfs.py`, `materials/README.md`, and the matching README generator in `materials/tools/package_collection.py`. This reviewer did not author these edits. Review was read-only except this report; supplemental executions used `/tmp/catalogue-independent-k9si5prh`.

The helper-directory lookup honors an explicit override, otherwise tries the installed `/opt/codex` path and the earlier `/root/.codex` path. It checks accessibility before importing, and fails with an actionable diagnostic if no helper exists. The scope remains the documented OpenAI presentation runtime, not arbitrary Node installations. The new PDF-check aggregation correctly fails on each nonempty error list/dictionary or nonzero replacement count. The README text and generator agree.

`node --check materials/tools/build_decks.mjs` passed. An explicit nonexistent `RESEARCH_PRESENTATION_SKILL` failed at the intended diagnostic before importing the presentation runtime. Existing parent-run evidence in `catalogue-tool-validation.json` demonstrates successful native deck construction, LibreOffice export, valid-PDF validation, missing-text rejection, and empty-collection rejection; those are inspected evidence, not claimed as executions by this reviewer.

Independent extra checks copied the exact checker to a temporary material root and generated ten-page 16:9 PDFs with PyMuPDF and the bundled Noto Sans font:

| Case | Exit | Observation |
|---|---:|---|
| Complete valid synthetic deck | 0 | Ten slides checked; no errors |
| Required arrow missing while surrounding prose is present | 1 | `fallback_symbol_shortfalls` populated, ordinary missing-text count zero |
| Extra text span starting at x=-2 points | 1 | `out_of_page_spans` populated, ordinary missing-text count zero |
| Nine-entry slide manifest with ten-page PDF | 0 | **Only nine slides checked; false pass** |

An attempted U+FFFD PDF insertion did not survive extraction as U+FFFD, so that experiment did not exercise the replacement-character branch and is not counted as a successful test of it. The aggregation branch is straightforward on code inspection.

## CATALOGUE-01: silent truncated manifest

**Severity:** medium validation gap, pre-existing rather than introduced by this patch. The checker asserts PDF length ten but then uses `zip(pdf, doc['slides'])` without validating manifest length. A nine-slide JSON silently skips validation of PDF page ten and exits successfully. Resolution: require exactly ten manifest slides, and equal PDF/manifest lengths, before iterating; rerun the valid and truncated fixtures. More-than-ten manifests should likewise fail. This is relevant to the new failing-status contract even though the current seven manifests are all valid.

No other correctness regression was found in the four-file diff. The independent tests support the helper portability and nonzero-exit change; close CATALOGUE-01 before claiming complete slide-check coverage. These are document-pipeline checks, not scientific validation of the papers or independent visual inspection of every slide.

## Targeted recheck after author correction

The author added `assert len(doc['slides']) == len(pdf)` immediately after the existing ten-page PDF assertion. The revised checker was recopied to the same independent scratch fixture. The nine-slide manifest now exits 1 with the expected `(9, 10)` mismatch; an eleven-slide manifest exits 1 with `(11, 10)`; the complete ten-slide manifest still exits 0 and checks all ten pages. **CATALOGUE-01 is resolved** by these three executed boundary checks. This recheck did not rerun deck rendering or interpret scientific source claims.
