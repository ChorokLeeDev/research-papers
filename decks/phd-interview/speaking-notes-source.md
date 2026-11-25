지금까지 나눈 모든 피드백(1. 왜 Coverage를 쓰는지 그 존재 이유 명확화, 2. Slide 3의 흐름 개선, 3. Slide 4의 자연스러운 구어체 전환, 4. Slide 5의 SHAP/Coverage 직관화 및 Slide 6 브리지, 5. Slide 6의 전문 용어 완화, 6. Slide 9–10 타이밍 균형)을 모두 반영해 업데이트한 **전체 발표 스크립트 최종본**입니다.

예상 러닝타임은 약 13분 55초 (약 1,720단어)로 기존과 거의 동일하며, 10번 슬라이드의 시간 압박을 해소하기 위해 9번에서 15초를 옮겨 배분했습니다.

---

# Chorok Lee · Cologne TAIL · 14-minute self-presentation — timed English script (Updated)

Planned runtime: **14:00**. 12 main slides. Read-aloud text: ~1,720 words.

| Slide | Time window | Duration |
| --- | --- | --- |
| 1. What can our evidence tell us about predictive reliability? | 00:00–00:40 | 40s |
| 2. From economics to reliable ML systems | 00:40–01:50 | 70s |
| 3. A shift alarm is different from a coverage claim | 01:50–02:55 | 65s |
| 4. Three projects, one question about evidence | 02:55–03:40 | 45s |
| 5. UAI: model reliance helps explain vulnerability | 03:40–05:10 | 90s |
| 6. Thesis I: equal shift magnitudes, different coverage | 05:10–07:00 | 110s |
| 7. Thesis II: an honest answer can be a range | 07:00–08:50 | 110s |
| 8. ICLR: what can an additional label audit establish? | 08:50–10:25 | 95s |
| 9. How I work: from a failure to a precise question | 10:25–11:10 | 45s |
| 10. Why TAIL: from identification to guarantee design | 11:10–12:35 | 85s |
| 11. What coverage remains when validity only partially holds? | 12:35–13:30 | 55s |
| 12. Build reliability claims from the evidence we have | 13:30–14:00 | 30s |

---

## 1. What can our evidence tell us about predictive reliability? · 00:00–00:40

Thank you for the opportunity to speak with you. I am Chorok Lee, a master's student in Software Engineering at KAIST. My research asks what the information available to a model evaluator can actually establish about predictive reliability. I will briefly introduce my background, then explain how a study of conformal coverage failures led to my thesis on identification and related work on selective labels. I will finish with the direction I would like to develop at TAIL.

## 2. From economics to reliable ML systems · 00:40–01:50

My undergraduate degree is in Economics from Yonsei University's Underwood International College, and I spent an exchange year at Dartmouth. I then worked as a software engineer before starting my master's at KAIST in February 2025, supervised by Professor Insik Shin. I expect to complete the degree in February 2027. My graduate preparation includes probability and statistics, stochastic calculus, Bayesian machine learning, and deep learning.

In parallel, I have worked at SAP Labs Korea as a software engineering intern. My projects have included retrieval evaluation, agent workflows, and tools for accessing cloud telemetry. Before SAP, I built data pipelines and GraphRAG components at a legal AI startup. These experiences make implementation and measurement a natural part of my research. For a PhD, I want to develop the statistical foundations behind those measurements: when a seemingly reassuring evaluation is informative, and when it cannot answer the question we care about.

## 3. A shift alarm is different from a coverage claim · 01:50–02:55

In high-stakes decisions, a single prediction is not enough—we want a prediction set that comes with a formal safety promise. Conformal prediction provides this through **coverage**: the probability that the true label actually falls inside the predicted set. Under standard exchangeability assumptions, this guarantee holds on average across test points.

After deployment, however, two things change. Input distributions shift, and the true labels needed to verify that safety promise are often missing or selective. Because we can still observe features and model scores, it is tempting to rely on a drift alarm or a stable confidence histogram as a proxy for coverage. **But those signals measure the wrong thing.** A shift metric tells us how inputs changed, whereas coverage depends on how inputs and scores relate to true outcomes. My work asks which parts of that relationship survive in the summaries we observe—and what conclusions remain justified when they do not.

## 4. Three projects, one question about evidence · 02:55–03:40

