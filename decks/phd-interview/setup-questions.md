# If the professor asks about the setup

Use the short answer first. The read-aloud script stays in [speaking-notes.md](speaking-notes.md).

| Paper | What goes in? | What does the model do? | What comes out? |
|---|---|---|---|
| UAI | A row of tabular features | A frozen LightGBM classifier predicts class probabilities; APS builds a set | A set of possible labels; we check whether it includes the true label |
| AISTATS | A feature vector | A fixed model produces one numerical score; a set rule uses it | A label set; we ask what its coverage can be |
| ICLR | A partial record of correct, wrong and pending predictions | An auditor privately queries some existing pending answers | One alarm decision, with a false-alarm limit |

## UAI

1. **Setup:** feature row → class probabilities → prediction set. SHAP separately explains the fitted model’s output.
2. **Assumptions:** the usual coverage promise needs exchangeable calibration/test cases and independent model fitting. The theoretical mechanism adds explicit assumptions about a damaged component.
3. **Hypothesis:** could reliance on a feature help explain failure when its predictive relationship changes?
4. **Result:** a historical association, with documented selection, pipeline and follow-up limitations.
5. **Theorem:** a bound for an idealized probability mixture. Its mixture share is distinct from measured SHAP concentration.

**“If the labels are random, shouldn’t SHAP be spread evenly?”**

“Not necessarily. If labels are independent of the inputs, there is no real population signal. But a model fitted to a finite sample can still learn accidental patterns and use some features more than others. SHAP explains that fitted model. Random labels alone do not force equal feature attribution.”

If the model is constant, all feature attributions can be zero. A top-feature share then needs a convention because the total is zero. Stochastic labels that still depend on the inputs are a different case: they can contain genuine signal.

**“Isn’t one very useful feature a good thing?”**

“Yes, it can be. The concern is whether the relationship making it useful changes. Concentration by itself does not say that the feature is bad or that coverage will fail.”

**“What exactly is concentration?”**

“For each feature, average the size of its SHAP contribution. Divide the largest feature average by the total. It is a summary of the fitted model’s attribution, not a proof of causal importance.”

**“Does 90% mean you include labels until probabilities add to 0.9?”**

“No. Ninety percent is the desired coverage. A separate labelled calibration sample supplies the score threshold. The threshold is not automatically 0.9.”

**“What does APS do?”**

“It orders labels by their reported probability and computes cumulative scores. The label-set rule then uses a calibration threshold.”

There are different conventions. At probabilities (0.60, 0.25, 0.15), inclusive candidate scores are (0.60, 0.85, 1.00). At threshold 0.80, score inversion includes only the first label. A rule that also includes the threshold-crossing label returns the first two. The audited theorem uses score inversion; the historical SALT implementation used crossing sets.

**“What did you actually prove?”**

“For a simplified model combining two probability components, I assume one component stops supporting the true label and the other stays stable. Under those assumptions, increasing the damaged component’s share worsens particular score and coverage bounds. This is not a proof that measured SHAP concentration always lowers actual coverage.”

For the monotonic bounds, hold the threshold, damage bound and residual law fixed. The expected score lower bound rises when the damaged component’s true-label bound is below the residual mean. The coverage upper bound is non-increasing under the theorem’s additional threshold condition. For the coverage upper bound with lambda < 1, the extra condition is ε ≤ (1−q)/(K−1); for the expected score lower bound, it is ε < E[h(y_true)]. Keep q, ε and the residual law fixed. The theorem’s share is lambda. Measured SHAP concentration is C. No equality between them has been established. The historical selected-16 correlation is 0.853; all 17 give 0.654. The separate later eight-task panel gives −0.238 with inclusive sets and −0.262 with crossing sets. Those protocols must remain distinct.

## AISTATS I — first, the label rule is known

