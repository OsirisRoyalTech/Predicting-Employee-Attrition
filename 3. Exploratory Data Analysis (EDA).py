# Let's visualize the data and explore relationships between features and the target variable.
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the correlation matrix to see how features are correlated
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Visualize the distribution of the target variable (Attrition)
plt.figure(figsize=(6, 4))
sns.countplot(x='Attrition', data=df)
plt.title('Attrition Distribution')
plt.show()

# Visualize the relationship between age and attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='Age', data=df)
plt.title('Age vs Attrition')
plt.show()
