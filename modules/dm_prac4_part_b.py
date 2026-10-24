# Practical - 04: Data Preprocessing and Cleaning
# Part B: Data Cleaning

import pandas as pd
import numpy as np

# Load the Dataset
df = pd.read_csv("data/Employee_Analytics.csv")

# 1. Display Missing Values
print("\n========================================")
print("Missing Values in Each Column")
print("========================================")
print(df.isnull().sum())

# 2. Replace Missing Values using Statistical Methods
print("\n========================================")
print("Handling Missing Values")
print("========================================")

# Age -> Median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Salary -> Mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Experience -> Median
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

# Performance -> Mean
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())

# Location -> Mode
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("Missing values replaced successfully.")

# 3. Verify Missing Values
print("\n========================================")
print("Missing Values After Replacement")
print("========================================")
print(df.isnull().sum())

# 4. Identify Duplicate Records
print("\n========================================")
print("Duplicate Records")
print("========================================")
duplicate_count = df.duplicated().sum()
print("Number of Duplicate Records :", duplicate_count)

# 5. Remove Duplicate Records
df = df.drop_duplicates()
print("Duplicate records removed successfully.")

# 6. Verify Duplicate Records After Removal
print("\n========================================")
print("Duplicate Records After Removal")
print("========================================")
print("Remaining duplicates:", df.duplicated().sum())

# 7. Remove Leading and Trailing Spaces
print("\n========================================")
print("Removing Extra Spaces")
print("========================================")
text_columns = ["Employee_Name", "Department", "Designation", "Employment_Type", "Location"]
for column in text_columns:
    df[column] = df[column].str.strip()
print("Extra spaces removed successfully.")

# 8. Standardize Gender Values
print("\n========================================")
print("Standardizing Gender Values")
print("========================================")
df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "M": "Male",
    "female": "Female",
    "F": "Female"
})
print("Unique Gender Values:", df["Gender"].unique())

# 9. Standardize Department Names
print("\n========================================")
print("Standardizing Department Names")
print("========================================")
df["Department"] = df["Department"].replace({
    "Information Technology": "IT",
    "Human Resources": "HR"
})
print("Unique Department Names:", df["Department"].unique())

# 10. Display Cleaned Dataset
print("\n========================================")
print("Cleaned Employee Dataset")
print("========================================")
print(df.to_string(index=False))

# 11. Save Cleaned Dataset
df.to_csv("data/Employee_Analytics_Cleaned.csv", index=False)
print("\nCleaned dataset saved as data/Employee_Analytics_Cleaned.csv")
