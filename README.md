# Research Papers

> 2026-10-09 KST: [Seven-paper follow-up review completed](audit/2026-10-08/followup/next-cycle-20261009.md), with UAI statistical corrections and an AISTATS chronology correction. All seven main checkpoints and written file hashes verified. [Linear tracking](audit/2026-10-08/followup/linear-README.md): UAI **YEO-169**, KG **YEO-170**. ICLR/AISTATS/ICAIF remain submitted **on hold**; uploaded-file identity is unverified.

Chorok Lee · Research catalogue · Updated 9 October 2026

논문별 저장소, 기준 원고, 한 페이지 소개와 한·영 1분 스피치를 모았습니다. 금융 논문 세 편의 차이는 아래 비교표에서 확인할 수 있습니다. 아래 7개 항목은 프로젝트/버전 목록이며 독립적인 출판 논문 수를 뜻하지 않습니다.

## Statistical audit and current revisions

**Replacement review packages, 2026-10-09:** [current files, hashes and tracking](audit/2026-10-09/replacement-review-sync.md). UAI proposed v3 (24 pages / 7 source files) and KG proposed v4 (45 pages / 34 source files) are on dedicated review branches. PDFs and ZIPs are attached to YEO-169/170 and were downloaded back with matching SHA-256. No arXiv replacement was performed; the issues remain Todo. The exact commits below take precedence over older root PDFs for this review.

[**2026-10-08 audit: all seven papers**](audit/2026-10-08/README.md). 앞선 감사의 수정과 연구 작업은 각 저장소의 `main`에 통합했습니다. 아래 UAI·KG의 최종 replacement 준비본은 별도 리뷰 브랜치에 보존합니다. 통계적 오류, 재현된 결과, 미확보 증거를 논문별로 구분합니다.

The briefs, speeches and presentation collection below are historical September summaries. They have not been scientifically rewritten after this audit. Consult the audit and the revised artifacts before reusing their claims, particularly the ICAIF performance estimates and UAI inferential explanations. A reported historical number is not a newly reproduced result.

