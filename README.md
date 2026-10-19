---
owner: "danny hazley"
status: "active dev"
checkpoint: "c0"
---

# Flood Lens: Applied Machine Learning

FloodLens is a personal learning project exploring how satellite imagery can be turned into traceable water maps and
used alongside geographic information such as roads and land cover.

The goal is to understand and build a complete applied machine-learning workflow: inspect data, compare methods,
evaluate unfamiliar events, produce geographic outputs, and develop a usable local application.

**Status:** Planning and setup. Models, results and application features described below are planned.

## Run locally

With Python 3.13 and [uv](https://docs.astral.sh/uv/) installed, sync the locked development environment and run the
current package smoke command from the repository root:

```sh
uv sync --locked --all-groups
uv run --locked flood-lens
```

The current command prints `Hello from flood-lens!`. It confirms the installed package entry point runs; it does not
perform flood mapping.

## Data

The intended primary dataset is [Sen1Floods11](https://github.com/cloudtostreet/Sen1Floods11), which provides Sentinel-1
radar imagery and reference water labels from historical flood events.

The initial task is to identify **observed water at the time of acquisition**, including permanent water.

Data work will include:

- Recording source versions, checksums and provenance.
- Checking radar bands, units, geographic alignment and missing pixels.
- Separating complete events for training, development and evaluation.
- Preserving original files and documenting verified technical repairs.
- Flagging ambiguous labels while retaining supplied annotations initially.

Original project code will use the MIT licence. Dataset materials retain their applicable terms and attribution
requirements. MIT or CC BY 4.0 is currently a working assumption for the data, not a confirmed licence finding.

## Learning Areas

- Python packaging, dependency management, and CI/CD.
- Raster data, coordinate systems, validity masks and GIS integration.
- Simple water-detection baselines and compact segmentation models.
- PyTorch training, controlled experiments and model artifacts.
- Event-aware evaluation, leakage, error analysis and uncertainty.
- Reproducible geospatial inference and machine-readable exports.
- API contracts, background jobs, persistence and failure handling.
- Interactive maps and accessible analysis workflows.
- Adapting shared engineering components to a separate land-cover task.
- Using AI assistance transparently while understanding and reviewing the work.

## Limitations

FloodLens is a learning prototype, not an operational emergency-response service.

- Observed water does not necessarily represent newly flooded land.
- Outputs do not establish building damage, road safety, displacement or repair costs.
- Flood forecasting is outside the initial scope.
- Limited event coverage and imperfect labels constrain evaluation.
- Model confidence can be misleading, particularly on unfamiliar conditions.
- Geographic outputs require checking and human interpretation.

Results will be reported with their scope and limitations. Modest performance, negative findings and a baseline
outperforming the neural model are valid outcomes.

## Expected Outcomes

- An understandable, locally reproducible applied-ML prototype.
- A documented dataset audit and event-based evaluation.
- A fair comparison between a simple baseline and a compact neural model.
- Georeferenced water layers with validity information and provenance.
- A local service and interactive inspection/export workflow.
- A bounded experiment exploring reuse on another task.
- A learning record covering decisions, failures, AI assistance and reusable engineering patterns.

## Use of AI

- Provider: Open AI | Codex
- All agents are available in `.github`
