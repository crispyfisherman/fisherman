from pathlib import Path
import sqlite3


def connect():
    db = sqlite3.connect(":memory:")
    db.executescript(Path(__file__).with_name("schema.sql").read_text())
    db.execute("INSERT INTO inventory VALUES (?, ?)", ("TEA-01", 10))
    db.commit()
    return db
