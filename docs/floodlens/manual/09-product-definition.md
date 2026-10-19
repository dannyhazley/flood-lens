# Product definition and applied workflow

**FloodLens is a proposed analytical component for turning satellite observations into a traceable, uncertainty-aware water layer that an analyst can use alongside other geographic evidence.** It is a personal portfolio prototype. Implementation has not begun, and no analyst-time saving, operational benefit or model performance has been measured.

The central applied scenario is:

> FloodLens produces a traceable, uncertainty-aware flood-impact layer from satellite imagery. A larger emergency-management, infrastructure or environmental system could combine that layer with roads, buildings, farms, habitats, population and field reports to decide what needs inspection or recovery attention.

Here, **“flood-impact layer” describes its intended place in a wider workflow**. The initial scientific output must be labelled **observed water at acquisition time**. It can include permanent water. It does not establish which water is new, predict future floods, prove building damage, infer displacement or calculate repair costs. A more precise newly inundated-area layer requires the later paired-change extension in [05-project-scope](05-project-scope.md).

The first user is Danny acting as a geospatial analyst on a bounded historical case. A reviewer may subsequently repeat the task. Neither is evidence that a government agency or emergency team uses the system. The product question is whether the workflow helps this user produce a usable, traceable inspection brief, with fewer omissions or less effort than manual scene review. That question is tested below.

## A concrete applied walkthrough

Use one historical flood event and **one small road corridor or study area** for the first demonstration. Roads are the proposed first asset type; no road dataset has been selected or licensed yet. Choose an explicitly permitted source at checkpoint 5 or use clearly labelled synthetic road geometry for a software demonstration. Synthetic overlays can verify integration but cannot establish real exposure or analyst value in a real location.

| Stage | What happens | FloodLens contributes | What remains outside FloodLens / must be checked |
|---|---|---|---|
| **1. A flood event occurs** | A wider organisation records an event, a question and an area of interest, such as “which road segments should be checked?” | Stores the supplied event ID, study boundary and analysis question | Does not detect the event before observations, forecast it, issue warnings or decide emergency priorities |
| **2. Satellite observations become available** | A provider supplies imagery with acquisition time, sensor metadata and processing history | Accepts only approved, supported assets; records source, time, checksum and terms | Does not control satellite revisit, delivery latency or preprocessing quality. A historical replay is not a live response system; record observation age separately from processing time |
| **3. FloodLens validates the scene** | The pipeline checks bands/units, readability, CRS, transform, masks, footprint and expected coverage | Produces a quality report and either accepts the supported scene or gives an explicit failure | A structurally valid raster can still contain sensor ambiguity or poor labels. Repair requires recorded evidence; a plausible preview alone does not prove alignment |
| **4. FloodLens produces a water/inundation layer** | The frozen method runs on supported pixels | Saves observed-water classes, a probability layer when supported, and validity information with model and run IDs | Initially this is observed water, not independently validated new inundation. Permanent water, radar shadow and vegetation can affect interpretation; no flood depth or consequence estimate is created |
| **5. Confidence and geography are checked** | The analyst examines coverage, uncertainty, known failure cases and geographic placement | Displays raw/calibrated status, withheld coverage, warnings and traceable georeferenced exports; benchmark metrics appear only where valid references exist | Probability is not proof. Unknown conditions can be confidently wrong. Without labels, scene accuracy is unknown; human comparison with other observations is still required |
| **6. The layer is overlaid with other evidence** | The analyst loads the bounded road layer and sees overlap with water, uncertainty and missing coverage | Aligns declared coordinate systems and creates candidate review items, retaining source dates and geometry IDs | An overlap is a reason to inspect, not proof a road is closed or damaged. Bridges, positional error, water under infrastructure, resolution and outdated asset maps can mislead. Buildings, farms, habitats, population and field reports are later integrations, not all required features |
| **7. An analyst prioritises inspection or recovery attention** | The analyst records candidates, uncertainty, rationale and information still needed | Supports a review queue and exports a brief that another person can inspect; analyst decisions are recorded separately from predictions | Does not dispatch teams, recommend safe routes or make funding decisions. An accountable human combines access, vulnerability, field reports and other priorities in the larger system |
| **8. Limits and verification requirements are recorded** | The brief names the observation time, inspected area, method, confidence limitations and next verification step | Preserves inputs, settings, warnings, analyst notes and result checksums so the analysis can be repeated | Field verification and authoritative situation assessment remain necessary. The portfolio brief is a historical demonstration, not an operational incident report |

A useful final brief might say, **only after the evidence exists**: “These road segments intersect the mapped water footprint; these other segments cross unavailable or uncertain imagery; verify both groups against field reports.” It must not replace that statement with “these roads are damaged” or “these routes are safe.” A segment outside the mapped water can still be unsafe or unobserved.

## Minimum complete experience — checkpoint 5

