import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

print("========== DATABASE INTEGRITY CHECK ==========\n")

# Check foreign key violations
cursor.execute("PRAGMA foreign_key_check;")
violations = cursor.fetchall()

if violations:
    print("Foreign key violations found:")
    print(violations)
else:
    print("No foreign key violations found!")

# Check date records
cursor.execute("SELECT COUNT(*) FROM dim_date;")
print("Date records:", cursor.fetchone()[0])

# Check tables
tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\n========== FINAL TABLE COUNTS ==========\n")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table}: {cursor.fetchone()[0]}")

conn.close()