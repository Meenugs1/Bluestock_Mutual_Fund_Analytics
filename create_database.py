import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Read schema.sql
with open("schema.sql", "r") as file:
    schema = file.read()

# Execute schema
cursor.executescript(schema)

conn.commit()

# Verify tables
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")

tables = cursor.fetchall()

print("Database created successfully!")
print("\nTables created:")

for table in tables:
    print("-", table[0])

conn.close()