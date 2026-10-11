# Synthetic incoming review comments

These are practice inputs, not findings about any company project. Do not give them to the blind first reviewer.

- **C-01, bot:** The inventory reservation and order insertion might allow a partial update when order insertion fails.
- **C-02, human:** The order ID is interpolated directly into the SQL, which permits SQL injection.
- **C-03, bot:** Extract a repository layer and an event bus before merging this change to make the design more extensible.
