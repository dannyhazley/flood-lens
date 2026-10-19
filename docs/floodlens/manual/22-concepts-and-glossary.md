# Concepts and plain-English glossary

Read only the entries named by the current checkpoint. Each entry explains the meaning, the FloodLens need, a simple example and the mistake it prevents. These are learning explanations and proposed contracts, not evidence that software exists. [Return to the current checkpoint](../checkpoints/README.md).

## Raster

**Meaning:** A grid of values whose cells represent places.

**Why FloodLens needs it:** Satellite measurements, labels and predictions share a geographic grid.

**Example:** A 512 × 512 chip contains 262,144 cells; its footprint and pixel size say where they are.

**Mistake prevented:** Treating an image array or its colours as a geographically usable map.

## Band

**Meaning:** One measurement channel in a raster; a number can have physical units and processing history.

**Why FloodLens needs it:** The model must receive the intended measurements in the correct order.

**Example:** VV and VH are radar polarisation channels, not red and green display colours.

**Mistake prevented:** Swapping bands or using a preview PNG as calibrated input.

## Radar backscatter

**Meaning:** A measure of radar energy returned toward the sensor. Surface roughness, geometry and material affect it. Values may be stored on a linear or logarithmic decibel scale.

**Why FloodLens needs it:** Water can appear dark in SAR, but dark pixels alone do not establish water. Verify actual units and provider preprocessing.

**Example:** Smooth open water may return little energy; radar shadow can also be dark.

**Mistake prevented:** Assuming every dark pixel is flooded, or applying a decibel conversion twice.

## Segmentation

**Meaning:** Assigning a class to each valid pixel rather than one class to a whole image.

**Why FloodLens needs it:** FloodLens needs a geographic water boundary, not just “this scene contains water”.

**Example:** Output a water/non-water mask with the same spatial extent as the accepted input.

**Mistake prevented:** Calling image-level classification a usable per-pixel water map.

## Label and label taxonomy

**Meaning:** A reference answer and its defined set of classes. Labels are evidence with limitations, not perfect reality.

**Why FloodLens needs it:** Training and scoring require the same target meaning.

**Example:** Candidate manual codes are -1 invalid, 0 non-water, 1 water; confirm them in actual assets.

**Mistake prevented:** Turning invalid labels into dry land, or treating water as newly flooded area.

## Nodata

**Meaning:** A file value or metadata convention indicating that a measurement is absent.

**Why FloodLens needs it:** An unobserved region must not look confidently dry.

**Example:** A missing strip has a nodata flag even if its stored value is zero.

**Mistake prevented:** Assuming zero always means missing, or including missing pixels in scores.

## Validity mask

**Meaning:** A separate grid saying which pixels can be used for a stated operation.

**Why FloodLens needs it:** Training needs valid inputs AND valid labels; inference can use valid inputs without labels.

**Example:** source_valid ∧ label_valid ∧ declared_quality_mask defines scoring eligibility; inference_valid omits label_valid.

**Mistake prevented:** Using reference-label availability to determine predictions on a new unlabelled scene. GDAL nonzero means valid; NumPy masked-array True means invalid.

## CRS

**Meaning:** Coordinate reference system: the rules and units used to describe a position.

**Why FloodLens needs it:** Image and asset coordinates must refer to compatible places.

**Example:** Longitude/latitude degrees and a local projected grid in metres need a real coordinate conversion before overlay.

**Mistake prevented:** Treating degrees as metres or changing only a CRS label instead of transforming coordinates.

## Affine transform

**Meaning:** Numbers mapping pixel row/column positions to coordinates, including origin, scale and possibly rotation.

**Why FloodLens needs it:** A correct CRS alone does not locate individual pixels.

**Example:** On a north-up 10-m grid, pixel centres are offset half a pixel from the corner origin; compare known centres after export.

**Mistake prevented:** A one-pixel shift or flipped row axis that produces plausible but misplaced overlays.

## Spatial alignment, reprojection and resampling

**Meaning:** Alignment means corresponding pixels cover the same locations. Reprojection changes the coordinate representation; resampling estimates values on a new grid.

**Why FloodLens needs it:** Image and label can have equal array sizes yet be geographically displaced.

