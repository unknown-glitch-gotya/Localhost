# Practical - 05: Data Discretization and Visualization (Complete Code)

import pandas as pd
import matplotlib.pyplot as plt

# Load Cleaned Data
df = pd.read_csv("data/Employee_Analytics_Cleaned.csv") if os.path.exists("data/Employee_Analytics_Cleaned.csv") else pd.read_csv("data/Employee_Analytics.csv")

# Discretization via pd.cut()
df['Age_Category'] = pd.cut(df['Age'], bins=[20, 30, 40, 60], labels=['Young', 'Adult', 'Senior'])
df['Salary_Category'] = pd.cut(df['Salary'], bins=[400000, 800000, 900000, float('inf')], labels=['Low', 'Medium', 'High'])
df['Experience_Category'] = pd.cut(df['Experience'], bins=[0, 2, 5, 10, float('inf')], labels=['Beginner', 'Intermediate', 'Experienced', 'Expert'])
df['Performance_Category'] = pd.cut(df['Performance'], bins=[0, 2, 3.5, 4.5, 5], labels=['Poor', 'Average', 'Good', 'Excellent'])
df['Training_Category'] = pd.cut(df['Training_Hours'], bins=[0, 20, 40, 60, float('inf')], labels=['Low', 'Medium', 'High', 'Very High'])

print("Discretized Data Head:\n", df[['Employee_Name', 'Age_Category', 'Salary_Category', 'Performance_Category']].head())

# Visualizations: Bar chart, Histogram, Pie chart, Boxplot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
df['Age_Category'].value_counts().plot(kind='bar', ax=axes[0, 0], color='skyblue', title='Age Category (Bar Chart)')
axes[0, 1].hist(df['Salary_Category'].dropna().astype(str), bins=10, edgecolor='black', color='coral')
axes[0, 1].set_title('Salary Category (Histogram)')
df['Performance_Category'].value_counts().plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%', title='Performance (Pie Chart)')
axes[1, 1].boxplot(df['Training_Hours'].dropna())
axes[1, 1].set_title('Training Hours (Boxplot)')
plt.tight_layout()
plt.show()
