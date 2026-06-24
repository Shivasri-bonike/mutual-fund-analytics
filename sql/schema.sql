CREATE TABLE dim_fund (
amfi_code TEXT PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
expense_ratio_pct REAL
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date TEXT,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
date_id INTEGER,
nav REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
date_id INTEGER,
amfi_code TEXT,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
alpha REAL,
beta REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
year INTEGER,
quarter INTEGER,
aum_crore REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);
