# Independent scientific and communication review

Reviewer: scientific_review agent. This is an automated editorial review, not human peer review. Scope: seven-paper communication collection, 29 September 2026.

## Review conference, round 1: source scope

The reviewer independently read the pinned source copies and sent the following issues to the content authors before their drafts. The exchanges are real agent messages; resolutions below are recorded only after checking responses or revised files.

| Paper | Source-located issue | Request to author | Status |
|---|---|---|---|
| UAI | `sources/uai2026.tex`, Theorem “Score Inflation Under Concentrated Feature Shift,” A1 footnote: probability-space additivity is idealized; measured TreeSHAP is a log-odds proxy. | Present the theorem as a directional bound under its assumptions, never an empirical SHAP guarantee. | Author acknowledged and plans to state this distinction; draft review pending. |
| UAI | §Data separation, stratified correlation table, threshold framework: primary sample is 8 SALT plus 8 external multiclass tasks; Stack Overflow is excluded; cutoff and protective rules are exploratory. | Distinguish 16-task primary endpoint from 17-task auxiliary analysis; keep false positives/negatives and exploratory threshold explicit. | Author acknowledged and plans to show sales-office and KDDCup99 failure cases. |
| KG | `sources/kg-uncertainty.tex`, §Limitations, Historical results, and `sources/kg/empirical_results.tex`: observed-target recovery differs from factual truth; three seeds do not replicate graphs; historical .986 AUROC/43% headline is unreconciled. | Use current revision results only; never claim truth probabilities, conformal guarantees, independent replication, or historical headline validation. | Author acknowledged, retrieved empirical input and supporting tables. |
| KG | §Training counts: zero bits are deterministic functions of exact role counts. §Reciprocal study: prediction accuracy and raw missing-role AUROC change together under multiple training changes. | Separate representation effects from new information and descriptive sign reversal from causal effect of improving accuracy. | Author proposes comparison of 10.05→44.35% observed-target accuracy and .6893→.3639 AUROC, explicitly tied to predictor regime. |
| ICLR | `sources/iclr2027.tex`, abstract, main theorem, finite certificates: fixed query count with cohort size tending to infinity differs from finite count-tail/truthful certificates. | Scope 57-query and 2,645-cohort examples; preserve truthful labels, count-tail class, frozen cohort and committed missingness. Nonrejection does not certify safety. | Sent to theory author; draft review pending. |
| AISTATS | `sources/aistats2027.tex`, §Setup, abstract: known logistic conditional label law differs from marginal source calibration; exact identification differs from bounded-density sensitivity. | Keep the two regimes distinct, binary frozen score and density-ratio assumption explicit; grid-valid threshold selection is not arbitrary threshold search. | Sent to theory author; draft review pending. |
| Return-decay | `sources/factor-regime.tex`, timing construction, sequential inference: residual includes current return, and all 48 intervals crossing zero does not establish equivalence. | Forecast t+1; label constructed crash ratio as simulation/artifact; explain inconclusive intervals without universal negative claim. | Sent to finance author; draft review pending. |
| Source exclusion | `sources/regime-predictability.tex`, estimand taxonomy and temporal inference: gate source paths survive coefficient ablation; negative fitted gain does not remove oracle information; inference targets capped losses. | Preserve source removal across fit/filter/tuning/scaling, precise sign-disagreement denominator, capped-loss inference and forecast proximity. | Sent to finance author; draft review pending. |
| ICAIF | `sources/icaif2026.tex`, §Decay prediction and Limitations: 7 events/30 pairs, 6/10 holdout accuracy, full-sample HMM assignments. K-selection paragraph conflicts with full-sample footnote. | Mark exploratory, avoid clean prospective-validation claim, show holdout near CV headline; retain original-TeX edition provenance. | Sent to root/ICAIF author; draft review pending. |
| ICAIF | §Online detection: rolling HMM 6.6 days is detection delay with F1 .39; frozen OOS does not survive multiplicity correction. | Do not portray 6.6 days as decay advance warning, or OOS failure as proof of genuine economic decay. | Sent to root/ICAIF author; draft review pending. |

