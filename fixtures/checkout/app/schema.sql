CREATE TABLE inventory (sku TEXT PRIMARY KEY, available INTEGER NOT NULL CHECK (available >= 0));
CREATE TABLE orders (order_id TEXT PRIMARY KEY, sku TEXT NOT NULL, quantity INTEGER NOT NULL CHECK (quantity > 0));
