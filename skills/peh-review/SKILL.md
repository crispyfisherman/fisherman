---
name: peh-review
description: "Independently review a PR or diff in a fresh context, focusing on concrete regressions and contract deviations. Use for a first review of your own or a colleague's code. Return grounded candidate findings; do not fix, publish comments, or merge."
---

# Independent Review

Write all engineering outputs in English. Read [review.md](references/review.md) for the review contract and finding format.

## Obtain independence

Run the review in a fresh agent or new CLI session. If the host already started this skill in an isolated context, perform the review directly; do not spawn another reviewer. Otherwise use one supported fresh reviewer, with high reasoning effort only when supported. Provide repository location, exact base/head or working-tree scope, intent, acceptance contract, and project instructions. Do not pass implementation chat, proposed bugs, fixes, or other reviewers' findings. Do not assume a subagent is another model or that /clear creates the same isolation as a new session.

If isolation is unavailable, state that limitation and provide a standalone handoff prompt for a new session. Do not describe a context-contaminated pass as independent. Read repository code afresh. Share source facts and behavior contracts, not a previous agent's confidence.

## Review

1. Snapshot the reviewed revision. Resolve the actual base rather than assuming main. For a branch review inspect merge-base…head; for local work explicitly cover committed changes, staged changes, unstaged changes, and relevant untracked files. Record which are included. Read-only git commands are sufficient; do not checkout or reset the user's work.
2. Read changed code, callers, state/data owners, and applicable tests. Compare requested intent and acceptance checks with actual behavior. Expand only along a concrete dependency or failure path; never generate a repository-wide system report.
3. Examine observable failure paths: authorization, state transitions, concurrency, transactions, retries, API compatibility, errors, and cleanup as applicable. Trace any candidate to a real entry point and affected operation.
4. Use established tests when useful. Prefer a focused test over a browser E2E when it proves the same claim. Keep any experimental test outside the source tree or in an isolated temporary copy. Do not alter application code or shared test fixtures. Report commands actually run and limits; do not claim a reproduction from reasoning alone.
5. Return only actionable, in-scope candidate defects with evidence. Return “No actionable findings” when appropriate. Keep unresolved concerns separate from confirmed failures. Do not require a quota of findings or classify style preferences as bugs.

Stop after one independent pass. Do not post to GitHub, reply to Cursor, resolve threads, change bot settings, push, merge, fix, or repeatedly poll for zero comments. peh-interrogate can validate these candidates later when requested. Preserve the existing review engine: if the user explicitly requests an available code-review skill, use it within the fresh worker and normalize its output into this contract; never invent a missing tool or invoke it recursively.
