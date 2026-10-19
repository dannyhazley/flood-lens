# Dataset alternatives and extensions

**Choose a dataset for a defined task.** More scenes, a permissive code licence or a polished repository do not establish usable labels, geographic independence or rights to redistribute the data.

| Candidate | Intended role | Evidence currently available | Decision |
|---|---|---|---|
| [Sen1Floods11](https://github.com/cloudtostreet/Sen1Floods11) | Primary water-segmentation candidate | Original metadata, manual-label inventory and splits audited; imagery not inspected | Proceed only after the gates in [02](02-dataset-research.md) |
| [S1GFloods](https://github.com/Tamer-Saleh/S1GFlood-Detection) | Possible paired flood-change extension | Authors report 5,360 pairs from 46 events; README states research/non-commercial terms | Audit representation, event IDs, georeferencing and terms before selecting |
| [Tian's Sentinel-1/HAND samples](https://www.hydroshare.org/resource/fb2fb1e511f7456c8379912db441845a/) | Feature-based water-classification alternative | Explicit CC BY statement and tabular pixel samples | Could support a narrower classifier; not a substitute for spatial segmentation imagery |
| Small land-cover segmentation dataset | Checkpoint 6 transfer experiment | Dataset not selected or validated | Apply the selection checklist below within a five-hour research cap |

S1GFloods predicts a different target from a single-date water mask. Its repository badge does not override the data-specific terms in its README. Download access and patch structure have not been validated here; do not treat image-file channels as calibrated radar bands without inspecting their construction.

## Fallback order

1. Resolve Sen1Floods11 access, rights and spatial integrity for the bounded water task.
2. If a gate fails, spend a bounded part of checkpoint 1 comparing a replacement with equivalent task semantics and independent groups.
3. If only tabular samples are practical, explicitly revise the scope, model and demonstration to pixel classification. Record the lost spatial capability.
4. If no source fits the budget, finish the audit and stop before training. A rejection report is useful evidence, but it is not a completed segmentation model.

Do not quietly switch to paired change detection merely because a dataset is available; it introduces alignment, temporal provenance and different labels.

## Selection checklist for the transfer task

Require explicit usable terms, downloadable assets, documented label taxonomy, recoverable spatial groups, a manageable local subset and an independent reference target. Prefer labels that genuinely differ from water/non-water and geography that supports a defensible spatial holdout. Reject label maps derived from the same model being evaluated.

Inspect the data before committing to a neural architecture. A scene-classification dataset does not satisfy a segmentation demonstration without changing the task. Labels on a different grid require a documented alignment decision; merely resizing arrays is insufficient.

The five-hour source-selection cap is included in checkpoint 6's 35–45 hours. At the cap, select a defensible source or record the feasibility result. Avoid an open-ended dataset hunt or several half-finished transfer studies.

## Preserved comparative research

The broader agency/data survey remains in the initial alternatives review (private/source-manual context; not required by this kit). The original DONKI audit (private/source-manual context; not required by this kit) and RiverWatch recommendation (private/source-manual context; not required by this kit) explain the earlier shortlist; they do not define current implementation work.

Related: [05-project-scope](05-project-scope.md) · [07-transferable-engineering](07-transferable-engineering.md) · 15-risks-and-open-questions (private/source-manual context; not required by this kit)

## Keep source selection tied to the applied question

The second task tests reuse of data/experiment/output machinery; it does not add damage estimation to FloodLens. The proposed C5 road overlay is a **separate vector-context source**, not training truth. Choose one permitted small source or labelled synthetic geometry and record its date/CRS/terms. Synthetic roads can prove integration but cannot prove real exposure or decision value for an actual community. Do not make selecting several asset datasets a new research track.
