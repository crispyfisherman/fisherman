# Migrating the existing agents and understanding skill

This migration uses the three supplied agent definitions and uploaded `frontend-system-understanding` as reference material. The actual IcyBox repositories were not inspected. Treat version numbers, commands, paths, and architectural facts as candidates to verify against current code before moving them into authoritative project docs.

## What can be retired

The mobile-frontend-dev, web-frontend-dev, and product-manager files are role-specific Claude subagent definitions (`model`, `tools`, persona, delegation boundaries), rather than portable task skills. They are optional ways to route implementation work. The new harness does not itself implement features; the existing main Claude Code implementation workflow can continue doing that.

| Existing entry | Suggested migration | Material to retain |
| --- | --- | --- |
| product-manager | Retire first if it only adds an intermediate planning/dispatch step; use the main session plus peh-change-contract and existing planning skills | Real requirements/acceptance criteria, mobile/web ownership, backend dependencies |
| mobile-frontend-dev | Retire after its unique rules are reachable through current project instructions | App root/entry points, API boundary, token/storage owners, balances, launch/native workflows, local modules, analytics |
| web-frontend-dev | Retire after its unique rules are reachable through current project instructions | API/auth/SSE owners, image data source, actual type/build commands, team UI conventions |
| frontend-system-understanding | Replace after comparing two real learning/review sessions with peh-trace-system | Intent, affected architecture/state, ownership/caches, final stacked-PR behavior, critical reading paths, explicit uncertainty |

Archive retired agent files outside active `.claude/agents` and `~/.claude/agents` directories before deleting them. Do not delete files in this environment based only on the pasted definitions. Check whether other prompts or skills still reference their names, especially product-manager's dispatch specs. Then test one mobile and one web change with the main implementation session and preserved project rules.

## Put project facts in project docs

Portable harness skills describe the workflow. IcyBox-specific facts belong in the project's current `CLAUDE.md`/`AGENTS.md` and linked docs, or a local personal overlay if shared-doc edits require team agreement. Do not copy the entire IcyBox configuration into global skills. Prefer one maintained source of truth and short pointers over duplicate monoliths.

Preserve or verify these supplied constraints before retirement:

- `icebox` and `icybox` refer to the same product; locate the actual mobile/web/backend roots.
- Frontend work must ground API contracts in the Rust backend. Flag needed backend changes; do not invent compatible payloads or fake backend behavior.
- Mobile network access uses the established `lib/api.ts` layer; match actual server error codes and inspect balance wire-unit conversions, secure token ownership, Zustand/React Query/SSE state and balance-cache refresh.
- Mobile development uses the project env wrapper. Preserve the project's explicit policy for native builds/prebuilds and custom plugins/patches. Do not assume a clean prebuild is harmless.
- Read the real test command and file inclusion rules. Verify that newly added tests actually run.
- Web auth keeps backend JWT and persisted store ownership distinct. Read the actual image snapshot source and API response, rather than guessing from the item catalog.
- Verify web type checking separately from a build if the build ignores TypeScript errors. Verify whether the previously nonfunctional lint setup is still nonfunctional.
- Keep team-agreed Next Image/Link and root-chrome conventions in project scope. Blanket page/component/layout conventions are project preferences, not universal correctness laws. Do not convert architectural preferences into global lint rules or “bugs” without a concrete behavior/contract and team agreement.

Remove role boilerplate, fixed `model: opus`, exhaustive tool lists, mandatory superpowers brainstorming, and named dispatch-agent dependencies when they no longer support the user's current workflow. These are routing choices, not the underlying project constraints.

## What trace-system changes

The uploaded frontend-system-understanding covers eleven broad report steps. Preserve its useful intent/data/state/architecture principles, but make the learning unit smaller and more explicit:

- Any domain, including workers/services/DB/infrastructure boundaries; do not require UI.
- One actual caller/input and starting state, then exact operations with values and source anchors.
- A stored/cache ownership map when relevant, including refresh/derived values and multiple copies.
- Named transactions/requests/retries and one failure path, not unexplained architectural labels.
- First analyze the final combined behavior for stacked PRs; do not mistake intermediate branches for the final system.
- An optional prediction and focused correction at each important boundary, rather than a long report the user still cannot explain.
- Useful support entry points: where to modify the behavior and where to investigate a failure.

Use study mode for spare-time learning and change mode for affected before/after flows. Use peh-explain-review for a confusing finding and peh-interrogate for whether the finding is actually valid. Do not conflate these three questions.

## Migration acceptance

1. Every unique project constraint from the old agents has a verified destination or an explicit unresolved status.
2. No existing dispatch caller requires a retired agent name.
3. One small mobile and one small web feature can run under the main session with correct API/native/environment/test behavior.
4. Two learning units explain the causal flow more clearly than the old report, with exact operations rather than vague terms.
5. Existing obsidian-project-brain stays responsible for deliberate notes/progress logging.

Only then remove the archived definitions if they have no remaining use. Keeping a thin specialist agent later is reasonable when it provides measurable domain tooling or isolation; a fixed team is not required by this harness.