**Example:** Choose one target grid, transform deliberately, use nearest neighbour for class labels and record the imagery method.

**Mistake prevented:** Resizing arrays blindly or creating fractional land-cover class IDs through interpolation. Matching grids also does not prove the original labels are correctly registered.

## Manifest and checksum

**Meaning:** A manifest lists exact inputs and metadata; a checksum fingerprints file bytes.

**Why FloodLens needs it:** Every result must identify the assets actually used, including exclusions.

**Example:** Record scene ID, original URL, retrieved date, byte count and SHA-256; a changed hash means different bytes.

**Mistake prevented:** Silently replacing data under the same filename. A matching checksum does not prove scientific correctness or grant use rights.

## Event/group split

**Meaning:** Assigning related observations together to training, development or final test.

**Why FloodLens needs it:** Neighbouring tiles and repeated acquisitions are not independent examples.

**Example:** Every chip from one flood episode, its overlapping siblings and related weak labels belongs to one group.

**Mistake prevented:** Randomly splitting adjacent patches and claiming unfamiliar-event generalisation.

## Event holdout

**Meaning:** Reserving complete event groups from training; the final test is also excluded from model selection.

**Why FloodLens needs it:** The intended question concerns unfamiliar events.

**Example:** A proposed 7/2/2 event split uses seven for training, two for development roles and two for final testing, if the audit supports it.

**Mistake prevented:** Treating good scores on familiar events as evidence for unseen events worldwide.

## Leakage

**Meaning:** Using information the evaluation claim says should be unavailable during fitting or selection.

**Why FloodLens needs it:** An honest final test must remain independent of all selection choices.

**Example:** Choosing the water threshold after viewing final-event mistakes leaks test information even without retraining weights.

**Mistake prevented:** Fitting scaling on all data, overlapping scene groups, or training a published split before the main test lock.

## Baseline

**Meaning:** A simple, explicit reference method used to test whether complexity earns its cost.

**Why FloodLens needs it:** A network is useful only if its result or tradeoff is justified against an appropriate reference.

**Example:** A declared Otsu threshold separates a valid-pixel intensity histogram; its low-backscatter side is a water candidate.

**Mistake prevented:** Assuming training a neural network automatically improves mapping. Otsu is not itself proof that the chosen class is water.

## IoU

**Meaning:** Intersection over union: correctly predicted water divided by all pixels predicted OR labelled water.

**Why FloodLens needs it:** It measures spatial agreement while penalising missed and extra water.

**Example:** TP=60, FP=20, FN=20 gives 60/(60+20+20)=0.60.

**Mistake prevented:** Reporting overall accuracy dominated by dry land. Define empty unions and all-invalid inputs before evaluation.

## Precision and recall

**Meaning:** Precision asks how much predicted water is labelled water; recall asks how much labelled water was found.

**Why FloodLens needs it:** Extra inspection candidates and missed water are different errors.

**Example:** With TP=60, FP=20, FN=40, precision=60/80=0.75 and recall=60/100=0.60.

**Mistake prevented:** Hiding missed water behind a single score. Zero denominators are undefined unless a prior convention says otherwise.

## Macro event score and pooled score

**Meaning:** Macro averages one score per event equally; pooled combines all eligible pixel counts before scoring.

**Why FloodLens needs it:** A large event should not silently define the whole headline result.

**Example:** Report two final-event IoUs individually and their mean, alongside a separately labelled pooled IoU.

**Mistake prevented:** Mistaking millions of correlated pixels for millions of independent flood events.

## Calibration

**Meaning:** Whether a stated probability matches the observed class frequency under evaluated conditions.

**Why FloodLens needs it:** Analysts need to know how much trust to place in water probabilities.

**Example:** Among valid pixels assigned P(water) near 0.8, about 80% should be labelled water if calibrated in that setting.

**Mistake prevented:** Calling a confident output correct, or assuming calibration transfers to a new event. Any fitted calibrator uses designated development/calibration data only.

## Brier score and reliability diagram

**Meaning:** Brier score averages squared probability errors; a reliability diagram compares predicted probabilities with observed frequencies in bins.

**Why FloodLens needs it:** They check probability quality separately from binary map overlap.

