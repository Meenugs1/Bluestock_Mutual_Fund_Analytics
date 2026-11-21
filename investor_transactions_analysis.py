from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

transactions_file = list(RAW_DATA_DIR.glob("*investor_transactions*.csv"))[0]

df = pd.read_csv(transactions_file)

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())
print("\n--- TRANSACTION DATA QUALITY CHECK ---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Investor-Date-Scheme Records:")
print(df.duplicated(
    subset=["investor_id", "transaction_date", "amfi_code", "transaction_type"]
).sum())

print("\nNon-positive Transaction Amounts:")
print((df["amount_inr"] <= 0).sum())

print("\nTransaction Date Range:")
print(df["transaction_date"].min(), "to", df["transaction_date"].max())

print("\nUnique Investors:")
print(df["investor_id"].nunique())

print("\nUnique Schemes:")
print(df["amfi_code"].nunique())

print("\n--- TRANSACTION TYPE ANALYSIS ---")

print("\nTransaction Count:")
print(df["transaction_type"].value_counts())

print("\nTransaction Amount by Type:")
print(df.groupby("transaction_type")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- MONTHLY TRANSACTION ANALYSIS ---")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["month"] = df["transaction_date"].dt.to_period("M")

print("\nMonthly Transaction Count:")
print(df.groupby("month").size())

print("\nMonthly Transaction Amount:")
print(df.groupby("month")["amount_inr"].sum())

print("\nMonthly Transaction Type:")
print(df.groupby(["month", "transaction_type"]).size().unstack(fill_value=0))
print("\n--- INVESTOR AGE GROUP ANALYSIS ---")

print("\nInvestor Count by Age Group:")
print(df.groupby("age_group")["investor_id"].nunique().sort_values(ascending=False))

print("\nTransaction Count by Age Group:")
print(df["age_group"].value_counts())

print("\nTransaction Amount by Age Group:")
print(df.groupby("age_group")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2).sort_values("sum", ascending=False))
print("\n--- INVESTOR GENDER ANALYSIS ---")

print("\nInvestor Count by Gender:")
print(df.groupby("gender")["investor_id"].nunique())

print("\nTransaction Count by Gender:")
print(df["gender"].value_counts())

print("\nTransaction Amount by Gender:")
print(df.groupby("gender")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- INVESTOR GENDER ANALYSIS ---")

print("\nInvestor Count by Gender:")
print(df.groupby("gender")["investor_id"].nunique())

print("\nTransaction Count by Gender:")
print(df["gender"].value_counts())

print("\nTransaction Amount by Gender:")
print(df.groupby("gender")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- INVESTOR INCOME ANALYSIS ---")

print("\nAnnual Income Statistics (in Lakhs):")
print(df["annual_income_lakh"].describe().round(2))

print("\nInvestor Count by Income:")
print(df.groupby("annual_income_lakh")["investor_id"].nunique())
print("\n--- INCOME BRACKET ANALYSIS ---")

df["income_bracket"] = pd.cut(
    df["annual_income_lakh"],
    bins=[0, 5, 10, 20, 30, 50, 100, float("inf")],
    labels=["0-5L", "5-10L", "10-20L", "20-30L",
            "30-50L", "50-100L", "100L+"],
    right=True
)

print("\nInvestor Count by Income Bracket:")
print(df.groupby("income_bracket", observed=False)["investor_id"].nunique())

print("\nTransaction Count by Income Bracket:")
print(df["income_bracket"].value_counts().sort_index())

print("\nTransaction Amount by Income Bracket:")
print(df.groupby("income_bracket", observed=False)["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- CITY TIER ANALYSIS ---")

print("\nInvestor Count by City Tier:")
print(df.groupby("city_tier")["investor_id"].nunique())

print("\nTransaction Count by City Tier:")
print(df["city_tier"].value_counts())

print("\nTransaction Amount by City Tier:")
print(df.groupby("city_tier")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- PAYMENT MODE ANALYSIS ---")

print("\nInvestor Count by Payment Mode:")
print(df.groupby("payment_mode")["investor_id"].nunique())

print("\nTransaction Count by Payment Mode:")
print(df["payment_mode"].value_counts())

print("\nTransaction Amount by Payment Mode:")
print(df.groupby("payment_mode")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))
print("\n--- KYC STATUS ANALYSIS ---")

print("\nInvestor Count by KYC Status:")
print(df.groupby("kyc_status")["investor_id"].nunique())

print("\nTransaction Count by KYC Status:")
print(df["kyc_status"].value_counts())

print("\nTransaction Amount by KYC Status:")
print(df.groupby("kyc_status")["amount_inr"].agg(
    ["count", "sum", "mean", "median"]
).round(2))