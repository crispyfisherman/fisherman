# Contract shape

- **Scope:** repository, branch or commit, feature, relevant files.
- **Intent:** what a named user or caller can do after the change.
- **Example:** actual input, starting state, expected response and resulting state.
- **Ownership:** who owns UI state, persistent data, and external effects.
- **Allowed change:** specific surfaces and allowed contract/schema changes.
- **Invariants:** facts that must remain true, including failure behavior.
- **Non-goals:** explicit limits on refactoring and adjacent features.
- **Acceptance:** command or scenario, expected observation, required environment.
- **Open decisions:** unresolved product choices and missing boundaries.

Prefer one table when comparing intended and actual behavior. Refer to exact code symbols and file locations rather than phrases such as “the backend handles it.”
