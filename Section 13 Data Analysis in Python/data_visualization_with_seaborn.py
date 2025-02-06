import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
print(tips)

# Create scatter plot

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter plot of total Bill vs Tip")
plt.show()

sns.lineplot(x="size", y="total_bill", data=tips)
plt.title("Line plot of Total bill by size")
plt.show()

# Categorical Plots
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bar plot for total bill by days")
plt.show()

# Box plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# Violin plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

# Histogram
sns.histplot(tips["total_bill"], bins=10, kde=True)
plt.show()

# KDE Plot
sns.kdeplot(tips["total_bill"], fill=True)
plt.show()

# Pairplot
sns.pairplot(tips)
plt.show()

# Heatmap
corr = tips[["total_bill", "size", "tip"]].corr()
print(corr)

sns.heatmap(corr, annot=True)
plt.show()

# Custom data
df = pd.read_csv("Section 13 Data Analysis in Python/data/csv/sales_data.csv")
print(df.head())

## Plot total sales by product
plt.figure(figsize=(10, 6))
sns.barplot(x="Product Category", y="Total Revenue", data=df, estimator=sum)
plt.title("Total Sales by product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()


## Plot total sales by Region
plt.figure(figsize=(10, 6))
sns.barplot(x="Region", y="Total Revenue", data=df, estimator=sum)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
