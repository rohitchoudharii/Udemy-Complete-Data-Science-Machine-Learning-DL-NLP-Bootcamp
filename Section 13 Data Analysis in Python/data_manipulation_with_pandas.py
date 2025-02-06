import pandas as pd

folder = "Section 13 Data Analysis in Python"
df = pd.read_csv(f"{folder}/data.csv")

print(df.tail())
print(df.describe())
print(df.dtypes)

# Handling missing values
print(df[df.isnull()])

print(df.isnull().any())
print(df.isnull().sum())

df_filled = df.fillna(0)

# filling missing values with the mean of the columns
df["Sales_fillNa"] = df["Sales"].fillna(df["Sales"].mean())
print(df)

# Rename columns
df.rename(columns={"Date": "Sales Date"}, inplace=True)

# CHange datatypes
df["Value_new"] = df["Value"].fillna(df["Value"].mean()).astype(int)
print(df)

df["Neew Value"] = df["Value"].apply(lambda x: x**2)
print(df)

## Data aggregating and grouping
grouped_mean = df.groupby("Product")["Value"].mean()
print(grouped_mean)

print(df.groupby(["Region", "Product"])["Value"].mean())

print(df.groupby(["Region"])["Value"].agg(["mean", "sum", "count"]))

# Merging and joining Dataframes
df_1 = pd.DataFrame({"Key": ["A", "B", "C"], "Value": [1, 2, 3]})
df_2 = pd.DataFrame({"Key": ["A", "B", "D"], "Value": [1, 2, 4]})

print(pd.merge(df_1, df_2, on="Key", how="inner"))
print(pd.merge(df_1, df_2, on="Key", how="outer"))
print(pd.merge(df_1, df_2, on="Key", how="left"))
print(pd.merge(df_1, df_2, on="Key", how="right"))
