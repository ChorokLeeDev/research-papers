# How Many More Labels Are Needed? Minimax Evaluation under Selective Labels

Chorok Lee | KAIST

A model can look accurate because its difficult cases remain unlabeled. If an evaluator pays for more labels, how many are enough to detect an important risk increase? This paper turns that question into a worst-case audit-design problem.

## Question

Consider a frozen model and a fixed cohort whose outcomes already exist but are only partly visible. The process withholding labels may know every outcome, so the observed cases can be selectively easy. The evaluator privately queries some pending cases and tests whether an acceptable-risk claim has been violated. Power means the probability of detecting a specified higher-risk alternative; false-alarm control limits rejection under the acceptable-risk class. The target is a risk-generating law, not simply the realized cohort error fraction.

## Approach

The paper derives the exact limiting worst-case power for each fixed query budget, allowing the benchmark auditor to use the full record and adapt its queries. A uniform, nonadaptive truthful audit attains that frontier. The comparison distinguishes the number of requested labels from the information supplied about their reliability. It also compares count-tail guarantees, cumulative predictable-risk budgets, and mean-risk bounds; these assumptions support different conclusions even when the visible protocol is unchanged.

## Main evidence

Under truthful labels and count-tail risk bounds, a finite certificate shows that exactly 57 queries are necessary and sufficient for 95% worst-case power with 1,000 predictions, 500 pending labels, acceptable risk 10%, alternative risk 20%, and false alarms at most 5%. Every 56-query adaptive policy falls short, while a supplied 57-query rule exceeds the target. Separately, numerical asymptotic calculations at the same risks and missing fraction require 94 queries with a known 10% symmetric noise channel, compared with 367 when only conditional reliability bounds are known. Those are limiting budgets, not finite-cohort certificates.

## Why the scope matters

The 57-query rule is tuned to 20% risk: its power falls to 1.15% at 12%. A private mixture partly repairs this to 8.66% while preserving 95% power at 20%. Even complete labels for 1,000 predictions yield only 65.32% optimal power for 10% versus 12% risk; at least 2,645 complete-label predictions are needed to reach 95%. Mean risk alone can impose a low power ceiling even with all outcomes visible. More labels cannot replace a sufficient cohort or a defensible risk guarantee.

## Practical meaning

Before auditing, specify the risk claim, meaningful alternative, cohort, pending-count bound, and label-reliability assumptions. Use a matching finite certificate when available and inspect performance away from the planning alternative. The analysis assumes committed selection, private sampling, accessible existing outcomes, and one deadline. It provides mathematical design evidence, not deployment validation. Failure to reject does not certify acceptable risk.

## KEY TAKEAWAY

Audit power depends on three separate resources: how many labels are acquired, what is known about their quality, and how many predictions are available.

Source: https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/38b792da07a174980303e6cb9272e5f5e3bd9bac/paper/body.tex
