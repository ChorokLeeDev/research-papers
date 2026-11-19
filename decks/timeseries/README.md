# Time Series & AI Forecasting · course final

**Multi-horizon factor volatility: what needs recalibration?**

- [Presentation PDF](deck.pdf): six slides, 4:3 Beamer style matching the other decks.
- [Five-minute speaking notes](speaking-notes.md).
- [Complete course-criteria checklist](requirements-check.md).
- [Rendered-page checks](deck-check.json) and [numerical source checks](verification.json).

The presentation forecasts the log sum of future squared factor returns
over 5, 10 and 20 trading observations. It compares intercept-only,
response and memory recalibration against a completed-block naïve benchmark,
with RMSSE from training-only scales and chronological out-of-sample errors.
All six U.S. factors are evaluated equally.

All mandatory course criteria are covered. The deck contains point
forecasts; prediction intervals are an optional extension, not a reported
probabilistic result. Historical evaluation data were reused, and no
economic gain or uniform superiority is claimed.

This folder is a verified PDF snapshot, following the copied-course-deck
convention used for e-prop. The editable source, figure builder, archived
metrics and full provenance remain in the source project's
docs/techtalk/course-final directory. The local source path and SHA-256
hashes of every copied file are recorded in [copy-manifest.json](copy-manifest.json).

When the course deck changes, refresh this PDF and its companion checks
from that source directory so the collection remains consistent.
