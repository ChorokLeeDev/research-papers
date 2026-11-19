# Final presentation requirements check

Checked against the supplied course announcement. The deck contains six
English slides and a five-minute Korean speaking script. Every mandatory content item is
covered. Prediction intervals are not included; this is a point-forecast
presentation, with calibrated intervals identified as a possible extension.

| Criterion | Slide | Evidence / assessment |
|---|---|---|
| What is forecast? | 1 | Explicit next-5/10/20-observation log squared-return-sum target |
| Why does it matter? | 1 | Missed risk increases and unnecessary exposure cuts |
| Who uses it, for what decision? | 1, 6 | Risk manager setting horizon-specific factor-exposure caps |
| Clear, specific research question | 1 | Refit level, response or memory when the horizon changes? |
| Practical value of better forecasts | 1, 6 | Exposure decisions at a fixed risk budget; potential effects are distinguished from unmeasured economic benefits |
| Data source | 2 | Archived U.S. Fama–French five factors plus momentum |
| Data period | 2 | 1990-01-02 to 2024-12-31 |
| Frequency and observation count | 2, 3 | Daily; 8,817 observations per factor, 3,753 evaluation origins per horizon |
| Plot of key data features | 2 | Six training-period panels show persistent high/low volatility episodes; no unsupported seasonality claim |
| Proposed methods and suitability | 3 | EWMA weights recent volatility with few parameters; B/C/D separate level, response and memory |
| At least one benchmark | 3, 4 | Naïve forecast repeating the most recent completed h-observation block |
| Out-of-sample evaluation | 3 | Chronological 2010–2024 evaluation; refit every three years on the preceding ten years; completed-label gap |
| Forecast horizons | 1, 3, 4 | h=5/10/20 trading observations |
| MASE or RMSSE for point forecasts | 3, 4 | RMSSE; daily lag-1 differences and fixed pre-2010 training scales explicitly defined |
| Probabilistic accuracy measures | — | Not applicable: no predictive distribution or interval is produced |
| Method-versus-benchmark comparison table | 4 | B/C/D/CV and naïve, all three horizons, arithmetic mean of equally weighted factor scores |
| Forecast plot | 5 | Daily out-of-sample predictions versus future targets, all six factors; h=20, fixed illustration year 2013 |
| Prediction intervals where possible | 6 | Optional item not supplied; calibrated intervals are a stated extension, with no coverage claim |
| Quantified improvement | 4 | B: 9.4% lower mean RMSSE than naïve at h=20; D: only 0.07% lower than B, worsening four factors |
| Key takeaway and decision implication | 6 | Separate adjustment decisions; start with common memory and validate added parameters before use |
| Limitations and possible extensions | 6 | Reused historical data, noisy risk proxy, no economic endpoint; prospective validation and intervals |
| At most 5–6 slides | All | Six rendered pages |
| More time on results/interpretation than standard methods | 4–5 | 120 seconds (75+45) versus 50 seconds for methods/evaluation; total 300 seconds (40/50/50/75/45/40) |
| Report out-of-sample accuracy only | 4–5 | Accuracy uses 2010–2024 evaluation forecasts; slide 2 is explicitly descriptive training data |
| Every axis labelled with units | 2, 5 | Calendar year or forecast-origin month; log summed squared decimal returns; RMSSE is unitless |

The numerical audit binds claims to the exact US factor × horizon × model
rows, recomputes their frozen MSE/MAE, verifies common evaluation origins,
and checks the named baseline and training-only RMSSE denominator.
All six factors' adverse and favorable D-versus-B results are retained.

Automated rendered-page checks and source hashes are recorded in
**deck-check.json** and **verification.json**. The layout check also checks
page bounds and LaTeX overflow. The speaking durations are a preparation
plan; actual delivery should be rehearsed against five minutes.
