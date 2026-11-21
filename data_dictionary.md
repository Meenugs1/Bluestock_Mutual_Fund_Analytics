# Bluestock Mutual Fund Analytics – Data Dictionary

## 1. Project Overview

This database is designed to analyze mutual fund schemes, historical Net Asset Value (NAV), investor transactions, scheme performance, and fund-house Assets Under Management (AUM).

**Database:** SQLite  
**Database file:** `bluestock_mf.db`  
**Total tables:** 6

---

## 2. Table: dim_fund

Stores mutual fund scheme details and classification information.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier (Primary Key) |
| fund_house | TEXT | Asset management company or fund house |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Broad fund category |
| sub_category | TEXT | Specific fund sub-category |
| plan | TEXT | Scheme plan type |
| launch_date | TEXT | Scheme launch date |
| benchmark | TEXT | Benchmark index used for comparison |
| expense_ratio_pct | REAL | Annual expense ratio in percentage |
| exit_load_pct | REAL | Exit load applicable to the scheme |
| min_sip_amount | REAL | Minimum SIP investment amount |
| min_lumpsum_amount | REAL | Minimum lump-sum investment amount |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk classification of the scheme |
| sebi_category_code | TEXT | SEBI category code |

---

## 3. Table: dim_date

Stores calendar information used for time-based analysis.

| Column | Data Type | Description |
|---|---|---|
| date_id | INTEGER | Date key in YYYYMMDD format (Primary Key) |
| full_date | TEXT | Full calendar date in YYYY-MM-DD format |
| year | INTEGER | Calendar year |
| month | INTEGER | Calendar month (1–12) |
| day | INTEGER | Day of the month |
| quarter | INTEGER | Calendar quarter (1–4) |

---

## 4. Table: fact_nav

Stores historical Net Asset Value (NAV) records for mutual fund schemes.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Scheme identifier (Foreign Key referencing dim_fund) |
| date | TEXT | NAV date (Foreign Key referencing dim_date) |
| nav | REAL | Net Asset Value per unit |

**Primary Key:** (amfi_code, date)

---

## 5. Table: fact_transactions

Stores investor transaction records.

| Column | Data Type | Description |
|---|---|---|
| transaction_id | INTEGER | Unique transaction identifier (Primary Key, auto-generated) |
| investor_id | TEXT | Investor identifier |
| transaction_date | TEXT | Date of transaction (Foreign Key referencing dim_date) |
| amfi_code | INTEGER | Scheme identifier (Foreign Key referencing dim_fund) |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in Indian Rupees |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | City classification (T30 or B30) |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender category recorded in the dataset |
| annual_income_lakh | REAL | Investor annual income in lakh rupees |
| payment_mode | TEXT | Mode used for payment |
| kyc_status | TEXT | Investor KYC verification status |

---

## 6. Table: fact_performance

Stores scheme return, risk, and performance indicators.

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Scheme identifier (Primary Key and Foreign Key) |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Benchmark three-year return percentage |
| alpha | REAL | Excess return relative to a benchmark, as defined by the dataset |
| beta | REAL | Sensitivity to benchmark movements, as defined by the dataset |
| sharpe_ratio | REAL | Risk-adjusted return indicator |
| sortino_ratio | REAL | Risk-adjusted return using downside volatility |
| std_dev_ann_pct | REAL | Annualized standard deviation of returns |
| max_drawdown_pct | REAL | Maximum observed peak-to-trough decline percentage |
| aum_crore | REAL | Scheme assets under management in crore rupees |
| expense_ratio_pct | REAL | Scheme expense ratio percentage |
| morningstar_rating | REAL | Rating value provided in the dataset |
| risk_grade | TEXT | Risk grade assigned in the dataset |

---

## 7. Table: fact_aum

Stores fund-house-level AUM data over time.

| Column | Data Type | Description |
|---|---|---|
| date | TEXT | Reporting date (Foreign Key referencing dim_date) |
| fund_house | TEXT | Fund house name |
| aum_lakh_crore | REAL | Assets under management in lakh crore rupees |
| aum_crore | REAL | Assets under management in crore rupees |
| num_schemes | INTEGER | Number of schemes managed by the fund house |

**Primary Key:** (date, fund_house)

---

## 8. Database Relationships

- `dim_fund.amfi_code` → `fact_nav.amfi_code`
- `dim_date.full_date` → `fact_nav.date`
- `dim_fund.amfi_code` → `fact_transactions.amfi_code`
- `dim_date.full_date` → `fact_transactions.transaction_date`
- `dim_fund.amfi_code` → `fact_performance.amfi_code`
- `dim_date.full_date` → `fact_aum.date`

---

## 9. Data Sources

- Fund Master
- NAV History
- Investor Transactions
- Scheme Performance
- AUM by Fund House

Data cleaning and validation were performed before loading the datasets into SQLite.
