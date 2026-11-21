from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

fund_master_file = list(RAW_DATA_DIR.glob("*fund_master*.csv"))[0]

df = pd.read_csv(fund_master_file)

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\n--- FUND HOUSE ANALYSIS ---")
print("Unique fund houses:", df["fund_house"].nunique())
print(df["fund_house"].value_counts())

print("\n--- CATEGORY ANALYSIS ---")
print(df["category"].value_counts())

print("\n--- SUB-CATEGORY ANALYSIS ---")
print(df["sub_category"].value_counts())

print("\n--- RISK CATEGORY ANALYSIS ---")
print(df["risk_category"].value_counts())

print("\n--- PLAN ANALYSIS ---")
print(df["plan"].value_counts())
print("\n--- DATA QUALITY CHECK ---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate AMFI Codes:")
print(df["amfi_code"].duplicated().sum())

print("\nDuplicate Scheme Names:")
print(df["scheme_name"].duplicated().sum())

print("\nUnique AMFI Codes:")
print(df["amfi_code"].nunique())

print("\nUnique Scheme Names:")
print(df["scheme_name"].nunique())

print("\n--- NAV HISTORY INSPECTION ---")

nav_history_file = list(RAW_DATA_DIR.glob("*nav_history*.csv"))[0]
nav_df = pd.read_csv(nav_history_file)

print("\nNAV History Shape:", nav_df.shape)

print("\nNAV History Columns:")
print(nav_df.columns.tolist())

print("\nFirst 5 NAV Records:")
print(nav_df.head())

print("\nData Types:")
print(nav_df.dtypes)
print("\n--- NAV HISTORY INSPECTION ---")

nav_history_file = list(RAW_DATA_DIR.glob("*nav_history*.csv"))[0]
nav_df = pd.read_csv(nav_history_file)

print("\nNAV History Shape:", nav_df.shape)

print("\nNAV History Columns:")
print(nav_df.columns.tolist())

print("\nFirst 5 NAV Records:")
print(nav_df.head())

print("\nData Types:")
print(nav_df.dtypes)
print("\n--- AMFI CODE VALIDATION ---")

fund_codes = set(df["amfi_code"])
nav_codes = set(nav_df["amfi_code"])

common_codes = fund_codes.intersection(nav_codes)
missing_codes = fund_codes.difference(nav_codes)
extra_codes = nav_codes.difference(fund_codes)

print("Fund Master unique codes:", len(fund_codes))
print("NAV History unique codes:", len(nav_codes))
print("Matching codes:", len(common_codes))
print("Codes missing in NAV History:", len(missing_codes))
print("Extra codes in NAV History:", len(extra_codes))

print("\nMissing AMFI Codes:")
print(missing_codes)
print("\n--- NAV DATA QUALITY CHECK ---")

print("\nMissing Values:")
print(nav_df.isnull().sum())

print("\nDuplicate NAV Records:")
print(nav_df.duplicated().sum())

print("\nDuplicate Scheme-Date Records:")
print(nav_df.duplicated(subset=["amfi_code", "date"]).sum())

print("\nNon-positive NAV Values:")
print((nav_df["nav"] <= 0).sum())

print("\nNAV Date Range:")
print(nav_df["date"].min(), "to", nav_df["date"].max())