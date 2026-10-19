# End-to-end system architecture

**Build one executable analysis package, then expose its stable behaviour through a local service and map workspace.** Every layer must preserve the meaning, geography and provenance of the water output. This is an implementation design, not evidence that any of these components exists.

The full path is: **approved observations → source manifests/checksums → raster validation and explicit alignment → eligible scenes and masks → event/group splits → baseline/neural experiments → frozen model artifact → inference contract → geographic outputs/report → bounded jobs/service → interactive analyst workspace → export and human review**. Asset geometry joins the output at the application boundary. A larger organisation could ingest the resulting layer and brief into its own recovery workflow; FloodLens does not own that wider decision system.

Read [22-concepts-and-glossary](22-concepts-and-glossary.md) for unfamiliar terms and [09-product-definition](09-product-definition.md) for what the analyst does with the result. Implement only the part required by the current checkpoint.

## Components, boundaries and evidence

| Component | Input → output | Why it exists / example | First checkpoint and failure rule |
|---|---|---|---|
| Source approval | Provider documentation → data card and intended-use decision | Prevents treating publicly reachable files as automatically redistributable | 1; unresolved necessary rights stop using that source for the intended activity |
| Acquisition manifest | Approved asset reference → local asset ID, checksum and retrieval record | A changed download can be detected instead of silently changing an experiment | 1; missing or mismatched bytes are quarantined, not accepted |
| Raster validator | Asset → bands/units/grid/mask/label report | Equal array dimensions do not prove two rasters cover the same ground | 1; unknown units or missing CRS produce explicit unsupported status |
| Alignment/preparation | Valid source grids → approved analysis grid and derived manifest | A documented reprojection may align different grids without losing source history | 1/2; keep originals; categorical labels cannot be smoothed into new classes |
| Dataset and group registry | Eligible scenes → task version and event/overlap groups | All tiles from an event follow the same experimental role | 2; cross-partition related scenes block the claimed held-out evaluation |
| Experiment runner | Train/development roles → baseline/model runs and selection report | Makes “is learning useful?” a matched comparison, not two unrelated screenshots | 2–4; selection never reads final-test scores |
| Model artifact | Frozen method/configuration → loadable method bundle and model card | A weight file alone does not identify preprocessing, units or threshold | 3/4; mismatched task/input schema fails before prediction |
| Inference package | Supported scene + method bundle → complete output bundle | The same numerical path serves CLI, API and batch processing | 5; no partial result can appear as successful |
| Context/asset adapter | One approved road layer + result → candidate review table | Adds an inspectable asset-overlap demonstration without inferring damage | 5; unknown CRS/date/source is flagged; no safe-road conclusion from non-overlap |
| Service/worker/store | Bounded request → persisted job and result references | A browser can submit work, refresh and learn why a job failed | 7; a response accepting a job is not a completed analysis |
| Map workspace/export | Metadata/tiles/reports → understandable local analysis and portable files | Users can inspect uncertainty, provenance and asset context before sharing a brief | 8/9; downloads preserve the scientific raster, not just screen colours |

## Proposed repository layout

These are future repository paths, not files created by this documentation task. Add directories when needed; avoid an empty framework on day one.

```text
floodlens/
  README.md                  # True status and verified reproduction instructions
  pyproject.toml             # Package/dependencies; lockfile beside it
  src/floodlens/
    data/                    # Manifests, validation, alignment, windows and masks
    tasks/                   # Explicit water/land-cover target contracts
    experiments/             # Group splits, baseline, training and evaluation
    inference/               # Artifact loading and shared analysis pipeline
    reports/                 # Metrics, figures, provenance and export
    context/                 # One bounded asset overlay, from checkpoint 5
    service/                 # API, job records and worker, from checkpoint 7
  configs/                   # Small versioned task/run configurations
  manifests/                 # Scene, derived-asset and split records; no secrets
  tests/fixtures/            # Synthetic or expressly redistributable small samples
  docs/
    progress.md              # Sessions, actual hours, concrete outputs and blockers
    checkpoints/             # C0.md–C9.md evidence and acceptance results
    decisions.md             # Recorded scientific and engineering tradeoffs
  web/                       # Browser workspace, from checkpoint 8
  data/                      # Ignored source cache and local prepared data
  artifacts/                 # Ignored model bundles and large outputs
  runs/                      # Ignored local run bundles and job database
```

The vault owns this manual and the cross-session state. The repository owns executable reproduction and technical records required to reproduce a release. Do not make the application depend on an absolute path into this personal vault. Keep the job database and active software outside the iCloud-synchronised vault; save exported reports/links in the vault instead of treating file sync as a database transaction system.

## Contracts: what each record must say

