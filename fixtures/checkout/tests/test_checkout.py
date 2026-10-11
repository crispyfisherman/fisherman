import unittest
from app.routes import submit_checkout
from app.store import connect


class CheckoutTests(unittest.TestCase):
    def test_creates_order_and_reserves_stock(self):
        with connect() as db:
            status, body = submit_checkout(db, {"order_id": "O-1", "sku": "TEA-01", "quantity": 2})
            self.assertEqual((status, body["status"]), (201, "created"))
            self.assertEqual(db.execute("SELECT available FROM inventory").fetchone()[0], 8)
            self.assertEqual(db.execute("SELECT quantity FROM orders").fetchone()[0], 2)

    def test_rejects_insufficient_stock(self):
        with connect() as db:
            status, _ = submit_checkout(db, {"order_id": "O-1", "sku": "TEA-01", "quantity": 20})
            self.assertEqual(status, 422)
            self.assertEqual(db.execute("SELECT available FROM inventory").fetchone()[0], 10)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM orders").fetchone()[0], 0)


if __name__ == "__main__":
    unittest.main()
