# Four roles, one maintainer

| Role | Use | Artifact | Boundary |
|---|---|---|---|
| Guide | Start/resume, current-checkpoint tickets, authorised Jira updates | One session-sized plan/ticket and handoff | No unsolicited backlog or product implementation |
| Tutor | Concept, API, exercise, review of reasoning | Lesson/learning record and explain-back | No whole-checkpoint solution dump; no invented understanding |
| Engineer | Explicit pair/delegate implementation or debugging | Explained bounded diff and observed checks | No scope expansion, auto-commit or final-test tuning |
| Reviewer | Meaningful diff/experiment/output/release | Specification + standards/evidence findings | No silent fixes or human-validation claim |

Invoke the skills in the main conversation, e.g. `$floodlens-tutor`. If a separate context helps, request the matching custom agent by name. Profiles live under `.codex/agents`, inherit your model/permissions/MCP and do not override them. Do not launch all four simultaneously. One writer; optionally one additional reviewer.

Mode is explicit: **teach** = concept/prediction/attempt/check, **pair** = small explained implementation together, **delegate** = requested bounded implementation followed by explanation/review. Generated code remains AI-assisted. You choose the mode per task and can change it; record that change. Routine authorised actions do not require repeated permissions, but changed scope, actual external writes and human review declarations cannot be inferred from a skill.

These rules reduce unexamined generation through bounded tasks, verification, learning evidence and disclosure. They cannot prove comprehension or guarantee correct code. Tests, actual review and your ability to explain/troubleshoot remain essential.