There are three stages in this research trajectory. My published UAI 2026 paper studies a diagnostic: whether feature-importance concentration helps anticipate coverage vulnerability in gradient-boosted classifiers. My master's thesis, submitted to AISTATS 2027, asks an identification question: **what can shift and confidence summaries actually tell us about coverage?** My related ICLR 2027 submission asks an intervention question: **how much can a limited label audit reveal about model risk when labels are selective and noisy?** The latter two papers are under review. Together, they move from observing failures to understanding information limits, and then to acquiring information that can resolve them.

## 5. UAI: model reliance helps explain vulnerability · 03:40–05:10

The empirical starting point was a COVID-19 supply-chain case study. Several classification tasks experienced the same temporal disruption, but their conformal coverage deteriorated very differently. Standard shift indicators detected the disruption without explaining that variation in failure severity.

I studied feature-importance concentration: **how much of a model's decision relies on its single most influential feature**, measured using SHAP attribution scores. Across sixteen multiclass tasks in nine domains, gradient-boosted models that leaned heavily on one feature suffered much steeper drops in **coverage—meaning their prediction sets failed to include the true label far more often.** I also derived a theoretical bound showing how a shift in that top feature directly lowers this reliability rate in an idealized model.

The diagram illustrates the mechanism rather than plotting experimental measurements. If a model relies heavily on a feature hit by the shift, the same external disruption can hurt it far more. **However, this diagnostic is still exploratory and tied to tree-based models—it cannot explain the broader sensitivity failures we see in neural networks.** That limitation raised a deeper question: is our diagnostic simply imperfect, or **do standard shift summaries discard the information needed to identify coverage in the first place?**

## 6. Thesis I: equal shift magnitudes, different coverage · 05:10–07:00

To see if standard shift metrics miss critical information, I first study a simple classification setup where we know how the model's confidence translates into actual accuracy. Imagine comparing two distribution shifts that move the data by the exact same distance, but in different directions: one moves along the direction the model uses to make decisions, and the other moves sideways along irrelevant features. Standard distance metrics give the exact same number for both because they ignore direction—yet the first shift breaks our coverage guarantee while the second leaves it untouched. On the bright side, as long as the model's confidence still reflects true accuracy, looking at how confident the model is overall—the distribution of its absolute scores—is enough to predict the exact coverage.

## 7. Thesis II: an honest answer can be a range · 07:00–08:50

Next, I remove that ideal assumption—in real deployments, we no longer know the exact formula linking confidence scores to true accuracy, and we cannot see the test labels. Here, miscoverage is simply $1 - \text{coverage}$—the probability that our prediction set misses the true label. Because a confidence score compresses many features into a single number, different inputs with very different true miscoverage rates can land on the exact same score—so two test sets can look identical in their scores while having completely different coverage. Instead of guessing a single number, I calculate the exact best-case and worst-case coverage consistent with our data—and these bounds are sharp, meaning both extremes can actually happen in reality. This uncertainty disappears only when inputs with the same confidence score truly share the exact same miscoverage probability. Focusing on coverage matters because it directly tells us whether our safety guarantee still holds after deployment—and knowing the sharp worst-case bound lets us catch silent reliability failures before we trust a false sense of certainty.

## 8. ICLR: what can an additional label audit establish? · 08:50–10:25

My related ICLR paper takes the next step: asking for missing answers. Think of a loan model that only sees outcomes for people it approved—because rejected applicants never get a loan, we never see whether they would have paid it back, making a risky model look deceptively safe. With a fixed budget to audit only a few hidden outcomes, intuition says to inspect risky groups—but how many queries should go to each group when we don't know what worst-case risk is hiding behind the missing labels? I solve this by finding the exact optimal budget split that maximizes our chance of catching an unsafe model against any worst-case scenario, while keeping false alarms strictly below a preset limit. I also prove that no adaptive auditing strategy can beat this detection limit with the same budget. For my research, this turns ad-hoc data collection into a rigorous blueprint for deciding exactly how many missing labels we need to certify safety.

## 9. How I work: from a failure to a precise question · 10:25–11:10

The way I contribute to a research group is by connecting empirical failure patterns to precise statistical models, and then building checks that test those models' limits. In the UAI project, I started from an observed failure pattern; in my thesis, I turned that into counterexamples, a sufficient statistic, and sharp bounds, validated through simulations and controlled replay on UCI datasets.

My engineering background helps me build reproducible pipelines and keep experimental assumptions separate from deployment claims. What I want to strengthen during a PhD is deeper theoretical formulation through close collaboration—especially in robust conformal procedures and the design of useful uncertainty sets.