## Review conference, round 2: draft criticism and revisions

### Return-decay residuals

The initial draft correctly matched the regional score tables, interval endpoints, and post-results history contrasts. The reviewer found a material communication omission: the displayed Gaussian risk ratio could be mistaken for a result from the fitted inverse-linear residual. Source §Timing, lines 62, 80, and 87 explicitly uses a known-zero benchmark and a negative-Sharpe cutoff and states that it does not reproduce the fitted nonzero decay curve. The reviewer requested this distinction on slide 4, the poster, and both introductions, plus the score unit on the history table. The author implemented all changes; direct rereading verified the zero-benchmark distinction and explicit non-reproduction/non-attribution qualification in slide 4, the poster, and English/Korean introductions. Content issue resolved.

### UAI

The draft preserves the idealized theorem boundary, 8+8 pooled task composition, null-shift controls, cutoff counterexamples, seed interpretation, and model-family scope. Tables were checked against `tab:main_results`, `tab:stratified_correlation`, and `tab:framework_validation`. The reviewer challenged the opening phrase “before a distribution shift arrives”: validation already occupies the COVID onset period. Author replaced it with “before future test data arrive,” verified by rereading. This is a timing refinement, not a change to the diagnostic's validation-time computation. The author also replotted the exact 16 source tuples to resolve overlapping figure labels. The reviewer inspected both the source script and the replot: the replot extracts the tuples using Python AST rather than retyping them, preserves their coordinates, and labels the figure as a replot. The resulting four callouts are separated and readable.

### ICAIF

The draft retains the original ten-page edition, seven decay events, pair split, 6/10 holdout, and CV standard deviations; it separates regime detection delay from decay prediction and source-region effects from survival-model validation. The reviewer checked the online-HMM table, OOS table, regional narrative, and full-sample caveat against the source. Two specific refinements were requested and implemented by root: label poster ± values as fold standard deviations rather than leaving uncertainty type implicit; translate the Korean description as “교차검증 폴드 간 표준편차” rather than wording suggesting temporal windows. No substantive content blocker remained after these fixes.

### ICLR

The reviewer challenged how the fixed-k asymptotic frontier would be distinguished from finite sample results. The author answered by using a regime table marked “fixed k as n grows,” followed by a separately scoped finite 57-query slide. The reviewer verified query budgets 56/57, the noise table 94 versus 367, the mean-risk ceiling, off-design power, and cohort 2,645 against the source. A residual ambiguous phrase “finite entries are numerical” was revised to “Numerically inverted budgets for 95% limiting power; these are not finite-cohort guarantees.” No substantive content blocker remained.

### AISTATS

The author visibly attaches the known logistic link to the exact confidence result and separates the calibrated-source counterexample and density-cap interval. Numeric scale/rejection/replay tables match their generated source inputs. The reviewer found that “conditional error mass” could be misread as a target conditional probability. The author revised the displayed integrand to `E_P[ωe | T]`, explicitly identifies it as error mass per unit source magnitude mass, and explains that division by `a > 0` gives target conditional error. This preserves the theorem's source-measure integration. No substantive content blocker remained.

### Knowledge graph

Current revision numbers were checked against `empirical_results.tex`: raw-score direction reversal, count additions beyond disagreement, hindsight floors, candidate restriction, and fixed-threshold answer rates. The reviewer asked that the positive learned-count contribution sit beside the raw-score failure and that the changed training regime not be framed as a causal effect of accuracy. The draft does both. The reviewer additionally requested plain definitions of AURC and Brier in the poster and introductions and expansion of LR/HGB on the evidence slide. Author implemented these changes; rereading verified them. Content issue resolved.

### Source exclusion

