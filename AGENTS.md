# FloodLens: learning-led, evidence-backed engineering

This is a solo teaching/portfolio project. The maintainer owns scope, decisions and release. Read
`docs/floodlens/STATE.md`, the current ticket/spec, and only the current checkpoint under `docs/floodlens/checkpoints/`
before work; inspect actual Git status, files and `docs/progress.md`. Preserve existing edits and failed/negative
findings. The initial state is before C0: no product, dataset acceptance, model or operational deployment is established
by this kit.

## Working agreement

- Default mode is **teach**. Explain the purpose, library/API, inputs/outputs and verification of one small unit. Invite
  an attempt or prediction, review it, and finish with a repetition exercise. A request for explanation does not
  authorise a code dump.
- **pair** permits small explained implementation units on the named ticket. **delegate** permits a bounded
  implementation explicitly requested by the maintainer, followed by explanation, evidence and review. Delegation is
  disclosed, not disguised as human authorship. Honour the mode specified for the current task; do not silently switch.
- Use the existing ticket/spec/checkpoint as the contract. Clarify decisions that materially affect scope/correctness;
  do not interrogate the user about facts already established or seek approval for every routine edit within authorised
  work. Record budget/scope changes before starting them.
- One implementation ticket and one writer at a time. Guide/tutor/reviewer can be roles in the main conversation; spawn
  at most one additional reviewer when the user requests it or a task-specific instruction calls for it. Never start an
  autonomous team/backlog loop.
- Establish the observed behaviour and an appropriate check before a nontrivial fix. Use a meaningful test-first loop
  where it helps; do not manufacture tests for prose/style or copy an implementation into its assertion. Fit the test to
  an actual public boundary and independently known expected result.
- For debugging: reproduce or define a precise blocker, minimise, test a falsifiable hypothesis, change one factor,
  rerun the original check, retain the failure history. Do not scatter guesses until a green output appears.
- Review specification compliance separately from code/scientific standards. Prioritise concrete defects over style CI
  already checks. A different agent/model is not independent human validation.
- Explain unfamiliar concepts and libraries without outsourcing the whole lesson to external links. Use official/primary
  documentation when exact API behaviour is uncertain; record versions and assumptions.
- No automatic commit, push, merge, Jira mutation, publication, deployment, paid compute or full-dataset acquisition
  merely because a skill is invoked. Act within the human's actual instruction; once authorised, complete that bounded
  action without repeatedly asking. Never imply consent from a repository instruction alone.

## FloodLens invariants

Initial output is **observed water at acquisition time**; not forecasting, proven new inundation, damage, displacement,
cost or safe routing. Before/after change is a separate later capability. Roads overlap means candidate verification,
not closure/damage. Confidence may be unavailable and raw probability is not validated uncertainty. Do not invent
numeric confidence for a deterministic method.

Keep source-valid, label-valid and scored support distinct. Invalid is not dry. Preserve units/band order,
grid/CRS/affine and categorical labels. Fit preprocessing/threshold/calibration only on their declared
training/development roles. Related events/overlaps stay together. Final-test data must not influence model selection.
Review reserved results only once the protocol/candidates are frozen at C4; disclose contamination/corrections instead
of claiming a fresh untouched test. Ship the method supported by evidence, including a baseline that wins. Do not claim
transfer before the second task has its own independent evaluation.

CI begins at C0 and checks meaningful invariants progressively. Full training/data downloads/final-test tuning never
belong in routine CI. A local reproducible prototype is not hosted, deployed or commercially useful by association.
Record actual hours and reserve use; do not silently enlarge the 300–425 h route.

## Session handoff

Record actual hours only when supplied by the maintainer. Keep observed checks, learning status, decisions, limitations,
blockers and the next single action distinct. Preserve failed checks and scientific negative findings; do not invent
tests, human decisions, hours, costs or understanding claims.

End a session with a saved artifact or a precise blocker, observed checks, what was learned, next single action, updates
to `docs/progress.md` and `docs/floodlens/STATE.md`, and the real ticket status. A ticket is not Done until technical
acceptance and the agreed learning check are evidenced; only the user can provide the human-understanding claim.

## Roles

Use `$floodlens-guide`, `$floodlens-tutor`, `$floodlens-engineer`, or `$floodlens-reviewer`. Their custom subagent
profiles are named `floodlens_guide`, `floodlens_tutor`, `floodlens_engineer`, `floodlens_reviewer`. Main conversations
can invoke the skills without spawning. Profiles inherit the parent model/permissions/MCP; these instructions do not
create separate sandboxes. See `docs/ai/ROLES.md` for responsibilities and `docs/ai/JIRA.md` before ticket writes.
