# Technology choices and when to introduce them

**Use Python for the analysis, portable geospatial files for the result, and familiar web tools only once the analysis works.** This is a proposed stack, not an installed or compatibility-tested environment. Choose compatible versions at each checkpoint, lock the working combination and record the hardware/OS. “Latest” documentation is a reference, not a verified version matrix.

A technology earns its place by solving the current checkpoint's problem. First explain the task without naming the tool: “I need the exported pixels to stay at the same coordinates,” then use Rasterio; “I need a job to remain identifiable after refresh,” then add a persisted job store. The [glossary](22-concepts-and-glossary.md) explains the underlying concepts.

## The default sequence

| Introduce | Technology / format | Meaning, problem solved and small example | Why now; why not earlier? |
|---|---|---|---|
| **Checkpoint 0** | Git, Python, `pyproject.toml`, uv and lockfile | Git records code history; the environment specifies what runs it. A fresh shell can execute the same small package command | Reproduction starts before scientific work. Add only a minimal environment; model/browser packages would create unrelated setup failures now |
| **Checkpoint 0–1** | pytest and a small formatter/linter setup | Automated checks exercise meaningful rules: a tiny wrong-grid fixture must fail. Formatting keeps code review readable | Establish one working check first, then scientific fixtures as their rules exist. No need for a large testing framework before behaviour is defined |
| **Checkpoint 1** | NumPy and Rasterio/GDAL | NumPy handles numerical grids; Rasterio exposes their geography, bands and masks. Read one image/label pair and compare geographic transforms | A normal image loader may lose units, nodata and coordinates. These tools are needed at the first raster audit, after source use is approved |
| **Checkpoint 1–2** | JSON/CSV manifests, Python tables and Matplotlib | Small records preserve asset/event identities; saved plots explain validity, bands and class balance | Inspectable files suffice for a small experiment. A database, warehouse or tracking server adds no necessary value yet |
| **Checkpoint 2** | Otsu routine from scikit-image, or a small verified implementation | A histogram threshold gives a cheap reference method. Save the band, valid-pixel histogram and class-direction rule | The model needs a fair baseline. Do not introduce a neural stack before labels, splits and masks are understood |
| **Checkpoint 3** | PyTorch and one compact U-Net implementation | Tensors, automatic gradients and saved parameters support training a spatial predictor. First fit a tiny training subset | Only after an accepted task, split and baseline exist. The aim is to test learned context, not adopt a large framework ecosystem |
| **Checkpoint 3–4** | Versioned configuration and local run manifests | A run ties parameters and figures to data/split/code versions. A simple table compares all declared trials | The bounded search does not initially need an MLflow server; local records prevent notebook state becoming the only provenance |
| **Checkpoint 5** | GeoTIFF, JSON and HTML/Markdown reports | GeoTIFF carries scientific arrays with spatial metadata; JSON carries machine-readable lineage; the report explains the result | Portable output is required before a product interface. PNG is an additional preview, never the geographic deliverable |
| **Checkpoint 5** | QGIS; GeoPandas/Shapely only where programmatic vector operations are needed | QGIS independently opens rasters/roads; vector tools can check geometry and intersections. A tiny road corridor tests integration | The first analyst overlay needs a geographic check. Use one asset type and simple rules; no general GIS editor or spatial database is needed |
| **Checkpoint 7** | FastAPI with typed request/response validation | An API is a documented way for another program to request work. Submit scene/method IDs and return a stable job ID | Wrap the already tested package. An API before checkpoint 5 would make data/model debugging depend on networking |
| **Checkpoint 7** | SQLite plus one bounded local worker | SQLite stores job state and references; the worker executes the package outside the request. Refresh sees the same queued/running/result state | Persistent jobs become necessary with the connected workflow. Keep rasters as files; a distributed queue is not justified by a local single-user demonstration |
| **Checkpoint 8** | React, TypeScript and Vite | Components render views; types help keep client contracts explicit; Vite runs/builds the web interface. A result card reads actual API data | Danny already has related React/Vite experience. Build the UI after real result and service contracts exist; a type annotation does not replace runtime/API validation |
| **Checkpoint 8** | MapLibre GL JS and pregenerated display layers first | The map lets users inspect geographic layers, legends and asset context. Use one aligned result/road overlay | It solves spatial exploration once results exist. Benchmark small display products before adding a tile service |
| **Checkpoint 8–9** | Playwright plus manual keyboard/clarity checks | Browser tests cover selection → job → map → export and failure recovery; manual review catches confusing language and map interaction | Complete journeys must exist first. Automated browser success alone does not establish accessibility or analyst usefulness |
| **Checkpoint 9** | Clean local installation and a versioned release bundle | Another environment reconstructs the demonstrated result and report from the recorded instructions | This turns working local code into reproducible evidence. A public host remains optional and needs its own tested boundary |

## Deliberately optional choices