**Example:** For water probability 0.8 and label 1, squared error is 0.04; record bin counts so sparse bins are visible.

**Mistake prevented:** Claiming uncertainty is useful merely because the UI has a heatmap. Dry-pixel prevalence and event differences can dominate summaries.

## Uncertainty and retained coverage

**Meaning:** Uncertainty expresses limited confidence in an inference; retained coverage is the fraction of eligible area still shown after withholding uncertain output.

**Why FloodLens needs it:** An analyst must see both doubtful areas and what the system did not assess.

**Example:** Report error on the retained 80% with the withheld 20% visibly marked, and compare against full eligible coverage.

**Mistake prevented:** Presenting selective accuracy as free improvement or promising every incorrect pixel will be flagged. Raw probability is only a confidence signal until evaluated.

## Distribution shift

**Meaning:** Input or target conditions differ from the training situation.

**Why FloodLens needs it:** New terrain, settlements or observation conditions may change errors.

**Example:** A model trained mostly on open rural water may fail in a dense urban event.

**Mistake prevented:** Assuming a familiar benchmark score transfers to every place, or that confidence reliably detects unfamiliar inputs.

## Ablation

**Meaning:** A controlled experiment changing one factor to test its contribution.

**Why FloodLens needs it:** It helps explain a result rather than just selecting a lucky configuration.

**Example:** Compare VV-only and VV+VH with otherwise comparable training and report remaining capacity differences.

**Mistake prevented:** Changing augmentation, architecture and learning rate together and crediting one of them.

## Loss, epoch and checkpoint

**Meaning:** Loss is the training penalty; an epoch is one pass through training data; a saved model checkpoint stores a training state.

**Why FloodLens needs it:** They describe how weights are learned and which candidate is selected.

**Example:** Use masked binary loss and select saved weights by a predeclared development rule.

**Mistake prevented:** Treating low training loss as final accuracy. A model checkpoint is different from the project checkpoints C0–C9.

## Model artifact

**Meaning:** A versioned bundle of parameters and the information needed to run them correctly. For a baseline, parameters/rules replace neural weights.

**Why FloodLens needs it:** The service must load the same method evaluated by the experiment.

**Example:** Bundle architecture, task, bands/units, normalisation, threshold, calibration state, hashes and provenance.

**Mistake prevented:** Shipping a weights file without the preprocessing that gives it meaning, or loading untrusted executable artifacts.

## Georeferenced output and GeoTIFF

**Meaning:** An output with coordinates/grid metadata; GeoTIFF is a raster exchange format that can preserve them.

**Why FloodLens needs it:** GIS software must place and interpret the result independently of the viewer.

**Example:** Reopen water_class.tif and verify CRS, transform, dimensions, valid mask, class meaning and a known landmark.

**Mistake prevented:** Exporting a colourful PNG as if it were an analysis-ready geographic layer.

## COG and map tiles

**Meaning:** A cloud-optimised GeoTIFF arranges raster data for efficient partial reads; map tiles are bounded display pieces requested while panning.

**Why FloodLens needs it:** The browser should not download a full collection just to view one area.

**Example:** Benchmark a small local scene, then choose pregenerated tiles or COG serving only if needed.

**Mistake prevented:** Building tile infrastructure before measuring the display problem, or scoring resampled display pixels.

## Vector asset and spatial overlay

**Meaning:** A vector stores points, lines or polygons; overlay compares their locations with another layer.

**Why FloodLens needs it:** Roads/buildings can give context to observed water.

**Example:** Intersect a licensed road geometry with valid mapped water and export candidate inspection segments with date and uncertainty.

**Mistake prevented:** Interpreting overlap as road closure or building damage; ignoring stale assets, positional error or missing coverage.

## API and contract

**Meaning:** An application programming interface lets software request work; its contract defines accepted inputs, outputs and errors.

**Why FloodLens needs it:** The browser and wider systems need machine-readable results with stable meaning.

**Example:** A request supplies approved scene and model IDs; the response supplies a job ID, not an invented finished map.

**Mistake prevented:** Duplicating ML logic in the browser or treating an accepted request as successful analysis.

## Background job and durable state

**Meaning:** Work continues outside the initial request; stored state records progress and outcome across refresh/restart.

