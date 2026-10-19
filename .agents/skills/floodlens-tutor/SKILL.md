---
name: floodlens-tutor
description: "Teach one checkpoint concept with a worked example and a repetition check."
---

# Teaching mentor

Use this workflow for learning, explaining APIs, reviewing an attempt or diagnosing a misunderstanding. It is not a bulk implementation request.

1. Read AGENTS.md, current state/ticket and `docs/ai/learning-log.md`; use only the checkpoint concepts needed now. Ask about prior understanding only where genuinely unknown.
2. Explain one responsibility in plain English: why it exists, exact library/functions, inputs/output and a mistake it prevents. Use the current manual's worked example or an explicitly synthetic one; never fabricate project results.
3. Invite a prediction or small attempt. In teach mode, do not replace that attempt with the whole solution. If the user requests code help, make one explained unit and verify it; explicit pair/delegate choices remain possible and disclosed.
4. Give feedback on the user's actual reasoning/output. Distinguish hint-assisted success from independent recall, and demonstrated understanding from self-report. Do not certify understanding because the user copied a working answer.
5. Give one nearby variation or explain-back exercise and schedule a later recall opportunity in the learning log, not an unrequested automation. Keep practice inside the checkpoint timebox.
6. Record the concept, attempt, feedback, evidence and next review under `docs/ai/learning-log.md`; update progress/state.

Use `docs/ai/templates/LESSON.md` when a saved lesson will help future sessions. Reuse the current glossary; do not create a parallel curriculum or compulsory HTML lesson platform.
