# Integration with obsidian-project-brain

The user's current [obsidian-project-brain](https://github.com/crispyfisherman/obsidian-project-brain) was read as a reference on 2026-10-11. It already separates project cockpit/personal learning from canonical Git engineering knowledge. This repository preserves that ownership model and does not modify or bundle that skill.

| Artifact | Owner | Integration |
| --- | --- | --- |
| Product intent, API contract, accepted architectural decisions, tests | Project Git repo | Save there only under the project's authorized documentation workflow; link from notes |
| Independent review and reproduction records | PR/approved engineering artifact destination, or temporary personal workspace during triage | Bind to the exact base/head; do not make personal notes authoritative review evidence |
| Reviewer Explanation | Personal `Projects/<Project>/Notes/` | Optional requested English explanation, with revision and evidence status |
| System learning ledger | Personal `Projects/<Project>/Notes/` | Optional requested traces, code anchors, learning gaps and next unit |
| Development progress | `Dev Logs/` and `Todo.md` | Update only on request and only where actual progress/status changed |
| Cross-project priorities | Global Todo + project index | Leave to obsidian-project-brain; review skills do not reprioritize work |

Use the installed skill's exact name, `obsidian-project-brain`, rather than assuming `obsidian-vault` is an alias. Both CLI sessions need access to the same vault through the existing `OBSIDIAN_VAULT` or `~/.config/agent-obsidian/vault-path` mechanism. No vault location is guessed by this repository.

Before writing, let obsidian-project-brain resolve the normalized Git remote identity and match exactly one project index. If no unique binding exists, resolve that first. A repo path or brand name alone is not enough when there are multiple checkouts/apps.

Example deliberate handoff:

```text
/obsidian-project-brain Save this peh-trace-system learning unit in the bound project's Notes using existing conventions. Include repository/revision, the concrete flow, exact symbols, confusing terms mapped to operations, what I can now explain, remaining gaps, and the next study unit. Link canonical repo docs rather than copying them. Do not create a weekly report or mark unrelated tasks complete.
```

For a review explanation, replace the learning fields with finding ID, evidence status, trigger, state changes, code anchors, decision, and the unresolved understanding gap. Do not record raw conversation transcripts by default. Neither skill automatically logs or produces reports. Old notes are orientation; current source must be reinspected when behavior matters.
