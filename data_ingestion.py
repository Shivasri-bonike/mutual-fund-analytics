import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("=" * 50)
        print("File:", file)
        print("Shape:", df.shape)
        print("Columns:", list(df.columns))
        print("Missing Values:")
        print(df.isnull().sum())
        print()