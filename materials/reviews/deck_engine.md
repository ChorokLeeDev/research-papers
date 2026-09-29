# Presentation production and review record

Completed 2026-09-29. Seven English presentations, each exactly ten slides, are available as editable PPTX and PDF in `output/{id}/slides_en.*`.

## Design and construction

- Used the Presentations skill and `@oai/artifact-tool` ES modules. No slide screenshots or python-pptx construction.
- Shared the navy/slate, white, Noto Sans system with the poster/introduction builder. Each paper has its own accent. Full manuscript titles appear on covers; ICAIF explicitly identifies the original ten-page preprint edition.
- The narrative moves from the question and definitions to evidence, limitations, and a final takeaway. Native editable tables carry exact results. Equations use editable plain Unicode text with adjacent definitions. Source figures preserve manuscript evidence; the UAI figure is the author's checked replot of unchanged source data.
- All 70 slides contain speaker notes with manuscript/source locators and version information. Each final slide includes a repository pointer.

## Review conference and revisions

This was an exchange of actual agent feedback and revisions, not a simulated human peer review.

1. Initial UAI, ICAIF, and factor-regime deck renders were individually inspected. Dense tables and figure captions approached the footer. Content was moved upward, table padding/row heights were tightened, and captions gained explicit footer space. A three-column factor-regime comparison was reflowed around its actual text height.
2. The independent scientific reviewer inspected representative long-title, equation, evidence-table, and takeaway slides. They accepted the visual hierarchy but confirmed the UAI figure-caption collision. That figure layout was corrected and re-reviewed.
3. Root independently flagged ICAIF's table footnotes and requested visible edition provenance. Both were corrected. The reviewer subsequently accepted ICAIF cover/slide 6 and factor-regime slide 7.
4. Author/scientific review corrections were incorporated before the final build: ICLR noisy-query qualifiers, AISTATS source-mass normalization, UAI deployment-time language, finance timing/benchmark definitions, and KG metric definitions.
5. The complete 70-slide render sweep found a dense AISTATS table and expanded AISTATS equation explanation too close to the footer. Row spacing and equation-to-explanation spacing were adjusted while retaining the scientific qualifications.
6. Regime slide 6 received shorter table labels, explicitly reviewed and approved by the scientific reviewer. The row denominators, interval meaning, and the qualifier that **both component gains** lie within the tolerance were preserved. Explicit column widths eliminated unnecessary wraps. Root and the reviewer accepted the final AISTATS 6 and Regime 6.
7. Final PDF comparison caught a further Regime slide 4 footer collision in LibreOffice's rendering. The gap between the equation and explanation was reduced without changing content or font size. The regenerated PPTX render and final PDF were both visually checked and are clear.

## Final verification

- Seven PPTX packages passed the skill's integrity/layout finalizer, including 16:9 dimensions, exact ten-slide counts, native table ownership, font policy, bullet geometry, heading fit, and Artifact Tool import.
- Package inspection confirms 70 slides, 70 speaker-note parts, and 29 native editable tables in total.
- All 70 deck slides were inspected as individual rendered images, with affected slides inspected again after revisions.
- All seven final PDFs have ten 16:9 pages. Thirty representative final PDF pages were individually inspected: covers, equations where present, result/dense tables, the UAI evidence plot, and the corrected AISTATS/Regime pages.
- PDF text checks found no missing expected content after accounting for LibreOffice's fallback-symbol extraction order, no missing symbols, no replacement characters, and no off-page text spans. A body-text check also found no text entering the footer zone on content slides.
- The original 17 extraction flags were not omissions: arrows, roots, inequalities, and approximation signs were written as separate fallback-font spans. They render correctly; both surrounding text and symbol counts were checked. The report preserves this distinction in `fallback_symbols_reordered_in_extraction`.
- Content snapshots match the final deck content. ICAIF's only later JSON difference is the poster-only `raster_only: true` figure metadata, which does not affect slides.

## Reproduction and practical limits

Builder: `tools/build_decks.mjs`. PDF verification: `tools/check_deck_pdfs.py`. Finalization receipts and renders: `qa/{id}/slides/`; PDF renders: `qa/{id}/slides_pdf/`; extraction report: `qa/deck_pdf_checks.json`.

PPTX text and tables remain editable. Source figures are embedded images. PDFs preserve the reviewed appearance with embedded fonts; editing PPTX elsewhere may require Noto Sans for matching wraps. Files were validated with the Artifact Tool and LibreOffice, not a separate Microsoft PowerPoint application. This production review did not rerun the papers' empirical studies.
