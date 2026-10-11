# Personal Engineering Harness

A portable, English-only workflow for Claude Code implementation, independent Codex review, evidence-based decisions, and learning unfamiliar systems. Six individually installable skills; no Cursor configuration changes, mandatory agent team, automatic PR replies, or automatic merging.

## Install

Requires Python 3.9+, Git, and your existing Claude Code and/or Codex CLI. No package installation or API key is required by these skills. Keep this repository in a permanent folder, for example `~/dev/fisherman`.

```bash
mkdir -p ~/dev
git clone https://github.com/crispyfisherman/fisherman.git ~/dev/fisherman
cd ~/dev/fisherman
python3 scripts/install.py --target both --dry-run
python3 scripts/install.py --target both
```

Use `--target claude` or `--target codex` to install one host. `--skills peh-trace-system peh-review` selects a subset. Existing skills with conflicting names are preserved and installation stops with their paths; there is no force-overwrite option.

If you already installed the earlier Git bundle, run its installer with `--target both --uninstall` before installing this clone. Keep the old folder until you have confirmed the new installation. Clone the published repository for future updates; the earlier bundle and this GitHub upload have separate commit histories. Use `git pull --ff-only` followed by rerunning the installer to update the skills.

The installer links Codex skills under `~/.agents/skills` and Claude skills under `~/.claude/skills`. Claude variants are generated locally: every skill requires explicit invocation; `peh-review` uses `context: fork`, a general-purpose agent, foreground execution, and high effort. The fork receives the invocation arguments, not the implementation conversation. Codex variants use explicit invocation metadata; their review instructions require a fresh reviewer/session and honest disclosure when isolation is unavailable. Neither host is guaranteed to run a different model simply because it starts a subagent.

Use `/skills` or the skill picker to confirm discovery. In Claude Code type `/peh-review ...`; in Codex type `$peh-review ...`. Restart a CLI if discovery has not refreshed. For an older CLI that rejects Claude's `effort`/`background` fields, update the CLI or remove only those generated adapter fields and use foreground/high effort through the host's supported controls. The canonical skills remain host-neutral.

After editing or pulling this repository, rerun the installer to refresh Claude adapters. Codex links read the canonical files directly. Uninstall only this repo's links with `python3 scripts/install.py --target both --uninstall`. Move the repo only after uninstalling; reinstall at the new path.

## Skills and boundaries

| Skill | Purpose | Default output | Writes |
| --- | --- | --- | --- |
| peh-change-contract | Agree on intent and compare expected vs actual implementation | Short behavior contract or comparison | Only a requested report destination |
| peh-review | Fresh-context independent first review | Candidate findings and scope/evidence | No application or shared config writes |
| peh-interrogate | Blind second review when requested; verify all supplied findings | Evidence status and action decisions | No application or shared config writes |
| peh-explain-review | Personal explanation of a confusing finding | Concrete values, code walkthrough, useful Mermaid | Only a requested personal report |
| peh-correct | Prevent a recurring mistake with a proven constraint | One scoped rule and fail/pass proof | Explicit local-only/project/proposal scope |
| peh-trace-system | Learn any system one execution flow at a time | Orientation, causal trace, failure path, checkpoints | No application or shared config writes |

The `peh-` prefix avoids collisions with installed Matt Pocock, Ponytail, code-review, or pstack commands. The skills can coexist with those tools and the existing obsidian-project-brain workflow. They do not assume those plugins are installed or replace their implementations. See [docs/obsidian.md](docs/obsidian.md) for deliberate personal-note handoffs and [docs/migration.md](docs/migration.md) for retiring the old IcyBox role agents and frontend-system-understanding skill without losing project constraints.

## Development order

1. **Checkpoint A — intent:** use peh-change-contract before implementing a single feature. Review ownership, allowed change boundaries, and acceptance examples yourself. Use peh-trace-system for only the uncertain boundary, if needed.
2. **Implement:** use your existing Claude Code workflow. Have it implement the contract and run appropriate behavior checks. For frontend work, keep screenshot/design comparison separate from functional correctness.
3. **Checkpoint B — planned vs actual:** compare the diff against the unchanged contract. Unexpected ownership, API, schema, or external-effect changes are decision points.
4. **Independent review:** start a new Codex session for a Claude-authored change and invoke peh-review with the exact scope and intent. For colleagues' PRs, this can be the starting step; reconstruct intent from the PR/contract.
5. **Evidence triage:** give peh-interrogate the independent findings and any existing Cursor/human comments. Ask for a blind second pass only if the first pass was not already independent or the risk justifies another model. Run the smallest meaningful repro; use E2E when real system boundaries matter.
6. **Checkpoint C — understand the decision:** use peh-explain-review for the finding you cannot confidently explain. Trace the affected flow in depth only for an unclear, high-risk, or unexpectedly changed boundary.
7. **Fix and verify:** use the existing implementation agent for the approved minimal fixes. Recheck affected findings against the new head and run relevant checks. A prior review is not automatically valid after new changes.
8. **Prevent recurrence:** use peh-correct only when a mistake repeats or you deliberately want prevention for a serious case. Do not run it on every PR.

