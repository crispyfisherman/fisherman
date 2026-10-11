# Review contract

Record repository, base SHA, head SHA, working-tree coverage, intent source, reviewer/engine identity, and checks performed. A high effort setting and a separate thread improve independence; they do not establish correctness or model diversity.

For each finding use a stable ID and:

- **Claim:** a concrete behavior, not “this might be unsafe.”
- **Trigger:** named caller/user, input, and relevant initial state.
- **Expected / actual:** observable difference and who is affected.
- **Path:** entry point → changed symbol → data or external effect; cite current file:line locations and symbols.
- **Evidence:** executed test or reproducible code path; identify any assumption.
- **Status:** `reproduced`, `supported-by-code`, or `unresolved`; never imply a test ran when it did not.
- **Severity:** impact and realistic likelihood, not the size of a possible refactor.
- **Minimal remedy direction:** the smallest behavior change that would address the defect. Do not implement it.

An existing defect outside the diff is backlog unless the change exposes or worsens it. A formatter issue, speculative optimization, generic “best practice,” and an alternative architecture are not correctness findings by themselves.

Project instructions and docs are useful context but may be stale. Name the conflicting executable behavior and the unresolved intended behavior; do not silently treat either as authoritative product intent.
