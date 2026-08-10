import pandas as pd
import numpy as np
df = pd.read_csv("student_performance.csv")
print("Dataset:")
print(df)
print("\nDataset Information:")
df.info()
print("\nFirst 5 Rows:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Department"] = df["Department"].fillna("Unknown")
print("\nDataset After Handling Missing Values:")
print(df)
print("\nSelected Columns:")
print(df[["Name", "Department", "Marks"]])
print("\nStudents with Marks Greater Than 80:")
print(df[df["Marks"] > 80])
print("\nStudents with Marks Greater Than 80 and Age Less Than 22:")
print(df[(df["Marks"] > 80) & (df["Age"] < 22)])
print("\nStudents Sorted by Marks:")
print(df.sort_values("Marks", ascending=False))
print("\nGroupBy Department:")
grouped = df.groupby("Department")["Marks"].agg(
    ["count", "mean", "min", "max", "sum"]
)
print(grouped)
print("\nPivot Table:")
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc=["mean", "max", "min"]
)
print(pivot)
print("\nNumPy Statistical Analysis:")
marks = np.array(df["Marks"])
print("Mean Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))
df.to_csv("cleaned_student_performance.csv", index=False)
print("\nCleaned dataset exported successfully.")
