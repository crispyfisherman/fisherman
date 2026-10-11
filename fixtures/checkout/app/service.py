def reserve_stock(db, sku, quantity):
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    updated = db.execute(
        "UPDATE inventory SET available = available - ? WHERE sku = ? AND available >= ?",
        (quantity, sku, quantity),
    )
    if updated.rowcount != 1:
        raise ValueError("insufficient stock")


def place_order(db, order_id, sku, quantity):
    with db:
        reserve_stock(db, sku, quantity)
        db.execute(
            "INSERT INTO orders (order_id, sku, quantity) VALUES (?, ?, ?)",
            (order_id, sku, quantity),
        )
    return {"order_id": order_id, "status": "created"}
