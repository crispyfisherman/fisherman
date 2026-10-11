# Trace output and evidence

Start with a concrete example and its scope. A table is often clearest:

| Step | Input/state | Actual symbol and file:line | Operation | Output/state | Owner/boundary |
| --- | --- | --- | --- | --- | --- |

Use exact inspected symbols. Give realistic values, labeled as illustrative when they are not runtime captures. Show a short excerpt only for code that explains the difficult step. Explain each condition or mutation that affects the scenario.

When stored/cached state is central, add a small ownership table: value → origin → authoritative owner → allowed writers → copies/caches → refresh/invalidation trigger → derived or independently stored. Explain how a stale copy affects this concrete scenario. Keep architectural changes separate from correctness findings and identify only the few symbols worth reading personally.

Label evidence:

- **Observed in source:** a reachable path, call registration, schema, or test assertion was inspected.
- **Executed:** a named check ran and produced the reported observation.
- **Hypothesis:** plausible but not established by inspected source or execution.
- **Unknown:** unavailable repository, environment, product intent, or external implementation.

Use a compact Mermaid diagram only when ordering, branching, or ownership is useful. Keep at most five nodes horizontally; split long cross-domain traces. Match diagram labels to the execution table. Do not infer cross-service rollback from a local DB transaction. Do not present retries as guaranteed without inspecting their trigger, limits, and idempotency.

Conclude the unit with the invariant, one failure path, where to change behavior, where to investigate, and the remaining gaps. Reason from current code and explicit contracts; historical docs are navigation aids that may be stale.
