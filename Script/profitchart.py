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