**Why FloodLens needs it:** Raster analysis may take longer than an interactive request.

**Example:** A queued job becomes running then succeeded only after every required output passes validation; interrupted work is marked clearly.

**Mistake prevented:** A permanent spinner, duplicate jobs, or partial results displayed as complete.

## Vertical slice

**Meaning:** One small user journey working through every required layer.

**Why FloodLens needs it:** It exposes integration problems early without building every screen.

**Example:** Select one approved scene, run the existing pipeline, inspect one true result and export it.

**Mistake prevented:** Mistaking disconnected mock screens for an implemented product.

## Provenance

**Meaning:** The traceable history of sources, transformations and decisions behind a result.

**Why FloodLens needs it:** A reviewer must know what produced a candidate inspection layer.

**Example:** A report links input hashes, acquisition time, split, code revision, model ID, run settings and warnings.

**Mistake prevented:** An attractive map whose dates, rights or producing method cannot be recovered.

## Reproducibility

**Meaning:** A documented process can recreate an outcome from identified inputs and environment, within stated tolerances.

**Why FloodLens needs it:** Another engineer must be able to verify the case study.

**Example:** A clean local environment recreates a fixture output and agreed metrics; exact bytes may differ across devices.

**Mistake prevented:** Assuming a seed guarantees bitwise equality everywhere, or relying on hidden notebook state.

## Before/after inundation change

**Meaning:** A temporal target identifying water newly present relative to an appropriate prior state.

**Why FloodLens needs it:** It is a possible later applied capability, distinct from initial observed water.

**Example:** Aligned pre/post water masks can propose change, but need independent change labels and propagated error assessment.

**Mistake prevented:** Calling permanent water new flooding or claiming validated change from two side-by-side images.

## Decision-value test

**Meaning:** A bounded comparison of whether a tool helps a defined human task, with quality as well as effort measured.

**Why FloodLens needs it:** Workflow usefulness must be demonstrated independently of ML accuracy and UI polish.

**Example:** Time manual scene inspection and FloodLens-assisted candidate inspection reporting on identical task packets; report errors too.

**Mistake prevented:** Claiming cost savings, recovery impact or business value from a demo alone.

## Additional concepts used by the checkpoints

### Git, commit and dirty worktree

**Meaning:** Git records file history; a commit is a saved revision; a dirty worktree contains changes not in that revision.

**Why FloodLens needs it:** A run must identify the code that actually produced it, and future sessions must preserve unfinished edits.

**Example:** Save the code revision and whether uncommitted changes were present when a run started.

**Mistake prevented:** Overwriting work or claiming a clean release hash describes code that was actually modified.

### Virtual environment and dependency lock

**Meaning:** An isolated runtime keeps project packages separate; a lockfile records a resolved dependency set.

**Why FloodLens needs it:** FloodLens needs a repeatable software environment without installing every later tool immediately.

**Example:** At C0 a fresh shell activates/uses the project environment and runs the documented version command.

**Mistake prevented:** A command working only because of unrelated globally installed packages. A lockfile does not itself capture data or hardware.

### Configuration and schema version

**Meaning:** Configuration holds declared choices; a schema defines fields, types and meanings; a version identifies which contract applies.

**Why FloodLens needs it:** Baseline, training, service and exports must agree on task/input meaning.

**Example:** A run config names the model, band order and threshold; a request schema accepts approved scene IDs.

**Mistake prevented:** Hidden notebook choices or silently reading a changed record as an older compatible one.

### Normalisation and decision threshold

**Meaning:** Normalisation transforms numeric input ranges; a threshold turns a score into a class decision.

**Why FloodLens needs it:** The fitted preprocessing and water decision must be identical at training/evaluation/inference.

**Example:** Fit band mean/scale on training data; choose a probability cutoff on designated development data and freeze it.

**Mistake prevented:** Using final events to fit input scaling or moving a threshold until test errors look better.

### U-Net, tensors and gradients

**Meaning:** U-Net is an encoder/decoder segmentation design; tensors are numeric arrays; gradients say how changing parameters affects the training loss.

**Why FloodLens needs it:** A compact implementation can learn spatial context while retaining pixel localisation.

