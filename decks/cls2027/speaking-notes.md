# Chorok Lee · CLS 2027 · 4-minute research video — timed English script

Planned runtime: **04:00**. 5 main slides. Read-aloud text: ~470 words.
Times are rehearsal targets, including pauses and slide changes. Time one full rehearsal before presenting. Do not read source footers aloud.

Record your own spoken presentation in English. Save the final video as **13470_Chorok_Lee_CLS2027.mp4**. The deck and script are preparation files, not the requested video.

| Slide | Time window | Duration |
| --- | --- | --- |
| 1. Chorok Lee | 00:00–00:40 | 40s |
| 2. Where it started: the same shock, very different damage | 00:40–01:15 | 35s |
| 3. My thesis: give an honest range, not a false single number | 01:15–02:15 | 60s |
| 4. Related work: how many labels does it take to catch a bad model? | 02:15–03:05 | 50s |
| 5. At CLS: two projects on trustworthy evaluation | 03:05–04:00 | 55s |

## 1. Chorok Lee · 00:00–00:40

Hello, I'm Chorok Lee. I'm a master's student in software engineering at KAIST, advised by Professor Insik Shin, finishing in February 2027. I came to this from economics at Yonsei, with an exchange year at Dartmouth. My research asks one question: when we check whether a model is reliable, what can the evidence we actually have really tell us — and what more would we need to collect? I study this when the data shifts after deployment and the true answers are missing or unreliable.


## 2. Where it started: the same shock, very different damage · 00:40–01:15

My first question came from COVID. In my published UAI paper, many prediction tasks were hit by the very same disruption — yet some stayed reliable and others fell apart. I wanted to know why. My finding: the models that leaned almost all their weight on one single feature were the ones that broke, because when the world changed, that one feature changed too. That gave a warning sign you can compute before deployment. But it only works for one family of models — which pushed me to a deeper question.


## 3. My thesis: give an honest range, not a false single number · 01:15–02:15

Here's the deeper question. After the data shifts, we can't measure a model's reliability directly — we only see summaries, like how far the data moved and how confident the model is. Can those summaries tell us how reliable the model still is?

My thesis answer has two parts. First, a plain "how far did the data move" number is not enough: I show two shifts that move the data by the exact same amount, where one breaks the model and the other doesn't. So that number alone can't tell them apart.

Second — and this is the part I care about most — when the information is limited, the honest answer isn't a single reliability number, it's a range. I prove the exact best-case and worst-case reliability the evidence allows. That's valuable because it separates "we're unsure because our sample is small" from "the evidence we have simply cannot pin this down." For a PhD, I want to extend this to models whose confidence is itself untrustworthy.


## 4. Related work: how many labels does it take to catch a bad model? · 02:15–03:05

My related ICLR work asks a practical follow-up. A model can look good just because its hard cases were never checked. So: how many of those missing answers do we have to go check before we can be confident the real error rate is too high — without crying wolf?

I work out that exact number. And I show something useful: if you don't know how trustworthy your checker is, no amount of extra checking fixes that — knowing your checker's reliability is a separate resource from doing more checks.


## 5. At CLS: two projects on trustworthy evaluation · 03:05–04:00

At CLS, I'd like to pursue two projects. First, when a model's confidence can't be trusted under a data shift, describe the full set of reliabilities the evidence still allows — a range, not a guess. Second, prove how many labels you truly need to certify a deployed model's risk when the hard cases are the ones left unchecked.

Both connect directly to the groups there — Celestine Mendler-Dünner's work on risk scores, and Moritz Hardt's on the limits of evaluation. The joint ETH and Tübingen setup, with the twelve-month exchange, is exactly the place to take one of these problems from theory to real evaluation, across both groups. Thank you.
