import pandas as pd

df = pd.DataFrame({
    "Name": ["Ayush", "Rahul", "Aman", "Priya", "Neha"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Marks": [85, 90, 78, 92, 88]
})

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("Processed DataFrame:")
print(df)

df.to_csv("final_students.csv", index=False)

print("\nData exported successfully to final_students.csv")

exported_df = pd.read_csv("final_students.csv")

print("\nVerified Exported Data:")
print(exported_df)