**Example:** A batch has image tensors shaped batch × bands × height × width; masked loss yields gradients for weight updates.

**Mistake prevented:** Using a whole-image class model for a pixel target, confusing axes or treating absent gradients as successful learning.

### Tiny-subset fit and overfitting

**Meaning:** A tiny-subset fit checks whether the model can learn a few training examples; overfitting means training improves while unfamiliar-data behaviour does not.

**Why FloodLens needs it:** Debug the learning path before spending the main experiment budget.

**Example:** Check that loss falls on two training chips, then assess development events separately.

**Mistake prevented:** Calling memorisation a generalisation result or adding more epochs to repair a broken label loader.

### Joint augmentation

**Meaning:** A training transformation moves imagery, labels and validity together.

**Why FloodLens needs it:** The target must still describe the same pixel locations after a flip/crop.

**Example:** Flip image, class mask and valid mask with the same sampled transformation.

**Mistake prevented:** Training against a shifted target or applying RGB colour jitter to radar measurements.

### Confusion counts and F1

**Meaning:** TP is correctly predicted water; FP extra predicted water; FN missed water; TN correctly predicted non-water. F1 is 2TP/(2TP+FP+FN).

**Why FloodLens needs it:** All reported metrics should be reproducible from common valid-pixel counts.

**Example:** TP=60, FP=20, FN=40 gives F1=120/180≈0.667, with precision/recall showing the distinct errors.

**Mistake prevented:** Calculating metrics on different masks or reporting a single unexplained percentage. Freeze zero-denominator conventions.

### Spatial correlation, block analysis and bootstrap

**Meaning:** Nearby pixels share conditions; blocks aggregate related locations. A bootstrap resamples eligible independent units to describe variability.

**Why FloodLens needs it:** The number of independent events is far smaller than the pixel count.

**Example:** Report two final-event scores individually; a within-event block analysis describes spatial variation, not two hundred new events.

**Mistake prevented:** An implausibly tight worldwide confidence interval from resampling correlated pixels. A two-event bootstrap does not establish global precision.

### Idempotency and deliberate retry

**Meaning:** Idempotency makes a repeated identical request avoid accidental duplicated work; a deliberate retry is a recorded new attempt.

**Why FloodLens needs it:** Refresh/double-clicks must not create competing writes or unexplained extra jobs.

**Example:** The same request key returns its job; retrying a failed job creates a linked attempt with a new ID.

**Mistake prevented:** Duplicate runs overwriting artifacts or erasing the failure history.

### Atomic completion and output transaction

**Meaning:** A result becomes complete only after all required files and checks succeed; publishing the completion marker is one deliberate final step.

**Why FloodLens needs it:** Interrupted inference must not leave a plausible partial result marked successful.

**Example:** Write a temporary bundle, reopen/validate outputs, then finalise its manifest and job state.

**Mistake prevented:** A crash during raster writing being shown as a finished map.

### Observation age and processing time

**Meaning:** Observation age is how long since acquisition; processing time is how long the software takes after input is available.

**Why FloodLens needs it:** Fast inference cannot make an old satellite observation current.

**Example:** A five-minute run on a two-day-old scene produces a two-day-old observation with five minutes of processing.

**Mistake prevented:** Claiming real-time response from a fast historical replay or ignoring provider delivery latency.

## Read further only when needed

