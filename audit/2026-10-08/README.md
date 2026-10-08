# Statistical and reproducibility audit — 8 October 2026

This audit covers all seven projects listed in `papers.json`, including their linked manuscript repositories. The requested priority is statistical correctness. The user reported an ICAIF concern described as “statistical error”; no full reviewer report was supplied. No venue decision or reviewer verdict is inferred from that description.

## Scope and evidence rules

The frozen repository commits and original artifact hashes are in [baselines.json](baselines.json). Published/submitted records and provenance snapshots are preserved. Corrections are made on revision branches, without merging main or submitting to a venue. Each paper retains its own initial review, issue ledger, commands, evidence and unresolved limitations in `audit/2026-10-08/` in its own repository.

The first pass covers theorem assumptions, statistical estimands, information timing, leakage, sample/event denominators, uncertainty, multiplicity, citations, and agreement among source, executable analyses and reported artifacts. A second reviewer checks substantive corrections; targeted follow-up continues where a concrete check can resolve a material issue. We do not search indefinitely, optimize acceptance scores, or treat agent agreement as proof.

Classifications are **verified**, **contradicted**, **uncertain**, and **unavailable**. Missing evidence does not establish fabrication. Tests can establish implementation properties, not novelty or broad empirical validity. Fresh reproductions and deterministic counterexamples are distinguished from historical results and new proposed experiments. Agent checks share model/tool limitations and are not independent human peer review.

## Environment and current limits

The cloud machine supports Python, TeX, numerical analysis, PDF inspection and the supplied presentation runtime. A separate shared environment at `/workspace/research-review-env` adds pinned pytest 9.1.1 and CPU torch 2.14.0 to the existing numerical libraries. Raw data are downloaded only through repository-supported sources with the provided checksum checks; full retraining is not assumed necessary for ledger verification.

Fresh requests to arXiv, Crossref and PMLR returned proxy HTTP 403. Required academic destinations have been saved in the environment network draft, but draft persistence does not establish runtime access. External bibliographic claims remain unverified until a permitted primary-source response is observed. Local bibliography consistency can still be checked. No credential values are requested or recorded.

## Catalogue reproducibility correction

The slide builder assumed presentation helpers lived under `/root/.codex`; the current runtime provides them under `/opt/codex`. It now discovers either standard path and supports an explicit `RESEARCH_PRESENTATION_SKILL`. The PDF checker previously wrote missing-content findings while returning success; it now fails for missing text/glyphs, out-of-page spans, replacement characters and empty input.

[Executable validation](catalogue-tool-validation.json) records a fresh ten-slide deck/PDF build, a passing full-content check, a deliberately missing-text case that fails, and an empty-collection case that fails. These validate the document toolchain only, not the paper's scientific conclusions. Generated validation outputs remain outside the tracked deliverables.

Paper findings and milestones will be recorded here as their source corrections and independent rechecks complete.
