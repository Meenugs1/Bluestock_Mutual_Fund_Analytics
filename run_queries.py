import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

# Read SQL file
with open("queries.sql", "r") as file:
    sql_content = file.read()

# Remove SQL comment lines
cleaned_lines = []

for line in sql_content.splitlines():
    if not line.strip().startswith("--"):
        cleaned_lines.append(line)

cleaned_sql = "\n".join(cleaned_lines)

# Split into individual queries
queries = cleaned_sql.split(";")

print("=" * 70)
print("BLUESTOCK MUTUAL FUND ANALYTICS - SQL RESULTS")
print("=" * 70)

query_number = 0

for query in queries:
    query = query.strip()

    if not query:
        continue

    query_number += 1

    print(f"\n{'=' * 70}")
    print(f"QUERY {query_number}")
    print("=" * 70)

    try:
        df = pd.read_sql_query(query, conn)

        print(f"Total rows returned: {len(df)}")
        print("\nResults:")

        if df.empty:
            print("No results found.")
        else:
            print(df.head(10).to_string(index=False))

            if len(df) > 10:
                print(f"\nShowing 10 of {len(df)} rows.")

    except Exception as e:
        print(f"Error executing query: {e}")

conn.close()

print("\n" + "=" * 70)
print("SQL ANALYSIS COMPLETED")
print("=" * 70)