Start with small JSON/CSV records and explicit validation. A **contract** is the agreed meaning of fields and allowed behaviour: for example, `bands = [VV, VH]` is an ordered scientific input, not an arbitrary pair of image channels. Include a schema version so incompatible changes cannot be mistaken for old records. These are proposed field requirements to formalise during implementation.

| Record | Required fields / meaning |
|---|---|
| Source scene | `scene_id`, provider/source URI, retrieval time, SHA-256, byte size, acquisition interval, supplied event ID and reconciled group ID, footprint, CRS, affine transform, dimensions, band names/order, units, dtype, scale/offset, source preprocessing, masks, rights reference |
| Label asset | Source/label IDs and hashes, provider taxonomy, class/ignore codes, annotation method/date where available, label grid, validity, pairing evidence and use terms; “unknown” is recorded explicitly |
| Prepared asset | Parent source IDs/hashes, output hash, analysis grid, resampling per band/mask, transformations, tool/config/code versions and exclusions; source bytes remain immutable |
| Dataset/task | Eligible scene/label IDs, excluded IDs with reasons, class meanings, mask rules, event aliases, overlap-group rule, data card and version |
| Split | Dataset version, group → train/development/calibration/final assignments, reason for allocation, overlap-check report, freeze date/hash and permitted test access; calibration role is optional and must be real if used |
| Experiment | Code revision, dirty-worktree status, configuration hash, dataset/split IDs, method/seed, environment/device, training-only normalisation, trial purpose, metrics, time/memory and selection role |
| Model artifact | Method ID, task, architecture/weights or deterministic baseline parameters, trusted-file hashes, input units/order, preprocessing, output meaning, selected threshold, calibration status, training/selection lineage, supported limitations and model card |
| Analysis request | Request schema version, approved scene IDs, task/method artifact ID, declared processing options, output grid policy and optional approved asset-layer ID; user-supplied arbitrary URLs/files are outside the first service contract |
| Analysis run | Run/request ID, immutable requested configuration, input/artifact hashes, timestamps, device/environment, stage/state, warnings, error code, output-manifest reference and runtime |
| Asset context | Layer ID/hash, source/date/terms, geometry ID/type, CRS, study boundary, geometry validity and intersection rule; no implied real-world damage label |
| Output/report | Run/task/version, raster role/classes/units, grid/masks, input lineage, probability/calibration meaning, thresholds, geographic summaries, warnings, report/candidate-table paths and hashes |

