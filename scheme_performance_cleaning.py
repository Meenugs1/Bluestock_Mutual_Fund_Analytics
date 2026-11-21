import pandas as pd

# Load scheme performance dataset
df = pd.read_csv(
    "data/raw/1788499985420-bb134abf-07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

# 1. Validate return columns are numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nReturn Columns Data Types:")
print(df[return_columns].dtypes)

print("\nMissing Return Values:")
print(df[return_columns].isnull().sum())

# 2. Flag return anomalies
# Flag unusually high or low returns for investigation.
anomaly_threshold = 100

for col in return_columns:
    anomalies = df[df[col].abs() > anomaly_threshold]

    print(f"\nAnomalies in {col} (absolute value > 100%):")
    print(anomalies[["scheme_name", col]])

# 3. Validate expense ratio
print("\nExpense Ratio Validation:")

invalid_expense_ratio = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Out-of-range Expense Ratios:")
print(invalid_expense_ratio[["scheme_name", "expense_ratio_pct"]])

# 4. Check missing values after validation
print("\nMissing Values After Validation:")
print(df.isnull().sum())

# 5. Check duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# 6. Save cleaned dataset
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

# 7. Final validation
print("\n--- FINAL SCHEME PERFORMANCE DATA ---")
print("Final Shape:", df.shape)
print("Minimum Expense Ratio:", df["expense_ratio_pct"].min())
print("Maximum Expense Ratio:", df["expense_ratio_pct"].max())

print("\nCleaned scheme performance dataset saved successfully!")