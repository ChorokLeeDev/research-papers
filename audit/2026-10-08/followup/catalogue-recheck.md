# Independent catalogue consistency recheck — 2026-10-08

Scope: the current recovery/revision milestone only. This is an independent read-only comparison of the catalogue, seven paper reports and their peer checks, exact Git objects, public-version comparison records, and two prepared Linear requests. It is **not** a new whole-paper scientific review cycle or another execution of the experiments. Only this report was added by the reviewer.

**Disposition: no remaining catalogue-consistency blocker found.** One provenance wording ambiguity in the UAI request was reported and corrected before this report was completed.

## Pinned paths and commits

Programmatically checked each `papers.json` audit entry using `git cat-file -t <commit>:<path>` for its report, independent recheck and revised artifact: **21/21 paths exist as committed blobs**. All seven exact commits agree with `reviewed-main-commits.json`, local `main`, and the corresponding local `origin/main` tracking ref. This is a local Git-object/ref check, not an additional claim of newly contacting GitHub for each URL.

| Repository | Verified main commit |
|---|---|
| selective-labels-minimax-iclr2027 | `21588a434f920ae1d6769ba9145df2017218df63` |
| conformal-coverage-identification-aistats2027 | `c9d1f21510df33eb28a785efba476ca9425517b9` |
| conformal-covid-uai2026 | `533814f27add9dd05bcebb74e71ea21bfeb76649` |
| kg-uncertainty-revision | `af000ebf0c896c4ab0a75ad0f8874077c1eece0a` |
| factor-regime-revision | `d6f6d1e7410c4961126d8be759431b3eb9287da7` |
| regime-predictability-revision | `bbf84ffaac9aca05e434884e517027f57d324e4f` |
| factor-decay-icaif2026 | `4b088580b5b1756c180c4064640f1dcc558dd825` |

All **14 current README links** (report/artifact per project) and all seven displayed finding summaries exactly match the JSON. Historical communication materials remain explicitly historical. The two request descriptions' pinned links also resolve to committed blobs at their stated heads. Each Markdown request exactly equals its JSON title plus description, including after the final wording correction.

## Summary-to-evidence comparison

Read the seven current recovery/follow-up reports and separate-agent rechecks. The catalogue accurately preserves these material distinctions:

- **ICLR:** new fixed-model reconstruction, 10,000 current predictions/ranks and 48 exact probabilities are checked; old confidence-order hashes still differ and the historical strict replay remains failed. The 26/27 bibliographic corroboration and remaining primary-text access gaps are retained.
- **AISTATS:** protocol chronology is qualified; 27 cited metadata records/nine full-text versions and 18/19-page packages are checked. No new numerical results or changed proof is claimed.
- **UAI:** 24 refitted follow-up models/528 equal arrays and negative **sample task associations** do not recover or explain the original missing 50-seed study. The date-truncated join defect is confined to the recovered snapshot. Unsupported operational/hyperparameter claims are withdrawn.
- **KG:** public v3 is the expanded three-graph study; the 77,595 repeated query records, 216 candidate fits and 462 displayed values are checks of retained retrospective reconstruction, not independent graph-population replication. Original added-run/checker/pretest chronology remains unverified. Numerical deviations and adverse risk endpoints are disclosed.
- **Factor:** the complete 5,040-fit/648,000-entry reconstruction and 166 stable fields/table match do not authenticate the unavailable original archive bytes.
- **Regime:** all 800 original file hashes are recovered through explicitly documented reconstruction and gzip timestamp restoration; 400 reruns and independent loss/interval checks do not constitute a new external experiment. Numerical results remain unchanged.
- **ICAIF:** 1,830 regressions, 240 cohorts and 48 overlapping prediction records support the limited chronological reconstruction. The 3/1 eligible held-out cases are all events, making AUC/C-index undefined. No favorable replacement or validation of the original 0.933 is asserted.

The account-wide receipt is described as an evidence search across 31 owned repositories, not a scientific audit of unrelated repositories. Public/private counts sum to 31; forks and empty repositories are overlapping attributes, not extra projects. This catalogue check does not repeat the coordinator's account enumeration/history search. It confirms that the text states its scope and does not claim that absent tracked artifacts never existed.

## Actual public versions and proposed requests

- **UAI 2601.00908v2:** independently opened the preserved public source tar and compared `main.tex` and `references.bib` with original commit `96d9616961e5ae8607373181d35262cb21a2b0d1`; both are byte-identical. The material-correction request corresponds to that actual public version and the revised statistical/empirical interpretation.
- **KG 2512.22318v3:** independently compared the preserved public tar with the preserved expanded source ZIP: **34 common files are byte-identical**, with only arXiv `00README.json` extra in the tar. The draft request accurately treats v4 as proposed, not submitted.
- **Factor 2512.11913v3 and regime 2601.10732v2:** independently checked every recorded source-member hash against the public tar and current source. **25 factor** and **19 regime** non-manuscript scientific members match exactly. Read the complete manuscript diffs: they concern evidence availability/reconstruction provenance, without changed scientific methods, equations, tables, numerical results or conclusions. The decision that this recovery alone does not require a substantial scientific replacement is supported; a future provenance note remains possible.
- The absence of an identified public ICLR/AISTATS/standalone ICAIF deposit is stated as a search outcome. A local `arxiv` file is not treated as proof of publication. ICAIF is not conflated with the separate regime paper's arXiv identifier.

**Finding and closure:** the first UAI request phrasing could be read as proving that the historical hyperparameter table itself was produced by the recovered aggregate-perturbation code. The available evidence establishes the recovered code's behavior and missing original refit provenance. The final JSON and Markdown now say exactly that before withdrawing the unsupported robustness claim. No numerical conclusion or paper file changed for this correction.

The status files explicitly say **prepared, not written to Linear**, contain no invented external issue ID, and make no arXiv/venue-submission claim. The follow-up README and JSON explicitly state that the user's next whole-paper review cycle has **not started** and remains sequenced after confirmed Linear updates. This consistency check closes the current milestone; it does not bypass that sequence or claim external persistence.

## Final targeted recovery-surface closure

After the catalogue comparison, the reviewer checked all 11 advertised PR heads across the 31 account repositories. All were already reachable from the inspected histories, with zero additional commits or paths. A single archived embedded-repository pointer has no authoritative recorded remote; its target commit was absent from all 31 local object databases and was not returned by authenticated commit queries across all 31 repositories (29 HTTP 422 responses, two HTTP 409 responses from empty repositories; a known-commit positive control returned HTTP 200 and the correct SHA). No new original experiment evidence or material alternate manuscript was recovered. The pointer remains a provenance limit, not proof of nonexistence. This was targeted closure of the current recovery scope, not the next full review cycle. Private receipts are retained outside the public catalogue; aggregate results and their receipt hash are recorded in `account-recovery-scope.json`.
