import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataset = pd.read_excel("HousePricePrediction.xlsx")

# Printing first 5 records of the dataset
print(dataset.head(5))

# Identify and exclude non-numeric columns (like object and possibly others)
numeric_cols = dataset.select_dtypes(include=['float64', 'int64']).columns

# Plotting heatmap of correlations for numeric columns only
plt.figure(figsize=(12, 6))
sns.heatmap(dataset[numeric_cols].corr(), cmap='coolwarm', annot=True, fmt='.2f', linewidths=2)
plt.title('Correlation Heatmap of Numeric Features')
plt.show()

# Example for handling categorical columns (unique values and distribution)
object_cols = dataset.select_dtypes(include=['object']).columns

# Plotting unique values count for categorical features
unique_values = [dataset[col].nunique() for col in object_cols]
plt.figure(figsize=(10, 6))
plt.title('Number of Unique Values in Categorical Features')
plt.xticks(rotation=90)
sns.barplot(x=object_cols, y=unique_values)
plt.show()

# Plotting distribution of categorical features
plt.figure(figsize=(18, 36))
plt.suptitle('Distribution of Categorical Features')
index = 1

for col in object_cols:
    plt.subplot(11, 4, index)
    sns.countplot(data=dataset, x=col)
    plt.xticks(rotation=90)
    plt.xlabel(col)
    index += 1

plt.tight_layout()
plt.show()
