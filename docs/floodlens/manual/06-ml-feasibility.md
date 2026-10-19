# Machine-learning feasibility

**Assessment: technically plausible, with material data and generalisation risks.** FloodLens offers a useful combination of data analysis, computer vision and software engineering. No model performance, training duration or completed raster integrity check is available yet.

## Why this is a real modelling problem

Inputs are sensor observations with spatial structure; the target is independently annotated water on valid pixels. A threshold baseline makes the value of learned patterns testable. A compact network can use local context, but that is a hypothesis to evaluate rather than a reason to assume success.

The audit found 446 manual chips across eleven filename event groups. That is enough to attempt a bounded experiment after validation, but the number of pixels exaggerates the amount of independent evidence. Spatial correlation, label uncertainty and event selection dominate the strength of generalisation claims. [Audit evidence and remaining gates](02-dataset-research.md).

## Feasibility gates

| Gate | Evidence needed | Current state | Failure response |
|---|---|---|---|
| Usable data | Clear rights/use scope, accessible files and documented target | Metadata accessed; annotation terms unresolved | Resolve or select a replacement |
| Spatial integrity | Readable bands, aligned grids, valid labels and known units | Not checked on imagery | Repair with a recorded method or reject affected assets |
| Independent evaluation | Verified event IDs, overlap checks and frozen groups | Standard splits inspected; new split not created | Reduce the claim or change the source |
| Learning path | Tiny-subset fit, finite loss, valid gradients and sensible output | Not implemented | Debug data/loss before larger runs |
| Affordable experiments | Measured loading, memory and short training throughput | Hardware/cost not established | Smaller model, batch or experiment scope |
| Added value | Matched baseline/model results and a justified selection | No results | Retain the better method, including the baseline |
| Transfer | Different task, appropriate labels and independent evaluation | Dataset not selected | Finish first case study; report unresolved transfer honestly |

## Strong hypotheses within a small budget

Primary hypothesis: learned spatial context improves macro event-level water IoU over the declared simple baseline under the same data eligibility and masks.

One ablation can ask whether adding the second radar band improves development-event performance, or whether geometric augmentation improves it. Choose one before running experiments; keep other settings fixed. Record variability and compute. If the result is inconclusive, explain the sample and budget limits rather than expanding indefinitely.

An optional feature classifier can help distinguish useful per-pixel information from spatial-model benefit. It is not a compulsory extra modelling track. Weak labels, pretraining and ensembles each introduce provenance, evaluation and compute costs and remain optional.

## Compute feasibility before commitments

Benchmark a representative loader pass, the baseline and a short neural run on named local hardware. Record input dimensions, batch size, device, peak memory and elapsed time. Estimate a full run from measured batches with allowance for validation and checkpointing. A successful smoke run does not establish a full training budget.

Select a model size and number of trials that fit the milestone's review ceiling. Use CPU for data validation and the baseline; select supported acceleration only after checking the actual environment. No purchased GPU time or always-on hosting is part of the current plan.

## What makes a completed result valuable

Useful results include a cleanly demonstrated improvement, a baseline that remains competitive, an event-specific failure, or a dataset gate that prevents a misleading experiment. Each requires an inspectable artifact and a precise conclusion. Finishing an investigation is different from demonstrating the originally hoped-for predictive capability.

Related: [11-machine-learning-design](11-machine-learning-design.md) · [13-engineering-milestones](13-engineering-milestones.md) · 15-risks-and-open-questions (private/source-manual context; not required by this kit)

## Applied-system feasibility is a separate gate

Model quality, geographic output correctness and analyst usefulness are three separate checks. C5 must prove a supported output reopens in the correct place and can be combined with one permitted/synthetic road layer. C7–C9 must compare the bounded workflow with manual inspection using the protocol in [note 09](09-product-definition.md). No gain, a quality tradeoff or an unusable export is reportable; a neural score alone does not prove value. A stronger deterministic baseline may remain the delivered method, with confidence unavailable clearly stated instead of fabricated.
