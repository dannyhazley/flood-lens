# Checkpoint budgets, gates and intermediate releases

This is the **authoritative budget ledger**. [Note 19](../checkpoints/README.md) gives ordered tasks; [note 21](../STATE.md) records actual progress. All work remains planned. A gate passes on evidence, never because its hours have elapsed.

## The commitment in hours

| Checkpoint | Work | Hours | Useful release |
|---|---|---:|---|
| 0 | Repository and environment setup | 3–5 | A reproducible empty project; no data/model claim |
| 1 | Data rights, provenance and raster-quality audit | 17–20 | Accepted dataset and audit, or precise source rejection |
| 2 | Event-aware evaluation and simple baseline | 20–30 | Frozen protocol and reproducible development baseline |
| 3 | Compact segmentation model and controlled experiments | 30–45 | Loadable candidate and bounded development comparison |
| 4 | Unseen-event evaluation, failures and confidence | 30–45 | Locked final results and honest reliability report |
| 5 | Dependable geospatial inference workflow | 25–35 | Local input-to-output analysis plus one asset overlay |
| 6 | One independently evaluated land-cover task | 35–45 | Independent second result and measured reuse ledger |
| 7 | Service contracts, job state and product workflow | 25–35 | Persistent bounded service and workflow-test protocol |
| 8 | Interactive map and analysis workspace | 55–80 | Connected inspection workflow over real outputs |
| 9 | Hardening, reproduction, demo and final case study | 25–35 | Reproducible release and measured decision-value result |
| **C0–C6 planned work** | Analytical and engineering core | **160–225** | Six substantive releases plus setup |
| **Core contingency** | Explicitly allocated troubleshooting | **20–35** | No automatic extra features |
| **C0–C6 envelope** | Core including contingency | **180–260** | Can stand alone |
| **C7–C9 planned work** | Service, workspace and release | **105–150** | Complete local product |
| **Product contingency** | Explicitly allocated troubleshooting | **15** | Fixed additional reserve |
| **C7–C9 envelope** | Product including contingency | **120–165** | Optional decision to continue after core |
| **Full planned work** | C0–C9 | **265–375** | |
| **All contingency** | 20–35 + 15 | **35–50** | |
| **Full route** | Planned work + contingency | **300–425** | Complete portfolio product route |

The first meaningful checkpoint is the **C0–C2 review at 40–55 hours**: repository, source audit, valid split design and simple baseline. C0 itself is **3–5 hours**. C0 plus C1 is 20–25 hours; setup was previously hidden inside milestone 1 and is now separate, not counted twice. The first five substantive checkpoints through C5 take **125–180 work hours**, before allocated contingency.

“400+ hours” describes the upper part of this full route, up to 425 hours, not a second mandatory extension beyond 425. The lower endpoint assumes a usable source, straightforward environment and restrained presentation. The upper endpoint allows deeper learning and integration. If actuals exceed the ceiling, agree a new estimate or reduce scope; do not conceal extra time. Optional hosting and new scientific tasks are not automatically included.

## Where the work time goes

These are two views of the same hours, not additional budgets. Log one primary category per time entry; avoid counting the same debugging hour as both learning and testing. Scientific analysis means interpreting evidence and designing comparisons, not merely running code. Presentation means preparing a figure/demo/draft; publishing is a separate deliberate action.

| C | Learning | Implementation | Scientific analysis | Testing | Documentation | Presentation | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1–2 | 0 | 0.5 | 0.5–1 | 0–0.5 | 3–5 |
| 1 | 3–4 | 4–5 | 5 | 2–3 | 2 | 1 | 17–20 |
| 2 | 3–4 | 6–9 | 5–8 | 3–4 | 2–3 | 1–2 | 20–30 |
| 3 | 4–6 | 10–15 | 8–12 | 4–5 | 3–5 | 1–2 | 30–45 |
| 4 | 4–6 | 5–8 | 12–18 | 4–5 | 3–5 | 2–3 | 30–45 |
| 5 | 3–4 | 10–14 | 2–3 | 6–8 | 3–4 | 1–2 | 25–35 |
| 6 | 5–6 | 10–13 | 10–13 | 5–6 | 3–4 | 2–3 | 35–45 |
| 7 | 4–5 | 12–18 | 2–3 | 4–5 | 2–3 | 1 | 25–35 |
| 8 | 6–9 | 28–40 | 5–8 | 10–14 | 3–4 | 3–5 | 55–80 |
| 9 | 1–2 | 5–7 | 5–7 | 7–9 | 4–6 | 3–4 | 25–35 |

**Optional work:** zero additional committed hours. Each checkpoint names possibilities, but taking one requires substituting an equivalent task explicitly or recording a separately approved extension. Do not spend contingency on new models, cloud services, paired change detection or extra dashboards. Unused contingency is not a target to consume.

## Cumulative work before contingency

| Through checkpoint | Work hours | Decision |
|---|---:|---|
| C0 | 3–5 | Environment works; begin source decision |
| C1 | 20–25 | Rights and raster acceptance pass, or change source |
| C2 | 40–55 | First investment review; continue only with a defensible baseline/protocol |
| C3 | 70–100 | Freeze candidates; better results are not guaranteed |
| C4 | 100–145 | Scientific result is recorded, including negative findings |
| C5 | 125–180 | Dependable standalone water-analysis release |
| C6 | 160–225 | Core outcome; add 20–35 contingency only as actually allocated |
| C7 | 185–260 | Stable service and bounded user journeys |
| C8 | 240–340 | Connected product ready for measured workflow assessment |
| C9 | 265–375 | Full release; +35–50 total reserve gives 300–425 |

## Gate and contingency discipline

At every checkpoint save `docs/checkpoints/CN.md`, the revision/run identifiers, acceptance checks, actual hours by category, limitations and one next task. Add any reserve allocation to a ledger with date, reason, hours, remaining reserve and effect on scope. Elapsed machine time and human effort are different: record both, but this plan estimates human project hours. Do not silently count an unattended training night as eight hours of personal work.

A completed rejection report or failed hypothesis is a useful intermediate release, but it does not pass a missing capability gate. C7 can follow an honestly documented C6 feasibility outcome if C5 works and the scope decision is recorded; the overall claim must then say transfer remains unproven. A valid negative baseline/model comparison can pass C3/C4. A broken split or missing georeference cannot.

Cut optional polish and extra experiments first. Preserve rights, independent evaluation, validity masks, geographic correctness, provenance and decision-value measurement. Keep one asset type and two complete product journeys. Sources, decisions and old budget variants remain in the archive (private/source-manual context; not required by this kit).

## Teaching-depth clarification — CI from C0

The expanded build guides explain work already needed for a dependable release, including explicit CI at C0 and staged delivery later. The base ledger remains 300–425 h including reserve; it has not silently gained an unbudgeted infrastructure track. CI requires no full model, source download or live host.

C0’s 3–5 h is a **guided setup estimate**, not an estimate for independently learning all Git/packaging/Actions concepts from zero. If those topics are new, explicitly allocate 2–3 h from the existing 20–35 h core contingency and record the reason. C0 may then take 5–8 actual hours; the 40–55 h first-review figure remains base work, and actual first-review effort with that allocation may be 42–58 h. This is transparent reserve use, not a second total or a promise to fit an unfamiliar task. Re-estimate if repeated setup blockers consume more.

At every checkpoint, record what you can explain/repeat independently. Repetition exercises should be small thought experiments or synthetic checks inside the learning allocation; rebuilding the entire software twice would need a new estimate.