Use [STAC's Item/Collection/Asset concepts](https://stacspec.org/en/about/stac-spec/) to understand scene metadata and linked assets; the implementation can remain a local manifest. The purpose is consistent identity and spatial/time metadata. A STAC server is not required, and a standard catalogue does not make different sensor measurements scientifically interchangeable.

Checksums identify bytes and detect change; they do not prove that a provider's metadata or labels are true. An acquisition date describes the observation, while a retrieval date describes when it was obtained. Preserve both so an old scene is not mistaken for a current situation.

## Raster grids and masks: the rules shared everywhere

1. **Validate before transforming.** Read dimensions, CRS, transform, bounds, pixel size, band units and nodata. Pair input and label using source identities, then compare their geographic grids. Two 512 × 512 arrays can cover different places. Inspect a footprint overlay and known coordinates as well as metadata.
2. **Choose one analysis grid.** Prefer the approved native input grid for the first task. If alignment is necessary, specify destination CRS/transform/resolution/shape and resampling. Record why the change is justified. Nearest-neighbour treatment preserves categorical label codes; imagery resampling needs a scientifically defensible choice. Reprojection can align coordinate grids but cannot automatically repair a physically misregistered sensor scene. See [Rasterio reprojection](https://rasterio.readthedocs.io/en/stable/topics/reproject.html) for source/destination transforms and the controlled operation.
3. **Keep three meanings separate.** `input_valid` means all required bands and quality rules permit inference. `label_valid` means a reference answer is usable. `evaluation_valid = input_valid AND label_valid` defines scored pixels. An unlabelled but observed pixel may receive a prediction; it cannot contribute an accuracy measurement.
4. **Keep uncertainty separate from missingness.** A `retained` or review mask indicates whether the frozen confidence policy accepts a prediction. It is not nodata. Preserve the full valid prediction plus the review/retention layer; report coverage and score the predeclared all-valid task as well as selective summaries. Never remove difficult pixels silently.
5. **Encode validity consistently.** Internally use an explicitly named boolean mask where `True` means usable. Convert at library boundaries: GDAL/Rasterio valid masks and NumPy masked-array masks have opposite boolean meanings. Check the conversion with a small fixture; [Rasterio's mask guide](https://rasterio.readthedocs.io/en/stable/topics/masks.html) explains this distinction.
6. **Apply shared transformations.** Training and inference call the same unit conversion/normalisation code. Fit learned values on training data only. Jointly transform imagery, labels and masks during augmentation. Specify padding and context treatment around invalid pixels so missing input cannot silently become a useful-looking zero-valued feature.
7. **Count each evaluated location deliberately.** Windowed inference needs a declared overlap/stitching policy, edge crop/padding and seam check. Do not score overlapping windows as independent duplicate pixels. Reject an all-invalid scene with an explicit unscorable/no-output reason.
8. **Calculate geography from geography.** Area/length summaries use a suitable local projected/equal-area or geodesic method with units and method recorded. Pixel counts multiplied by degree units or display-map metres are not a reliable area calculation. The raw water area and asset intersection are distinct outputs.

## Experiments and delivered inference are different operations

The split registry controls experiments: training fits parameters; development chooses; final test measures the frozen method once under the protocol in [11-machine-learning-design](11-machine-learning-design.md). The run registry controls execution: it records which method processed which scene, regardless of whether labels exist. A benchmark run may attach a separate evaluation report; normal inference must not invent one.

Freeze the selected artifact before checkpoint 4. The artifact may represent Otsu or another simple baseline, so the delivery interface cannot assume every method supplies neural probabilities. For a deterministic baseline, show its method, masks and known limitations; report probability uncertainty as unavailable. Do not turn distance from a threshold into calibrated probability without a separately evaluated method.

At checkpoint 6, reuse machinery through a new task contract with its own bands, class codes, groups, metrics and model. Reject loading a water artifact against a land-cover schema even if array shapes happen to match. Shared code is not a shared scientific result.

## The inference/output transaction

The proposed checkpoint 5 command accepts only documented input types and runs these stages in order:

1. Resolve approved scene and trusted method IDs; check hashes, schema, bands/units and resource bounds.
2. Validate the grid/masks; emit a structured validation record. Refuse unsupported inputs with a specific reason.
3. Run shared preprocessing and windowed inference, using the frozen stitching and threshold policies.
4. Write a **temporary** run directory. Preserve the approved scientific grid in the canonical outputs; display reprojection is a derived product.
5. Save the predicted class raster, input-validity mask, optional probability raster and optional review/retention mask. Use explicit class codes/nodata that cannot be confused; record the encoding in the manifest.
6. Save `run.json`, `validation.json`, `outputs.json`, a readable report and preview. Add metrics only through a separately eligible label/evaluation path. If road context is requested, save candidate IDs, intersection rule, uncertain/invalid coverage and analyst review requirements.
7. Reopen output rasters and verify dimensions, CRS, transform, masks, class range and declared units; compare selected coordinate/value samples. Check hashes and the complete file list.
8. Finalise the directory and completion manifest only after those checks pass; mark the run succeeded. A crash before finalisation leaves temporary files, never a successful result.

Suggested portable bundle: `water.tif`, `input-valid.tif`, `probability.tif` when supported, `review-mask.tif` when defined, `candidate-roads.csv` when context exists, `run.json`, `outputs.json`, and `report.html` or Markdown. GeoTIFF preserves georeferencing. A PNG preview is a view of the result and cannot replace the scientific raster. COG is a possible later delivery layout, not a new scientific output; [GDAL's COG documentation](https://gdal.org/en/stable/drivers/raster/cog.html) is for creation/overview/validation options when that need arises.

## Bounded service, jobs and recovery — checkpoint 7

Keep numerical logic in the package. The service validates the request and submits a job; a separate bounded local worker runs the same pipeline. Start with one worker and measured scene/byte/time/disk limits. SQLite holds job metadata and references, while rasters remain files. This is a single-user local application, not a distributed production queue.

Proposed endpoints are `POST /jobs`, `GET /jobs/{id}`, `GET /jobs/{id}/result`, `POST /jobs/{id}/cancel` where supported, and `GET /scenes` / `GET /methods`. Formalise examples and error schemas before the UI. A valid accepted submission returns a stable ID and pending state; retrieving a result before success reports that it is not ready. Reject malformed inputs before queueing where possible. Use an idempotency/request key to prevent an accidental double-click from launching duplicate work; an intentional retry creates a new job linked to the failed one.

| Transition | Required behaviour |
|---|---|
| Accepted → `queued` | Persist request/configuration before acknowledging it |
| `queued` → `running` | Claim atomically so two workers cannot own the same job; record start and current stage |
| `running` → `succeeded` | Only after the verified complete output manifest exists |
| `queued` → `cancelled` | No worker starts it; preserve the cancellation record |
| `running` → cancellation requested | Worker stops at a documented safe boundary; only then mark `cancelled`; show unsupported cancellation honestly |
| `queued`/`running` → `failed` | Save failed stage, stable error code, readable message and retry advice; preserve diagnostic information |
| Process restart with old `running` rows | Reconcile outputs and worker ownership; mark interrupted work failed/retryable unless a verified completed bundle can safely be reconciled; never leave a permanent spinner or assume success |

Store phase progress such as “validating” or “writing outputs” before inventing percentages. Test restart just before and just after output finalisation, retries, cancellation and a full disk/resource error. FastAPI's [background-task documentation](https://fastapi.tiangolo.com/tutorial/background-tasks/) explains simple tasks after a response and the limits for heavy work; merely adding an in-process background callback does not provide the persistence/recovery contract above.

Use stable error codes such as `MISSING_BAND`, `UNSUPPORTED_UNITS`, `GRID_MISMATCH`, `NO_VALID_PIXELS`, `ARTIFACT_MISMATCH`, `RESOURCE_LIMIT` and `INTERRUPTED`. Give a safe next action and run ID. Preserve original inputs and prior valid outputs. Logs should identify stages and versions without exposing secrets or unrestricted local paths.

## Map, context and export — checkpoint 8

The browser requests small metadata, suitable previews/tiles and the original export links. It does not download whole training collections or run scientific preprocessing in components. Render unavailable, uncertain and water areas differently; colour must not be the only cue. Show acquisition time, task, method and validity near the map. A benchmark replay is labelled as such.

Start with pregenerated display products for the small demonstration. Introduce a raster tile service only if a measured viewport/loading experiment justifies it. A basemap needs its own provider terms, attribution and offline/failure behaviour. Keep the scientific output in its approved grid and preserve the display transformation separately.

The road overlay adapter validates geometry and source/date, transforms it deliberately and records whether candidates are defined by exact intersection, rasterisation or another declared rule. Fix that rule before the workflow comparison. Use a small synthetic fixture with known intersections and a permitted real example if available. Candidate status may be “mapped water overlap”, “uncertain”, “unobserved” or “no mapped overlap”; the last is not a safety assessment. Analyst annotations reference the original run and remain distinguishable from predicted classes.

Export must be usable without the browser: include source and asset IDs, dates, CRS, masks, method/calibration status, limitations, attribution and human verification requirements. Reopen the rasters and road geometry independently, then reproduce a summary from the exported values. The [decision-value test](09-product-definition.md) measures whether this flow improves a bounded task.

## Reproduction and optional hosting — checkpoint 9

A clean local reproduction needs code revision, dependency lock/environment, approved input retrieval or tiny distributable fixture, asset hashes, model bundle, configuration, command, expected outputs and numeric tolerances. Document both **inference reproduction** from a frozen artifact and the more expensive **training reproduction** path. A lockfile alone does not reproduce data, hardware behaviour or a missing model.

Run fast meaningful CI checks on synthetic fixtures: alignment, mask semantics, split overlap, metric edge cases, artifact incompatibility, output round trip and service transitions. Full training is a deliberate experiment, not every-commit CI. Test the actual browser success/failure/export journeys separately. Record operating system, hardware, elapsed/active time, memory, disk and supported limits; repeat only when changes or failures justify it.

A local application with an evidence-backed release can complete this route. Optional hosting is a later choice within explicitly remaining time: document allowed data, trusted artifacts, authentication/access boundary if exposed, compute limits, storage retention, basemap dependencies, costs, restart and shutdown. Test the actual remote path before calling it hosted. A reachable demo is still not an operational deployment with accountable users, validated incident procedures and service obligations.

Related: [11-machine-learning-design](11-machine-learning-design.md) · [12-technology-stack](12-technology-stack.md) · [19-checkpoint-playbook](../checkpoints/README.md) · [21-project-state-and-handoffs](../STATE.md)

## Delivery/quality plane — established at C0 and extended later

Alongside the scientific data flow, establish a source-control → clean CI → candidate-artifact path. C0 defines the GitHub Actions workflow and local equivalents: locked install, Ruff checks, pytest package behaviour, package build and independent wheel installation. C1–C8 progressively add actual scientific, geographic, service and UI invariants. CI results are engineering evidence; they do not substitute for frozen ML evaluation or analyst-task measurement.

At C9 a manually chosen revision/model bundle produces a verified delivery candidate with checksums, environment record and fixture output. Public release and optional environment-gated hosting are separate decisions, with health/smoke/rollback checks if actually implemented. No delivery pipeline automatically retrains on final events or promotes a model because a metric improved. The concrete code-free specification and library/function walkthroughs are inside each checkpoint in [note 19](../checkpoints/README.md).
