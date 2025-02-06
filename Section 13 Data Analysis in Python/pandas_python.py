import pandas as pd

# Series: Pandas series are one dimensional array like object that can hold any data type.
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series \n", series)
print(type(series))

# Create series forom dictionary
data = {"a": 1, "b": 2, "c": 3}
series_dict = pd.Series(data)
print(series_dict)

data = [10, 20, 30]
index = ["a", "b", "c"]
print(pd.Series(data, index=index))

# Dataframe: It is similar to a table.
data = {
    "Name": ["John", "Jack", "Jill"],
    "Age": [25, 30, 45],
    "City": ["Mumbai", "New York", "Florida"],
}
df1 = pd.DataFrame(data)
print(df1)
print(type(df1))

data = [
    {"Name": "Jack", "Age": 32, "City": "Mumbai"},
    {"Name": "Jill", "Age": 35, "City": "New York"},
    {"Name": "John", "Age": 37, "City": "Florida"},
]
df = pd.DataFrame(data)
print(df)

df = pd.read_csv("Section 13 Data Analysis in Python/sales.csv")
print(df)
df.head()

# Accessing data from dataframe
type(df1["Name"])

# loc
print(df1.loc[0]["Name"])  # Select 0 index. loc[row][column]
print(df1.loc[:2]["Age"])
# iloc
print(df1.iloc[0][0])
print(df1.iloc[[0, 1], [1]])

## Accessing a specified element using at
print(df1.at[1, "Name"])
print(df1.at[1, "Age"])

print(df1.iat[1, 0])
print(df1.iat[1, 1])

# Data manipulation with dataframe
df1["Salary"] = pd.Series([5000, 5500, 502])

print(df1)

# axis defines row or column. axis 0 is row, axis 1 is column
df1.drop("Salary", axis=1, inplace=True)

df1["Age"] = df1["Age"] + 1
df1

# remove row 0 in df1
df1.drop(0)

# Special functions to describe data
print("Data types: \n", df.dtypes)
print("Statistical summary: \n", df.describe())
