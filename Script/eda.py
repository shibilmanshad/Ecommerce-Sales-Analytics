import pandas as pd

df = pd.read_csv("Data/cleaned_superstore.csv")

print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Quantity:", df["Quantity"].sum())

print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Category")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\nSales by Region")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nTop 10 States by Sales")
print(
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Category")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))