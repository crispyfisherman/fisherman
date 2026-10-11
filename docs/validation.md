# Observed validation on 2026-10-11

## Structure and installation

Six canonical skill folders passed the skill-creator quick validator and this repository's metadata/reference checks. Nine automated tests passed for installation into a temporary home, independent skill selection, existing-skill preservation, collision handling, no-write dry runs, repeated installation, adapter refresh, uninstall, and external local-workspace isolation. Both host layouts were also installed and removed in a disposable home.

The Claude and Codex CLIs themselves were not available in the execution container. Actual CLI discovery/fork behavior on the user's Mac remains a first installation check; the adapter fields and locations were checked against official documentation.

## Fresh-context behavioral trials

Workers received only raw fixture source, the requested skill, task scope, and relevant contract/inputs. They used fresh contexts. These were agents from the same model family, not a claim of independent Claude/Codex model comparison. The fixture is synthetic; no company source or production system was used.

| Workflow | Observation |
| --- | --- |
| peh-review | One independent pass found and executed a real regression: duplicate checkout returned 409 but reduced stock from 8 to 6 with only one order. The exact base preserved stock 8. Existing happy-path/insufficient-stock tests passed, exposing their coverage gap. |
| peh-interrogate | Reproduced and deduplicated that defect; refuted a supplied SQL-interpolation claim using placeholders and a real SQL-shaped value; dismissed an event-bus/repository-layer merge prerequisite as unsupported scope. Evidence status and disposition stayed separate. |
| peh-explain-review | Named the two exact SQLite transactions, UPDATE/INSERT/COMMIT/ROLLBACK operations, captured values, source locations, minimal remedy, and an optional prediction. Used a compact failure-path diagram. |
| peh-trace-system study | Explained one UI→request→response boundary with values and symbols, marked the missing HTTP adapter as outside the fixture, and stopped at one learner checkpoint. |
| peh-correct local-only | Created an external behavioral check. The target implementation failed (exit 1); a one-transaction fixture passed (exit 0); a duplicate-precheck-only fixture failed a forced insertion edge (exit 1). The target's 89 entries, including ignored files and git metadata, retained content, permissions, sizes, and timestamps. |

The correction trial also checked a successful recovery after rollback. It did not introduce shared lint, CI, hooks, type changes, or source edits. Review/study/triage targets remained clean.

## Limits

These trials exercise the initial behavior with a small UI boundary and a real Python/SQLite route/service flow. They do not establish reliability on the user's Rust/React Native/Next.js projects, cover every instruction, or prove autonomous merging is safe. peh-change-contract received structure validation; its conversational comparison behavior still needs a real feature trial. The state/cache and stacked-PR learning refinements were incorporated from the user's uploaded skill and remain pilot targets.

Use the five-PR and three-study-unit plan in testing.md before deciding which steps to automate. Track actual host duration/token metrics where available and record unresolved evidence honestly.
