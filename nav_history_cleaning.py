import pandas as pd

# Load NAV history dataset
df = pd.read_csv(
    "data/raw/1788499983331-4389156d-02_nav_history.csv"
)

print("Original Shape:", df.shape)

# 1. Convert date to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Check invalid dates
invalid_dates = df["date"].isna().sum()
print("\nInvalid Dates:", invalid_dates)

# Remove records with invalid dates
df = df.dropna(subset=["date"])

# 2. Sort by fund code and date
df = df.sort_values(["amfi_code", "date"])

# 3. Check missing NAV values
print("\nMissing NAV Before Filling:", df["nav"].isna().sum())

# 4. Forward fill NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

print("Missing NAV After Filling:", df["nav"].isna().sum())

# 5. Remove duplicate records
duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows Found:", duplicate_rows)

df = df.drop_duplicates()

# Remove duplicate fund-date records
duplicate_fund_dates = df.duplicated(
    subset=["amfi_code", "date"]
).sum()

print("Duplicate Fund-Date Records:", duplicate_fund_dates)

df = df.drop_duplicates(
    subset=["amfi_code", "date"],
    keep="first"
)

# 6. Validate NAV values
invalid_navs = (df["nav"] <= 0).sum()
print("\nInvalid NAV Values (<= 0):", invalid_navs)

df = df[df["nav"] > 0]

# 7. Final sorting
df = df.sort_values(["amfi_code", "date"]).reset_index(drop=True)

# 8. Save cleaned dataset
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

# 9. Final validation
print("\n--- FINAL NAV DATA ---")
print("Final Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print(
    "Duplicate Fund-Date Records:",
    df.duplicated(subset=["amfi_code", "date"]).sum()
)
print("Minimum NAV:", df["nav"].min())
print("Maximum NAV:", df["nav"].max())
print("Date Range:", df["date"].min(), "to", df["date"].max())

print("\nCleaned NAV dataset saved successfully!")