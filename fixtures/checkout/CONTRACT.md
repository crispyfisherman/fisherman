# Checkout contract

This is a small, disposable learning fixture, not company code or a complete HTTP application. The JavaScript client demonstrates the UI boundary; the Python route is called directly by integration tests. Authentication and real network transport are outside this change.

Submitting a new order with available inventory must create exactly one order and reduce inventory by the requested quantity. Return 201 with the order ID. If order insertion fails, return a conflict and leave inventory unchanged. Invalid quantities and insufficient stock must not change either table. Duplicate order IDs are conflicts, not idempotent successes.

The requested change reorganizes transaction blocks for readability while preserving these behaviors. No public payload/schema or UI changes are intended.

Acceptance: success, insufficient stock, invalid quantity, and duplicate order conflict with unchanged inventory after the failed request.
