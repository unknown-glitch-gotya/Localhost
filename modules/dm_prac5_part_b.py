# Practical - 05: Data Discretization and Visualization
# Part B: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the discretized dataset
df = pd.read_csv("data/Employee_Analytics_Discretized.csv") if os.path.exists("data/Employee_Analytics_Discretized.csv") else pd.read_csv("data/Employee_Analytics.csv")

# Ensure discretized columns exist for visualization
if 'Age_Category' not in df.columns:
    df['Age_Category'] = pd.cut(df['Age'], bins=[20, 30, 40, 60], labels=['Young', 'Adult', 'Senior'])
if 'Salary_Category' not in df.columns:
    df['Salary_Category'] = pd.cut(df['Salary'], bins=[400000, 800000, 900000, float('inf')], labels=['Low', 'Medium', 'High'])
if 'Performance_Category' not in df.columns:
    df['Performance_Category'] = pd.cut(df['Performance'], bins=[0, 2, 3.5, 4.5, 5], labels=['Poor', 'Average', 'Good', 'Excellent'])

# -------------------------------
# 1. Bar Chart - Age Category
# -------------------------------
plt.figure(figsize=(6, 4))
df['Age_Category'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Employees by Age Category")
plt.xlabel("Age Category")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Histogram - Annual Salary
# -------------------------------
plt.figure(figsize=(6, 4))
plt.hist(df['Salary_Category'].dropna().astype(str), bins=10, edgecolor='black', color='coral')
plt.title("Distribution of Annual Salary")
plt.xlabel("Annual Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Pie Chart - Performance Category
# -------------------------------
plt.figure(figsize=(6, 6))
df['Performance_Category'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Performance Category Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Box Plot - Training Hours
# -------------------------------
plt.figure(figsize=(6, 4))
plt.boxplot(df['Training_Hours'].dropna())
plt.title("Training Hours Distribution")
plt.ylabel("Training Hours")
plt.tight_layout()
plt.show()

print("Visualization completed successfully.")
print("Dataset saved as Employee_Analytics_Discretized.csv")
