# When Marginal Shift Magnitudes Cannot Identify Conformal Coverage Loss

Chorok Lee | KAIST

A deployment dataset can move far from training data without harming a particular predictor, or move in a consequential direction that a generic drift magnitude does not reveal. This paper asks when common monitoring summaries actually determine prediction-set coverage.

## Question

Coverage is the probability that a prediction set contains the true label. A drift test instead asks whether data distributions differ. The paper studies what is lost when deployment data are reduced to rotation-invariant discrepancy values or to a frozen classifier’s confidence distribution. It separates a change alarm from an estimate of the coverage consequence, then asks what additional assumptions can restore identification.

## Equal drift can have unequal effects

Under a known binary logistic label law, two equal-length Gaussian translations can produce identical source-to-target drift magnitudes. One follows the model’s score direction and can change coverage; the other is orthogonal and leaves it unchanged. A calibrated scale construction approaches excess miscoverage 1/2 − α, or 40 percentage points at α = 0.1. This is a sharp mathematical example, not a typical failure rate. Its standardized shift diverges, and raw target observations can still distinguish the two target laws.

## When confidence is sufficient

With the known logistic conditional label law, the distribution of absolute scores determines the complete coverage curve; equal curves also imply equal absolute-score distributions. Maximum predictive confidence carries exactly the same information in this binary model. This is stronger than detecting drift, but it relies on the known label law. Perfect source calibration alone is insufficient: the paper constructs targets with the same constant 90% confidence and unchanged signed scores but error rates of either 0% or 20%, while source error is 10%. The full conditional label law remains unchanged; hidden covariate groups are reweighted.

## What can be said without the link

Given source confidence calibration, target confidence frequencies, and a specified bound Γ on the covariate density ratio, the paper derives a sharp interval of possible target errors. The same two target laws attain its lower and upper endpoints at every threshold. With a fixed full source kernel, confidence becomes sufficient when conditional errors have no hidden variation within nondegenerate confidence levels. A finite-sample version uses labeled source data and unlabeled target scores, allowing threshold choice within a prespecified grid.

## Evidence and limits

Simulations and independent optimization checks support the formulas. Controlled learned-score replay on two UCI datasets records 7,200/7,200 simultaneous band containments across 72 conditions, but the intervals are conservative; only nine conditions improve risk-only population bounds. These are sensitivity results under an imposed cap, not deployment validation. Confidence observations cannot establish Γ or rule out conditional-label shift. The finite guarantee is fixed-sample and does not cover unrestricted repeated monitoring.

## KEY TAKEAWAY

A useful monitor must report what its data and assumptions identify: a distribution change, an exact coverage curve, or only a defensible interval.

Source: https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/76661fdf862959345ea22ea2ab5494a4171a6eab/paper_aistats2027/reliance_alignment.tex
