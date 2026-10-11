---
name: peh-explain-review
description: "Create a personal Reviewer Explanation in clear English, with exact code symbols, data values, execution paths, evidence status, and useful diagrams. Use when a review comment is difficult to understand even though its English is readable. Do not reinterpret unverified claims as facts or edit code."
---

# Reviewer Explanation

Write in English for an engineer who can read code but has not built this part of the system. Explain the particular operation under review before its technical label. Read [explanation.md](references/explanation.md) for the output shape and specificity standard. Read [obsidian.md](references/obsidian.md) only when the user requests a saved personal explanation.

1. Identify the finding, current revision, evidence status, and user's point of confusion. If only a comment is supplied, inspect the relevant code. Preserve uncertainty; never turn “may” into “does.” Refer to peh-interrogate for verification only when requested, not as an automatic additional agent pass.
2. Start with one concrete caller action and named starting values. Show the expected result and the claimed or observed result. Distinguish an illustrative value from captured runtime data.
3. Walk the smallest complete execution path, using actual file:line locations and symbol names. For each hop explain what enters, what changes, who owns it, and what leaves. If the repository lacks a boundary's implementation, mark it unknown.
4. Explain terms at the first relevant operation: identify the specific transaction and the writes within and outside it; identify the precise UI state and its owner; identify the precise request or retry and its side effect. Avoid unclear pronouns such as “it” when more than one entity is in scope.
5. Show one compact Mermaid diagram when branching, ordering, or multiple state owners materially help. Label failure branches and transaction/async boundaries; connect diagram steps to code anchors. Include a small code walkthrough for the few lines that explain the mechanism. Do not claim access to the original author's private reasoning.
6. Explain the minimal fix direction, the invariant it restores, the check that would prove it, and why a broader refactor is or is not necessary. Separate the short teammate-facing comment draft from this personal explanation. Do not publish either.
7. End with one optional prediction or teach-back question tied to the flow. If the user answers, compare their model with the code and clarify only the missing link. Do not turn every explanation into a required quiz or ask many questions at once.

Cover one unclear finding in depth by default. For several findings, give a decision index and expand the selected or highest-risk one first. Usually use 400–800 words for a deep explanation; extend only to close a specific gap. Save to Obsidian or another personal destination only on request, using the installed obsidian-project-brain workflow when available.