1. **Setup:** vector input x → scalar score s(x) = wᵀx → model probability → label set. Labels are 0 or 1.
2. **Assumptions:** the actual chance of label 1 equals the logistic formula applied to the score, in both source and target. The equal-distance construction also uses source symmetry and rotation-invariant summaries.
3. **Hypothesis:** can a distance summary identify how much coverage changed?
4. **Result:** equal distance summaries can accompany different coverage. Keeping score magnitudes instead is sufficient under the known rule.
5. **Theorem:** the negative result applies to the stated restricted summaries; the positive result applies to the full score-magnitude distribution under the known rule.

**“What is the input, and what is the score?”**

“The input is a feature vector. In the theoretical example, a fixed linear model multiplies it by a weight vector and adds the contributions to produce one number. That number is the binary logit.”

In the theory, the score function is prescribed. The real-data replay fits, then freezes, regularized logistic classifiers. It does not assume their fitted probabilities equal actual target label probabilities.

**“Is this an MLP’s hidden vector?”**

“No. An MLP can have a hidden vector, but that is not the score in this construction. The input and weight are vectors; the score is scalar. The two class logits can be written as (0, s), with a scalar gap s.”

**“If the score is one number, where is the direction?”**

“Direction is in the input space. If the model uses only the first coordinate, moving that coordinate changes the score. Moving the second coordinate does not. Those movements can have the same length.”

**“What is the score-to-label rule?”**

“A logistic formula converts the score into a reported probability. Here we additionally assume that it is the actual chance of label 1. Training a classifier does not itself establish that assumption.”

A score of +2 gives about 88% for label 1; −2 gives about 12% for label 1. Under the known rule, the predicted label is about 88% likely to be correct in both cases.

**“What is the absolute-score distribution?”**

“Take each score’s size and ignore its sign. Then record how often small and large sizes occur. It is a distribution, not one average confidence number.”

**“What is the whole coverage curve?”**

“At one set threshold, coverage is one number. Vary the threshold and you get a coverage value for every choice. Those values form the curve.”

**“What threshold turns the score into label 1?”**

“A point classifier can choose label 1 when its logit is at least zero, equivalent to probability at least 0.5. A conformal prediction set uses a separate candidate-label score and threshold.”

In this paper the candidate score is R(x,y) = −(2y−1)s(x), and the set includes y when R(x,y) ≤ q. For q ≥ 0, it returns both labels when |s| ≤ q, otherwise just the predicted label.

## AISTATS II — now, the label rule is unknown

1. **Setup:** keep a frozen numerical score, but no known formula connecting it to actual labels. We observe labelled source examples and unlabelled target scores.
2. **Assumptions:** the chance of a label at a given full input stays fixed; only the mix of inputs changes. A stated cap limits how much an input type can become more common.
3. **Hypothesis:** can the same score distribution conceal different coverage?
4. **Result:** yes. Different mixes of inputs can have the same scores and different chances of error.
5. **Theorem:** calculate the smallest and largest coverage compatible with the supplied summaries and cap. Allowed laws attain the endpoints.

**“How can the score stay the same?”**

“The score compresses many features into one number. Different inputs can land on that number. The model need not preserve every difference that matters for the true label.”

**“Give me a concrete example.”**

“Imagine the model always reports 90% for label 1 and returns the set {1}. In the source, 90% of inputs really have label 1. In a permitted new mix, that becomes 80%; in another, 100%. Every model score stays the same.”

This is the paper’s constant-score construction: the conditional label rule for each full input remains fixed, while input frequencies change. A ratio cap of two permits both displayed target mixes. It is a mathematical example, not a loan experiment.

**“Is error rate one minus coverage?”**

“Miscoverage is one minus coverage: the set misses the true label. Ordinary classification error is different: the single predicted label is wrong. They coincide in the example because the set contains just one label.”

If the predicted label is 1, the true label is 0 and the set is {0,1}, the point prediction is wrong but the set covers the answer. In the paper’s general formula, conditional classification error helps calculate miscoverage only on inputs where the set is a singleton.

**“Is the frequency cap a neural-network weight?”**

“No. It limits changes in how common input types are. For example, a cap of two allows a type present in 10% of source cases to appear in at most 20% of target cases. It is an assumption about the population, not the model’s trained parameters.”

**“When does confidence become enough?”**

