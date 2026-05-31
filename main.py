import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fill missing values
df.fillna("Unknown", inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Data cleaning completed!")