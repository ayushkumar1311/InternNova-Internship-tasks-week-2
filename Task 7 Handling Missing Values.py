import pandas as pd

df = pd.read_csv("students_missing.csv")

print("Dataset Before Handling Missing Values:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values in Each Column:")
print(df.isnull().sum())

df_dropped = df.dropna()

print("\nDataset After Removing Rows with Missing Values:")
print(df_dropped)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Grade"] = df["Grade"].fillna("Not Available")

print("\nDataset After Filling Missing Values:")
print(df)