The author answered the reviewer's question by separating three estimands in a comparison table, explicitly noting that shared-gate ablation is meaningful for its own target. Displayed RMSE and mechanism/noisy-source simulation values were checked against source tables; the 42/240 denominator, 2,400 family, 776 margin inclusions, and 196 identical forecasts match the source's temporal slice. The reviewer requested explicit definitions of fitted excess-risk terms and plain explanation of normalized capped loss. The author implemented both: source-excluded/included excess risks are defined on slide 4, while slide 6, poster, and English introduction explain capping. Direct rereading verified the revisions. Content issue resolved.

## Rendered-artifact review, round 1

Inspected ICAIF poster, UAI Korean introduction, Return-decay English introduction, and UAI slides 3, 5, 9, and 10 as rendered images. The formula explanation, mitigation comparison, takeaway, main numeric hierarchy, evidence visuals, and adjacent limitations are readable. Concrete layout issues were sent to the engines:

- UAI slide 5 caption runs into the footer; deck engine independently identified this and is reducing figure height / reserving caption space. Other sampled slides passed.
- Return-decay English introduction footer sits too close to trim. Print engine agreed to preserve at least 12 mm safety.
- Korean introduction uses avoidable mid-word line breaks. Print engine is changing wrapping to word boundaries.
- ICAIF print artifacts need an explicit ten-page-versus-five-page edition statement, not only a commit hash. Print engine agreed to add it near the author.
- Pinned source links must appear in print footers. Print engine is implementing them.

Second samples inspected: ICAIF cover and slide 6, Return-decay slide 7. These pass: explicit ten-page edition, CV versus holdout distinction, score signs, intervals, uncertainty interpretation, and footers are clear. Revised AISTATS Korean introduction also passes: the Gamma symbol is present, word wrapping is improved, and footer has sufficient trim clearance.

## Review conference, final layout round

Final print samples verified the ICAIF edition note and fold-SD label, Return-decay introduction trim safety and zero-benchmark qualification, and the UAI exact-data replot. A new ICAIF vector-conversion regression was found: regime shading lost transparency and became saturated, reducing line contrast. The print engine confirmed it and is replacing that figure with a print-resolution raster of the original, composited on white; the UAI replot remains vector.

The final UAI evidence slide passes after its figure/caption spacing change. The deck reviewer and this reviewer jointly agreed compact labels for source-exclusion slide 6; the two component gains remain distinguished from their direct difference. The updated AISTATS error-mass definitions caused a formula-slide footer collision, which was sent to the deck engine for a layout adjustment without deleting the normalization distinction.

## Final independent disposition

All requested revisions were verified. The final ICAIF poster has restored pastel shading and a clearly visible blue evidence line; source edition and uncertainty qualifiers remain visible. Its figure was rasterized from the original at 432 dpi to preserve transparency, while the UAI replot stays vector. Final AISTATS slide 6 and source-exclusion slide 6 were viewed after reflow: all definitions, values, component-gain distinctions, captions and footers fit without overlap. The UAI figure slide and representative long-title introductions pass.

The reviewer also verified that `qa/print_metrics.json` again contains all 21 print outputs after targeted rebuilding, and read the aggregate validation report documenting one-page counts, A4/A0 dimensions, text bounds, complete previews, and source links. Full per-artifact layout sweeps and exported-slide checks are additionally documented by the rendering agents and root.

**Blocking content or layout issues found by this reviewer: none remain.**

Research limitations remain intentionally visible rather than “fixed” by presentation: ICLR protocol/risk assumptions and finite-versus-asymptotic scope; AISTATS known-link and density-cap assumptions; UAI observational/model-family scope and exploratory threshold; KG static recorded-target populations and research reuse; both finance audits' retrospective data, dependence and limited inferential resolution; ICAIF small event count, look-ahead and source-description inconsistencies. These are scientific scope statements, not unfinished artifact work.

This review verifies fidelity and communication against the pinned manuscripts and representative rendered artifacts. It does not claim human peer review, independent proof certification, re-execution of every experiment, new empirical replication, or conference acceptance.
