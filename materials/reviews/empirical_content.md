# Agent conference: empirical communication content

Participants: empirical_content (author of UAI/KG and reviewer of ICAIF), scientific_review (independent claim reviewer), root (ICAIF author and integration).

## Source work

- UAI pinned current main at `96d9616961e5ae8607373181d35262cb21a2b0d1`; read the complete camera-ready `paper/main.tex`, targeted results, theory assumptions, external protocols, model-family sensitivity, threshold table and limitations.
- KG pinned active revision at `208f21270f44cb5fe1e26a8b0e0b9dbab88f4a18`; read `manuscript.tex`, its full empirical-results input and key count, ensemble, predictor-quality tables. Historical performance is explicitly separate from current findings.
- Both repository roots returned no AGENTS.md. No repository files were modified by this agent.
- Original UAI figure was fetched, rendered and inspected. Its existing labels overlapped. Retrieved the exact source plotting script and replotted its sixteen numeric tuples with separated annotations. Recomputed Spearman correlation is 0.8529411764705882. Source script, original PDF and clean PNG/SVG are retained; no experimental data were changed.

## Scientific-review exchange and resolutions

1. Reviewer emphasized the UAI probability-space additive assumption and measured log-odds TreeSHAP distinction. Author agreed and placed the caveat beside the mechanism, on the poster, and in both introductions. No guaranteed mapping from measured C to future coverage is claimed.
2. Reviewer warned that the pooled sixteen-task result contains the original eight SALT tasks and is not independent replication. Author explicitly distinguishes eight external multiclass tasks, the excluded three-class auxiliary task, and four external null-shift controls.
3. Reviewer identified imprecise cover wording: “before a distribution shift arrives” ignores that validation already covers COVID onset. Author changed it to “before future test data arrive.”
4. Reviewer requested that the KG AUROC reversal not imply that better accuracy causes reversal. Author added the simultaneous-training-change caveat to slide 5, poster and EN/KO introductions, and placed learned-count benefits immediately after the raw-score failure.
5. Reviewer checked current KG numeric claims and requested accessible metric glosses. Author defined AURC and Brier in poster and introductions and expanded LR/HGB visibly on slide 6.
6. Root requested takeaway/noun titles instead of imperatives. Author changed final titles to “Model reliance and future coverage” and “Support as a predictor-specific diagnostic.”

## Review of ICAIF content sent to root

Checked `icaif2026.json` against original-source TeX: CV RSF 0.933 ±0.097, logistic AUC0.933 ±0.133, seven events, six of ten holdout, regime-delay table and regional IS/OOS distinctions matched. Highlighted a source ambiguity: the frozen OOS table uses Elevated n836, while the Data paragraph describes percentage-unit n953 and decimal-unit n836. Requested an adjacent note that return scaling changes regime assignments. Root agreed to add it in slide notes and poster. Also requested a plain explanation of F as evidence for source-lag contribution; root agreed. Existing notes correctly distinguish statistical threshold loss from disappearance of economic information.

## Remaining limits

These are agent editorial/scientific reviews, not human peer review or new empirical replication. UAI remains observational with exploratory thresholds, reused development tasks in the pooled endpoint, and model-family limits. KG uses two inspected static graphs with incomplete recorded-target labels and no temporal validation. ICAIF source inconsistencies are documented rather than silently repaired. Final PDF/PPTX layout review belongs to the integration pass.
