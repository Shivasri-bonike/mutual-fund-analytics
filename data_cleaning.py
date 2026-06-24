import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# 1. Clean nav_history.csv
# -----------------------------
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv("data/processed/clean_nav_history.csv", index=False)

print("✓ Cleaned nav_history.csv")


# -----------------------------
# 2. Clean investor_transactions.csv
# -----------------------------
tx = pd.read_csv("data/raw/08_investor_transactions.csv")

tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]
tx = tx[tx["transaction_type"].isin(valid_types)]

tx = tx[tx["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]
tx = tx[tx["kyc_status"].isin(valid_kyc)]

tx.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("✓ Cleaned investor_transactions.csv")


# -----------------------------
# 3. Clean scheme_performance.csv
# -----------------------------
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

if "expense_ratio_pct" in perf.columns:
    perf = perf[
        (perf["expense_ratio_pct"] >= 0.1)
        & (perf["expense_ratio_pct"] <= 2.5)
    ]

perf.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("✓ Cleaned scheme_performance.csv")

print("\nAll cleaning completed successfully!")