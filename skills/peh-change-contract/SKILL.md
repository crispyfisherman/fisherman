---
name: peh-change-contract
description: "Define or compare a small change contract: intent, observable behavior, ownership, boundaries, invariants, and acceptance evidence. Use before implementation or to compare an implementation with an existing contract. Do not implement or review unrelated code."
---

# Change Contract

Write all engineering outputs in English. Use this as a short agreement about behavior, not a design document for the whole repository. Read [contract.md](references/contract.md) for the output shape.

1. Establish the repository and requested feature, PR, or diff. Read applicable project instructions, current contracts, and the nearest implementation. Use code as evidence of current behavior; record conflicts with documentation.
2. Trace only enough of the existing flow to identify the owner of state, writes, and external effects. Name real components, handlers, tables, jobs, and third-party boundaries. Mark unavailable repositories as unknown rather than inventing their behavior.
3. Record one concrete input and expected result, the allowed surfaces, invariants, non-goals, and meaningful acceptance checks. For UI work, distinguish visual matching from behavior, accessibility, network failures, and state transitions. For service work, name relevant transaction, retry, authorization, and schema boundaries.
4. Resolve routine choices from the repository. Ask at most one focused question at a time for a missing product decision that would materially change the implementation. Do not ask the user for details that code can establish.
5. Return a compact contract, usually 300–600 words. Save it only to the requested destination; do not automatically edit AGENTS.md, CLAUDE.md, Obsidian, or project documentation.

In comparison mode, preserve the original intent. Report `met`, `deviated`, or `unknown` for each acceptance item, with current code or executed-check evidence. Distinguish a purposeful change that needs a decision from a defect. Do not rewrite the contract to make the implementation pass.

Stop once the change has clear boundaries and checkable behavior. Recommend peh-trace-system only for an unresolved flow; do not automatically launch another workflow.
