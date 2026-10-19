# Scope and claim boundaries

FloodLens is a personal applied-system prototype. It estimates **observed water** from supported satellite imagery, evaluates unfamiliar-event performance, produces traceable geographic outputs and tests a bounded analyst inspection workflow. It is one component that a larger government or enterprise recovery system could integrate with assets and field reports.

## Two hypotheses to test

1. Does a compact segmenter improve the declared event-aware water task over a simple baseline, under matched masks and metrics?
2. Does the delivered workflow improve a realistic historical inspection brief compared with manual scene review, without hiding quality errors?

Either can yield a negative result. A strong engineering case study records that outcome and selects the supported method/capability; it does not invent improvement to justify the project.

## Required route and limits

| Area | Required bounded work | Limit |
|---|---|---|
| Data | One primary source, explicit rights, manifests/hashes, raster audit and exclusions | Approved subset first; every later admitted asset passes the same gate |
| Evaluation | Whole-event/group protocol, leakage checks, common metric rules | Few events limit claims; no random-neighbour split for unseen-event claims |
| Modelling | One simple baseline, one compact U-Net family, bounded search, one ablation | Larger models, weak labels and ensembles are optional extensions |
| Reliability | Locked per-event results, errors, confidence assessment and coverage | Raw probability is not automatically calibrated uncertainty or shift detection |
| Inference | One supported scene/batch contract, shared preprocessing, georeferenced output/report | Trusted artifacts and local approved IDs; bounded resources |
| Applied example | One small road corridor or study area, permitted or labelled synthetic geometry | Overlap means candidate inspection, not damage/closure/safe routing |
| Transfer | One different labelled land-cover task with its own independent evaluation | Reused machinery does not imply reused weights or universal science |
| Service | Local single-user API, limited worker, durable state and failure/restart paths | No accounts, billing or multi-tenant platform |
| Workspace | Two connected journeys, aligned map/comparison/reliability/provenance/notes/export | No general GIS editor or unlimited ingestion |
| Decision value | Fixed manual-versus-assisted task packets and quality/time/reproduction rubric | Small portfolio study; no assumed business/incident outcome |
| Release | Clean local reproduction, evidence-led demo/case study and limitations | Public hosting/publishing not required for completion |

[Note 09](09-product-definition.md) defines the applied walkthrough and workflow study. [Note 19](../checkpoints/README.md) defines ordered tasks; [note 13](13-engineering-milestones.md) owns hours.

## Water, change and consequence

**Observed water:** water at acquisition time, potentially including permanent water. This is the first target.

**Before/after inundation change:** newly present water relative to a defensible prior state. It requires comparable aligned dates, independent temporal labels and error evaluation. Subtracting two imperfect water masks creates a candidate change estimate; it does not validate it. This is a later separately estimated capability.

**Future flood forecasting:** prediction before an event with issue-time inputs and a different target. It is outside this route.

**Damage, displacement, cost or ecological impact:** consequences need independent asset, field, population/economic or ecological evidence and accountable interpretation. Water overlap alone proves none of them. FloodLens does not recommend emergency actions or replace official situation assessment.

## Hours and intermediate stopping points

C0–C6 planned work is 160–225 h plus 20–35 contingency = **180–260 h**. C7–C9 adds 105–150 work +15 contingency = **120–165 h**. Full route = **300–425 h**. First C0–C2 review = **40–55 h** before contingency; setup is a separate 3–5 h within that total. “400+” refers to the upper end of the route, not an additional commitment.

Stop/review meaningfully at C2 (audited data and baseline/protocol), C5 (reproducible applied slice), C6 (core with transfer outcome) or C9 (full local product). A rejection/feasibility result is useful but cannot be renamed a passed capability. Product work can follow a documented transfer feasibility stop only with an explicit decision and narrowed final claim.

## Scope reduction and extension rules

Cut decorative UI polish, extra experiment variants and optional models first. Narrow input formats, geographic scope, trial counts or asset coverage rather than weaken rights, masks, independent evaluation, geographic correctness or provenance. Keep the bounded decision-value test; shorten its packets transparently if necessary, without changing success criteria after seeing results.

Do not spend contingency on new features. Record each change in note 08 and repository decisions with evidence, budget effect, claim effect and review trigger. Paired change analysis, sensor fusion, continuous monitoring, extensive external validation, professional user studies and operational hosting need separate estimates. No agent assistant, distributed training or generic platform framework is required.

This revision adds the **workflow evidence** needed to show more than a map; it does not expand FloodLens into a recovery decision authority. No recommendation to change the initial scientific target is supported by the current metadata alone.

## Teaching revision: engineering quality begins in C0

Configured CI and verified local-equivalent checks are part of setup, with remote-run/enforcement state recorded separately. Progressive CI/CD is a foundation for the existing route, not a new enterprise-platform track. Note 19 supplies concrete libraries, APIs, function responsibilities, worked checks and repetition exercises; it does not supply application code or perform implementation. Use existing contingency transparently if learning CI/packaging takes longer than guided setup estimates.
