import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/cleaned_superstore.csv")

sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig("sales_by_category.png")
plt.show()

plt.savefig("Visuals/sales_by_category.png")

profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")

plt.title("Profit by Category")
plt.ylabel("Profit ($)")
plt.tight_layout()

plt.savefig("Visuals/profit_by_category.png")
plt.show()

sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig("Visuals/sales_by_region.png")
plt.show()

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))
top_states.plot(kind="bar")

plt.title("Top 10 States by Sales")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig("Visuals/top_10_states.png")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("Visuals", exist_ok=True)

df = pd.read_csv("Data/cleaned_superstore.csv")

sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")

plt.tight_layout()

plt.savefig("Visuals/sales_by_category.png")

plt.show()