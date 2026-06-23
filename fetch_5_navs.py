import requests
import pandas as pd
import os

schemes = {
    "sbi_bluechip_nav": "119551",
    "icici_bluechip_nav": "120503",
    "nippon_largecap_nav": "118632",
    "axis_bluechip_nav": "119092",
    "kotak_bluechip_nav": "120841"
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        file_path = os.path.join("data", "raw", f"{name}.csv")

        df.to_csv(file_path, index=False)

        print(f"Saved: {name}.csv")

print("All 5 NAV CSV files created successfully!")