This order provides intent before code, independence before synthesis, and evidence before a fix. Personal explanation closes a concrete understanding gap without imposing a full-system report on every PR. Correction happens after a mistake is understood, so it does not turn speculation into permanent tooling.

Example invocation packet, with real values substituted:

```text
# Claude Code, before implementation
/peh-change-contract Define checkout behavior, ownership, non-goals, and acceptance checks. Do not implement.

# New Codex session, after implementation
$peh-review Review BASE_SHA...HEAD_SHA plus the explicitly listed local changes. Intent: [contract]. Do not edit code or read other review reports.

# Main session, after blind review
/peh-interrogate Verify the attached findings and Cursor comments against HEAD_SHA. Use smallest relevant reproductions. Do not fix or publish anything. No additional blind pass is needed.

# Personal decision help, only for unclear findings
/peh-explain-review Explain F-01. Name the precise operations, state owners, DB writes, and transaction. Use concrete values, code anchors, and a failure-flow diagram.

# After a recurring mistake
/peh-correct Prevent [evidenced mistake]. Scope: local-only. Keep the target repository completely untouched; prove the check rejects the bad case and accepts valid cases.
```

## Learning company code in spare time

Use **peh-trace-system in study mode**. There is no PR requirement, and it works for frontend, backend, infrastructure glue, background workers, and cross-service flows.

```text
/peh-trace-system study. I have 25 minutes. Inspect this repository and select one important flow that would help me support a teammate. Explain one boundary at a time in English, name the exact symbols and values, and ask one prediction question at a time. Do not edit code or generate a whole-repository report.
```

In Codex use `$peh-trace-system` with the same request. If you want a complete non-interactive explanation, say so. If a phrase remains unclear, ask it to expand just that step with concrete values and the relevant expressions. The skill's output must distinguish source facts, executed evidence, hypotheses, and unavailable boundaries.

Suggested sessions: a core write → its background job/retry → permissions → a read/cache path → an incident path. Adjust to the actual repository. Revisit one prediction after a few days: identify where you would change the behavior and where you would investigate its failure. Save a short learning ledger through obsidian-vault only when you ask; no scheduled logs or automatic weekly reports.

## Local-only correction

`local-only` means external personal state, not ignored files inside the company repo. The workspace helper uses `${XDG_DATA_HOME:-~/.local/share}/personal-engineering-harness/projects/NAME-HASH`, isolated by the canonical repo path. The skill creates checks/config/proof fixtures there and reads the target code. Shared lint, manifests, CI, hooks, agent instructions, and source remain unchanged.

The scope can be supplied in the invocation. If omitted, the skill first prepares the concrete rule and file plan, then asks once: local-only, project, or proposal. A local text/static check has stated limitations and cannot substitute for real type enforcement or team CI. Promote it later with explicit authorization for the named project changes.

## Test and adoption

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` for structure and installer/workspace checks. See [docs/testing.md](docs/testing.md) for behavioral trials and real-PR acceptance criteria, and [docs/automation.md](docs/automation.md) for future automation boundaries. These checks do not claim that an LLM will follow every instruction.

Start with five low-risk PRs and three 20–30 minute study units. Track elapsed time, actual host token/cost metrics when available, reproduced/refuted/unresolved findings, unnecessary edits, and whether you can explain the key invariant. Do not fabricate token counts. This repository intentionally ships no automatic polling, PR posting, fixing, hooks, or merging. Decide which steps to automate after the trials.

## Sources and compatibility

Installation and host-adapter behavior were checked on 2026-10-11 against [OpenAI skills documentation](https://developers.openai.com/codex/skills/) and [Claude Code skills documentation](https://code.claude.com/docs/en/skills). The prevention and multi-model challenge concepts were informed by [pstack correct](https://github.com/cursor/plugins/blob/main/pstack/skills/correct/SKILL.md) and [pstack interrogate](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md); these files are original, portable instructions rather than copied Cursor-only implementations.

CLI installation/discovery, model routing, and project environments must still be verified on your own machine. A clean review or agreement between two models is not proof of correctness.
