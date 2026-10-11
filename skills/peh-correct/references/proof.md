# Selecting and proving a constraint

- Prefer one source of truth or one state owner when a small bounded change removes a class of errors.
- Prefer types when an invalid state or unauthorized call can be rejected at compile time without harming the public contract.
- Prefer a lint/static check when the prohibited pattern is reliably recognizable. Name structural limitations of a text-based check; avoid substring scans that confuse comments, string literals, or valid neighboring cases.
- Prefer a behavioral test for ordering, transactions, retries, state transitions, authorization, and runtime edge cases. Avoid tests that merely duplicate the implementation.
- Use docs for judgment and missing intent, not as a claim that recurrence is prevented.

For each rule capture: actual previous mistake; smallest invalid example; valid counterpart; realistic edge case; exact check command; expected and observed exit/result; known evasion/false-positive limits.

For broad existing debt, prefer a baseline or changed-code rule rather than rewriting everything. Specify what the rule can and cannot detect. Show that it fails for the mistake because of the intended invariant, not because the fixture has a syntax error or missing dependency.

A failed check on a disposable historical copy and a passing current check are useful evidence. They do not prove that every future variation is prevented. Do not weaken established tests or rules to make the demonstration pass.
