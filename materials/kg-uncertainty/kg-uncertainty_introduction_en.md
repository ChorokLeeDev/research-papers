# Role Support in Knowledge-Graph Error Ranking: Predictor Regimes and Evaluation Policies

Chorok Lee | KAIST

A knowledge graph may never have seen an entity in a particular relation role. Does that make a new prediction unreliable? This paper shows why the answer depends on the predictor and the decision being evaluated, while identifying settings where learning from role counts remains useful.

## The question

Knowledge-graph completion predicts a missing entity in a triple. An error ranker then orders predictions for acceptance or review. The study asks whether relation-specific training support improves that ranking beyond confidence, frequency, and ensemble disagreement. Its outcome is recovery of recorded held-out answers: an unrecorded true fact can count as an error, so the experiment does not measure factual falsehood.

## The approach

Head-role and tail-role counts measure how often the relevant entity appeared in that relation role in training. Missing-role bits indicate a zero count. Features are evaluated at the predicted tail, without using hidden answers. The experiments cover 12 from-scratch DistMult/ComplEx predictors, six continued-training stages, and six fixed three-member ensembles on FB15k-237 and WN18RR. Logistic and nonlinear error heads compare nested feature sets on fixed predictions; candidate and acceptance policies are tested separately.

## The main result

On FB15k-237, a continued ComplEx regime raises mean recorded-target accuracy from 10.05% to 44.35%. Yet the raw positive missing-role penalty reverses its error-ranking direction: mean AUROC falls from 0.6893 to 0.3639. This comparison changes multiple training choices and predicted answers; it does not isolate accuracy as the cause. Learned counts still help. Adding continuous role counts beyond confidence, frequency, and explicit disagreement improves AURC (error across answer rates) and Brier (error-probability scoring) in all 12 fixed-ensemble/error-head comparisons. Gains do not imply lower selective risk at every answer rate.

## Why the evaluation policy matters

A missing-role bit is a deterministic function of its count, so it adds no conditional information; it can still change how a restricted scorer fits. At an 85% batch answer rate, count-based logistic models reach the hindsight error floor in all original runs but none of the continued-training runs. Candidate restrictions also have mixed effects: training-supported tails improve DistMult accuracy on FB15k-237 but reduce it on WN18RR, where 27.67% of queries lose every recorded target. Development-fixed thresholds produce unequal test answer rates, changing the tradeoff being compared.

## What this contributes

The contribution is an inspectable evaluation of when established support features help and when their interpretation fails. It does not establish a new uncertainty decomposition or calibrated factual truth. The two static graphs were repeatedly inspected; optimizer seeds and warm starts are not independent graph replications. New graphs, temporal transfer, more complete answer labels, and reproduction of historical results remain open.

## KEY TAKEAWAY

Treat role support as a predictor-dependent feature. Judge it against strong comparators under the exact candidate, error, and acceptance policy that matters.

Source: https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/208f21270f44cb5fe1e26a8b0e0b9dbab88f4a18/manuscript.tex
