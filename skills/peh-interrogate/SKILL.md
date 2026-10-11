---
name: peh-interrogate
description: "Challenge a change with an independent second review, then verify and classify findings from Claude, Codex, Cursor, or people using current code and targeted reproductions. Use to resolve disagreements, false positives, and overengineering concerns. Do not auto-fix or merge."
---

# Interrogate Findings

Write all engineering outputs in English. Read [verification.md](references/verification.md) for status definitions and the report shape. Treat every review comment as a claim, including your own findings.

1. Pin the current repository, base/head, intent, and working-tree scope. Fetch already-authorized review comments once if access is available; capture their IDs, source, and associated commit. If the head changed, reassess the findings against the new revision. Never assume an old reproduction still applies.
2. If a second independent pass is requested, arrange one fresh reviewer before showing it existing findings. When Claude authored the change, prefer a new Codex session if available; when Codex authored it, prefer a new Claude session. Read [second-review.md](references/second-review.md) only for this handoff. If another model is unavailable, state the actual model and independence limits. Do not invent Task model slugs, install another CLI, use another account, or silently invoke an API. A supplied blind review can be reused for the same revision.
3. Combine the returned findings with existing comments after the blind pass. Deduplicate by failure mechanism, not phrasing; preserve provenance. Multiple reviewers agreeing increases signal, not proof. Do not run more agents simply to obtain consensus.
4. For each meaningful finding, translate the claim into a falsifiable hypothesis: input, state, exact operations, expected observation, and observation that would refute it. Name the particular DB transaction, UI state, request, or retry rather than repeating broad terminology.
5. Attempt the smallest meaningful reproduction. Use existing unit/integration checks if they exercise the actual claim; use E2E for an issue that depends on real boundaries such as UI/API/DB coordination. Use disposable fixtures and environments. Do not change app code, shared configs, or production data. A mock that assumes the claimed result is not verification. Record preconditions, command, exit status, observed result, and missing infrastructure.
6. Classify every finding by evidence and disposition. Explain why an attractive refactor is unnecessary when a local fix suffices. If a comment is refuted, name the operation or check that disproves it. A passing happy path does not refute a failure path; a failed environment setup does not reproduce a bug.
7. Return the decision table and minimal recommendations. Include a concise comment draft for actionable findings without publishing it. Prepare a personal explanation only when requested, using peh-explain-review's format if installed; keep factual statuses unchanged.

Use one triage pass and at most one independent extra review per revision by default. After one setup failure, try one focused alternative; otherwise return `unresolved` with the exact blocker. This is a cost limit, not permission to omit relevant findings. Continue only when new evidence or a new revision justifies it.

Do not fix, resolve GitHub threads, post replies, repeatedly babysit Cursor, or merge. Stop when the actionable set and unresolved risks are clear, even when comments remain. Escalate uncertain authorization, persistent-data, cross-service, or compatibility failures to a human decision; do not label them safe for automatic merging.
