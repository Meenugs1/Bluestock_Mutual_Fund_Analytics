import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/1788499980509-304c1255-08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# 1. Convert transaction date to datetime
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

invalid_dates = df["transaction_date"].isna().sum()
print("\nInvalid Dates:", invalid_dates)

df = df.dropna(subset=["transaction_date"])

# 2. Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_transaction_types = ["Sip", "Lumpsum", "Redemption"]

invalid_transaction_types = df[
    ~df["transaction_type"].isin(valid_transaction_types)
]

print("\nInvalid Transaction Types:")
print(invalid_transaction_types["transaction_type"].unique())

# Convert standardized SIP to consistent uppercase
df["transaction_type"] = df["transaction_type"].replace(
    {"Sip": "SIP", "Lumpsum": "Lumpsum", "Redemption": "Redemption"}
)

# 3. Validate transaction amount
invalid_amounts = (df["amount_inr"] <= 0).sum()
print("\nInvalid Transaction Amounts:", invalid_amounts)

df = df[df["amount_inr"] > 0]

# 4. Validate KYC values
valid_kyc_status = ["Verified", "Pending"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc_status)
]

print("\nInvalid KYC Values:")
print(invalid_kyc["kyc_status"].unique())

# 5. Remove duplicate rows
duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows Found:", duplicate_rows)

df = df.drop_duplicates()

# 6. Final validation
print("\n--- FINAL TRANSACTION DATA ---")
print("Final Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status Values:")
print(df["kyc_status"].value_counts())

print("\nNon-positive amounts:", (df["amount_inr"] <= 0).sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nDate Type:", df["transaction_date"].dtype)

# 7. Save cleaned dataset
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned transaction dataset saved successfully!")