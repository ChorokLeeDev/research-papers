# Print artifact production and review

## Format and common design

Each paper receives an English A0 portrait poster (841 × 1189 mm) and two separate A4 one-page introductions. Posters and introductions use a white canvas, navy headings, slate body text, and paper-specific accents agreed with the slide-production agent. English Noto Sans and Korean Nanum Gothic are embedded; editable intro Markdown accompanies each PDF. Original source-figure PDF vectors are preserved when a PDF accompanies the PNG asset.

## First production pass

- Built ICAIF 2026, UAI 2026, and return-decay materials from content JSONs.
- Confirmed each output has exactly one page and correct page dimensions.
- Visually inspected ICAIF poster, UAI Korean introduction, and return-decay English introduction. No overlaps or clipped content. ICAIF source figure remains readable and the limitations appear with the final takeaway.
- Self-review identified awkward Korean syllable-level line breaks and insufficient source-version specificity in introduction footers. Updated wrapping to respect word boundaries and added a linked pinned source revision in each footer. Regenerated all first-pass outputs.
- Sent representative rendered pages to the independent scientific-review agent for substantive and presentation feedback. This is an automated agent review, not external human peer review.

## Conference feedback and revisions

The scientific-review agent inspected the first ICAIF poster, UAI Korean introduction, and return-decay English introduction. It requested visible edition context for ICAIF, a safer A4 footer margin, natural Korean word breaks, and pinned source links. All four requests were accepted and implemented. The explicit ICAIF edition note appears near the author in both languages and on the poster; it is also in the editable introduction Markdown.

A full visual sweep caught missing arrow glyphs and a missing Greek Gamma in the AISTATS Korean introduction. Added an embedded DejaVu symbol fallback, rebuilt all outputs, and checked the arrow and Gamma in rendered pages. The scientific reviewer confirmed the corrected AISTATS page.

The UAI source figure had overlapping original labels. The content author replotted the exact source coordinates with clear annotation leaders; the print engine now preserves that corrected figure as vector content. Scientific review confirmed the resulting UAI poster is clear.

Final Poppler inspection revealed the ICAIF source figure's transparency rendered as saturated regime colors when embedded as a PDF form. The reviewer and print engine independently observed the regression. The source drawing is now rasterized at 432 dpi with alpha composited onto white, retaining the original pastel shading and blue line. A `raster_only` figure flag makes this choice explicit and reproducible. UAI remains vector. The revised ICAIF poster was re-inspected after this change.

## Final verification

- All seven posters and fourteen introductions are complete. Each is exactly one page with the requested A0 portrait or A4 dimensions.
- Visually inspected all 21 print layouts across the production passes and re-inspected the changed final figures, glyphs, edition labels, and footers. No outstanding clipping, overlap, missing glyph, or unreadable-table defect remains.
- All text bounding boxes are inside page boundaries. Each PDF has a clickable source link. Source commits are visible.
- Font files, exact applicable license texts, and font provenance are bundled in `assets/fonts/` for portable rebuilding.
- Some Poppler outputs were truncated despite a successful process exit. Previews are integrity-checked; the final preview set was regenerated with the MuPDF fallback and verified as complete PNGs. PDFs were unaffected by this preview issue.
- `qa/print_validation.json` contains hashes and checks for all 21 final PDFs. `qa/print_metrics.json` aggregates all 21 outputs; targeted rebuilds now merge their metrics instead of replacing the other papers.

No external human peer review or new empirical reproduction is implied by this communication-artifact review.
