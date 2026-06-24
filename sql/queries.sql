-- 1. Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT strftime('%Y-%m', nav_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP YoY Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state;

-- 5. Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 6. Top funds by 1-year return
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 7. Average 3-year return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 8. Highest NAV recorded
SELECT MAX(nav)
FROM fact_nav;

-- 9. Total redemptions
SELECT SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 10. Count of funds by category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;