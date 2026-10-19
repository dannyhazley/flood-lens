# Jira through the user's connected MCP

The Atlassian connection was confirmed during kit preparation. Credentials, cloud IDs and personal account details are intentionally not bundled. The connection in one Codex client is not guaranteed to transfer to another client/machine; verify available tools in the actual repository session. No API token belongs in this repository.

1. If the Jira site/project is unset, discover accessible resources using the connected MCP and ask the user to choose the personal target once. Save a nonsecret site URL/project key only if the maintainer wants it recorded. Never select an employer workspace by assumption.
2. Discover/read project metadata, available issue types, required fields and transitions. Use actual returned IDs and parent/epic semantics; do not assume every Jira project has the same workflow. Use the connector's supported search tool for duplicates and exact JQL only for structured filtering.
3. Draft the current checkpoint's bounded tickets with the template. Prefer native dependency/parent links where supported. A connected MCP grants access, not a standing instruction to create/transition/comment. If the user explicitly authorises the batch, execute that scoped batch without repeatedly asking about routine fields.
4. Use real issue keys in branch names, commit messages and PR titles. Do not maintain duplicate GitHub Issues for the same work unless deliberately chosen. Code/evidence stays in GitHub; Jira owns task state; the manual owns learning/checkpoint gates.
5. Move to Review when the change/evidence is ready. Done requires technical acceptance plus the agreed learning evidence or an honestly documented limitation; user understanding cannot be supplied by an agent. Do not close parent epics automatically.
6. If a write partially fails, inspect which issues/changes succeeded before retrying. Avoid duplicates. Report remaining work and precise failure; never switch to a different project to make the command succeed.

Recommended solo board: checkpoints as epics, Backlog/Ready/In progress/Review/Done with a blocked flag, one active implementation ticket. Detail only the current checkpoint. Read/use only the Atlassian skills relevant to the actual request; do not publish status reports to Confluence or send messages because another skill happens to be installed.

Until a real Jira ticket exists, `LOCAL-1` may identify a clearly labelled local draft. Do not present it as a Jira issue or fabricate a URL. See [Atlassian GitHub linking](https://support.atlassian.com/jira-cloud-administration/docs/integrate-with-github/) when enabling the separate GitHub integration.
