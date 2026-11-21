# Bluestock Mutual Fund Analytics
## Data Quality Report – Initial Validation

### 1. Project Overview
The purpose of this analysis is to inspect the mutual fund datasets, understand their structure, and validate data quality before performing further analytics.

### 2. Fund Master Dataset

- Total records: 40
- Total columns: 15
- Unique fund houses: 10
- Missing values: 0
- Duplicate AMFI codes: 0
- Duplicate scheme names: 0

#### Category Distribution
- Equity: 34 schemes (85%)
- Debt: 6 schemes (15%)

#### Top Subcategories
- Large Cap: 14
- Mid Cap: 7
- Small Cap: 6
- Liquid: 3
- Gilt: 2

#### Risk Distribution
- Moderate: 16
- High: 8
- Very High: 6
- Low: 6
- Moderately High: 4

#### Plan Distribution
- Regular: 32 schemes (80%)
- Direct: 8 schemes (20%)

### 3. NAV History Dataset

- Total records: 46,000
- Total columns: 3
- Unique scheme codes: 40
- Missing values: 0
- Duplicate records: 0
- Duplicate scheme-date records: 0
- Non-positive NAV values: 0
- Date range: 03 January 2022 to 29 May 2026

### 4. AMFI Code Validation

Fund Master and NAV History were compared using `amfi_code`.

| Validation | Result |
|---|---:|
| Fund Master codes | 40 |
| NAV History codes | 40 |
| Matching codes | 40 |
| Missing codes | 0 |
| Extra codes | 0 |

All 40 scheme codes in Fund Master were found in NAV History.

### 5. Conclusion

Both datasets passed the initial structural data quality checks. No missing values, duplicate records, or invalid non-positive NAV values were identified in the checks performed.

The datasets are ready for the next stage of analysis. Further validation against official sources and business rules may still be required.