| Optional tool / capability | Introduce only if this observed problem appears | Cost or mistake to avoid |
|---|---|---|
| scikit-learn feature classifier | One declared experiment needs to distinguish per-pixel information from spatial modelling | An extra model family consumes evaluation time; it is not compulsory breadth |
| Parquet | Manifest/table size or typed-column work makes CSV awkward | Do not make a small audit harder to inspect for imagined scale |
| MLflow | Local run files become difficult to compare or artifacts are being misplaced | A tracker does not define a valid split or record decisions automatically; no tracking server is required for the core |
| COG | Measured display or range-access needs justify a tiled/overview layout | Validate the file and preserve scientific masks; avoid lossy compression of classes/probabilities |
| TiTiler | Pregenerated layers cannot serve the measured viewport/workload within budget | Adds a service and deployment dependency; its existence does not make arbitrary remote data safe or compatible |
| Container | A clean second environment exposes dependency differences that a container usefully controls | Still need data/model hashes, hardware notes and commands; containers do not guarantee identical neural results |
| Hosted demo | A public reviewer needs remote access and the measured cost/data terms fit | A hosted page is not proof of operational deployment or adoption; local completion remains valid |

Do not introduce accounts, billing, Kubernetes, distributed training, an agent assistant, a vector-search service or a multi-tenant platform in this route. There is no current applied question requiring them. Revisit only through a recorded scope decision, not an incidental package suggestion.

## The checks attached to each choice

**Environment:** use a fresh shell and a clean locked install. Record Python and package versions, OS and hardware. Do not copy an example documentation version without checking compatibility with Rasterio and the eventual acceleration backend. If installation fails, isolate the smallest package/import failure instead of changing several dependencies at once.

**Numerical/geospatial tools:** verify one value, one valid/invalid pixel and one known coordinate by hand. Rasterio valid masks and NumPy masked-array masks use opposite boolean meanings; perform the conversion explicitly. Keep scientific resampling and display stretching separate. A GIS viewer is an independent check on placement, not proof the classifications are correct.

