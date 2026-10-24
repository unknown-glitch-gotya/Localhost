# Practical - 05: Data Discretization and Visualization
# Part A: Data Discretization

import pandas as pd
import numpy as np

# Load Cleaned Dataset
df = pd.read_csv("data/Employee_Analytics_Cleaned.csv") if os.path.exists("data/Employee_Analytics_Cleaned.csv") else pd.read_csv("data/Employee_Analytics.csv")

print("Original Dataset:")
print(df.head())

# Discretize numerical attributes using Equal Width Binning

# Age -> Young, Adult, Senior
df['Age_Category'] = pd.cut(
    df['Age'],
    bins=[20, 30, 40, 60],
    labels=['Young', 'Adult', 'Senior']
)

# Annual Salary -> Low, Medium, High
df['Salary_Category'] = pd.cut(
    df['Salary'],
    bins=[400000, 800000, 900000, float('inf')],
    labels=['Low', 'Medium', 'High']
)

# Years of Experience -> Beginner, Intermediate, Experienced, Expert
df['Experience_Category'] = pd.cut(
    df['Experience'],
    bins=[0, 2, 5, 10, float('inf')],
    labels=['Beginner', 'Intermediate', 'Experienced', 'Expert']
)

# Performance Score -> Poor, Average, Good, Excellent
df['Performance_Category'] = pd.cut(
    df['Performance'],
    bins=[0, 2, 3.5, 4.5, 5],
    labels=['Poor', 'Average', 'Good', 'Excellent']
)

# Training Hours -> Low, Medium, High, Very High
df['Training_Category'] = pd.cut(
    df['Training_Hours'],
    bins=[0, 20, 40, 60, float('inf')],
    labels=['Low', 'Medium', 'High', 'Very High']
)

print("\nDataset After Data Discretization:")
print(df[['Employee_Name', 'Age_Category', 'Salary_Category', 'Experience_Category', 'Performance_Category', 'Training_Category']].head())

# Save Discretized Dataset
df.to_csv("data/Employee_Analytics_Discretized.csv", index=False)
print("\nDiscretized dataset saved successfully as data/Employee_Analytics_Discretized.csv")
