# A useful test and debugging loop

Use a public boundary with an independently known expected answer: a hand-counted mask/IoU, geographic fixture, saved job transition or real user export. Do not reproduce the implementation in its assertion or freeze internals for their own sake. Use the already-defined ticket/checkpoint seam; clarify only if that boundary is genuinely unsettled.

For a difficult bug: capture the exact symptom/command/version; build a small repeatable check; minimise; write falsifiable hypotheses; test one factor; fix and rerun the original case. If no reproduction is available, state that evidence gap and the next smallest probe; do not invent a successful fix or require production access by default. Keep failed results and remove temporary diagnostic clutter once its evidence is saved.

Test-first red/green is valuable for consequential behavioural changes. Refactoring with checks is allowed when justified by the task; documentation/style changes do not need contrived tests. Full ML training is not routine CI. Final-test results cannot become a debugging-driven selection loop.
