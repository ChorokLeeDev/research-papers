# Account-wide evidence recovery and verified revisions

> Latest replacement review files: [2026-10-09 synchronization record](../../2026-10-09/replacement-review-sync.md). UAI proposed v3 and KG proposed v4 remain unsubmitted.

The user requested continued work on every unresolved item, including a search of every repository in the same account. This follow-up covers the original seven catalogue projects and traces their evidence across all **31 account-owned repositories**, including 14 private repositories, three forks and two empty repositories. It is not a scientific audit of every unrelated project in the account.

Authenticated enumeration, complete non-shallow Git histories, **40,116 per-repository historical paths**, all repository release/Actions listings, and relevant archived sources were inspected. The sole available release restored a **33-part, 2,185,804,556-byte** archive with **6,488 members**, verified against its recorded whole-file SHA-256. Private raw payload remains in the private/local recovery checkout. [Search receipt](account-recovery-scope.json).

The final recovery-surface check also queried advertised PR heads across all 31 repositories: all **11 heads** were already in the inspected histories, adding no new commits or files. One archived embedded-repository pointer has no recorded remote; its target was absent from all 31 local object databases and unavailable through authenticated commit queries across all 31 repositories (with a known-commit positive control). Its tree and origin remain unauthenticated; this does not show the object never existed or exclude copies outside the requested account. No additional original experiment evidence was recovered.

## Tracking update — 2026-10-09 KST

The two arXiv correction tasks were **created in Linear and fetched again for verification**: [UAI YEO-169](https://linear.app/yeondu/issue/YEO-169) and [KG YEO-170](https://linear.app/yeondu/issue/YEO-170). Both remain Todo; this is task registration, not an arXiv replacement submission. Evidence commits and exact issue URLs are recorded in [the sync receipt](linear-sync-20261009.json).

The user supplied an arXiv account dashboard identifying three **new submissions on hold**: ICLR `submit/8134764`, AISTATS `submit/8147722`, and standalone ICAIF Factor Decay `submit/8147946`. This supersedes the previous failure to identify these submissions. These are internal submission IDs, not public arXiv article IDs. The submitted files have not been compared with current GitHub revisions. In particular, standalone ICAIF is not regime paper `2601.10732`.

The official public pages still list UAI v2 and KG v3 when checked in this session. The dashboard reports the three-active-submission block. [Official policy](https://info.arxiv.org/help/moderation/index.html#submission-rate) distinguishes two new submissions per month from replacement rate rules; it does not clearly settle whether a pending replacement is blocked by the active cap. [On-hold guidance](https://info.arxiv.org/help/submit_status.html) says to await instructions and avoid duplicate/delete-and-resubmit actions. No account action was performed.

The [next bounded seven-paper review is complete](next-cycle-20261009.md). Historical verification counts below describe the previous cycle; the new report separates actual reruns, corrections and remaining limits.

## Current outcomes

| Project | Executed work and corrected interpretation |
|---|---|
| ICLR | Exact original image/annotation inputs recovered; fixed-model training rerun. Independent raw-image inference checks all 50,000 feature rows and 10,000 predictions/current ranks; 48 exact rational audit probabilities match. Historical confidence-order hashes still differ, so the old strict replay failure is preserved. A new complete model/prediction/rank snapshot is independently checkable. 26 of 27 bibliography records corroborated; some publisher full texts remain inaccessible. |
| AISTATS | Unsupported before-outcome protocol assurance removed after history inspection; all 27 citation metadata records verified and nine primary full-text versions inspected. Version-sensitive Han–Qu citation explicitly pins v1. Proofs/code/results unchanged; new 18/19-page bundles independently compiled. |
| UAI | Complete eight-task follow-up recovered and 24 fixed-protocol models refitted; 528 arrays exactly reproduce. Both APS definitions give negative sample task associations, not the historical positive association. Raw data demonstrate total target-ID loss under the historical date-truncated join on the recovered snapshot. Unsupported hyperparameter, causal and operational claims are withdrawn. Original 50-seed ledgers remain unavailable; the follow-up does not identify their cause. |
| KG | Public v3 source is the expanded three-graph study. Earlier CoDEx exposure undermines an untouched-dataset interpretation. New fixed-protocol CoDEx, relation-ID and grouped analyses are retained and independently replayed; 77,595 query records, 216 candidate fits and 462 displayed numbers checked. A 44-page proposed v4 distinguishes reconstructed evidence, missing original execution records and small numerical differences. |
| Factor/crowding | The missing v10 evidence was rebuilt under the unchanged protocol. Independent validation checks 5,040 fits, 648,000 probability entries and 720 selections; all 166 stable comparison fields and the table match exactly. A complete new archive is supplied; original archive-byte identity is not claimed. |
| Regime predictability | Four hundred fixed runs were regenerated and independently checked. All 800 original raw-file hashes now match: 400 NPZ directly, 400 gzip members after explicit recovery of their original timestamp bytes. Losses and intervals are unchanged; the complete evidence archive and new-execution provenance are retained. |
| ICAIF | Same-account raw financial inputs support a new, explicitly retrospective chronological analysis. Independent checking covers 1,830 HAC regressions, 240 cohorts and 48 prediction records. Only 3 and 1 held-out eligible pairs occur, all events; AUC and C-index are undefined. No favorable replacement for the original 0.933 is invented. A false literature novelty contrast is also corrected. |

Current PDFs, reports and exact commits are linked in the [catalogue](../../../README.md) and [reviewed-main-commits.json](../reviewed-main-commits.json). Every substantive reconstruction or revision received a separate-agent recheck. Those checks found further manuscript and table problems, which were corrected before the final milestone. They are AI-assisted reviews with shared model/tool limitations, not independent human peer review.

## arXiv and Linear

Actual public-version PDFs and source packages were retrieved before deciding whether replacement is warranted:

- **UAI 2601.00908v2:** material correction required. Interpretation, mathematical/statistical claims and operational advice change; historical and recovered follow-up evidence must be separated.
- **KG 2512.22318v3:** material correction required. Proposed v4 revises provenance/pretest claims, the unverified original-checker claim and reconstruction-dependent table entries.
- **Factor 2512.11913v3 and regime 2601.10732v2:** scientific methods, equations, results and interpretation match. GitHub evidence/provenance recovery does not alone require substantial scientific replacements.
- At the previous audit, no existing arXiv deposit had been identified for ICLR/V33, AISTATS or standalone ICAIF. The account dashboard supplied on 2026-10-09 KST now identifies the three pending submissions above; announcement and uploaded-file identity remain unverified.

[Two concrete Linear requests](linear-README.md) include current corrected artifacts, independent review links and completion criteria. **They are now written to Linear and read back:** UAI YEO-169 and KG YEO-170. No arXiv replacement submission is claimed.

The user's latest instruction sequences the **next whole-paper review cycle after confirmed Linear updates**. The Linear prerequisite was completed before the [next cycle](next-cycle-20261009.md), which has now finished. The current recovery/revision milestone is complete; historical evidence that cannot be authenticated remains explicitly distinguished from valid new reconstruction, withdrawal of unsupported claims and genuinely verified original bytes. No arXiv or venue submission has been performed.
