
-- ============================================================
-- BLUESTOCK MUTUAL FUND ANALYTICS
-- DAY 2: ANALYTICAL SQL QUERIES
-- ============================================================

-- 1. Top 5 mutual funds by AUM
SELECT
    f.scheme_name,
    f.fund_house,
    p.aum_crore
FROM dim_fund f
JOIN fact_performance p
    ON f.amfi_code = p.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;


-- 2. Average NAV by month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Total transactions by transaction type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount_inr DESC;


-- 4. Transactions by state
SELECT
    state,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;


-- 5. Funds with expense ratio below 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;


-- 6. Top 10 funds by 3-year returns
SELECT
    f.scheme_name,
    f.category,
    p.return_3yr_pct
FROM dim_fund f
JOIN fact_performance p
    ON f.amfi_code = p.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 10;


-- 7. SIP transactions by month
SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS sip_transactions,
    ROUND(SUM(amount_inr), 2) AS sip_amount_inr
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY month
ORDER BY month;


-- 8. Investor transactions by city tier
SELECT
    city_tier,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr,
    ROUND(AVG(amount_inr), 2) AS average_transaction_inr
FROM fact_transactions
GROUP BY city_tier
ORDER BY total_amount_inr DESC;


-- 9. Funds with the highest risk-adjusted returns (Sharpe Ratio)
SELECT
    f.scheme_name,
    f.category,
    p.sharpe_ratio,
    p.return_3yr_pct,
    p.std_dev_ann_pct
FROM dim_fund f
JOIN fact_performance p
    ON f.amfi_code = p.amfi_code
WHERE p.sharpe_ratio IS NOT NULL
ORDER BY p.sharpe_ratio DESC
LIMIT 10;


-- 10. Fund house AUM trend over time
SELECT
    fund_house,
    date,
    aum_crore,
    num_schemes
FROM fact_aum
ORDER BY fund_house, date;
