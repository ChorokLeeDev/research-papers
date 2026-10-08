# One-page research briefs

Seven source-grounded English/Korean PDFs accompany the one-minute scripts in
the root README. They are explanatory briefs, not replacements for the papers.

These September briefs predate the [8 October statistical audit](../audit/2026-10-08/README.md). They are retained as historical summaries, not corrected current evidence. In particular, the ICAIF performance estimates were not reproduced and the UAI statistical interpretation required corrections; read the linked audit and current manuscripts before reusing these PDFs.

## Rebuild

Use Python 3 with `reportlab`. Set `BRIEF_FONT_DIR` to a directory containing
`NanumGothic-Regular.ttf` and `NanumGothic-Bold.ttf`, available from the
[Google Fonts Nanum Gothic directory](https://github.com/google/fonts/tree/main/ofl/nanumgothic).
The font is licensed under the SIL Open Font License; the license is retained
at [FONT_LICENSE.txt](FONT_LICENSE.txt). The PDFs embed font subsets.

```bash
BRIEF_FONT_DIR=/path/to/fonts python tools/build_briefs.py
```

`papers.json` records version provenance, and `briefs.json` contains reviewed
summary text. `manifest.json` records the generated PDFs' SHA-256 hashes.
After rebuilding, check that each PDF is exactly one page, inspect its rendered
layout, and recheck scientific claims against the recorded source version.

The ICAIF brief follows the actual five-page submission supplied by the author.
The related ten-page upstream draft is not its authoritative content source.
