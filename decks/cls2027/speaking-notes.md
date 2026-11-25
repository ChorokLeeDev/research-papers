# Chorok Lee · CLS 2027 · 4-minute research video — timed English script

Planned runtime: **04:00**. 5 main slides. Read-aloud text: 480 words.
Times are rehearsal targets, including pauses and slide changes. Time one full rehearsal before presenting. Do not read source footers aloud.

Record your own spoken presentation in English. Save the final video as **13470_Chorok_Lee_CLS2027.mp4**. The deck and script are preparation files, not the requested video.

| Slide | Time window | Duration |
| --- | --- | --- |
| 1. Chorok Lee | 00:00–00:40 | 40s |
| 2. The starting point: coverage fails differently | 00:40–01:15 | 35s |
| 3. Thesis: identify a range instead of assuming a point | 01:15–02:15 | 60s |
| 4. Related work: how much can more labels establish? | 02:15–03:05 | 50s |
| 5. At CLS: two projects in reliable evaluation | 03:05–04:00 | 55s |

## 1. Chorok Lee · 00:00–00:40

Hello, I am Chorok Lee, a master's student in Software Engineering at KAIST, supervised by Professor Insik Shin. I expect to complete my degree in February 2027. I previously studied Economics at Yonsei University, with an exchange year at Dartmouth. My research asks what observable evidence can establish about predictive reliability, and which additional observations make evaluation informative. I study these questions under distribution shift and selective or noisy labels.


## 2. The starting point: coverage fails differently · 00:40–01:15

My published UAI 2026 paper began with a COVID-19 case study: classification tasks facing the same temporal disruption lost conformal coverage by very different amounts. I studied SHAP concentration, the share of feature importance assigned to the top feature, as an exploratory vulnerability diagnostic. In the gradient-boosted models studied, concentration was associated with greater coverage loss. The diagnostic has model-dependent limits. This led me to a deeper question: which reliability conclusions can the summaries we observe actually determine?


## 3. Thesis: identify a range instead of assuming a point · 01:15–02:15

My master's thesis, submitted to AISTATS 2027 and currently under review, formalizes that question. First, in a binary setting with a known logistic label law, shifts can have equal rotation-invariant magnitudes but different conformal coverage. A more accurate estimate of the same magnitude cannot recover information it discarded. Under that known link, the absolute-score distribution does determine the full coverage curve.

Second, I remove the known-link assumption. Given source confidence calibration, target confidence frequencies, and an assumed covariate density-ratio bound, I derive a sharp partial-identification envelope: the range of coverage compatible with those inputs. The endpoints are attainable. This distinguishes uncertainty caused by a limited sample from ambiguity that the observed summaries cannot resolve. For a PhD, I want to extend this perspective to risk scores whose calibration is itself uncertain.


## 4. Related work: how much can more labels establish? · 02:15–03:05

My related ICLR 2027 submission studies evaluation when difficult cases can be missing their labels. For a frozen predictor and cohort with a committed partial record, I ask how well an additional audit can detect excessive risk while controlling false alarms. The paper characterizes an exact fixed-query asymptotic minimax detection frontier and an attaining rule for truthful queries.

With uncertain audit-label reliability, more requests need not resolve the ambiguity. Query count, knowledge of label quality, and cohort size are different resources. These results depend on specified risk and audit protocols. The broader question is how to acquire evidence that makes a reliability claim informative.


## 5. At CLS: two projects in reliable evaluation · 03:05–04:00

At CLS, I would like to pursue two projects from my motivation letter. First, partial identification of risk-score calibration under shift: characterize the confidence law itself as a set of possibilities supported by evidence. Second, label-budget lower bounds for certifying a deployed model's risk under selective observation. I would be excited to connect these questions to Celestine Mendler-Dünner's work on risk scores and Moritz Hardt's work on evaluation limits. The joint ETH and Tübingen environment, including the twelve-month exchange, would let me develop one problem through theory and empirical evaluation, with sustained collaboration across groups. Thank you.
