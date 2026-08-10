import pandas as pd
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ayush", "Rahul", "Aman", "Priya"],
    "Department": ["CSE", "ECE", "CSE", "ECE"],
    "Marks": [85, 90, 78, 92]
})
df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "City": ["Delhi", "Jaipur", "Bhopal", "Mumbai"],
    "Age": [21, 20, 22, 21]
})
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
merged = pd.merge(df1, df2, on="ID")
print("\nMerged DataFrame:")
print(merged)
df3 = pd.DataFrame({
    "ID": [5, 6],
    "Name": ["Neha", "Rohan"],
    "Department": ["CSE", "ECE"],
    "Marks": [88, 75]
})
concatenated = pd.concat([df1, df3], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated)
grouped = df1.groupby("Department")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)
print("\nGroupBy Result:")
print(grouped)
pivot = pd.pivot_table(
    df1,
    values="Marks",
    index="Department",
    aggfunc=["sum", "mean", "count", "min", "max"]
)
print("\nPivot Table:")
print(pivot)
