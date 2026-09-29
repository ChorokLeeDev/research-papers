# Predicting Factor Decay: ML Models for Cross-Factor Predictability Erosion

Chorok Lee | KAIST

Original ten-page TeX preprint edition; separate from the five-page submission.

A financial relationship can help a forecasting model for years and then weaken. This paper asks whether the change in that relationship can itself be anticipated.

## The research question

A factor is a return series representing an investment characteristic, such as value, size, or momentum. The motivating example asks whether past value-factor returns (HML) help predict the size factor (SMB), and how long that predictive contribution lasts. The focus is statistical predictability and its durability, rather than the economic cause of a factor's return.

## How the study works

The primary analysis covers six daily factors over 1990–2024 and 30 directed pairs. A Student-t hidden Markov model groups observations into statistical regimes. Within those regimes, Granger tests examine whether source-factor lags add information beyond the target's own history. Features such as initial signal strength and rolling variability then feed classifiers and survival models. The operational decay label concerns a loss of statistical significance within five years.

## What the paper reports

A random survival forest achieves a five-fold cross-validation C-index of 0.933, with a fold standard deviation of 0.097. That metric measures ordering of event times, not return prediction accuracy. The analysis contains only seven decay events among thirty pairs. On a separate ten-pair holdout, classification accuracy is 60%, or six correct predictions. The main US value-to-size relationship fails corrected tests in the 2013–2024 evaluation. Some regional crisis-state effects remain, but they do not independently validate the decay model.

## What the findings mean

The results motivate studying signal durability as a monitoring problem. They do not yet establish reliable future-time performance. Factor pairs share underlying series, the focal pair was selected after inspection, and some pre-2012 decay fits use regime assignments estimated with the full sample. The manuscript also describes the state-selection window inconsistently. A fully prospective evaluation would refit every stage using only data available at each training date. The separate 6.6-day rolling-HMM result measures regime detection delay after a change, not advance warning of factor decay.

## KEY TAKEAWAY

The distinct question is when an observed predictive relationship weakens. The available evidence supports further exploratory testing, with uncertainty and information timing central to the next study.

Source: https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/a0bd43ea47898011d0661710975658a8969299d5/arxiv/original-source-20260929/main.tex
