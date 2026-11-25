# Chorok Lee — research interview speaker notes

Nine slides. These are the corrected notes embedded in the reusable deck. The user-edited source script is preserved separately.

The 11:10 schedule below is a provisional rehearsal budget from sections 1–9, not a recorded duration. Adjust delivery and pauses within the interview’s time limit.

## 1. Can we tell when a model stops being reliable? · 00:00–00:40

Thank you for the opportunity to speak with you. I am Chorok Lee, a master's student in Software Engineering at KAIST. My research asks what the information available to a model evaluator can actually establish about predictive reliability. I will briefly introduce my background, then explain how a study of conformal coverage failures led to my thesis on identification and related work on selective labels. I will finish with the direction I would like to develop during a PhD.

## 2. From economics to building and evaluating ML · 00:40–01:50

My undergraduate degree is in Economics from Yonsei University's Underwood International College, and I spent an exchange year at Dartmouth. I then worked as a software engineer before starting my master's at KAIST in February 2025, supervised by Professor Insik Shin. I expect to complete the degree in February 2027. My graduate preparation includes probability and statistics, stochastic calculus, Bayesian machine learning, and deep learning.

In parallel, I have worked at SAP Labs Korea as a software engineering intern. My projects have included retrieval evaluation, agent workflows, and tools for accessing cloud telemetry. Before SAP, I built data pipelines and GraphRAG components at a legal AI startup. These experiences make implementation and measurement a natural part of my research. For a PhD, I want to develop the statistical foundations behind those measurements: when a seemingly reassuring evaluation is informative, and when it cannot answer the question we care about.

## 3. Does the set contain the right answer? · 01:50–02:55

When a wrong answer is costly, a prediction set gives us a way to express uncertainty. Coverage is the probability that the true label falls inside that set. Under standard exchangeability assumptions, conformal prediction provides a marginal guarantee across test points.

After deployment, inputs may shift and the true labels needed to check coverage may be missing or selective. We can still observe features and model scores, so a drift alarm or stable confidence histogram may look reassuring. But these measure different objects. A shift metric describes changes in inputs. Coverage also depends on how the inputs and scores relate to true outcomes. My work asks which parts of that relationship survive in the summaries we observe, and what conclusions remain justified when they do not.

## 4. Diagnose → understand limits → ask for evidence · 02:55–03:40

There are three stages in this research trajectory. My published UAI 2026 paper studies a diagnostic: whether feature-importance concentration helps anticipate coverage vulnerability in gradient-boosted classifiers. My master's thesis, submitted to AISTATS 2027, asks an identification question: what can shift and confidence summaries actually tell us about coverage? My related ICLR 2027 submission asks an intervention question: how much can a limited label audit reveal about model risk when labels are selective and noisy? The latter two papers are under review. Together, they move from observing failures to understanding information limits, and then to acquiring information that can resolve them.

## 5. A shift can hit what a model relies on · 03:40–05:10

The starting point was a COVID-19 supply-chain case study. Several classification tasks experienced the same temporal disruption, but their conformal coverage deteriorated very differently. Shift indicators detected the disruption without explaining that variation in failure severity.

I studied SHAP concentration: how much of the measured feature attribution is assigned to the top feature. It is a proxy for model reliance. Across sixteen multiclass tasks in nine domains, greater concentration was associated with greater coverage loss in the gradient-boosted classifiers studied. I also derived an idealized score and coverage-bound result under explicit assumptions; this is not a theorem that actual coverage must always decrease.

The diagram is schematic. A shift that hits a feature with concentrated attribution can expose a vulnerability, but the diagnostic is exploratory and model dependent. It does not explain the global-sensitivity failures seen in neural networks. That raised the next question: is a diagnostic imperfect, or has the summary already discarded information needed to identify coverage?

## 6. Same distance. Different direction. Different coverage. · 05:10–07:00

I first study a controlled binary classification setting with a known logistic relationship between scores and labels. This is stronger than general source calibration.

Imagine two Gaussian shifts with the same magnitude. One is aligned with the model-score direction; the other is orthogonal to it. Rotation-invariant shift summaries give the same value, yet coverage can differ. The point is the lost directional information, not that every aligned shift must be harmful. Estimating the same magnitude more accurately cannot restore what that summary discarded.

The positive result is specific to this known-link setting: the absolute-score distribution determines the full coverage curve. That tells us what information coverage needs here. Next, I remove the known-link assumption.

## 7. The same score can hide different chances of error · 07:00–08:50

Next, the score-to-label relationship is no longer known. A score compresses many inputs into one number. Inputs with the same score may still have different conditional chances of error. Under covariate shift, reweighting those inputs can change coverage without changing the observed score summary.

The sharp range requires source confidence information, observed target confidence frequencies, the covariate-shift structure and an assumed bound on the covariate density ratio. Under those constraints, I characterize the best and worst coverage still compatible with the evidence. Sharp means that admissible laws attain the endpoints; it does not mean that data alone supply all the assumptions.

The structural refinement explains when this ambiguity disappears: conditional errors must have no hidden variation within confidence levels, apart from degenerate weight constraints. Source calibration by itself is not enough. The range makes the unresolved uncertainty visible instead of hiding it behind a single coverage estimate.

## 8. A limited audit can test a reassuring record · 08:50–10:25

My related ICLR paper asks what additional labels can establish. Imagine a fixed cohort whose outcomes already exist in an archive, but some labels have been withheld from the evaluator. The partial record is committed before an audit. A model may look reassuring because its difficult cases are still unlabeled.

With a limited budget, the evaluator privately requests some of those existing labels and tests whether risk is excessive while controlling false alarms. Finding one error is not by itself proof of excessive risk. The paper characterizes the exact fixed-query asymptotic minimax detection frontier over adaptive policies and gives an attaining rule for truthful queries, under its stated risk and audit protocols.

This is not a result about recovering nonexistent loan counterfactuals or optimally splitting a budget across groups. It asks what a fixed audit budget can establish, and what remains unresolved when label quality is uncertain.

## 9. Turn a failure into a precise, testable question · 10:25–11:10

The way I contribute to a research group is by connecting empirical failure patterns to precise statistical models, and then building checks that test those models' limits. In the UAI project, I started from an observed failure pattern; in my thesis, I turned that into counterexamples, a sufficient statistic, and sharp bounds, validated through simulations and controlled replay on UCI datasets.

My engineering background helps me build reproducible pipelines and keep experimental assumptions separate from deployment claims. What I want to strengthen during a PhD is deeper theoretical formulation through close collaboration—especially in robust conformal procedures and the design of useful uncertainty sets.

