# Source understanding and attribution

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills), reviewed at commit `49dd158d1076134a641b33efb035946536778336` on 16 October 2026. The repository itself describes its goal as real engineering. We adapt selected ideas, not an autonomous coding process or its complete installation.

| Inspected source at pinned revision | Useful idea | FloodLens adaptation |
|---|---|---|
| `skills/engineering/to-tickets/SKILL.md` | Verifiable slices/dependencies | Session-sized current-checkpoint tickets; early science does not force premature API/UI |
| `skills/engineering/tdd/SKILL.md` | Behaviour and independent expected answers | Meaningful checks at actual boundaries, proportional to risk; no ritual tests or repeated approvals for established seams |
| `skills/engineering/diagnosing-bugs/SKILL.md` | Tight reproduction and falsifiable probes | One factor/check at a time, precise blockers, retained failure evidence |
| `skills/engineering/code-review/SKILL.md` | Separate spec and standards axes | One review role/checklists, no compulsory two-agent team |
| `skills/productivity/teach/SKILL.md` | Stateful learning and recall | Short Markdown learning records/exercises tied to actual attempts; no compulsory HTML curriculum |
| `skills/productivity/handoff/SKILL.md` | Referenced context and minimal duplication | Repository state/progress references and concise handoffs |
| `skills/engineering/implement/SKILL.md` | Bounded work followed by checks/review | Preserve explicit teaching mode and human instructions; **do not adopt automatic commits** |

Instructions/scripts here are written for FloodLens; the upstream MIT notice is retained in [the bundled licence](../../licenses/matt-pocock-MIT.txt). No upstream installer, script, dependency or plugin was run, installed or automatically enabled.

Official references for packaging/behaviour: [skills](https://learn.chatgpt.com/docs/build-skills), [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [hooks](https://learn.chatgpt.com/docs/hooks), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Git hooks](https://git-scm.com/docs/githooks), [GitHub–Jira linking](https://support.atlassian.com/jira-cloud-administration/docs/integrate-with-github/). These explain formats/lifecycle; they do not prove live compatibility or product performance.

Builder inspected local Codex version `0.163.0-alpha.10.2`. Agent configuration was checked locally; live custom-agent behavior and Jira writes remain target-environment checks.

Official GitHub action tags resolved to pinned commit SHAs during packaging: {"actions/checkout": {"sha": "d23441a48e516b6c34aea4fa41551a30e30af803", "tag": "v6"}, "actions/setup-python": {"sha": "ece7cb06caefa5fff74198d8649806c4678c61a1", "tag": "v6"}, "actions/upload-artifact": {"sha": "ea165f8d65b6e75b540449e92b4886f43607fa02", "tag": "v4"}}.
