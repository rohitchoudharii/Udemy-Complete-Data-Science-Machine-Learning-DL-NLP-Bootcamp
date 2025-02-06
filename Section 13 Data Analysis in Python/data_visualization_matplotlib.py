import matplotlib.pyplot as plt

x = [i for i in range(1, 10)]
y = [j**2 for j in range(1, 10)]

plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Basic Line Plot")
plt.show()

# Customize line plot
plt.plot(x, y, color="red", linestyle="--", marker=".", linewidth=3, markersize=9)
plt.show()

# Multiple plots
x = [i for i in range(1, 6)]
y1 = [i**2 for i in range(1, 6)]
y2 = [i**3 for i in range(1, 6)]

plt.figure(figsize=(9, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color="red")
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(y1, x, color="blue")
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot(x, y2, color="green")
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot(y2, x, color="Yellow")
plt.title("Plot 4")

plt.show()

# Bar chart
categories = ["A", "B", "C", "D", "E"]
values = [i**2 for i in range(1, 6)]

plt.bar(categories, values, color="Purple")
plt.show()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, color="Red", edgecolor="black")
plt.show()

# Scatter plot
x = [i for i in range(1, 5)]
y = [i for i in range(2, 6)]

plt.scatter(x, y, color="blue", marker="x")
plt.show()

# Pie chart
labels = ["A", "B", "C", "D"]
sizes = [30, 20, 40, 10]
colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]
explode = (0.2, 0, 0, 0)

plt.pie(
    sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True
)
plt.show()

# Sales data visualization
import pandas as pd

sales_data = pd.read_csv("Section 13 Data Analysis in Python/data/csv/sales_data.csv")
print(sales_data)

print(sales_data.info())

total_sales_by_product = sales_data.groupby("Product Category")["Total Revenue"].sum()

print(total_sales_by_product)

plt.bar(total_sales_by_product.index, total_sales_by_product.values)
plt.show()

sales_trend = sales_data.groupby("Date")["Total Revenue"].sum()
print(sales_trend)

plt.plot(sales_trend.index, sales_trend.values)
plt.show()
