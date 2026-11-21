import pandas as pd
import sqlite3

# Read dates from datasets
nav_df = pd.read_csv("data/processed/nav_history_cleaned.csv")
transactions_df = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
aum_df = pd.read_csv(
    "data/raw/1788499984134-b0cbf625-03_aum_by_fund_house.csv"
)

# Extract dates
nav_dates = pd.to_datetime(nav_df["date"]).dt.normalize()
transaction_dates = pd.to_datetime(transactions_df["transaction_date"]).dt.normalize()
aum_dates = pd.to_datetime(aum_df["date"]).dt.normalize()

# Combine and remove duplicate dates
all_dates = pd.concat(
    [nav_dates, transaction_dates, aum_dates],
    ignore_index=True
).drop_duplicates().sort_values()

# Create date dimension
dim_date = pd.DataFrame({
    "full_date": all_dates.dt.strftime("%Y-%m-%d")
})

dim_date["date_id"] = pd.to_datetime(dim_date["full_date"]).dt.strftime("%Y%m%d").astype(int)
dim_date["year"] = pd.to_datetime(dim_date["full_date"]).dt.year
dim_date["month"] = pd.to_datetime(dim_date["full_date"]).dt.month
dim_date["day"] = pd.to_datetime(dim_date["full_date"]).dt.day
dim_date["quarter"] = pd.to_datetime(dim_date["full_date"]).dt.quarter

# Reorder columns to match database
dim_date = dim_date[
    ["date_id", "full_date", "year", "month", "day", "quarter"]
]

# Load into SQLite
conn = sqlite3.connect("bluestock_mf.db")

dim_date.to_sql("dim_date", conn, if_exists="append", index=False)

print("Date dimension loaded successfully!")
print("Total unique dates:", len(dim_date))
print("\nSample records:")
print(dim_date.head())

conn.close()