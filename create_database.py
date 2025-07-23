import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    order_items TEXT NOT NULL,
    total_price REAL NOT NULL,
    payment_mode TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully.")
