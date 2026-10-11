# Personal explanation shape

1. **The concrete problem:** actor, starting values, trigger, expected result, actual or claimed result, evidence status.
2. **Names used here:** a small mapping of confusing words to actual operations, objects, and symbols.
3. **Execution walkthrough:** step, input, symbol/file:line, operation, output, owner.
4. **Flow diagram:** only when it contributes; keep paths and uncertainty accurate.
5. **Why the finding matters:** invariant, affected actor, realistic consequence.
6. **Decision:** act-on/consider/dismissed/needs-evidence, minimum remedy, test, remaining uncertainty.
7. **Short PR comment draft:** optional, concise, English, grounded in the same evidence.
8. **Prediction:** one optional question that tests the user's model of the path.

Bad: “The transaction boundary allows partial updates.”

Good specificity: “In this illustrative example, update_order() commits orders.status='paid'. send_receipt() then fails before receipts.sent_at is written. Name the exact transaction block and the two call sites from the inspected repository before asserting this behavior. The order change and receipt marker could end up in different states. Whether that is a defect depends on the retry and delivery contract.”

The example is a writing standard, not a claim about the user's repository. Use that repository's actual symbols and evidence in the real report. Explain observed mechanisms and explicit tradeoffs, not generic architecture lessons.
