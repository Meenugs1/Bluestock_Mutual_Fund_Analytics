import pandas as pd
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
SUMMARY_DIR = BASE_DIR / "reports"

# Create folders if they don't exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

# List CSV datasets
csv_files = list(RAW_DATA_DIR.glob("*.csv"))

print("Data Ingestion Project")
print("-" * 40)

if not csv_files:
    print("No CSV files found in data/raw yet.")

else:
    for file in csv_files:
        df = pd.read_csv(file)

        print(f"\nDataset: {file.name}")
        print(f"Shape: {df.shape}")
        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nFirst 5 rows:")
        print(df.head())