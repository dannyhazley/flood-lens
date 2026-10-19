# Machine-learning experiment design

**Primary experiment:** compare a declared simple baseline and a compact neural segmenter on water/non-water labels from whole unseen events. This is a proposed protocol to freeze after the data audit; no experiment has been executed.

## 1. Define the task and information available

Input: verified Sentinel-1 radar bands, initially VV and VH if their actual representation is confirmed. Output: per-pixel probability of water and a binary mask on the input grid. Reference: manual labels on valid pixels. Preserve a separate ignore mask for source or label invalidity.

The target is observed water at acquisition time. Permanent-water products, terrain and optical inputs are optional features with separate provenance and ablation requirements, not hidden additions. Check temporal provenance before using a reference product in any issue-time claim.

## 2. Freeze partitions before model selection

The proposed starting allocation is seven training, two development and two final-test events, subject to identity, overlap and class-coverage checks. Assign by documented event/geographic considerations before model scores exist. All tiles, acquisition siblings, overlapping footprints and related weak labels follow their event group. Never randomly split neighbouring patches to support an unseen-event claim.

Training fits weights and preprocessing. Development selects configurations, stopping and any threshold. Final test is reserved for the frozen comparison. If calibration is attempted, preallocate a distinct calibration role, such as one development event with the other used for selection; explain how little evidence that leaves. Reporting raw probability reliability without a fitted calibrator is a valid bounded option.

**Published-split reproduction is a separate track.** Because its training set may contain events reserved by the main experiment, run it after the main protocol and final results are locked. Keep its artifacts and reporting separate; do not feed its learned parameters or test observations back into primary model selection. Milestone 2 defines this track but demonstrates the main baseline on development data.

Source/label integrity inspection before assignment is documented. After freezing, final-test error exploration happens only at the final evaluation. If a defect requires revisiting the experiment, record the invalidation and changed test status.

## 3. Establish meaningful references

Start with Otsu thresholding on a declared band and valid image pixels. Fix histogram construction, threshold scope, class direction and post-processing before final evaluation. Per-scene adaptation uses unlabelled test imagery; state that explicitly. A constant dry prediction is a useful sanity check for class imbalance, not a competitive solution.

Add one feature-based classifier only if it answers a specific question about available per-pixel information. Sample training pixels by event/scene so a large tile does not silently dominate. Evaluate the same valid regions as every other candidate.

## 4. Train one compact model

Use a small U-Net with verified channel ordering. First demonstrate learning on a tiny training subset to debug loading, augmentation, loss and gradient flow. Then use the frozen eligible training partition.

Start with masked binary cross-entropy. If class weighting or a Dice component is introduced, record why and keep the objective fixed within a comparison. Derive class weights and normalisation from training data only. An all-invalid batch must be skipped or rejected deliberately, never converted to a zero-loss success.

Apply spatial transforms jointly to images, labels and validity masks. Use nearest-neighbour resampling for categorical labels. Declare imagery resampling and verify alignment. Avoid generic RGB colour augmentation on radar values. Store raw sensor units and any transformation separately from display stretching.

Proposed search budget: one reference training configuration and at most three justified development variants before review. Choose one ablation, such as VV versus VV+VH, keeping architecture capacity and training policy as comparable as possible. Report residual differences. Repeat selected runs if affordable; publish all planned seed results rather than choosing the best seed.

Select the checkpoint using a declared development criterion and fixed early-stopping policy. Save configuration, dependency versions, code revision, dataset/split IDs, seed, logs, curves, timing and peak memory. Seeding supports reproducibility but does not guarantee identical results across devices/releases; [PyTorch documents these limitations](https://docs.pytorch.org/docs/stable/notes/randomness.html).

## 5. Score at the level of the scientific claim

Compute event confusion counts over valid evaluation pixels, avoiding duplicate counting in overlapping windows. Primary measure: mean event-level water intersection-over-union, with each event weighted equally. Also report every event's IoU, precision, recall, F1, valid count, water prevalence and pooled confusion totals. Pooled IoU answers a different weighting question and must be labelled separately.

For water IoU, TP / (TP + FP + FN). For an empty union, report an explicit empty-agreement flag and the predeclared convention (proposed score 1), plus a sensitivity summary excluding reference-empty events. Precision/recall with zero denominators are undefined and shown as such. An all-invalid event is unscorable and reported separately; it cannot silently disappear from the coverage report. Fix these rules before seeing test outputs.

Use paired event-level differences to compare methods. If there are only two final events, show both rather than claiming a precise worldwide confidence interval. Spatial-block analyses can describe within-event variation but do not manufacture new independent flood events.

## 6. Examine reliability and failure

For probabilistic models, report per-event Brier score and reliability diagrams with documented binning. Majority dry pixels can dominate probability summaries, so also inspect prevalence, class-conditioned behaviour and event differences. Do not invent calibrated probabilities for a deterministic threshold method.

Show error versus retained coverage as uncertain predictions are withheld. Disclose the fraction and spatial distribution withheld. Choose any operating threshold on development/calibration data, then apply it unchanged to final events. A confidence overlay does not establish out-of-distribution detection or reliable emergency decision-making.

Inspect a small declared set of conditions supported by actual metadata or annotation: boundaries, shadows, built areas, vegetation or missing observations. Hand-reviewed case labels must be identified as such. Report plausible explanations as hypotheses; do not infer causality from visual association.

## 7. Finish the experiment

Export an immutable result table, selected/alternative model artifacts, a model card, aligned example panels and a limitations note. State where a baseline won, where the network failed and what would require new evidence. Re-run final inference only to fix a recorded execution defect, not as another tuning loop.

The second land-cover task gets a separate ontology, split, baseline and metric specification. Reusing this experiment machinery is measured engineering transfer; reusing its scores or water labels is not.

Related: [02-dataset-research](02-dataset-research.md) · [04-literature-review](04-literature-review.md) · [13-engineering-milestones](13-engineering-milestones.md)

## Delivered meaning and workflow evaluation

Keep `source_valid`, `label_valid`, `evaluation_valid` and `review/uncertainty` information distinct. Evaluation/loss require valid source AND valid labels; inference validity must work without labels. An uncertainty-withholding policy must never silently change the denominator of the full-coverage headline metric. Store full and retained results separately.

Keep the candidate/model selection rule frozen on development evidence before C4. Final-test results can establish the selected method’s limits; they are not a fresh optimisation loop. A documented defect correction changes test status and must be retained. A predeclared deterministic baseline may be the delivered method without a fabricated confidence layer.

The workflow study in note 09 tests software-assisted inspection using development/demo packets and a separate quality rubric. It does not add new training labels, tune the model on final-event errors or establish damage/forecasting capability. User feedback about layout is distinct from model-selection evidence; record any scientific change it motivates as a new experiment with an appropriate independent evaluation.

## Follow-along implementation reference

The C2/C3/C4 build guides in [note 19](../checkpoints/README.md) specify concrete NumPy/scikit-image/scikit-learn/PyTorch operations, sample/batch shapes, masked loss reduction, optimisation order, architecture starting dimensions, saving/reloading, event count arithmetic and confidence/coverage examples. Use them to implement the protocol one verified unit at a time. They are teaching defaults, not executable code, trained artifacts or a performance claim. Keep the scientific gates above intact when translating a library operation into code.
