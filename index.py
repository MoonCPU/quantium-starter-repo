from os import listdir
from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent
mypath = base_dir / "data"

results_dfs = []
for file in listdir(mypath):
    fullpath = mypath / file
    df = pd.read_csv(fullpath)
    results_dfs.append(df)

df = pd.concat(results_dfs)
filtered_df = df[df["product"].str.lower() == "pink morsel"]
# strip the "$" symbol, and convert this string to a float
filtered_df["price"] = filtered_df["price"].str.replace("$", "", regex=False).astype(float)
filtered_df["sales"] = filtered_df["price"] * filtered_df["quantity"]
filtered_df = filtered_df.drop(columns=["product", "price", "quantity"])

print(filtered_df.head())

filtered_df.to_csv("sales.csv", index=False)