1. Select one approved scene or a bounded scene list from a manifest.
2. Read its event identity, acquisition time, sensor, supported bands and quality status.
3. Run the selected method using a versioned configuration. The method may be the simple baseline if it proved preferable.
4. Inspect imagery, water output, validity and uncertainty when available. Reference labels and error overlays have clear benchmark-only labels.
5. Open the same geographic output in an independent GIS viewer and inspect known locations.
6. Add the single permitted or synthetic road layer. Record intersections, uncertain/no-observation areas and the limits of interpreting them; avoid a complex ranking algorithm.
7. Save an export bundle and short inspection brief with provenance and human verification requirements.

A report plus a small local viewer or a QGIS project can complete this checkpoint. Save an actual result before adding a service or large interface. Display stretching makes imagery readable; it never changes the numerical input to a model. An unlabelled scene has no accuracy score merely because a model produced an output.

## Connected product — checkpoints 7–9

| Area | User can do | Completion evidence |
|---|---|---|
| Event catalogue | Select supported scenes by event/date/geography; see observation age and data quality | Counts match the manifest; unsupported and empty results are explained |
| Analysis workspace | Pan/zoom an aligned map; toggle source, water, reference, validity, uncertainty and the one asset layer | Known points and bounds agree with the exported raster; legends distinguish dry, water, uncertain and unavailable |
| Run centre | Submit a bounded job, see real persisted state and recover from failure | Refresh/restart preserve truthful status; cancellation is shown only where implemented |
| Comparison view | Compare compatible baseline/model runs or descriptive event summaries | Same target, valid support, metric rules and versions are required for a scientific comparison; two dates are not labelled validated change detection |
| Reliability view | Inspect confidence status and coverage, including withheld areas | Probabilities are labelled raw or calibrated; no artificial confidence layer is invented for a deterministic baseline |
| Inspection review | Flag candidate road segments and record rationale or verification needed | Analyst annotations remain separate from machine predictions; candidates include uncertain/unobserved cases where relevant |
| Provenance panel | Follow source → preparation → method → run → export | The downloaded report retains the same identifiers, source terms and warnings |
| Export flow | Download geographic rasters, a candidate table and a readable brief | Exports reopen correctly and retain masks, units, source dates, analysis boundary and attribution |
| Saved workspace | Restore selections and analyst notes | Local single-user persistence is stated; this is not multi-user case management |

The two required journeys are **successful inspection brief** and **unsupported/interrupted input with recovery**. In the first, selection leads to a real result, asset review, caveat and export. In the second, the user sees the failed stage and next action while previous valid results remain available. A designed screen is not a connected capability until it uses the actual service outputs.

## Why this is more than printing a map

A coloured image is useful for communication, but the proposed value rests on checks and repeatable work surrounding it. None of the following benefits is assumed achieved.

| Capability | Concrete contribution to a decision workflow | How to test the proposed value |
|---|---|---|
| **Repeatability** | The same accepted input and method can be applied again without undocumented choices | Rerun a fixed packet and compare class/validity arrays, identifiers and documented numeric tolerances |
| **Scale** | A bounded batch can use the same rules for each scene and report failures individually | Count usable scenes completed within a fixed session; include rejected scenes and elapsed/active time |
| **Event comparison** | Standard summaries make differences and coverage visible across events | Compare compatible reports and verify each denominator/date; do not interpret different scenes as a validated temporal change estimate |
| **Machine-readable output** | Another program can consume masks, metadata and candidate tables without tracing colours by hand | Reopen an export and reproduce a summary from its values and manifest |
| **Uncertainty** | Areas requiring extra review can be explicit instead of hidden inside a convincing map | Measure recognition of uncertain/invalid regions, retained coverage and missed problems; confidence alone is not success |
| **Provenance** | A reviewer can find the exact source, method and settings behind a result | Ask a reviewer to identify them from the brief and reproduce the same run |
| **GIS integration** | A geographic output can be combined with permitted asset geometry | Measure overlay task completion and coordinate correctness in the application and independent GIS |
| **Failure detection** | Unsupported inputs produce a recorded failure instead of a believable wrong output | Include a known malformed scene in the task packet; check rejection, explanation and recovery |
| **Unseen-event evaluation** | The user sees evidence about unfamiliar events and observed weaknesses | Link the frozen checkpoint 4 report, including every held-out event and its limits; workflow tests do not replace this evaluation |
| **Analyst time and consistency** | Common steps and a structured report may reduce repeated effort and omissions | Compare manual and assisted tasks below, with quality constraints alongside time |

If the system is slower, uncertain areas are still missed, or the exported brief is harder to understand, record that outcome. A polished interface is not measured business value. A successful small workflow test supports only the tested tasks, participants, hardware and inputs.

## Decision-value test — protocol before results

**Question:** on a bounded historical inspection task, does FloodLens help an analyst produce a geographically correct, traceable review brief compared with manually inspecting the same scene(s)? This is a portfolio usability/engineering study, not a study of lives saved, response outcomes or commercial return.

**When:** checkpoint 5 supplies the first output/road-overlay example; checkpoint 7 freezes `docs/decision-value-protocol.md`; checkpoint 8 adds the minimum timing/state records; checkpoint 9 executes and reports the test. Use scientific-analysis/testing time already budgeted in those checkpoints. Extra participants, extra asset types and operational pilots are optional follow-on work.

