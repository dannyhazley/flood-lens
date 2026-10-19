# Literature that informs FloodLens

This is a focused design reading list. Source findings and proposed FloodLens decisions are distinguished below; none of these papers establishes performance for a model that has not yet been built. The earlier hydrology/space-weather review remains in the research archive (private/source-manual context; not required by this kit).

## 1. Sen1Floods11 — the data and reference problem

**Bonafilia, D., Tellman, B., Anderson, T. and Issenberg, E. (2020). _Sen1Floods11: A Georeferenced Dataset to Train and Test Deep Learning Flood Algorithms for Sentinel-1_. CVPR Workshops.** [Original paper](https://openaccess.thecvf.com/content_CVPRW_2020/html/w11/Bonafilia_Sen1Floods11_A_Georeferenced_Dataset_to_Train_and_Test_Deep_Learning_CVPRW_2020_paper.html) · [Author repository](https://github.com/cloudtostreet/Sen1Floods11).

The work provides georeferenced flood-event imagery, manual water labels and weakly labelled data to support radar water-mapping experiments. Its value here is an inspectable task and reference dataset with spatial metadata.

**Limit:** abundant pixels and weak labels do not remove the small number of independent events. Paper metrics are meaningful only with their exact split, preprocessing, target and aggregation. A water label is not automatically a new-inundation label.

**FloodLens decision:** reproduce a compatible baseline separately from the event-held-out experiment; keep weak-label training optional. The current licence/split findings in [02](02-dataset-research.md) come from direct archive inspection, not assumptions about the paper.

## 2. Otsu — a serious simple baseline

**Otsu, N. (1979). _A Threshold Selection Method from Gray-Level Histograms_. IEEE Transactions on Systems, Man, and Cybernetics, 9(1).** [Original publication / DOI](https://doi.org/10.1109/TSMC.1979.4310076).

The method selects a threshold from an intensity histogram using class separation. It provides a reproducible, inexpensive reference before learning spatial patterns.

**Limit:** an intensity partition does not intrinsically identify water. SAR scenes may contain several land-cover distributions, little water, and dark non-water surfaces. Image-wide statistics also differ from a fixed threshold learned on training data.

**FloodLens decision:** predeclare the band, histogram validity mask, threshold scope and which side represents water. Report failure cases and explicitly allow per-scene unlabelled-image adaptation for this method. Do not tune preprocessing or threshold rules against final-test labels.

## 3. U-Net — a manageable learned spatial model

**Ronneberger, O., Fischer, P. and Brox, T. (2015). _U-Net: Convolutional Networks for Biomedical Image Segmentation_. arXiv:1505.04597; MICCAI 2015.** [Original manuscript](https://arxiv.org/abs/1505.04597).

The architecture combines a contracting path for context with an expanding path for localisation. The authors demonstrated their training approach on biomedical segmentation, using augmentation to make limited labelled imagery more useful.

**Limit:** those results concern different sensors and labels. They do not guarantee that a U-Net trained on a few flood events will generalise to a new landscape.

**FloodLens decision:** use a compact two-band implementation as a tractable hypothesis about learned spatial context. Start from scratch to keep the training provenance clear. Check tiny-subset learning, then compare on exactly the baseline's valid evaluation pixels. A larger backbone is not an automatic next step.

## 4. Calibration — separate confidence from correctness

**Guo, C., Pleiss, G., Sun, Y. and Weinberger, K. Q. (2017). _On Calibration of Modern Neural Networks_. ICML, PMLR 70:1321–1330.** [Paper and proceedings](https://proceedings.mlr.press/v70/guo17a.html).

The authors study miscalibration in neural classifiers and post-processing methods, including temperature scaling. Their classification experiments motivate checking probability quality independently from classification accuracy.

**Limit:** a method working on those benchmarks is not evidence that it remains calibrated under new flood events or spatial dependence. Calibration is also different from detecting an unfamiliar input.

**FloodLens decision:** report reliability plots and Brier scores by event. Any calibration fit uses designated development/calibration data, with the split disclosed. Compare calibrated and raw outputs only if the budget and data support it; do not call raw probabilities validated uncertainty.

## 5. WILDS — evaluation under distribution shift

**Koh, P. W. et al. (2021). _WILDS: A Benchmark of in-the-Wild Distribution Shifts_. ICML, PMLR 139:5637–5664.** [Paper and full author list](https://proceedings.mlr.press/v139/koh21a.html).

WILDS assembles real distribution-shift tasks, including satellite and wildlife examples, and evaluates generalisation beyond conventional sampled test sets. It motivates a distinction between doing well on familiar data and remaining useful when conditions change.

**Limit:** WILDS results are neither a measurement of FloodLens nor proof that two reserved flood events represent the globe.

**FloodLens decision:** separate published-split reproduction from held-out-event evaluation. Show individual event results and observed failure conditions. A second land-cover experiment requires its own valid split and target, even when it shares infrastructure.

## 6. DAM-Net / S1GFloods — a later temporal problem

**Saleh, T., Weng, X., Holail, S., Hao, C. and Xia, G.-S. (2024). _DAM-Net: Flood detection from SAR imagery using differential attention metric-based vision transformers_. ISPRS Journal of Photogrammetry and Remote Sensing, 212:440–453.** [Author repository and publication citation](https://github.com/Tamer-Saleh/S1GFlood-Detection) · [Earlier manuscript, 2023](https://arxiv.org/abs/2306.00704).

This work pairs before/after SAR imagery and introduces a differential-attention approach. It is useful background for distinguishing change analysis from single-date segmentation.

**Limit:** data representation, pairing, event independence and data-specific terms still need their own audit. Architecture complexity does not resolve those requirements.

**FloodLens decision:** keep paired change modelling outside the current C0–C9 commitment. If later selected, begin with a simple temporal comparison and a paired-model baseline before considering a transformer. Published scores cannot be copied into the FloodLens case study.

## Reading order and extraction rule

Read the Sen1Floods11 data documentation first, then U-Net, Otsu, calibration and WILDS as their milestones approach. DAM-Net is extension reading. For each implemented method record the exact inputs, target, split unit, missing-data policy, metrics and one limitation. Reading is useful when it changes a design decision or produces a checkable hypothesis.

Related: [11-machine-learning-design](11-machine-learning-design.md) · 16-references (private/source-manual context; not required by this kit)

## Turn reading into a small artifact

At C1 extract sensor units, class meaning and geographic assumptions from the dataset documentation; at C2 write the precise Otsu rule and metric conventions; at C3 sketch U-Net’s context/localisation path and state the ablation hypothesis; at C4 explain what calibration can and cannot establish under event shift. Save a few sentences in the checkpoint report stating what changed in the implementation or evaluation. Reading is part of each checkpoint’s learning budget, not a separate unbounded literature phase.
