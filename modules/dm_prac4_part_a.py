# Practical - 04: Data Preprocessing and Cleaning
# Part A: Dataset Exploration

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load Dataset
df = pd.read_csv("data/Employee_Analytics.csv")

print("=" * 70)
print("               EMPLOYEE ANALYTICS DATASET")
print("=" * 70)

print("\n1. First Five Records")
print("-" * 70)
print(df.head().to_string(index=False))

print("\n2. Last Five Records")
print("-" * 70)
print(df.tail().to_string(index=False))

print("\n" + "=" * 70)
print("3. DATASET INFORMATION")
print("=" * 70)
df.info()

print("\n" + "=" * 70)
print("4. DATASET DIMENSIONS")
print("=" * 70)
rows, columns = df.shape
print(f"Number of Rows    : {rows}")
print(f"Number of Columns : {columns}")

print("\n" + "=" * 70)
print("5. COLUMN NAMES")
print("=" * 70)
for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

print("\n" + "=" * 70)
print("6. DATA TYPES")
print("=" * 70)
datatype = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.values
})
print(datatype.to_string(index=False))

print("\n" + "=" * 70)
print("7. Statistical Summary")
print("=" * 70)
print(df.describe().astype(int))