### 1. Freeze the task and comparison

- Define the same deliverable for both modes: a map/overlay, candidate road IDs, uncertain or unobserved locations, an acquisition timestamp, sources/method, limitations and verification actions. This is a triage brief, not a demand for hand-drawn pixel-perfect ground truth.
- **Manual mode:** permitted imagery and the asset layer in QGIS, a legend/metadata sheet, ordinary GIS tools and the same blank brief template. The participant manually inspects scenes and records candidate segments; no FloodLens predictions are supplied. Record any other tools used.
- **Assisted mode:** the same inputs, task instructions and brief template through FloodLens, including automated processing time and manual correction/review. Record model confidence availability; a baseline-only version must say when uncertainty estimates are unavailable.
- Fix three small task packets: one representative scene; a bounded three-scene packet; and a deliberately invalid or misaligned fixture. Use approved development/demo examples selected by a stated coverage/quality rule. The malformed fixture is clearly synthetic in the report. Do not choose only scenes where FloodLens already looks good.
- Record the exact input/model/asset versions, hardware, cold/warm cache policy, time limit (proposed 30 minutes per mode per packet), training/practice instructions and operator experience before scored runs. Stop timing only when the brief is usable under the rubric, not when the first coloured pixels appear.
- Use one practice packet outside the scored packets. Counterbalance manual/assisted order across packets and record the order. Reusing scenes creates memory effects: disclose this. One developer acting as the analyst is a self-study with strong familiarity bias; it cannot stand in for professional user research.

### 2. Set the quality rubric before testing

Make a reference checklist from valid benchmark annotations where available, geometry checks and separately documented human review. Record ambiguity instead of inventing certainty. A synthetic known water/road intersection can verify geometry logic; it cannot validate real road impact. A reviewer who did not build the interface is preferable if available; otherwise identify Danny as both builder and assessor.

A brief is **usable for this demonstration** only if it opens, covers the assigned area, preserves geographic placement, names acquisition time and sources, distinguishes unavailable from dry areas, retains limitations, and identifies a verification action. Any false claim of damage/safe access, missing source identity, undisclosed missing coverage or critical geographic displacement is a critical failure. Count candidate/reference disagreements, missed review items and false flags separately; a quicker answer with more missed review items is not an unqualified improvement. Do not tune the neural model from workflow findings or reuse final-test feedback as fresh selection evidence.

### 3. Capture the measurements

| Measure | Exact observation to save |
|---|---|
| Time to usable first result | Wall-clock time from opening the assigned task to the first brief passing the rubric; active operator minutes and compute/wait time separately |
| Scene throughput | Eligible scenes completed within the fixed time limit; rejected/failed/incomplete scenes also counted |
| Repeated-run consistency | One assisted packet repeated from the same configuration; compare class/validity arrays and canonical metadata, excluding timestamps/run IDs; state tolerance for probabilities |
| Recognition of uncertainty | Number of preidentified ambiguous or unavailable areas correctly flagged, missed, or falsely flagged; record withheld coverage, not merely a confidence screenshot |
| Asset overlay | Task completion time, correct road IDs/geometry checks, candidate disagreements and whether exported overlay reopens correctly |
| Reproduction | Whether a clean run reconstructs a packet from its saved instructions and approved inputs; time, missing steps and failed checks |
| Brief usefulness | Rubric completion, omitted caveats and whether a reviewer can identify what needs verification without asking the developer; save actual comments only if obtained |
| Cost/limits | Hardware, peak memory, elapsed processing, setup/training time separately, data availability delay and any external dependency |

Save raw task records in `docs/workflow-study/task-results.csv`, outputs under a versioned artifact directory, and interpretation in `docs/decision-value-results.md`. Save a private recording only if useful and consented to by participants; notes and timestamps are sufficient.

### 4. Decide what the evidence supports

Predeclare the smallest practically worthwhile change at checkpoint 7, after a pilot and before scored runs. A starting portfolio criterion is at least one measurable gain in time, throughput, reproducibility or report completeness, **with zero critical failures and no hidden degradation in review-item quality**. Record the actual numeric threshold and reason in the protocol; do not choose it after seeing the outcome. Report paired packet results and absolute times/counts. Three packets and one operator do not justify population-wide significance claims.

Possible conclusions are: improvement under the stated conditions; a tradeoff such as faster batch handling but worse uncertain-area recognition; no meaningful difference; or an invalid test needing redesign. All are reportable. If only synthetic assets were possible, conclude about software integration and usability, not real exposure assessment. An unsuccessful decision-value test can still complete checkpoint 9 as a measured negative result, with the useful capability and unmet value claim clearly separated.

Related: [10-system-architecture](10-system-architecture.md) · [13-engineering-milestones](13-engineering-milestones.md) · [19-checkpoint-playbook](../checkpoints/README.md) · 20-linkedin-and-showcase-plan (private/source-manual context; not required by this kit) · [22-concepts-and-glossary](22-concepts-and-glossary.md)
