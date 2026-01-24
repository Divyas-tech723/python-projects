import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Load dataset  
df = pd.read_csv('sales_data.csv')  

# Line Plot: Sales over time  
plt.figure(figsize=(10, 5))  
sns.lineplot(data=df, x='Date', y='Sales')  
plt.title('Sales Over Time')  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()  

# Bar Plot: Sales by Region  
plt.figure(figsize=(8, 5))  
sns.barplot(data=df, x='Region', y='Sales', estimator=sum)  
plt.title('Total Sales by Region')  
plt.tight_layout()  
plt.show()  

# Heatmap: Correlation matrix  
plt.figure(figsize=(6, 4))  
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')  
plt.title('Feature Correlation')  
plt.tight_layout()  
plt.show()
