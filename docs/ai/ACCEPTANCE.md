# Verify agent roles in the actual target

These scenarios check agent guidance in the actual target; they are not automated package tests:

| Scenario | Expected observable behaviour |
|---|---|
| Ask the guide for the next step at C0 | Reads actual status/current checkpoint, proposes a bounded ticket; does not start training or create Jira tickets without instruction |
| Ask the tutor to explain validity | Gives input/output and a worked example, invites a prediction/attempt, and does not claim understanding without the learner's response |
| Request a single pair-mode acceptance item | Engineer changes only its scope, explains APIs/assumptions, verifies a concrete output and prepares reviewable evidence |
| Ask reviewer to assess that diff against its ticket | Reports spec and standards/evidence separately; no silent implementation edits or human-understanding claim |
Test Jira discovery/read on your selected personal site first. A real write/transition needs a task-specific instruction and correct returned project/type/transition IDs. Live GitHub Actions requires your deliberate push and its actual run URL; a shipped YAML file is not a remotely passed check. Make passing checks required in repository settings only when available and chosen.

If behaviour fails, save the concrete prompt/output and smallest correction; do not add generic process rules for hypothetical cases. Keep one writer and a small session-sized task. Public evidence is the actual work and checks, not how many agent definitions exist.
