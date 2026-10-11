# Future automation

The shipped skills are workflows, not an autonomous PR service. Skills describe behavior; host permissions, tests, CI, and merge policies provide enforceable controls.

After the manual trials, consider automating only a step that has reliable inputs and observable output. Keep every result bound to repository + base/head + working-tree scope. Invalidate affected review/repro evidence on a new head. Reuse unaffected evidence only when its inputs and dependency path are unchanged and the reason is explicit.

| Step | Useful later automation | Human decision that remains |
| --- | --- | --- |
| Contract comparison | Flag unexpected surfaces/ownership or missing acceptance evidence | Product intent and accepted tradeoffs |
| First review | One fresh pass after required checks | Material unresolved findings |
| Bot triage | One snapshot and deduplication per revision | Ambiguous intent or unsupported/high-impact claims |
| Reproduction | Focused disposable checks and captured results | Missing/inaccurate environment and unsupported boundaries |
| Correction | Run an adopted local constraint | Promote to shared lint/types/architecture/CI |
| Personal explanation | Expand selected unclear findings | Your understanding and escalation judgment |
| Merge | Only a separately authorized controller with branch protections and exact revision checks | Risk eligibility and repository-specific merge policy |

Do not optimize for zero review comments. A resolved defect, documented refutation, or explicit decision is completion; new speculative comments are not a mandate to refactor. Limit one triage pass and one optional independent extra reviewer per revision unless new evidence warrants more.

For any later automatic fixing/merging, separately define allowed file surfaces, maximum change size, checks that must pass, uncertain finding rules, polling/iteration limits, and a human escalation path. Permission to use these skills is not permission to post PR replies or merge code. Changes to the company's Cursor bot remain outside this repository's scope.
