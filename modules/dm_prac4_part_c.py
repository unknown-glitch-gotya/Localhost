# Practical - 04: Data Preprocessing and Cleaning
# Part C: Data Transformation

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load Cleaned Dataset
df = pd.read_csv("data/Employee_Analytics_Cleaned.csv") if os.path.exists("data/Employee_Analytics_Cleaned.csv") else pd.read_csv("data/Employee_Analytics.csv")

# 1. Convert Categorical Data into Numerical Data using Label Encoding
print("\n========================================")
print("Label Encoding")
print("========================================")

encoder = LabelEncoder()
categorical_columns = ["Gender", "Department", "Designation", "Employment_Type", "Location"]

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column].astype(str))

print("\nCategorical attributes converted successfully.")
print("\nDataset After Label Encoding")
print(df.head().to_string(index=False))

# 2. Normalize Numerical Data using Min-Max Scaling
print("\n========================================")
print("Min-Max Normalization")
print("========================================")

scaler = MinMaxScaler()
numerical_columns = ["Age", "Salary", "Experience", "Performance", "Training_Hours"]

# Formula: Scaled = (Value - Min) / (Max - Min)
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

print("\nNumerical attributes normalized successfully.")
print("\nDataset After Normalization")
print(df.head().to_string(index=False))

# 3. Save Final Processed Dataset
df.to_csv("data/Employee_Analytics_Processed.csv", index=False)
print("\n========================================")
print("Data Transformation Completed")
print("========================================")
print("Processed dataset saved as data/Employee_Analytics_Processed.csv")
