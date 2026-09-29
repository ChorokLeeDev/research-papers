# Finance communication review conference

Date: 29 September 2026. This is a recorded exchange between AI agents preparing communication materials, not external or human peer review.

## Sources and authored drafts

- factor-regime: current `revision/2026-09-26-factor-validity`, commit `87dced92128746b8f7c82c5ad1a659e2ff9ad929`. Full manuscript and six included result tables read through the GitHub plugin and stored under `sources/`.
- regime-predictability: current `revision/pi-interview-arxiv-20260926`, commit `ad08f1e2aeef9e4ec667b787d8ae00430c60f65f`. Full manuscript and four included result tables read through the GitHub plugin and stored under `sources/`.
- Each JSON contains ten English slides, English poster content, English and Korean introductions, speaker notes, and a claim-provenance ledger. Each deck includes multiple native evidence tables. Figures are not required to convey these comparisons.

## Feedback received and resolved

1. **Theory-content reviewer and independent scientific reviewer: timing example was insufficiently specific in visible text.** Although notes defined the Gaussian construction, slide/poster/intro readers could mistake its 1.606 risk ratio for the fitted nonzero residual. Added the zero benchmark and negative-Sharpe high state directly to slide 4, poster, and both introductions. Explicitly state that it isolates timing without reproducing the fitted residual or allocating the observed historical association to a timing artifact. This changes explanatory precision, not the numerical result.
2. **Theory-content reviewer: source scope for deterministic-feature identity.** Added that X includes all construction inputs, fitted history, and time. The claim does not apply merely to the four basic controls. Added the fixed historical tenth-percentile event definition to both introductions.
3. **Both reviewers: capped-loss scale and sign must be visible.** Added score = min(squared forecast error / c, 1), with c fixed from training, to the temporal results slide and poster. Added gain = restricted-procedure loss minus source-included loss; positive favors inclusion. The label uses restricted procedure because shared-gate ablation does not fully exclude source information. Separate simulation slides explicitly use uncapped conditional squared loss in synthetic target-squared units; the reconstruction slide uses RMSE in basis points.
4. **Independent scientific reviewer: excess-risk notation and English readability.** Changed the risk functional to a distinct script-R, defined E_R and E_U as excess risks relative to respective oracles, and added an English introduction explanation that capping limits large-error contributions. Plain-English editable equation text accompanies mathematical notation.
5. **Root editor: subject headings.** Changed final slide titles to “Requirements for a defensible forecast claim” and “Information paths and inference targets.”

The reviewers checked displayed financial and synthetic values against the pinned manuscripts and included tables. They found no unsupported displayed numbers. Both affirmed that unresolved intervals are not equivalence, fitted negative gain is not absence of oracle information, and shared-gate ablation remains valid for its separately named estimand.

## Reciprocal review sent to theory-content author

Read ICLR/AISTATS JSON drafts and checked current source passages. Confirmed the 57-query finite certificate, 94-versus-367 noise-information contrast, minimum 2,645 complete-label cohort, known-link/unknown-link distinction, hidden-error confidence counterexample, and 7,200 controlled replay results.

- **ICLR completion labels:** “Acceptable completion” risked equating a realized 10% cohort error fraction with the law-level acceptable-risk hypothesis. Requested labels by realized error fraction. Author agreed.
- **ICLR current-source completeness:** the frozen 57-query rule's 1.15% power at 12% risk was displayed, but the current manuscript also reports a private mixture reaching 8.66% while retaining 95.02% at 20% risk. Requested this partial remedy be included while retaining the larger-cohort obstruction. Author agreed; neither result proves a uniform off-design guarantee.
- **AISTATS threshold domain:** the displayed error formula is for q >= 0 whereas whole-coverage-curve equivalence is over all real thresholds. Requested explicit domain distinction. Author agreed.
- **AISTATS sharpness scope:** requested visible compressed-information qualification; fixing the complete source kernel can yield tighter bounds. Author agreed.

## Remaining limits

No experiments were rerun. Content uses archived results, retaining their retrospective-vintage, evaluation-exposure, correlated-market, conditional-inference, and simulation-external-validity qualifications. Final rendered layout review is handled by the parent build process. No independent financial replication or new validation is claimed.
