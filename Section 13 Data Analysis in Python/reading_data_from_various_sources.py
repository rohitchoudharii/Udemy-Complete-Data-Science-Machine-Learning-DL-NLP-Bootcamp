import pandas as pd

# Read json data
df_json = pd.read_json("Section 13 Data Analysis in Python/data/json/test.json")
print(df_json)
print(df_json.to_json())
print(df_json.to_json(orient="records"))

# Read data from online csv
df_csv = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
    header=0,
    sep=";",
)
print(df_csv)

df_html = pd.read_html("https://www.fdic.gov/bank-failures/failed-bank-list")
df_html = df_html[0]
print(df_html)

pd.to_pickle(df_html, "Section 13 Data Analysis in Python/data/pickle/fidc_pickle")

df_pickle = pd.read_pickle("Section 13 Data Analysis in Python/data/pickle/fidc_pickle")
print(df_pickle)
