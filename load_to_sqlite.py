import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/clean_nav_history.csv")
tx = pd.read_csv("data/processed/clean_investor_transactions.csv")
perf = pd.read_csv("data/processed/clean_scheme_performance.csv")

# Load fund master
fund = pd.read_csv("data/raw/01_fund_master.csv")

# Write to SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
tx.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database loaded successfully!")