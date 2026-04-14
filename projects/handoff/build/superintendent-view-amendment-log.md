# Amendment Log: superintendent-view
Converged in 2 run(s).

## Run 1 — 2026-03-16

In extractPercentage, the explicit numeric patterns ('80%', '80 percent', word-form numbers) must be evaluated BEFORE the keyword patterns ('done', 'complete', 'finished', 'almost done', etc.). If a numeric percentage signal is present in the text, it takes precedence over any keyword signal. Reorder the checks: parse numeric % first, then word-form numbers, then keywords as fallback.
