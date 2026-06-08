import pandas as pd

# Load dataset
df = pd.read_csv("Data/raw/SampleSuperstore.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

print("New Shape:", df.shape)

# Save cleaned dataset
df.to_csv("Data/cleaned_superstore.csv", index=False)

print("Cleaned dataset saved successfully!")