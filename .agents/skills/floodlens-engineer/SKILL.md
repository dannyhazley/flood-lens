---
name: floodlens-engineer
description: "Implement or debug the authorised ticket in small explained, verified units."
---

# Engineering partner

Use only when the human asks for implementation/debugging on a bounded FloodLens ticket or explicitly selects pair/delegate mode. In teach mode, begin with explanation/prediction and avoid implementing the entire checkpoint.

1. Read AGENTS.md, the actual ticket/acceptance, current checkpoint and Git status. List relevant existing files/contracts, changes to preserve, and the smallest verifiable outcome. Do not invent an implementation from the plan alone.
2. Establish the seam and expected behaviour. For a nontrivial defect/feature, use a failing example/test with an independent expected answer where useful. For a low-impact change, use proportional verification instead of ritual tests.
3. Explain the next unit's APIs, input/output and assumptions; implement only that unit. Keep numerical operations distinct from I/O/report/service/UI. Do not add an architecture, model family or dependency to make the diff look sophisticated.
4. Diagnose failures through a tight reproduction and one falsifiable change at a time. If reproduction or data rights are unavailable, record the exact blocker. Do not conceal failed checks or edit expected values to match a bug.
5. Run checks appropriate to the change, capture observed outputs, and inspect the final diff. Protect masks, geography, split independence, frozen test information, method artifacts and complete-output state. A losing model is a valid result, not permission for unlimited search.
6. Produce a reviewable diff, explanation, verification and limitations. Request the reviewer role when appropriate; do not automatically spawn an implementation team. Update progress/state.
7. Commit/push/merge/Jira changes only when actually instructed.

Read `docs/ai/references/DEBUG-AND-TEST.md` for difficult debugging or test design; it is not a mandatory ceremony for every edit.
