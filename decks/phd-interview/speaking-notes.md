# Chorok Lee — research interview speaking notes

Nine slides. One short read-aloud paragraph per slide, based on the [user-edited TAIL script](speaking-notes-source.md). The **Back to point** line is a cue for returning after a question.

[UAI](#slide-5) · [Thesis I](#slide-6) · [Thesis II](#slide-7) · [ICLR](#slide-8) · [Basic setup questions](setup-questions.md)

The times are a rehearsal budget. Questions and pauses can change the duration.

<a id="slide-1"></a>

## 1. Can we tell when a model stops being reliable? · 00:00–00:40

> **Back to point:** “What can the evidence tell us about reliability?”

Thank you for the opportunity to speak with you. I am Chorok Lee, a master’s student in Software Engineering at KAIST. My research asks what our available evidence can tell us about predictive reliability. I will briefly introduce my background, then explain how a study of conformal coverage failures led to my thesis and related work on missing labels. I will finish with the direction I would like to pursue during a PhD.

<a id="slide-2"></a>

## 2. From economics to building and evaluating ML · 00:40–01:50

> **Back to point:** “My engineering experience shapes how I investigate research questions.”

My undergraduate degree is in Economics from Yonsei University’s Underwood International College, and I spent an exchange year at Dartmouth. I worked as a software engineer before starting my master’s at KAIST in February 2025, supervised by Professor Insik Shin. I expect to graduate in February 2027. My preparation includes probability, statistics, stochastic calculus, Bayesian machine learning and deep learning. At SAP Labs Korea, I have worked on retrieval evaluation, agent workflows and cloud telemetry; before SAP, I built data pipelines and GraphRAG components at a legal AI startup. These experiences make implementation and measurement a natural part of my research. During a PhD, I want to deepen the statistical foundations behind those measurements.

<a id="slide-3"></a>

## 3. Does the set contain the right answer? · 01:50–02:55

> **Back to point:** “Coverage asks whether the set includes the true answer.”

When a single answer is uncertain, a model can return a set of possible labels. **Coverage** is how often that set contains the true label. **Miscoverage** is how often it misses, so it equals one minus coverage. Conformal prediction promises a minimum coverage on average when calibration and future cases are statistically interchangeable. After deployment, the inputs can change and the true labels may be unavailable. We can still see model scores and input changes, but those alone need not tell us whether the set still contains the right answer. My work asks what evidence is enough to check that particular promise.

<a id="slide-4"></a>

## 4. Diagnose → understand limits → ask for evidence · 02:55–03:40

> **Back to point:** “Three projects ask what our evidence can establish.”

There are three stages in this research trajectory. My published UAI 2026 paper asks whether a model’s reliance on one feature helps explain coverage loss under shift. My master’s thesis, submitted to AISTATS 2027, asks what shift and confidence summaries can actually tell us about coverage. My related ICLR 2027 submission asks how much we can learn by checking a limited number of missing labels. The latter two papers are under review. Together, they move from observing failures to understanding what our summaries leave unresolved, then to asking for information that can help.

<a id="slide-5"></a>

## 5. A shift can hit what a model relies on · 03:40–05:10

> **Back to point:** “A useful feature can become a vulnerability if its predictive relationship changes.”

The starting point was a COVID-19 supply-chain case study. For each task, a LightGBM classifier takes a feature row and produces class probabilities; APS turns those probabilities into a label set. I used SHAP to measure how strongly the fitted model uses its top feature, as measured by SHAP. The question was whether a change affecting that feature could help explain coverage loss. The published sixteen-task summaries reported a positive association, but later checks with a different pipeline did not reproduce this pattern, so this remains exploratory. A simplified model gives a conditional bound when its dominant component stops supporting the true label. That raised the next question: what information do shift summaries leave out?

<a id="slide-6"></a>

## 6. Same distance. Different direction. Different coverage. · 05:10–07:00

> **Back to point:** “Direction belongs to the input shift; the model score is one number.”

I first use a fixed linear model with two labels, 0 and 1. It turns a feature vector into one numerical score. I assume a known logistic formula also gives the actual chance of label 1. Imagine the model uses only the first of two coordinates. Moving the inputs along that coordinate changes its scores; moving them sideways along the second does not. I construct two Gaussian shifts with the same distance but these different directions. Distance summaries that ignore the direction give the same value, while coverage can differ. Under the known label rule, keeping the distribution of score magnitudes is enough to determine coverage for every choice of set threshold.

<a id="slide-7"></a>

## 7. The same score can hide different chances of error · 07:00–08:50

> **Back to point:** “The same score can hide different chances that the set misses the answer.”

Next, I remove that assumption: we no longer know how the score connects to the true label. We assume the label rule for each full input stays the same, while the mix of inputs changes. Many features are squeezed into one score, so different inputs can get the same score while their sets have different chances of missing the answer. Using source labels, target scores and a limit on how much input types can become more common, I work out the lowest and highest possible coverage. These bounds are **sharp**: permitted cases reach each end. The range shows whether the evidence is enough to support the promised coverage.

<a id="slide-8"></a>

## 8. A limited audit can test a reassuring record · 08:50–10:25

> **Back to point:** “The question is how many existing answers we need to check.”

My related ICLR paper takes the next step: asking for missing answers. Imagine a model has already made a thousand predictions, but five hundred existing outcomes are withheld. We keep the model fixed. After the partial record is committed, we privately sample pending cases and check their answers. We raise an alarm only when the error evidence passes a rule designed to limit false alarms. In one specified truthful-label experiment, distinguishing 10% from 20% error at a 5% false-alarm level needs a minimum budget of 57 queries for at least 95% detection. More generally, I prove the best worst-case detection limit for a fixed query budget as the cohort grows, and give a rule that reaches it.

<a id="slide-9"></a>

## 9. Turn a failure into a precise, testable question · 10:25–11:10

> **Back to point:** “I connect a research question to an implementation and a test.”

The way I contribute is by connecting empirical failure patterns to precise statistical questions, then building checks that test their limits. In my thesis, that meant counterexamples, coverage bounds, simulations and controlled replay on real-world benchmark datasets. My engineering background helps me build reproducible pipelines and keep experimental assumptions clear. During a PhD, I want to strengthen the theoretical formulation through close collaboration, while developing methods and experiments that make reliability claims useful. Thank you, and I would be happy to discuss the model setups, the results or possible first projects.
