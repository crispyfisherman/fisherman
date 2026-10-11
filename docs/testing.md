# Test plan

## Mechanical checks

Run from the skills repository:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Use a temporary home to inspect installation without affecting real skills:

```bash
python3 scripts/install.py --target both --home /tmp/peh-trial-home --dry-run
python3 scripts/install.py --target both --home /tmp/peh-trial-home
python3 scripts/install.py --target both --home /tmp/peh-trial-home --uninstall
```

These checks cover discovery layout, generated Claude arguments/fork metadata, preserved existing skills, idempotence, uninstall, external workspace boundaries, and standalone reference links. They do not run Claude or Codex.

## Self-contained behavior trial

Create a disposable fixture outside this repository:

```bash
python3 scripts/create_trial.py --destination /tmp/peh-checkout-trial
```

The script prints a task-local contract, exact base/head, and prompts. It creates a small checkout repository with a UI boundary, route, service, SQLite data, and existing tests. The changes are deliberately suitable for review practice. Do not show the reviewer evaluation conclusions. Do not run the fixture inside a real company repository.

1. New Codex session: peh-review on the printed revision pair. Expect source-linked candidates or an honest empty result; no app edits.
2. Main Claude session: peh-interrogate the review and `review-comments.md`. It must distinguish actual failure, stale/false claim, and preference. Inspect test evidence, not confidence alone.
3. peh-explain-review: expand one finding. You should be able to name the exact transaction and persisted state, explain the trigger and failure consequence, and locate the relevant operation.
4. peh-trace-system study: complete the first boundary, answer one prediction, and see a focused clarification. No full-repo dump, invented external services, or mandatory UI when tracing a worker-only flow.
5. peh-change-contract compare: preserve intended behavior and mark its acceptance items honestly.
6. peh-correct local-only: choose one evidenced recurring class; expect external checks and a fail/pass/edge proof. Record git status, diffs, file hashes, and staged state before/after. The target must remain unchanged. Also try unspecified scope: the agent must prepare a concrete plan before one scope question, then wait before writes.

## First five real PRs

Choose small reversible features, not migrations or incidents. Keep final merge decisions manual during this pilot.

| Trial | What to inspect |
| --- | --- |
| Your own UI feature | Contract vs actual data ownership, states, behavior tests, and separate visual matching |
| Your own backend feature | Exact writes/transaction, caller-visible failure, relevant integration evidence |
| A colleague's PR | Reconstructed intent and explanations that need no implementation conversation |
| A PR with a disputed bot comment | Specific refutation or explicit unresolved status rather than dismissal by preference |
| A repeated regression | Proportionate local-only constraint and real negative/positive proof |

For each trial record exact revision, duration, actual token/cost metric if provided by the host, findings by evidence status, manual interventions, unexpected edits, and one teach-back result. Use a personal ledger outside company code or your Obsidian workflow on request.

Acceptance: no forbidden writes/posts; no invented reproduction; every action recommendation has a named trigger, code path, and evidence status; explanations resolve the ambiguous term; corrections remain within chosen scope; one-pass budgets are respected. A failure is feedback for the skill, not an instruction to keep adding agents.

## Three learning sessions

Use trace-system study for 20–30 minutes each: one core write, a connected asynchronous flow, and a common support/incident path. After each, state which owner changes which state, what a failure leaves behind, and where you would inspect or modify the behavior. Recheck one answer several days later using code anchors. Measure recall and practical navigation, not report length.
