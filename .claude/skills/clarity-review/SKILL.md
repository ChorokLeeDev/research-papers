---
name: clarity-review
description: >-
  Review any explanatory writing — presentation scripts, speaker notes, slides,
  papers, reports — and make it clear to its intended audience without dumbing
  down the content or inventing facts. Use when the user asks to "make this
  clearer", "a non-expert should understand this", "simplify the notes", "review
  for clarity", "이해 안 돼", "너무 어렵다", "쉽게 고쳐줘", or points at a sentence and
  asks what it means. Works claim-by-claim against the source of truth so numbers
  and formulas stay honest.
---

# Clarity review

Make writing land for its intended reader — the one who hasn't read the other
sections, hasn't seen the related work, and will be lost by one undefined term —
while keeping every claim true to its source. Clarity is not simplification:
you remove confusion, not content.

## When to use

The user wants text (a talk script, speaker notes, slide bullets, a paper
passage, a README) to be followable by its audience. Triggers include "make it
clearer", "a newbie should get this", "simplify", "what does this sentence
mean?", or any pointed quote with a "???". Also use proactively while editing
explanatory material.

## The core moves

Apply these in order of impact. Each is a concrete edit, not a vibe.

1. **Define every term on first use.** The first time a reader meets a piece of
   jargon, define it inline in plain words — don't assume an earlier section or
   another talk introduced it. A standalone reader must not hit an undefined
   word. (Example pattern: "SHAP — a method that splits a prediction into how
   much each feature contributed.")

2. **Intuition before formalism.** Lead with the plain idea or the "why", then
   the mechanism, then (optionally) the notation. "My intuition was simple: …"
   beats opening on a definition.

3. **Ground every abstraction in a concrete example.** Replace symbols and
   abstract nouns with something the reader can picture: a specific model
   (`score = 3·income + 0·eye-colour`), a running scenario (a loan model, a
   15%-flagged audit), named stand-ins. Keep one example per concept and reuse
   it; don't switch examples mid-thread.

4. **No ambiguous pronouns or vague actors.** "They", "it", "the vendor",
   "the region" must each have one clear, named referent already on the page.
   Give recurring actors stable role names (e.g. owner vs auditor) and use the
   same word throughout — never two labels for one thing.

5. **Cut flourish and hedging.** Delete rhetorical padding ("provably, not
   hand-waving", "it is worth noting that", "almost disappointingly"). Say the
   thing plainly. Drop clause-piles; one idea per sentence.

6. **Level for a mixed audience.** Write the main thread so a non-specialist
   follows it; demote the formal names and proofs to a short parenthetical or a
   backup slide ("For the math audience: …"). Never make the expert detail the
   only path through.

7. **Connect the pieces.** End a unit by pointing to the next; open the next by
   picking up that thread. Remove two passages that make the same point — give
   each a distinct job (e.g. intuition → explicit construction → general
   theorem), never a restatement.

## Source-grounding discipline (do not skip)

Clarity edits must not corrupt facts. This is the part that separates a review
from a rewrite that reads well and says something false.

- **Every number, formula, and claim gets checked against the source of truth**
  (the paper, the data, the results file). Open it and verify — do not trust the
  draft, and do not reconstruct a value from memory.
- **Distinguish an illustrative number from a headline result.** If a figure is
  "28% in this specific example", say *illustrative*; don't present it as the
  paper's finding. Check the source's own wording (captions, theorem statements)
  to tell which it is.
- **If you explain a mechanism ("how is this computed?"), the explanation must
  match the source.** If the source doesn't state the mechanism, say so and keep
  the claim at the level the source supports — never invent an algorithm the
  author would have to defend.
- **When a formula helps, quote the real one** from the source (e.g.
  `power = min_u R_k(u, u+d)`), not a plausible-looking stand-in. Render it so it
  survives the output format (watch for Unicode subscripts that a mono font drops
  — prefer ASCII like `R_k`, `beta`, `X_1`).
- **Preserve honest scope and caveats.** Make a limitation *clear*, not *gone*.
  Don't inflate a hedged result to sound more certain than its source.

## Workflow

1. Read the passage and name its intended audience (who's listening, what they
   already know).
2. Locate and open the source of truth for any number/formula/claim before
   touching those sentences.
3. Pass through the core moves above. For each edit, keep the meaning; change
   only the clarity.
4. Where the user pointed at a specific sentence, fix *that* and then scan for
   the same problem elsewhere (an undefined term is usually undefined everywhere).
5. Keep vocabulary and examples consistent across the whole document; reconcile
   any term you changed in one place everywhere it appears.
6. If the medium renders (PDF/slides), rebuild and visually verify: no clipped
   text, no dropped glyphs, figures match what the text claims.

## What this skill does NOT do

- It doesn't shorten for its own sake or strip necessary technical content.
- It doesn't add claims, numbers, or mechanisms not in the source.
- It doesn't restructure an argument the author deliberately chose — it clarifies
  the one that's there.
