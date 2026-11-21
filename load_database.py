
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Read datasets
fund_df = pd.read_csv(
    "data/raw/1788499983024-b042c300-01_fund_master.csv"
)

nav_df = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

transactions_df = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

performance_df = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

aum_df = pd.read_csv(
    "data/raw/1788499984134-b0cbf625-03_aum_by_fund_house.csv"
)

# Remove descriptive columns already stored in dim_fund
performance_df = performance_df.drop(
    columns=["scheme_name", "fund_house", "category", "plan"]
)

# Load datasets into tables
fund_df.to_sql("dim_fund", engine, if_exists="append", index=False)
nav_df.to_sql("fact_nav", engine, if_exists="append", index=False)
transactions_df.to_sql("fact_transactions", engine, if_exists="append", index=False)
performance_df.to_sql("fact_performance", engine, if_exists="append", index=False)
aum_df.to_sql("fact_aum", engine, if_exists="append", index=False)

print("All datasets loaded successfully!")

# Verify row counts
tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

with engine.connect() as connection:
    for table in tables:
        count = connection.exec_driver_sql(
            f"SELECT COUNT(*) FROM {table}"
        ).scalar()

        print(f"{table}: {count} rows")