| Project | Current audited artifact | Finding and limit |
| --- | --- | --- |
| **ICLR 2027** | [Revision / version map](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/51ecd493f952b51b58ea2d26b5962cf2c4073f3d/v33/README.md) · [Audit](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/51ecd493f952b51b58ea2d26b5962cf2c4073f3d/audit/2026-10-08/followup-data-and-citations.md) | Raw inputs recovered; fresh model, 10,000 predictions and 48 exact audit probabilities checked. Historical confidence-order mismatch remains explicitly preserved. |
| **AISTATS 2027** | [Revision / version map](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/caa312a59285365e273fd602636017b627d51d22/revision/2026-10-09-chronology/aistats_submission.pdf) · [Audit](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/caa312a59285365e273fd602636017b627d51d22/audit/2026-10-08/followup/README.md) | Protocol timing qualified; all 27 cited primary metadata records and nine full-text versions checked. Numerical results unchanged. |
| **UAI 2026** | [Proposed v3 PDF](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/be2265d46b8c93969f1587f869497e9374409565/submission/replacement-20261009/UAI_2601.00908_v3_proposed.pdf) · [source ZIP](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/be2265d46b8c93969f1587f869497e9374409565/submission/replacement-20261009/UAI_2601.00908_v3_proposed_source.zip) · [changes and review](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/be2265d46b8c93969f1587f869497e9374409565/submission/replacement-20261009/REVIEW.md) | Separate eight-task follow-up does not reproduce the positive association. Original 50-seed evidence remains missing; diagnostic and operational threshold are unvalidated. |
| **KG uncertainty revision** | [Proposed v4 PDF](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/2492ce7828b3226d52eae50fa0eb51134783f366/output/replacement-20261009/KG_2512.22318_v4_proposed.pdf) · [source ZIP](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/2492ce7828b3226d52eae50fa0eb51134783f366/output/replacement-20261009/KG_2512.22318_v4_proposed_source.zip) · [changes and review](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/2492ce7828b3226d52eae50fa0eb51134783f366/output/replacement-20261009/REVIEW.md) | Public v3 already used three graphs. Proposed v4 corrects provenance and labels new work retrospective; original chronology remains unverified. |
| **Factor/crowding revision** | [Revision / version map](https://github.com/ChorokLeeDev/factor-regime-revision/blob/823d6cc42b4ff9f6e1f336e472c77ead75362b2c/output/factor-crowding-reconstructed-evidence-20261008.pdf) · [Audit](https://github.com/ChorokLeeDev/factor-regime-revision/blob/823d6cc42b4ff9f6e1f336e472c77ead75362b2c/audit/2026-10-08/factor-v10-reconstruction.md) | Complete v10 reconstruction: 5,040 fits, 648,000 entries; 166 stable fields and table match exactly. New evidence is distinguished from missing original archive bytes. |
| **Regime predictability revision** | [Revision / version map](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/bfc8c61ca5f31fbb598454d072f6767cb3bd6c62/output/regime-predictability-evidence-recovery-20261008.pdf) · [Audit](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/bfc8c61ca5f31fbb598454d072f6767cb3bd6c62/audit/2026-10-08/regime-evidence-recovery.md) | All 800 raw files restored to original hashes; 400-run reconstruction and independent loss/interval replay pass. Scientific results unchanged. |
| **ICAIF 2026** | [Revision / version map](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/63a03a95f4150b4af38d0eeb625743d83d4bb86a/revisions/2026-10-08/rebuild/research-addendum.md) · [Audit](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/63a03a95f4150b4af38d0eeb625743d83d4bb86a/audit/2026-10-08/recovery-and-rebuild.md) | New chronological reconstruction independently checks 1,830 regressions and 240 cohorts. Held-out AUC/C-index are undefined with 3 and 1 eligible events; original 0.933 is not validated. |

## Historical research communication materials

[**Open the full collection**](materials/README.md) · [Download all files](materials/research_materials_2026-09-29.zip)

각 논문별 **영어 10장 발표 슬라이드(PPTX·PDF), 영어 A0 포스터, 영어·한국어 각각 1쪽 소개서**를 제공합니다. 총 7세트이며, 아래의 기존 1분 스피치·소개서와 별도로 제작했습니다. 원고 기반 내용 검토와 에이전트 간 교차 피드백을 반영한 자료입니다.

The collection records exact manuscript revisions and review changes. Factor Decay follows the original ten-page TeX preprint. [Source versions and review records](materials/README.md#source-versions).

## Historical manuscript and summary index

The tables below preserve the September manuscript packages and status labels used by the historical summaries. Their PDF and ZIP links are pre-audit records; use the current audited-artifact table above for October corrections and revised manuscripts.

### Reliable prediction and statistical evaluation

*예측 신뢰성과 통계적 평가*

| Paper / historical status | Historical manuscript | Historical arXiv source | Historical one-pager |
| --- | --- | --- | --- |
| **ICLR 2027** · [How Many More Labels Are Needed? Minimax Evaluation under Selective Labels](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/tree/main)<br>Submitted to ICLR 2027 · Decision pending (not accepted) | [Historical PDF](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/main/artifacts/iclr2027.pdf) | [Historical ZIP](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/main/artifacts/arxiv-source.zip) | [EN / KO PDF](one-pagers/iclr2027.pdf) |
| **AISTATS 2027** · [When Marginal Shift Magnitudes Cannot Identify Conformal Coverage Loss](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/tree/main)<br>AISTATS 2027 submission 644 | [Historical PDF](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/main/submission/aistats_submission.pdf) | [Historical ZIP](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/main/arxiv/reliance_alignment_arxiv_source.zip) | [EN / KO PDF](one-pagers/aistats2027.pdf) |
| **UAI 2026** · [Diagnosing Conformal Prediction Failures Under Distribution Shift: A COVID-19 Case Study](https://github.com/ChorokLeeDev/conformal-covid-uai2026/tree/main)<br>UAI 2026 camera-ready source | [Historical PDF](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/main/paper/main.pdf) | — | [EN / KO PDF](one-pagers/uai2026.pdf) |

### Knowledge graphs and error diagnosis

*지식 그래프와 오류 진단*

| Paper / historical status | Historical manuscript | Historical arXiv source | Historical one-pager |
| --- | --- | --- | --- |
| **KG uncertainty revision** · [Role Support in Knowledge-Graph Error Ranking: Predictor Regimes and Evaluation Policies](https://github.com/ChorokLeeDev/kg-uncertainty-revision/tree/main)<br>Active revision | [Historical PDF](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/main/output/kg-uncertainty-revised.pdf) | [Historical expanded ZIP — evidence unavailable](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/main/output/kg-uncertainty-arxiv-source.zip) | [EN / KO PDF](one-pagers/kg-uncertainty.pdf) |

### Financial forecasting and model evaluation

*금융 예측과 모델 평가*

| Paper / historical status | Historical manuscript | Historical arXiv source | Historical one-pager |
| --- | --- | --- | --- |
| **Factor/crowding revision** · [Return-Decay Residuals and Tail-Risk Forecasting: Timing Artifacts, Conditional Inference, and Cross-Market Evidence](https://github.com/ChorokLeeDev/factor-regime-revision/tree/main)<br>Active revision | [Historical PDF](https://github.com/ChorokLeeDev/factor-regime-revision/blob/main/output/factor-crowding-revised.pdf) · [arXiv](https://arxiv.org/abs/2512.11913) | [Historical ZIP](https://github.com/ChorokLeeDev/factor-regime-revision/blob/main/output/factor-paper-arxiv-source.zip) | [EN / KO PDF](one-pagers/factor-regime.pdf) |
| **Regime predictability revision** · [Source Exclusion in Regime-Gated Forecasting: A Cross-Market Audit of Equity-Factor Predictability](https://github.com/ChorokLeeDev/regime-predictability-revision/tree/main)<br>Active revision | [Historical PDF](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/main/output/regime-predictability-revised.pdf) · [arXiv](https://arxiv.org/abs/2601.10732) | [Historical ZIP](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/main/output/regime-predictability-arxiv-source.zip) | [EN / KO PDF](one-pagers/regime-predictability.pdf) |
| **ICAIF 2026** · [Predicting Factor Decay: ML Models for Cross-Factor Predictability Erosion](https://github.com/ChorokLeeDev/factor-decay-icaif2026/tree/main)<br>ICAIF 2026 submission 239 · Decision pending | [Historical preprint · 10 pages](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf)<br>[Submission record · 5 pages](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/submission/main_icaif_submission.pdf) | [Historical ZIP](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv_source.zip) | [EN / KO PDF](one-pagers/icaif2026.pdf) |

### How the three finance papers differ

**세 논문의 질문은 각각 “큰 손실의 전조인가?”, “예측에 도움이 되는 정보인가?”, “그 예측관계가 언제 약해지는가?”입니다.**

| Paper | 쉬운 질문과 예시 | Main focus / 핵심 초점 |
| --- | --- | --- |
| **[Return-Decay Residuals](https://arxiv.org/abs/2512.11913)** | 투자전략의 성적 악화가 다음 달 큰 손실의 전조일까?<br>예: 모멘텀 전략의 성적이 예상보다 나빠졌을 때 이후 손실 위험도 커지는가? | **Tail-risk warnings · 손실 위험**<br>전략 자체의 성적에서 만든 지표가 미래 위험을 예측하는지, 같은 시점의 정보가 겹쳐 생긴 연관성인지 점검합니다. |
| **[Source Exclusion](https://arxiv.org/abs/2601.10732)** | A의 정보를 알면 B를 더 잘 예측할 수 있을까?<br>예: 가치주 움직임을 알면 소형주 수익률 예측이 나아지는가? | **Value of source information · 정보의 예측 기여**<br>A를 예측식뿐 아니라 시장 국면 추정과 학습 과정에서도 완전히 빼고 비교하는 방법을 연구합니다. |
| **[Predicting Factor Decay](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf)** | 관측된 A→B 예측관계는 얼마나 오래 유지될까?<br>예: 과거에 유용했던 가치주→소형주 관계가 언제 약해지는가? | **Durability of predictive relationships · 예측관계의 지속기간**<br>관계가 약해지는 시점과 위험을 생존 분석·머신러닝으로 예측할 수 있는지 탐색합니다. |

The distinction is **future loss risk**, **the predictive contribution of a source**, and **the durability of a predictive relationship**. The last two papers share research history but ask different questions.

여기서 팩터는 가치주·소형주·모멘텀처럼 공통된 투자 특성을 묶은 수익률을 뜻합니다. 첫 논문은 개별 전략의 성적과 손실 위험을, 나머지 두 논문은 팩터 사이의 예측관계를 다룹니다. 관계의 지속기간을 해석하려면 정보의 기여부터 제대로 측정해야 하므로 Source Exclusion의 검증 문제는 Factor Decay에도 중요합니다. 다만 특정 모델의 표본 외 실패만으로 실제 예측정보가 사라졌다고 단정할 수는 없습니다.

**Evidence limits:** the two audit papers do not establish a robust general forecasting advantage. The historical Factor Decay manuscript reported seven decay events; its original 0.933 discrimination claim remains unvalidated. The separate chronological reconstruction has only 3 and 1 eligible held-out pairs, all events, so its AUC/C-index are undefined. The comparison above describes research questions, not proven trading benefits.

### Version notes

- **ICLR:** the current repository is `selective-labels-minimax-iclr2027`; manuscript and source links use its cleaned `artifacts/` and `paper/` layout.
- **Historical Factor Decay preprint:** the September [PDF](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf) and [arXiv source ZIP](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv_source.zip), prepared on 29 September 2026, use the **ten-page original TeX edition**, with six figures and 21 references. This replaces the earlier reconstructed upload package. The abstract and research text are preserved from the original TeX; author details and the publication wrapper were updated, and the missing figure was recovered from the original reference PDF. [Editable source](https://github.com/ChorokLeeDev/factor-decay-icaif2026/tree/main/arxiv/original-source-20260929) · [Provenance](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/PROVENANCE.md). Package preparation does not establish arXiv publication or newly validate the experiments.
- **ICAIF submission record:** the separate five-page submitted PDF remains authoritative for that submission. The existing ICAIF one-pager and one-minute introduction below describe that five-page version; they are not new summaries of the ten-page preprint. The exact submitted LaTeX source was not located.
- **Research lineage:** ICAIF and the regime-predictability revision share earlier research history. Their current claims and versions are tracked separately; later revision findings are not retroactively attributed to the ICAIF submission.
- **Maintained branches:** the audited projects are integrated on `main`. September summaries retain their exact historical source commits in [papers.json](papers.json); the October audit separately records reviewed versions and limitations. Live branch links may advance after either date.
- **Status:** venue labels identify the tracked version. Only explicitly stated decisions should be read as conference outcomes. Repository preparation does not upload or alter a conference submission.

## Historical one-minute research introductions

These September scripts and their manuscript links predate the statistical audit; they are retained as historical communication records. Consult the current audited artifacts above before reusing their claims.

English scripts contain approximately 130 words each. English and Korean versions are intended as natural spoken introductions; timing varies with speaking pace. The linked one-pagers give the question, method, findings, limits and source version.

### ICLR 2027: How Many More Labels Are Needed? Minimax Evaluation under Selective Labels

[Repository](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/selective-labels-minimax-iclr2027/blob/main/artifacts/iclr2027.pdf) · [Historical one-pager](one-pagers/iclr2027.pdf)

**English · about one minute**

Suppose a model looks accurate, but the difficult cases are exactly the ones whose labels have not arrived. How many extra labels would let us detect a real increase in risk? This paper treats that question as an audit design problem. We freeze the prediction cohort, allow the original labels to be selectively missing, and characterize the best achievable detection power under a fixed query budget. We then show why noisy audit labels change the answer: two apparently similar reliability guarantees can create different statistical experiments. The practical message is that query count is only one resource. Label reliability and cohort size can each become the bottleneck. Our numerical examples translate the theory into concrete budgets, while keeping the assumptions explicit. A failed alarm is not a certificate of safety.

**한국어 · 약 1분**

모델의 관측 정확도는 좋아 보이는데, 정작 어려운 사례의 라벨만 아직 도착하지 않았다면 어떻게 평가해야 할까요? 이 논문은 위험 증가를 발견하려면 라벨을 몇 개나 더 확인해야 하는지 묻습니다. 예측이 끝난 평가 집단을 고정하고, 기존 라벨의 누락이 결과와 연관될 수 있는 상황에서 정해진 질의 예산으로 달성할 수 있는 최적 검정력을 분석합니다. 추가로 얻는 라벨에도 오류가 있다면, 비슷해 보이는 신뢰도 조건이 서로 다른 검정 문제를 만든다는 점도 보입니다. 핵심은 라벨 개수만 늘린다고 해결되지 않는다는 것입니다. 라벨 품질에 대한 지식과 평가 집단의 크기도 각각 한계가 될 수 있습니다. 수치 예시는 이러한 가정 아래 필요한 예산을 구체화합니다. 경보가 울리지 않았다는 사실 자체가 모델이 안전하다는 보장은 아닙니다.

### AISTATS 2027: When Marginal Shift Magnitudes Cannot Identify Conformal Coverage Loss

[Repository](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/conformal-coverage-identification-aistats2027/blob/main/submission/aistats_submission.pdf) · [Historical one-pager](one-pagers/aistats2027.pdf)

**English · about one minute**

A distribution-shift alarm tells us that deployment data have changed. But does it tell us how often a conformal prediction set still contains the correct answer? This paper shows why those are different questions. Even equal shift magnitudes can correspond to very different coverage, and an unchanged confidence distribution can hide changes in error. We first identify what is recoverable when the label law is known. We then weaken that information and derive sharp upper and lower coverage bounds using source calibration, target confidence frequencies, and a density-ratio constraint. We also give a finite-sample version for a prespecified threshold grid. The central message is to match the conclusion to the information available: sometimes coverage is identifiable, sometimes only bounded, and sometimes a drift statistic simply cannot answer the coverage question.

**한국어 · 약 1분**

배포 데이터의 분포가 바뀌었다는 경보가 울리면, 예측 집합이 정답을 포함하는 비율도 얼마나 떨어졌는지 알 수 있을까요? 이 논문은 두 질문이 서로 다르다는 데서 출발합니다. 분포 변화의 크기가 같아도 포함률은 크게 다를 수 있고, 모델 신뢰도의 분포가 그대로여도 오류 구조는 바뀔 수 있습니다. 먼저 라벨 생성 법칙을 아는 경우 무엇을 정확히 복원할 수 있는지 밝힙니다. 다음으로 그 가정을 약하게 바꾸고, 원본 데이터의 신뢰도 보정, 배포 데이터의 신뢰도 빈도, 밀도비 제한만으로 가능한 포함률의 상한과 하한을 구합니다. 유한한 표본에서 미리 정한 임계값들에 적용하는 방법도 제시합니다. 핵심은 가진 정보에 맞는 결론을 내리는 것입니다. 정확히 식별할 수 있는 경우, 범위만 제시할 수 있는 경우, 분포 변화 통계만으로는 답할 수 없는 경우를 구분합니다.

### UAI 2026: Diagnosing Conformal Prediction Failures Under Distribution Shift: A COVID-19 Case Study

[Repository](https://github.com/ChorokLeeDev/conformal-covid-uai2026/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/main/paper/main.pdf) · [Historical one-pager](one-pagers/uai2026.pdf)

**English · about one minute**

Why can the same distribution shift barely affect one prediction task and seriously damage another? This paper studies that question through the COVID-19 disruption and conformal prediction. The central idea is that vulnerability depends on how the model uses its features, not just on how much the input distribution changes. We measure SHAP concentration: how much feature importance is carried by the most influential feature. For gradient-boosted classifiers, concentrated dependence is associated with larger coverage losses across the studied tasks. A theoretical analysis explains one route through which this can happen under explicit assumptions, while external datasets test how far the diagnostic transfers. This is a warning indicator, not a universal safety certificate. Its usefulness depends on the model and shift mechanism, and proposed thresholds still need prospective validation.

**한국어 · 약 1분**

같은 분포 변화를 겪어도 어떤 예측 과제는 거의 영향을 받지 않고, 어떤 과제는 정답 포함률이 크게 떨어지는 이유가 무엇일까요? 이 논문은 코로나19 시기의 변화와 컨포멀 예측을 통해 이 질문을 살펴봅니다. 핵심 아이디어는 입력 분포의 변화량뿐 아니라 모델이 특징을 사용하는 방식도 취약성을 결정한다는 것입니다. 가장 중요한 특징 하나가 전체 SHAP 중요도에서 차지하는 비율을 집중도로 측정합니다. 연구한 그래디언트 부스팅 분류기에서는 이 의존이 집중될수록 포함률 손실이 큰 경향을 보였습니다. 이론 분석은 명시적인 가정 아래 가능한 작동 경로를 설명하고, 외부 데이터 실험은 진단이 어디까지 옮겨가는지 확인합니다. 이것은 보편적인 안전성 인증이 아니라 사전 경고 지표입니다. 모델과 변화의 종류에 따라 유용성이 달라지며, 제안한 기준값은 향후 검증이 필요합니다.

### KG uncertainty revision: Role Support in Knowledge-Graph Error Ranking: Predictor Regimes and Evaluation Policies

[Repository](https://github.com/ChorokLeeDev/kg-uncertainty-revision/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/main/output/kg-uncertainty-revised.pdf) · [Historical one-pager](one-pagers/kg-uncertainty.pdf)

**English · about one minute**

In a knowledge graph, an entity may have little or no observed support for a particular relation role. Should we automatically treat its prediction as unreliable? This revision shows why the answer depends on the predictor. A simple missing-support score can rank errors in one regime and reverse direction as prediction quality changes. Rather than proposing a new intrinsic uncertainty measure, we test what role counts add beyond confidence, frequency, and ensemble disagreement. Continuous counts help fitted error ranking and probability scoring in the reported ensemble comparisons, but binary missingness adds no information beyond those counts. Evaluation policy matters too: changing candidate sets or coverage thresholds can change the apparent benefit. The main contribution is a disciplined diagnosis of when support helps, with claims limited to observed graph targets rather than factual truth.

**한국어 · 약 1분**

지식 그래프에서 어떤 개체가 특정 관계의 역할로 거의 관측되지 않았다면, 그 예측은 자동으로 불확실하다고 봐야 할까요? 이 개정 논문은 답이 예측기에 따라 달라진다는 점을 보여줍니다. 관측 이력이 없다는 단순한 점수는 한 학습 상태에서는 오류를 잘 가리키지만, 예측 성능이 달라지면 방향이 뒤집힐 수 있습니다. 그래서 새로운 고유의 불확실성 척도를 주장하기보다, 역할별 횟수가 신뢰도, 빈도, 앙상블 불일치에 더해 어떤 정보를 주는지 평가합니다. 보고된 비교에서는 연속적인 횟수가 오류 순위와 확률 점수의 적합에 도움이 됩니다. 다만 관측 유무를 나타내는 이진 변수는 횟수에 없는 새 정보를 만들지 않습니다. 후보 집합과 포함 비율 같은 평가 정책도 결과를 바꿉니다. 핵심은 역할 정보가 도움이 되는 조건을 분명히 하는 것이며, 기록된 정답에 대한 오류와 사실 자체의 확실성을 구분하는 것입니다.

### Factor/crowding revision: Return-Decay Residuals and Tail-Risk Forecasting: Timing Artifacts, Conditional Inference, and Cross-Market Evidence

[Repository](https://github.com/ChorokLeeDev/factor-regime-revision/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/factor-regime-revision/blob/main/output/factor-crowding-revised.pdf) · [Historical one-pager](one-pagers/factor-regime.pdf)

**English · about one minute**

A financial indicator can look predictive for reasons that have little to do with forecasting the future. This revision examines a return-decay residual and asks three separate questions: what information it contains, when that information becomes available, and how the forecasting model is selected. We show that overlapping same-month quantities can generate an impressive risk association even without future predictability. We also show that replacing an existing component with its residual may preserve the information while changing the regularization geometry and fitted predictions. Cross-market evaluations therefore compare explicit baselines, timing rules, histories, and tuning procedures. The evidence does not establish a robust general forecasting advantage, but uncertainty remains too wide to prove universal failure. The contribution is a clearer framework for deciding what an apparent financial signal actually demonstrates.

**한국어 · 약 1분**

금융 지표가 예측력이 있어 보인다고 해서 반드시 미래에 관한 정보를 담고 있는 것은 아닙니다. 이 개정 논문은 수익률 감쇠 잔차를 대상으로 세 가지를 나눠 묻습니다. 어떤 정보가 들어 있는지, 그 정보가 언제 이용 가능한지, 예측 모델을 어떻게 선택했는지입니다. 같은 달의 변수들이 겹치기만 해도 미래 예측력 없이 강한 위험 연관성이 나타날 수 있음을 보입니다. 또 기존 변수를 잔차로 바꾸는 변환은 정보를 추가하지 않으면서도 정규화의 형태를 바꿔 적합 결과를 달라지게 할 수 있습니다. 따라서 여러 시장의 평가에서는 비교 기준, 시간 순서, 학습 이력, 조정 절차를 명시합니다. 현재 결과가 전반적으로 안정적인 예측 개선을 입증하지는 않지만, 불확실성이 남아 있어 언제나 무효라고 결론 내릴 수도 없습니다. 핵심 기여는 관측된 금융 신호가 실제로 무엇을 보여주는지 구분하는 평가 틀입니다.

### Regime predictability revision: Source Exclusion in Regime-Gated Forecasting: A Cross-Market Audit of Equity-Factor Predictability

[Repository](https://github.com/ChorokLeeDev/regime-predictability-revision/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/regime-predictability-revision/blob/main/output/regime-predictability-revised.pdf) · [Historical one-pager](one-pagers/regime-predictability.pdf)

**English · about one minute**

If we remove a variable from a forecasting model, have we really removed its information? In a regime-gated model, the answer can be no. The variable may disappear from the forecast equation while still influencing the estimated market regime. This revision distinguishes removing explicit lags from excluding the source throughout fitting, filtering, and tuning. Those interventions answer different questions and can even change the sign of a comparison. We audit equity-factor forecasts across markets, replay uncertainty calculations with independent implementations, and use simulations to separate information in an ideal predictor from the performance of a fitted HMM. The empirical results do not establish a general predictive advantage. More importantly, failure of a particular fitted pipeline is not proof of noncausality. The contribution is to define source exclusion precisely before interpreting the evidence.

**한국어 · 약 1분**

예측 모델에서 변수를 하나 뺐다면, 그 변수의 정보도 정말 사라졌을까요? 국면별 예측 모델에서는 그렇지 않을 수 있습니다. 예측식에서 빠진 변수가 시장 국면을 추정하는 단계에는 여전히 영향을 줄 수 있기 때문입니다. 이 개정 논문은 명시적인 시차 변수만 제거하는 방법과 학습, 필터링, 조정 전 과정에서 해당 정보를 제외하는 방법을 구분합니다. 두 방법은 서로 다른 질문에 답하며 비교 결과의 부호까지 바꿀 수 있습니다. 여러 시장의 주식 요인 예측을 점검하고, 독립적인 구현으로 불확실성 계산을 재현하며, 시뮬레이션으로 이상적인 예측기에 존재하는 정보와 실제 적합된 HMM의 성능을 구분합니다. 실증 결과가 일반적인 예측 우위를 입증하지는 않습니다. 또한 특정 모델이 실패했다고 해서 구조적인 비인과성이 증명되는 것도 아닙니다. 핵심은 결과를 해석하기 전에 무엇을 어떻게 제거했는지 정확히 정의하는 것입니다.

### ICAIF 2026: Predicting Factor Decay: ML Models for Cross-Factor Predictability Erosion

[Repository](https://github.com/ChorokLeeDev/factor-decay-icaif2026/tree/main) · [Historical paper PDF](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/submission/main_icaif_submission.pdf) · [Historical one-pager](one-pagers/icaif2026.pdf)

**English · about one minute**

A factor relationship may work for years and then stop being useful. Can we forecast that erosion before relying on the signal becomes risky? This submitted paper combines regime-specific diagnostics, a survival-style decay model, and online regime classification to study that question. Initial signal strength is the leading reported predictor of subsequent erosion. The submitted results include a high cross-validated concordance index, but it is based on only seven decay events. The fast regime detector also has a clear accuracy tradeoff. Most importantly, the primary US relationship does not replicate in the post-break out-of-sample period. I therefore present this as exploratory evidence for monitoring signal durability, not as a profitable trading strategy or a confirmed causal mechanism. The ICAIF decision is still pending, and this summary follows the actual five-page submission.

**한국어 · 약 1분**

여러 해 동안 유용했던 금융 요인 간 관계가 어느 순간 예측력을 잃을 수 있습니다. 그렇다면 그 신호에 의존하는 것이 위험해지기 전에 약화를 예측할 수 있을까요? 이 제출 논문은 국면별 진단, 생존 분석 형태의 감쇠 모델, 온라인 국면 분류를 결합해 이 질문을 탐구합니다. 보고된 결과에서는 초기 신호의 강도가 이후 약화의 주요 예측 변수입니다. 교차 검증의 C-index는 높지만, 감쇠 사건이 일곱 개뿐이라는 점을 함께 봐야 합니다. 빠른 국면 탐지도 정확도와의 절충이 있습니다. 특히 핵심 미국 요인 관계는 구조 변화 이후의 표본 외 기간에서 재현되지 않았습니다. 따라서 수익성 있는 매매 전략이나 확인된 인과 기제로 제시하기보다, 신호가 얼마나 오래 유지되는지 모니터링하기 위한 탐색적 연구로 설명합니다. ICAIF 결과는 아직 나오지 않았으며, 이 소개는 실제 다섯 페이지 제출본을 기준으로 합니다.

## Maintenance

- Edit `papers.json` for links, statuses, source identities and current audit records; `briefs.json` retains the dated September summaries and speeches.
- Rebuild only this README with `python tools/build_briefs.py --readme-only`, or include the PDFs with `python tools/build_briefs.py`. The finance comparison and version notes are maintained in the README builder. See [one-pager build notes](one-pagers/README.md) for fonts and dependencies.
- Update the source commit and review the scientific claims whenever a summary changes. Preserve submitted artifacts and distinguish reported results from newly reproduced evidence.
