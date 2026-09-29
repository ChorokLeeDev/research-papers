# Theory content review conference

Date: 29 September 2026. Participants: theory_content, finance_content, scientific_review, root. This is an internal agent review, not human peer review.

## Source reading and draft scope

- ICLR manuscript: `paper/body.tex`, commit `38b792da07a174980303e6cb9272e5f5e3bd9bac`. Read the full main text and the relevant finite-budget, off-design, cohort-size, and reliability appendices. The source contains deterministic calculations and mathematical certificates, not a deployment study.
- AISTATS manuscript: `paper_aistats2027/reliance_alignment.tex`, commit `76661fdf862959345ea22ea2ab5494a4171a6eab`. Read the main text, `confidence_identification.tex`, and generated scale, test, learned-score tables and macros. Exact known-link results, compressed-information envelopes, and controlled replay are kept distinct.
- Each final JSON provides ten English slides, presenter notes, an English poster, and separate English/Korean one-page-introduction content. Numeric evidence is rendered as native tables.

## Round 1: independent scientific review

scientific_review checked the 57-query certificate, numerical 94/367 noisy budgets, 2,645 complete-label cohort result, mean-risk ceiling, Gaussian scale and MMD tables, and learned-score replay. It agreed with the numerical values and scope.

1. **Fixed-budget asymptotics could be mistaken for all-n guarantees.** The initial discussion proposed a regime table rather than placing an unexplained minimax formula on a slide. The final ICLR frontier slide says fixed k as n grows, requires 0 < beta < 1, and mentions the extra square-root-n condition for the critical passive comparison. The finite 57-query result occupies a separate slide. Reviewer accepted this resolution.
2. **"Finite entries are numerical" was ambiguous.** ICLR slide 6 now says: "Numerically inverted budgets for 95% limiting power; these are not finite-cohort guarantees." The exact blind-region conclusion remains distinct from numerical budget inversions.
3. **AISTATS conditional error mass was not visibly normalized.** The formula now explicitly uses `E_P[omega e | T]`. The adjacent bullet says it is error mass per unit source magnitude mass, not target conditional error. Notes explain that division by positive a gives target conditional error. All symbols are defined.

## Round 2: exchange with finance_content

finance_content read the theory drafts against their source tables and found no unsupported numeric results. It requested four refinements; theory_content agreed and implemented each.

1. **Realized completion versus risk law.** ICLR's illustrative table now labels columns "10%-error completion" and "20%-error completion", replacing "acceptable completion". Notes explain that the tested target is a risk-generating law rather than the realized fraction alone.
2. **Retain the partial remedy, not only its failure.** ICLR slide 8, poster, and EN/KO introductions now mention the private mixture: certified lower power 0.08661 at p = .12 while retaining 0.95017 at p = .20. This qualifies the original frozen rule's 0.011549 off-design power without weakening the complete-label cohort obstruction.
3. **Whole-curve equivalence versus displayed nonnegative-threshold formula.** AISTATS slide 4 explicitly says its displayed formula uses q >= 0, while the equivalence concerns all real thresholds.
4. **Scope of sharpness.** AISTATS slide 6 and poster now say the closed-form envelope is sharp over compatible experiments given compressed source quantities. A fixed full source kernel can yield tighter bounds. The conditional-error-heterogeneity criterion is retained in the notes and introductions.

No scientific disagreement remained after this discussion.

## Reciprocal finance review

theory_content independently read the two finance drafts, current manuscript sections, and their supplied generated evidence tables.

- **Return-decay residuals:** verified regional log-loss changes, conditional interval endpoints, 48-family result, history-crossing table, and Gaussian timing construction. Requested that the visible Gaussian null identify its high state as negative rolling Sharpe with a zero benchmark, since it does not reproduce the fitted residual pipeline. Also requested a standalone tail-event definition in the introduction and explicit inclusion of curve-fit history in the full-input information statement.
- **Source exclusion:** verified the 42/240 disagreements, 0/2400 crossings, 776 proximity-driven margin inclusions, 196 identical forecast cases, gate-only simulation table, and corrupted-source table. Requested a visible normalized capped-loss definition and positive-gain sign convention, to avoid conflating its 0.005 margin with raw MSE or economic utility.
- finance_content accepted these changes and reported that they were being incorporated. That agent maintains the resolution log for its own files.

## Communication and remaining limits

root requested direct subject-based slide titles; these were adopted. Formula slides include editable Unicode alternatives. Introductions have 446 English words each before headings. Notes remain within 120–220 words.

The review checks fidelity to the pinned manuscripts and clarity of communication. It is not a new proof verification, experiment reproduction, approval of deployment assumptions, or claim of conference acceptance. The finite ICLR certificate remains specific to its declared experiment. The AISTATS replay remains controlled and its cap remains an assumption. Root performs the independent rendering, clipping, pagination, and final artifact review.
