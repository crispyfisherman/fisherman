# Verification and decision table

Keep evidence status separate from the action decision:

| Evidence status | Meaning |
| --- | --- |
| reproduced | An executed check observed the claimed failure under named preconditions. |
| supported-by-code | Current executable paths establish the mechanism; it has not been reproduced. State assumptions and missing runtime evidence. |
| refuted | Current code or a relevant executed check contradicts the claim. Explain exactly how. |
| unresolved | Intent, code, environment, or evidence is insufficient; the finding remains open. |

| Disposition | Meaning |
| --- | --- |
| act-on | A material, in-scope defect warrants a fix; name the evidence status. |
| consider | A legitimate tradeoff needs a human decision. |
| dismissed | Refuted, duplicate, irrelevant to scope, or unjustified preference; preserve the reason. |
| needs-evidence | A material unresolved claim; do not auto-fix or auto-merge past it. |

Output: **Revision and scope**, **Reviewer independence**, **Finding table** (ID, claim, provenance, evidence status, disposition, evidence), **Executed checks**, **Minimal fix directions**, **Open decisions**.

Include file:line and symbol anchors, test commands actually run, resulting observations, and material coverage limits. Report `supported-by-code` when a deterministic path is clear but an execution environment is absent; do not demand browser E2E for every type-level or SQL claim. Report no reproduction rather than manufacturing one.
