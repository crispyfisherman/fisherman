---
name: peh-trace-system
description: "Learn or investigate any system through concrete, code-linked execution traces across UI, API, services, DB, queues, jobs, and external boundaries. Use for spare-time study, unfamiliar company code, incident preparation, or explaining a confusing flow. Read-only; not a full-repository report or code review."
---

# Trace System

Write all engineering outputs in English. Explain what exact operations do before naming the architectural concept. Read [trace.md](references/trace.md) for the evidence standard; in study mode also read [study.md](references/study.md). Read [obsidian.md](references/obsidian.md) only when the user requests a saved personal note.

## Choose a bounded mode

- **study:** default when learning unfamiliar code. Use a 20–30 minute learning unit around one behavior and interactive checkpoints.
- **trace:** follow one named scenario end to end, with a normal path and the relevant failure branch.
- **change:** explain how a supplied diff changes a flow and which invariants cross its boundaries. Do not turn this into an independent bug review.

If scope is broad, first inspect entry points and expose a small orientation map of domains and owners. Propose one high-value flow such as login, order creation, file delivery, a webhook, or a background job. Ask one selection question only when several materially different flows remain; otherwise state the selected scope and start. Do not read the entire repo before giving useful explanation.

## Trace from source

1. Pin repository/revision and the user's question. Read applicable instructions and inspect real entry points, registrations, imports, callers, schemas, and relevant tests. Separate observed source facts, executed observations, hypotheses, and unknowns.
   For stacked PRs that form one feature, first trace the combined final behavior from the verified base to the final head. Record ordering/dependencies and unavailable commits; then locate each change without treating intermediate states as the shipped architecture.
2. Pick a concrete caller/input and initial state. Trace the input to the observable result. Name actual UI state owners, route handlers, service methods, query/transaction blocks, tables, job producers/consumers, queues, caches, and third-party calls where present. Never force a backend-only flow to contain a frontend or guess missing services.
3. Explain each boundary's input/output shape, state owner, auth assumption, sync/async behavior, and failure/retry semantics. Cite current file:line and symbol anchors. Define unfamiliar abbreviations once. Distinguish the particular database transaction from a business operation also called a transaction.
   For significant stored or cached state, identify origin, authoritative owner, allowed writers, derived vs stored values, other copies, and invalidation/refresh triggers. Explain ambiguous or changed ownership as a fact to understand, not an automatic refactor recommendation.
4. Provide a readable execution walkthrough and a small diagram for useful branching/topology/order. Label failure, rollback, and asynchronous steps explicitly. Include a short code walkthrough for the hardest step, explaining relevant expressions and values. Use multiple small diagrams rather than a spaghetti diagram.
5. Trace one realistic failure branch, its resulting state, and what the caller sees. For a changed flow, compare before/after and identify affected owners. Explain why an invariant matters with this scenario; do not merely list design-pattern names.
6. Show “How we know”: source anchors and existing test assertions. Run focused non-destructive checks only when useful and permitted; do not require a working local environment merely to start learning. Mark unexecuted commands and unknown external behavior plainly.
7. Include “Where to change this behavior” and “Where to investigate a failure,” each with specific symbols and neighboring dependencies. This makes the unit useful when supporting teammates.

In study mode, teach one boundary at a time and use one optional prediction at each meaningful checkpoint. Wait for the user's answer before the next deep segment unless they requested a complete non-interactive report. Correct the missing causal link with code and values. Do not confuse a long report with understanding.

Keep the initial orientation short, then one flow per unit. Maintain a lightweight learning ledger only on request: revision, flow, understood boundaries, gaps, prediction outcome, and next unit. Use the existing obsidian-project-brain skill when available; do not assume an alias such as obsidian-vault is its installed name. Never install schedules or automatically log. Recheck code anchors on later visits.

Remain read-only for application code and shared configuration. Do not fix, refactor, post comments, or invoke all other skills. Stop when this flow and its gaps are clear. Suggest the next connected flow rather than asking the user to learn the whole repository.
