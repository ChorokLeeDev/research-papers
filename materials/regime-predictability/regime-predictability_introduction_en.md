# Source Exclusion in Regime-Gated Forecasting: A Cross-Market Audit of Equity-Factor Predictability

Chorok Lee | KAIST

If a model predicts tomorrow's small-stock returns using value-stock history, removing the value-stock regression coefficients sounds like a clean test of usefulness. But the information may remain inside the model's estimate of the market regime. This paper audits that hidden route.

## The question

Regime-gated forecasts blend several regression predictions using estimated state probabilities. A source factor can influence the explicit lag coefficients and the gate that weights the regressions. Shared-gate ablation removes only the explicit lag route. Complete source exclusion also removes the source from gate fitting, filtering, preprocessing, and tuning. Both comparisons are meaningful, but they answer different questions. A separate gate-value comparison asks whether gating improves on a pooled model with the same raw information.

## How the study evaluates it

The study first reconstructs the US HML-to-SMB relation: value-minus-growth information predicting a small-minus-big return spread. It then freezes an expansion across all 30 ordered directions among six factors in the US, Europe, Japan, and Asia Pacific excluding Japan. The expansion uses chronological training, validation, and annual refits, with January 2025–August 2026 reported separately. Five procedure comparisons and four weighting choices create a simultaneous temporal family of 2,400 endpoints. Inference concerns normalized squared loss capped at one, limiting the contribution of large errors; ordinary MSE remains descriptive.

## What the market evidence says

Shared-gate and complete-exclusion point estimates have opposite signs in 42 of 240 unweighted temporal HMM comparisons. Yet none of the 2,400 temporal endpoints has a simultaneous directional crossing. All 776 intervals inside a prespecified ±0.005 score-resolution margin are already explained by the compared forecasts being close; 196 pairs are identical. These results demonstrate sensitivity to removal and limited resolution, not confirmed reversals of population predictive content or general absence of information.

## Why an informative source can still hurt

Under squared loss, additional information has nonnegative oracle value when information sets are nested. Fitted models can nevertheless lose because extra approximation or estimation error outweighs that benefit. In a controlled noisy-source simulation, 10% binary corruption leaves oracle gain at +0.0708, while Gaussian- and Student-t-HMM gains become −0.0494 and −0.0486. This is synthetic evidence about procedure costs, not a financial mechanism. Correlated markets, retrospective data vintages, unverified outside exposure, and a limited architecture family constrain the empirical interpretation. Capped-loss intervals do not guarantee ordinary-MSE coverage, practical trading value, or a multi-day warning horizon.

## KEY TAKEAWAY

To ask whether a variable helps, first specify every path by which its information enters the model—and distinguish the variable's information from the fitted model's ability to use it.

Source: https://github.com/ChorokLeeDev/regime-predictability-revision/blob/ad08f1e2aeef9e4ec667b787d8ae00430c60f65f/manuscript.tex
