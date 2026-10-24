# Practical - 04: Data Preprocessing and Cleaning (Complete Code)
# Includes Part A: Exploration, Part B: Cleaning, Part C: Transformation

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# --- Part A: Exploration ---
df = pd.read_csv("data/Employee_Analytics.csv")
print("Dataset Shape:", df.shape)
print("Missing values count:\n", df.isnull().sum())

# --- Part B: Cleaning ---
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].median())
df["Performance"] = df["Performance"].fillna(df["Performance"].mean())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

df = df.drop_duplicates()

text_cols = ["Employee_Name", "Department", "Designation", "Employment_Type", "Location"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

df["Gender"] = df["Gender"].replace({"male": "Male", "M": "Male", "female": "Female", "F": "Female"})
df["Department"] = df["Department"].replace({"Information Technology": "IT", "Human Resources": "HR"})

# --- Part C: Transformation ---
encoder = LabelEncoder()
for col in ["Gender", "Department", "Designation", "Employment_Type", "Location"]:
    df[col] = encoder.fit_transform(df[col])

scaler = MinMaxScaler()
num_cols = ["Age", "Salary", "Experience", "Performance", "Training_Hours"]
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\nCleaned & Normalized Dataset (Head):\n", df.head())