“In the nondegenerate setting, when inputs with the same confidence also have the same true chance of being misclassified. Then changing their mix adds no hidden error variation. There are also degenerate cases where the allowed changes leave no freedom.”

**“Why focus on coverage?”**

“It checks the promise a prediction set makes: how often it includes the true answer. A range tells us whether the evidence supports that promise. Set size and other performance measures still matter.”

An error interval [L,U] becomes a coverage interval [1−U,1−L]. A population sharp interval and an interval estimated from finite samples are different; the latter must account for sampling uncertainty.

## ICLR — checking existing missing answers

1. **Setup:** freeze the predictor; commit the partial error record; privately query existing pending answers; make one alarm decision.
2. **Assumptions:** the hiding pattern is fixed before private queries. State the risk class, label reliability and hard query budget.
3. **Hypothesis:** distinguish an acceptable error law from a specified higher-error law while limiting false alarms.
4. **Result:** in the stated finite truthful experiment, 57 queries are necessary and sufficient for at least 95% detection at a 5% false-alarm level. The separate limiting minimum is 56.
5. **Theorem:** identify the best worst-case detection power for a fixed number of queries as the cohort grows, even among adaptive policies, and give a rule that reaches that limit.

**“What is the model?”**

“The predictor is already trained. The mathematical model in this paper is the auditor: it sees correct, wrong and pending entries, chooses which pending identities to query, and produces an alarm decision. Its theorem does not train another classifier or use feature vectors.”

**“Which cases do you query?”**

“For the truthful limiting result, privately sample uniformly among pending cases and combine the queried errors with the revealed record in a controlled test. The finite rule is calibrated separately. The paper does not claim an optimal split across high-risk subgroups.”

**“Why isn’t that just random sampling?”**

“The sampling step is simple. The contribution is proving how much detection power any strategy can guarantee against the allowed hiding patterns, and showing this rule reaches that limit. The finite example also proves that 56 cannot meet the target but 57 can.”

**“What are the null and alternative?”**

“In the basic model, each next prediction’s conditional chance of error is at most a under the null. The baseline alternative has independent errors with probability p greater than a. We compare the best worst-case chance of detecting that alternative at a preset false-alarm limit.”

The 57 certificate uses the original null/iid alternative or the paper’s truthful count-tail classes, at n = 1000, b = 500, a = 0.1, p = 0.2 and false-alarm level 0.05. An average-risk statement alone does not supply these assumptions.

**“Can you query rejected applicants’ loan outcomes?”**

“This protocol requires answers that already exist and can be retrieved. An outcome for a loan that was never issued is a different problem. An archive with existing but withheld outcomes is the appropriate example here.”

**“What does private mean?”**

“The hiding mechanism cannot see the auditor’s random choices before committing the record. It is a timing and randomness condition, not a differential-privacy claim.”

**“Does no alarm prove the model is safe?”**

“No. It means this test did not reject under its stated assumptions and budget. The result concerns detection power and false alarms, not a universal safety certificate.”

<details>
<summary>If asked about uncertain label quality</summary>

More queries and better knowledge of label quality are distinct resources. Outside the blind region, extra queries can compensate in the specified model; there is no universal substitution. In the blind region, compatible response laws conceal the difference for every fixed query budget in the large-cohort limit. This does not prove impossibility for every finite or growing-budget audit.

The 94-versus-367 comparison concerns numerical limiting budgets under a known 10% symmetric channel versus conditional reliability bounds. The separate 2645 figure is a necessary cohort size for complete truthful labels at alternative error 0.12, not a pending-query budget.

</details>

## Definition references

- [UAI audited setup and theorem](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/6a97650664dffeeaad8f090ee3903c9d72ed6d58/paper/main.tex).
- [AISTATS setup, known/unknown link and finite-sample protocol](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/c13bad9cfd3ef6574e8467e1a4ae87703258f71d/arxiv/source/main.tex).
- [ICLR audit model and theorem conditions](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/1c2535ac92f5e2f0a71ef4022852ef82f206d064/paper/body.tex).
