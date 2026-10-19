# FloodLens — data audit and evaluation contract

## What was directly checked on 12 October 2026

Read-only requests inspected the original Sen1Floods11 v1.1 bucket, STAC collections, event metadata, manual-label listing and supplied split manifests. No imagery was downloaded and no model was trained. URLs, hashes and retrieval times are saved in audit.json (saved private audit; not bundled) and collection-and-splits-audit.json (saved private audit; not bundled).

| Check | Observed result | Implication |
|---|---|---|
| Manual labels | 446 files in eleven filename event groups | Small independent event sample despite many pixels |
| Supplied train / validation / test | 252 / 89 / 90 entries, each spanning the same ten event names | These manifests do not establish complete event holdout |
| Bolivia split | 15 entries, separate from those three files | A supplied unseen-location case, but only one event |
| Event GeoJSON | 12 features, including Colombia | Metadata row count is not the number of manually labelled events |
| Naming | Files use `Mekong`; metadata includes Cambodia | Explicit mapping is needed; do not join on guessed names |
| Hand-labelled source and label collections | Both declare `license: proprietary` with no licence link | Original archive metadata does not verify an unrestricted open annotation licence |

Direct sources: [catalogue](https://storage.googleapis.com/sen1floods11/v1.1/catalog/catalog.json), [label collection](https://storage.googleapis.com/sen1floods11/v1.1/catalog/sen1floods11_hand_labeled_label/collection.json), [event metadata](https://storage.googleapis.com/sen1floods11/v1.1/Sen1Floods11_Metadata.geojson), [train manifest](https://storage.googleapis.com/sen1floods11/v1.1/splits/flood_handlabeled/flood_train_data.csv), [test manifest](https://storage.googleapis.com/sen1floods11/v1.1/splits/flood_handlabeled/flood_test_data.csv).

The collection licence value could be a metadata default; it does not by itself prove that research use is forbidden. Conversely, a third-party mirror's CC BY label does not resolve the original rights. Record definitive provider terms or select a better-documented alternative before committing to a publishable data/model release. No permission email has been sent.

## Dataset routes

**Sen1Floods11: candidate for water segmentation.** The [author documentation](https://github.com/cloudtostreet/Sen1Floods11/blob/master/docs/README.md) provides manual/weak labels, radar imagery and reference permanent-water layers. It remains scientifically useful if the rights issue is resolved. Invalid pixels must be masked. Weak labels must not become independent evaluation truth.

**S1GFloods: candidate for paired flood-change modelling.** The [authors' repository](https://github.com/Tamer-Saleh/S1GFlood-Detection) reports 5,360 before/after image pairs from 46 events in 2015–2022. Its README explicitly restricts dataset use to non-commercial/research purposes, despite a CC0 repository badge. The available patch representation, source sensor channels, georeferencing, independent event IDs and download terms still need inspection. Do not interpret PNG channels as calibrated radar bands. This is a promising alternative, not a fully audited replacement.

**Not a drop-in substitute:** [Tian's 2025 Sentinel-1/HAND samples](https://www.hydroshare.org/resource/fb2fb1e511f7456c8379912db441845a/) carry an explicit CC BY statement but are pixel-level tabular samples. They could support a feature-based classifier experiment; they do not automatically preserve the spatial imagery required for convolutional segmentation.

Select one primary dataset first. Keep dataset-specific models and label definitions separate; a water mask and a newly flooded-area mask are different targets.

## Two evaluation tracks

1. **Reproduction:** use published splits and report their exact meaning. Run this track after the main held-out-event protocol and final results are locked, since its training set may contain primary final-test events. Keep its artifacts and conclusions separate.
2. **Generalisation:** freeze event-grouped train/development/final-test partitions before tuning. All tiles, overlapping footprints, acquisition siblings and weak labels associated with a held-out event stay out of training. If paired datasets share events, cross-dataset overlap also needs checking.

For eleven labelled events, a proposed starting design is seven training, two development and two final-test events, subject to class/coverage audit. Use training-event folds for early model choices if resources allow. The final two events are not sufficient to claim global reliability. Additional leave-one-event-out experiments are a separate robustness study; they do not remain an untouched test if their results influence tuning.

Choose event IDs before examining model scores. Geography, orbit, landscape and event-level label counts can inform a documented split. Do not cherry-pick attractive test images.

## Models, measures and safeguards

- Compare a simple SAR threshold/Otsu method, a feature-based classifier where useful, and a compact U-Net on matched valid pixels.
- Fit normalisation, class weights and decision thresholds on training/development data only. Apply geometric augmentations jointly to image and mask. Never use interpolating resampling that turns categorical labels into fractional classes.
- Primary metric: macro-average water IoU across held-out events, with each event scored over its valid pixels. Also report per-event precision, recall, F1, pooled IoU and confusion counts. Define empty-water cases explicitly.
- Evaluate confidence using reliability/Brier measures and error-versus-retained-coverage curves on event-separated data. Softmax probability is not automatically trustworthy uncertainty. An ensemble is optional and adds compute.
- Bootstrap or compare at event/spatial-block level where evidence supports it; millions of correlated pixels do not justify tiny confidence intervals. With very few final events, report individual scores rather than implying precise global confidence.
- Inspect terrain shadow, urban areas, vegetation, boundaries and missing pixels. An uncertainty overlay does not guarantee out-of-distribution detection.

For change analysis, align pixel grids and acquisition geometry, preserve nodata, and validate new-inundation labels independently. A historical permanent-water map may itself incorporate later imagery: check its temporal provenance before making issue-time claims. Use a suitable projected/equal-area calculation for area summaries; geographic pixels are not a globally constant area.

## Checkpoint 1 completion gate

A usable dataset licence/use scope, verified labels and pairings, auditable event groups, recoverable georeferencing, a defensible event-grouping basis and affordable local compute plan. C2 then freezes the split before model selection. If one source fails, keep FloodLens and change the dataset/task scope. No blanket forecast, disaster-response or ecological-impact claim follows from a successful segmentation benchmark.

Related: [00-project-overview](../README.md) · [13-engineering-milestones](13-engineering-milestones.md)

## Imagery inspection protocol for checkpoint 1

The completed metadata audit does not establish that any raster opens correctly or that image and label grids agree. Inspect at least one chip from each event, then run collection-wide metadata/shape/mask checks on the selected assets. Expand visual inspection where those checks reveal anomalies. Preserve accepted and rejected records in a manifest rather than silently dropping inconvenient scenes.

| Field | Requirement |
|---|---|
| Scene identity | Stable asset ID, event ID, acquisition time, source URL and checksum |
| Input meaning | Verified band order, units, dtype, scaling and preprocessing history |
| Spatial identity | CRS, affine transform, bounds, dimensions and resolution |
| Label meaning | Provider definition, class codes, ignore value and annotation provenance |
| Validity | Separate source validity, label validity and any quality exclusions |
| Rights | Recorded terms for imagery, annotations, redistribution and derived artifacts |
| Split safety | Event mapping, duplicate/overlap checks and related acquisitions |

The candidate manual labels use invalid/non-water/water codes (-1/0/1); confirm values in the downloaded files before encoding them. Do not reinterpret invalid labels as dry land. Quantify valid-pixel and water prevalence by event, and investigate extremes. Fit any learned normalisation only after the split is frozen.

Collection summaries of counts and label coverage may inform a predeclared split before training. After assignment, reserve final-test imagery/results from model-directed exploratory work. Record any permitted initial inspection so the eventual test claim is transparent.

## Manual-label inventory from the audit

| Filename event | Chips |
|---|---:|
| Bolivia | 15 |
| Ghana | 53 |
| India | 68 |
| Mekong | 30 |
| Nigeria | 18 |
| Pakistan | 28 |
| Paraguay | 67 |
| Somalia | 26 |
| Spain | 30 |
| Sri-Lanka | 42 |
| USA | 69 |
| **Total** | **446** |

Counts come from the saved source listing audit, not a completed raster-level validation. Event identity, geography and flood episode must still be reconciled explicitly.

## Clarifications for the implementation manual — 16 October

Re-reading the saved label-collection JSON reveals **1,338 item links but only 446 unique item hrefs**, each repeated three times. Deduplicate stable asset/href identities before ingestion; catalogue-link counts are not independent labelled-scene counts. This is a local snapshot inspection, not a fresh remote licence audit. See the preserved label collection (saved private audit; not bundled).

C1 inspects an approved small event-diverse subset. Its report must distinguish **metadata inventory coverage** from **raster/pixel audit coverage**. C2 expands only to the approved experiment inventory and applies the same validation to every admitted asset before splitting/selection; no uninspected asset silently becomes accepted. If that inventory cannot fit the budget, narrow the study or revise the estimate explicitly. No data download is performed by this documentation task.

The author documentation describes VV/VH in decibels and candidate codes {-1,0,1}; verify the actual assets. A prose “10 m” resolution claim alongside a geographic CRS does not establish constant pixel area. Inspect the affine transform, coordinate units and latitude; use an appropriate projected/equal-area or geodesic area method for area summaries. No accepted geographic output exists yet.

Rights remain open: saved original licence fields are from 12 October, and author documentation consulted on 16 October did not establish a new definitive annotation grant. Do not equate accessible downloads with redistribution rights or overstate the meaning of a metadata default.
