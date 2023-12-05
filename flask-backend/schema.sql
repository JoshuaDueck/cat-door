--- Some tables required for the cat door application:
--- 1. cats (id, name, rfid)
--- 2. logs (timestamp, cat_id, action)

DROP TABLE IF EXISTS cats;
DROP TABLE IF EXISTS logs;

CREATE TABLE cats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rfid TEXT NOT NULL
);

CREATE TABLE logs (
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    cat_id INTEGER NOT NULL,
    action TEXT NOT NULL
);