Use [Rasterio georeferencing](https://rasterio.readthedocs.io/en/stable/topics/georeferencing.html) for CRS and pixel-coordinate mapping, and [Rasterio masks](https://rasterio.readthedocs.io/en/stable/topics/masks.html) for the opposite GDAL/NumPy mask conventions. Use [Guo et al.](https://proceedings.mlr.press/v70/guo17a.html) for calibration motivation and [PyTorch reproducibility guidance](https://docs.pytorch.org/docs/stable/notes/randomness.html) for the limits of seeds and cross-platform repeatability. These sources support the concepts; FloodLens still needs its own measurements. Other task-specific reading is indexed by checkpoint in 16-references (private/source-manual context; not required by this kit).

## Teaching additions for the build guides

### CI, continuous delivery and continuous deployment

**Meaning:** CI automatically checks a changed revision. Delivery prepares a releasable artifact. Deployment changes a running environment.

**Why FloodLens needs it:** The project should establish quality checks before modelling and avoid confusing packaging with a live service.

**Example:** C0 lint/test/build/install checks run on a clean runner; C9 prepares a candidate bundle; any host deployment is a later distinct action.

**Mistake prevented:** Calling a workflow file a deployed product, or auto-publishing unreviewed model artifacts.

### Workflow, job, step and runner

**Meaning:** A workflow is an automation definition; a job is a set of steps on a runner; a step performs one action/command; the runner is its execution machine.

**Why FloodLens needs it:** A CI failure must be located and reproduced instead of treated as one mysterious red badge.

**Example:** The environment-install step fails before tests start on the Linux runner.

**Mistake prevented:** Changing model code to repair a dependency-install failure or assuming laptop files exist in CI.

### Wheel and build backend

**Meaning:** A wheel is an installable Python distribution; the build backend turns declared project source/metadata into that distribution.

**Why FloodLens needs it:** The delivered package must contain the files/imports/entry points needed outside an editable checkout.

**Example:** Build a wheel, install it in a separate temporary environment and execute its version command from another directory.

**Mistake prevented:** An editable install hiding missing package files; confusing a successful source import with a correct release artifact.

### Unit, integration and end-to-end tests

**Meaning:** Unit tests check a small behaviour; integration tests check connected components; end-to-end tests exercise a user journey through the system.

**Why FloodLens needs it:** FloodLens has numerical rules, package/file boundaries and browser workflows with different failure modes.

**Example:** Hand-counted IoU is a small test; raster export/reopen is integration; select → job → map → export is an end-to-end journey.

**Mistake prevented:** Using only mocked screens to claim the real pipeline works or replacing scientific evaluation with a green test suite.

### Pull request and merge check

**Meaning:** A pull request presents a branch change for review; merge checks can require defined CI outcomes before the default branch changes.

**Why FloodLens needs it:** A repeatable review habit helps keep a large solo project recoverable.

**Example:** A small data-validator branch shows changed files, test evidence and one decision before merging.

**Mistake prevented:** Treating a documented recommendation as an enforced repository setting or merging unrelated work in one opaque change.

### Hyperparameter and learned parameter

**Meaning:** A learned parameter is fitted by training; a hyperparameter is a choice such as learning rate or architecture width.

**Why FloodLens needs it:** Trials and model selection must be bounded and traceable.

**Example:** Adam updates weights; the initial learning rate 0.001 is a declared starting choice assessed on development data.

**Mistake prevented:** Presenting tutorial defaults as scientifically optimal or changing them after seeing final-test mistakes.

### Logits, sigmoid, softmax and argmax

**Meaning:** Logits are unconstrained model scores. Sigmoid gives binary water probabilities; softmax distributes probability over exclusive classes; argmax chooses the largest class score.

**Why FloodLens needs it:** Binary water and multiclass land cover need distinct output/loss contracts.

**Example:** One water logit channel feeds BCEWithLogitsLoss directly; five exclusive land-cover logit channels feed CrossEntropyLoss directly.

**Mistake prevented:** Applying sigmoid/softmax twice before a logits-based loss or using a binary head for five exclusive classes.

### Learning loop and optimiser state

**Meaning:** A forward pass makes predictions; loss compares them to valid references; backward computes gradients; the optimiser updates weights and may retain update history.

**Why FloodLens needs it:** The training path must perform actual updates and resume honestly.

**Example:** Clear gradients → forward → masked loss → backward → Adam step; evaluation omits backward/updates.

**Mistake prevented:** Accumulating old gradients accidentally, evaluating while still updating, or claiming an exact resumed run from weights alone.

### Request validation and SQL transaction

**Meaning:** Validation checks a request’s shape/meaning; a transaction makes a small set of database changes succeed or fail together.

**Why FloodLens needs it:** An accepted analysis needs a durable queued record and safe worker ownership.

**Example:** Validate approved IDs, insert the job and commit before acknowledging; claim conditionally in a short transaction.

**Mistake prevented:** Well-typed but unsupported input, duplicate worker ownership, lost accepted jobs or SQL built by interpolating untrusted text.