**Model tools:** save training and inference preprocessing together. Record deterministic settings and their limits: the [PyTorch reproducibility note](https://docs.pytorch.org/docs/stable/notes/randomness.html) is the reference for seeds, determinism and cross-platform limitations. Measure a short run before promising a model-search budget. Keep training time separate from active working hours.

**Service tools:** one accepted HTTP request is not a finished job. Persist requests, use a bounded worker, reconcile interrupted jobs and publish only complete output bundles. SQLite is appropriate for this local metadata role; keep its active database on local storage with short transactions, and do not mistake synchronising its file through iCloud for multi-user operation. See [SQLite's usage guidance](https://www.sqlite.org/whentouse.html) for the local-store/concurrency boundary.

**Map tools:** verify coordinates after display reprojection, keep masks visible, and retain attribution. MapLibre supplies map rendering, not unrestricted basemap rights or unlimited tile capacity. Select a permitted basemap or an offline/no-basemap fallback deliberately. The export must work without the chosen basemap provider.

## Selective official documentation: read for a task

The following pages were checked on 16 October 2026. Read the indicated part when its checkpoint arrives; no dependency installation or data download was performed during this review.

| Read at | Primary documentation | Use it for |
|---|---|---|
| 0 | [uv project guide](https://docs.astral.sh/uv/guides/projects/) | Understand `pyproject.toml`, environment, lockfile and running the package; reproduce a minimal project, not every example dependency |
| 0–1 | [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | Make small repeatable test inputs, including a deliberately malformed raster |
| 1 | [Rasterio masks](https://rasterio.readthedocs.io/en/stable/topics/masks.html) and [reprojection](https://rasterio.readthedocs.io/en/stable/topics/reproject.html) | Learn valid/invalid conventions and explicit source/destination grids before implementing those checks |
| 2 | [scikit-image thresholding](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_thresholding.html) | Understand the histogram/threshold operation; decide water direction and masks for radar separately |
| 3 | [PyTorch reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) | Record seeded/deterministic options and realistic reproduction limits |
| 5 | [QGIS interface guide](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/qgis_gui.html) | Load and inspect independent geographic layers for round-trip QA and the manual comparison task |
| 5 | [GeoPandas overlay operations](https://docs.geopandas.org/en/stable/docs/user_guide/set_operations.html) | Understand vector intersection and CRS considerations if an automated asset operation is required |
| 7 | [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | Distinguish simple response-following work from heavy computation and the durable worker contract in note 10 |
| 7 | [SQLite appropriate uses](https://www.sqlite.org/whentouse.html) | Understand why a local job store is enough and when concurrency/network storage changes the decision |
| 8 | [Thinking in React](https://react.dev/learn/thinking-in-react), [TypeScript everyday types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html), [Vite guide](https://vite.dev/guide/) | Break the agreed screens into components, express client data shapes and create a minimal working build |
| 8 | [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/) | Learn sources/layers and build the first real geographic overlay |
| 8–9 | [Playwright getting started](https://playwright.dev/docs/intro) | Run one actual user journey and failure case in a browser |
| Only if justified | [GDAL COG driver](https://gdal.org/en/stable/drivers/raster/cog.html), [TiTiler](https://developmentseed.org/titiler/) | Evaluate output layout/tiling after the small performance spike; neither is an early prerequisite |

Dataset papers and scientific methods are covered in [04-literature-review](04-literature-review.md) and 16-references (private/source-manual context; not required by this kit). Do not treat engineering documentation as evidence of FloodLens accuracy.

## Cost and performance decisions

Record actual machine memory/storage, loader throughput, batch size, inference time, training duration and peak memory. A short representative run informs the next experiment; an unmeasured estimate is not a latency claim. The route assumes no paid compute or always-on host. If optional hosting is later chosen, measure supported file size, concurrency, output retention and tile traffic before selecting a provider and budget.

At a checkpoint ceiling, reduce optional tools and presentation polish before weakening masks, splits, provenance or geographic checks. An unfamiliar installation problem can be a genuine blocker; a preference for another framework is not. Capture the exact error, environment, last working revision and smallest reproduction for a focused future session.

Related: [10-system-architecture](10-system-architecture.md) · [13-engineering-milestones](13-engineering-milestones.md) · [18-start-here](../START.md) · [19-checkpoint-playbook](../checkpoints/README.md)

## Teaching-level defaults and API map

[Note 19 now contains a build guide inside every checkpoint](../checkpoints/README.md). Use those guides for the sequence and expected outputs. The map below tells you which tools to reach for without forcing you to invent a stack midway through a lesson. Retain a coherent existing choice where the actual repository already has one; record substitutions and verify the same contract.

| Checkpoint | Default tools | Core operations you should be able to explain |
|---|---|---|
| C0 | uv, a declared Python build backend, pytest, Ruff, GitHub Actions | Locked install/run/build; installed command/version; temporary test fixtures; lint/format; clean-run CI and wheel-install smoke check |
| C1 | pathlib/hashlib/json/csv, HTTPX when retrieval is needed, Rasterio, NumPy, Matplotlib | Hash bytes; bounded streaming; read metadata/bands/masks; construct source/label/scoring masks; validate grids; save annotated audit panels |
| C2 | NumPy, scikit-image; scikit-learn only where used | `threshold_otsu`; fixed group assignment/integrity checks; confusion counts; event versus pooled summaries |
| C3 | PyTorch and the existing data tools | Dataset/DataLoader; Conv2d/pooling/upsampling; masked BCEWithLogitsLoss; Adam/zero_grad/backward/step; eval/inference_mode; state_dict/reload |
| C4 | NumPy, scikit-learn calibration/metrics, Matplotlib | Brier calculation, reliability bins/counts, retained-coverage/error tables, fixed per-event report |
| C5 | argparse, Rasterio, GeoPandas/Shapely as needed, standard logging | One bounded command; write/reopen GeoTIFF; window transforms; coordinate conversion; candidate intersections; structured stage logs and finalisation |
| C6 | Same tools plus source-specific adapter; CrossEntropyLoss for exclusive multiclass | New bands/classes/dtypes; K-channel output; own independent split/confusion/IoUs; fresh task-specific parameters |
| C7 | FastAPI, Pydantic, sqlite3, HTTPX/TestClient, one worker | Input/status/result schemas; transactional queue/claim; parameterised SQL; persisted failure/restart/retry; actual pipeline call |
| C8 | React/TypeScript/Vite, npm lock, ESLint, MapLibre, Playwright; Vitest/Testing Library if needed | State/effect cleanup, fetch/abort, sources/layers/bounds, comparison eligibility, download checks, clean production build |
| C9 | Existing build/test/report tools | Isolated reproduction, paired task records/quality rubric, candidate artifact/checksums; separately chosen hosting/rollback |

**CI is introduced at C0**, not left until hardening. Add scientific fixtures as their behaviours exist, tiny CPU model checks at C3, export checks at C5, service checks at C7 and browser checks at C8. Full training, paid compute, real-data acquisition and test-set-driven model promotion remain outside routine CI. The C9 delivery candidate should be a reproducible artifact before any publication/deployment step.

**Logging:** introduce Python `logging.getLogger` and structured records at C5/C7. Record run ID, stage, input/model/config IDs, elapsed time, warnings and stable failure reason; avoid dumping arrays/secrets or unrestricted local paths. The outcome is a diagnosable failure, not a dashboard of impressive but unused metrics.

**Quality checks should earn their place:** track whether masks, groups, shapes, artifact reloads, coordinates, state and exports remain correct. A test-count/coverage target alone does not demonstrate correctness. Static type checking can be added to stable package contracts at C5 if it helps; it cannot prove the meaning of units or spatial alignment.
