# Transferable engineering with domain-specific scientific judgement

## Intended professional signal

“I can take unfamiliar observational data, formulate a measurable question, build and evaluate a model, explain its limits, and deliver a reproducible system.”

That is the capability this project is designed to demonstrate. FloodLens is the first case study. The plan demonstrates breadth through a flood-analysis case study followed by one bounded land-cover experiment. The same analytical discipline can support unfamiliar domains, while each application needs its own target and evidence.

## Reuse the right layers

| Layer | What can reasonably transfer | What must be reconsidered |
|---|---|---|
| Source acquisition | Retries, manifests, checksums, caching, provenance | Provider access, licence, schema, update cadence |
| Spatial data handling | Raster windows, CRS/transform checks, nodata masks, overlap checks | Sensor units, resolution, resampling, registration accuracy |
| Experiment machinery | Configuration, tracking, artifact storage, repeatable execution | Target, label semantics, loss, sampling and split unit |
| Evaluation framework | Event/group scoring, report generation, matched comparisons | Meaningful metrics, error costs and acceptable evidence |
| Model execution | Training/inference interfaces and package conventions | Architecture, bands, weights, classes and calibration |
| Application | Version reporting, validation, bounded jobs, output inspection | User question, output meaning and actionability |

Use a small explicit observation/task contract. A scene record carries acquisition interval, footprint, CRS, grid transform, asset/band identity, units, source hash, quality masks and rights information. A task configuration specifies label meaning, valid pixels, grouping/splits and metrics. The model bundle declares the task and input schema it accepts.

[STAC](https://stacspec.org/en/about/stac-spec/) provides established concepts for spatiotemporal assets, collections and metadata. Use compatible metadata conventions where helpful; a local manifest is enough initially. A generic catalogue does not standardise scientific meaning across sensors.

Build one working flood workflow first. Extract shared components when the second application reveals actual commonality. Do not spend the early milestones designing a universal plugin platform.

## Concrete applications to explain in interviews

| Application | Related technical capability | New evidence required |
|---|---|---|
| Wetland monitoring | Water segmentation, spatial alignment, seasonal comparison | Wetland-specific reference labels; vegetation/seasonal effects; no automatic habitat-health claim |
| Land-cover mapping | Raster training, spatial holdout, class metrics and map outputs | Different class taxonomy and possibly optical bands; independently labelled test areas |
| Agricultural monitoring | Temporal/spatial ingestion and change summaries | Crop calendars, ground observations and a valid stress/yield target |
| Infrastructure resilience to floods | Map overlays, provenance and uncertainty reporting | Reliable asset geometry and locally validated exposure interpretation; no inference of actual damage from overlap alone |

These are possible uses of the engineering methods. Only an implemented and independently evaluated second case study establishes practical transfer evidence. A change of industry label on the same demo does not.

## What does not transfer automatically

Radar backscatter and optical reflectance have different meanings. Water/non-water and land-cover classes require different labels. A model calibrated on one event distribution may become overconfident elsewhere. Performance thresholds reflect the user and error costs; a threshold suitable for one study is not universal. Pretrained weights may help only after sensor compatibility, training provenance and contamination are checked.

[Koh et al. (2021), WILDS](https://proceedings.mlr.press/v139/koh21a.html) demonstrates the importance of testing distribution shifts across real datasets. Here it motivates separate validation, not an assertion that a reusable pipeline produces a transferable model.

## The portfolio story

Start with a concrete flood-analysis question and show the data constraints that shaped the implementation. Present the baseline, learned model, event-held-out results and failure cases. Then show the second small application, identifying which components stayed unchanged, which were configured differently and which were rebuilt. Record adaptation time and tests reused; avoid treating lines of code reused as the sole measure of design quality.

That narrative exposes engineering judgement across contexts. It also gives a reviewer several finished artifacts before the entire roadmap is complete.

Related: [13-engineering-milestones](13-engineering-milestones.md) · 01-personal-goals-and-skills (private/source-manual context; not required by this kit)

## The upstream/downstream boundary

FloodLens could sit below an enterprise recovery workflow by exporting a timestamped raster plus validity, uncertainty status, model/source/run IDs and a readable/structured report. The integrating system owns asset inventories, prioritisation rules, field-report reconciliation and operational decisions. C5/C8 demonstrate the integration boundary with one bounded asset type; they do not build the whole organisation’s workflow. Measure adaptation effort and task usefulness rather than claiming benefit from a reusable interface alone.

## Reusable process learned through implementation

The transferable foundation is a clean package/environment and CI; immutable source/validation records; independent evaluation; small responsibility-focused functions; versioned artifacts; portable outputs; explicit jobs/errors; connected user journeys; and a quality-constrained usefulness test. Note 19 teaches each with concrete library operations and a small repetition exercise. Reuse the pattern and explain its assumptions before carrying code into another domain. A future project will still need different data semantics and evidence.
