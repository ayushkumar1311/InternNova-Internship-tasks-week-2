import pandas as pd

series = pd.Series([85, 90, 78, 92, 88])

data = {
    "Name": ["Ayush", "Rahul", "Aman", "Priya", "Riya"],
    "Age": [21, 20, 22, 21, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Pandas Series:")
print(series)

print("\nDataFrame:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

df["Grade"] = ["A", "A+", "B", "A+", "A"]

print("\nUpdated DataFrame:")
print(df)
