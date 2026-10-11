# Write scope

| Scope | Allowed result | Authorization |
| --- | --- | --- |
| local-only | External personal check, local config, and disposable proof fixtures; target repo remains untouched | Explicit scope choice or existing session authorization |
| project | Named source/test/type/lint/CI changes following team conventions | Explicit scope and concrete allowed changes; obey team policies |
| proposal | Concrete rule, file plan, examples, and proof design in the response | Default safe preparation while scope is undecided |

Use the helper in this skill's scripts directory, not a relative path in the target codebase:

`python3 PATH_TO_THIS_SKILL/scripts/local_workspace.py --repo /absolute/repo --create`

It chooses `${XDG_DATA_HOME:-~/.local/share}/personal-engineering-harness/projects/NAME-HASH`. NAME-HASH is based on the canonical git top-level path; an explicit `--base-dir` can select another external private destination. It rejects paths inside the target repository. Locate the installed skill path through the host or the skill file that was loaded; do not assume the current directory is the skills repo.

Do not overwrite an existing personal check without inspecting it. Avoid recording secrets in reports. Preserve the target's tracked, untracked, and staged state during local-only work. A check should print a specific fix direction and a nonzero exit status for a violation. A local convention is not evidence of a team requirement.

Promote a proved local rule only after the user authorizes the named project changes. Do not mistake an ignored file for a local-only write: ignored files can still change development behavior for the user or their agents.
