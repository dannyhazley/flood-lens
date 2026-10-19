# Review the relevant risk, not every possible risk

Keep **Specification** and **Standards/evidence** separate. Missing requested behaviour or added unrequested scope can fail the first even if the second looks clean. Name a concrete trigger/consequence and file/artifact reference. Code smells are judgement calls, not automatic failures; lint/style belongs in CI.

- C0: clean locked install, installed package/command, real CI versus configured file, secret/data exclusion and meaningful smoke check.
- C1: rights for intended use; raw units/bands; source versus label masks; pairing/grid/CRS; audited denominators; exclusions; duplicate asset links.
- C2: related/overlapping groups together; trained preprocessing isolation; hand counts/empty-invalid cases; final-test access; matched baseline support.
- C3: tensor/target/mask shapes, valid loss denominator, gradients/updates, tiny-subset diagnostic, bounded variants, reload/preprocessing provenance.
- C4: frozen candidates; no test-driven selection; event counts; raw/calibrated claims; confidence versus coverage; negative/failure evidence retained.
- C5: CRS/transform/value/mask round trip; area units; shared inference; trusted artifacts; bounded resources; partial-output rejection; overlay not damage.
- C6: genuinely different labels/inputs, own independent split/metrics/artifact; reuse versus weight/scientific transfer; feasibility honestly labelled.
- C7: accepted versus complete, durable queue/claim/state, idempotency, restart/retry/cancel, no arbitrary input fetching, actual pipeline integration.
- C8: real versus mocked data, aligned layers, absent truth/confidence, compatible comparison, stale requests, keyboard/error states, export reopening.
- C9: clean inference/training reproduction distinction, workflow study protocol/quality/time/error bias, claim-to-evidence links, local/hosted/deployed distinction.

A review should not expose reserved results to the selecting engineer prematurely. If the phase does not permit final-event access, review its protocol/fixtures rather than inspecting final predictions. At C4 report limitations without tuning. No findings means no identified issue within checked scope, not certification of safety or generality.
