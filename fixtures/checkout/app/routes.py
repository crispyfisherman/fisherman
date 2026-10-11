import sqlite3
from .service import place_order


def submit_checkout(db, payload):
    try:
        return 201, place_order(db, payload["order_id"], payload["sku"], payload["quantity"])
    except sqlite3.IntegrityError:
        return 409, {"error": "order conflict"}
    except ValueError as exc:
        return 422, {"error": str(exc)}
