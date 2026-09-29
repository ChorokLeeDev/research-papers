# Diagnosing Conformal Prediction Failures Under Distribution Shift: A COVID-19 Case Study

Chorok Lee | KAIST

A model can be confidently wrong after the world changes. Conformal prediction adds a set of plausible answers, but even that set can stop containing the truth. This paper asks whether the model's feature reliance offers an early warning before future data arrive.

## The question

Coverage is the fraction of examples whose true label appears in a prediction set. Standard conformal guarantees require exchangeability between calibration and future examples. The study examines why classifiers facing a shared COVID-era time split can have very different coverage losses. Its focus is gradient-boosted multiclass classifiers with Adaptive Prediction Sets (APS), targeting 90% coverage.

## The approach

The proposed diagnostic is top-1 SHAP concentration: the largest mean absolute feature attribution divided by the sum across features. It uses validation data only. If one feature dominates the model's measured reliance, a damaging change affecting that feature may make the predictor fragile. An idealized probability-mixture theorem formalizes a mechanism under explicit assumptions; it is not a guarantee for measured TreeSHAP concentration.

## What the evidence shows

Eight SALT supply-chain tasks exhibit coverage losses from 0.1 to 77.1 percentage points. The main experiments use 50 independent training seeds per task, not a 50-model prediction ensemble. Across a pooled set of 16 multiclass tasks in 9 domains, concentration and coverage loss have Spearman correlation 0.853, with reported p < 0.001 and bootstrap 95% interval [0.50, 0.96]. The pool comprises the original eight SALT tasks and eight external tasks. Four external tasks have documented shifts and four are null-shift controls. Within SALT, standard shift indicators are weakly associated with the severity of coverage loss.

## What the result does not promise

The exploratory 40% cutoff has exceptions. Sales-office exceeds it but barely loses coverage; KDDCup99 falls below it but has a seed-sensitive mean loss above the study's at-risk cutoff. A protective-secondary-feature rule is based on one case. The diagnostic is weaker for random forests and MLPs; low concentration does not rule out neural-network failures. The pooled correlation is not wholly independent validation of the threshold, and an association does not show that reducing concentration will necessarily improve coverage.

## Why it matters

The work adds a model-specific question to reliability assessment: does a plausible shift threaten the features on which this predictor relies? Concentration can guide inspection and monitoring before deployment. A prospective evaluation should freeze the diagnostic rule and test both coverage and prediction-set usefulness. Adaptive calibration may recover coverage by returning larger sets, so apparent statistical recovery can still leave a system less useful.

## KEY TAKEAWAY

Treat concentrated reliance as a warning to investigate, especially for boosted multiclass conformal models. It is not a certificate of failure or safety.

Source: https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/96d9616961e5ae8607373181d35262cb21a2b0d1/paper/main.tex
