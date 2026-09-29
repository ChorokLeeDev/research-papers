# Return-Decay Residuals and Tail-Risk Forecasting: Timing Artifacts, Conditional Inference, and Cross-Market Evidence

Chorok Lee | KAIST

A strategy has recently performed worse than its expected decline. Is that a warning that next month will bring a large loss—or does the warning simply reflect a loss already observed? This paper audits that distinction for equity-factor returns.

## Question

The proposed signal is a return-decay residual: a curve fitted to earlier rolling Sharpe ratios minus the currently observed rolling Sharpe. A large positive residual means performance has fallen below the curve. The paper asks whether this feature improves next-month tail-loss probabilities, with losses defined below a fixed historical tenth percentile. It separately asks what would justify interpreting the feature as investor crowding. These are different claims: predictive usefulness alone would not identify a participation mechanism.

## Why timing and benchmarks matter

The current rolling Sharpe includes the current return. Using it to explain a crash in that month can create a mechanical association. In a simplified zero-benchmark example, independent Gaussian returns and a negative-Sharpe high state produce an exact same-month risk ratio of 1.606 for a 36-month window; the next-month population ratio is one. This isolates timing, without reproducing the fitted residual or quantifying the historical artifact. A residual adds no information conditional on all its generating inputs, although it may help a restricted learner.

## What the study does

An eight-factor US reconstruction is followed by a fixed geographic extension covering six factors in Europe, Japan, and Asia Pacific excluding Japan. Ridge-logistic forecasts compare common return and volatility controls with residual, raw-Sharpe, and alternative-residual additions. The extension uses common histories, chronological training and validation, frozen and annually updated fits, and separate 2015–2024 and January 2025–August 2026 evaluations. Established simultaneous sequential bounds assess conditional expected score differences while allowing dependence under their stated assumptions.

## What the evidence supports

For the main regional era, the hyperbolic residual increases pooled log loss by 0.00704 with frozen fitting and 0.00233 with annual refitting; lower loss is better. Yet frozen Brier score improves slightly, and matched-history US comparisons can favor the residual. All 48 final conditional intervals include zero and still allow nontrivial benefits. Post-results diagnostics show how history, event thresholds, penalty selection, and feature coordinates can reverse rankings. The findings support careful evaluation of the tested procedure, not universal proxy failure or crowding identification. Retrospective vintages, correlated regions, disclosed prior research information, and unverified release times limit confirmation and live-trading claims.

## KEY TAKEAWAY

A disappointing performance residual may be useful, but timing-correct prediction, strong matched benchmarks, and uncertainty must establish that usefulness before an economic explanation is attached.

Source: https://github.com/ChorokLeeDev/factor-regime-revision/blob/87dced92128746b8f7c82c5ad1a659e2ff9ad929/manuscript.tex
