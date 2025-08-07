
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: species for i, species in enumerate(iris.target_names)})
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print(df.head())

# Explore structure and check for missing values
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# Clean the dataset
df_cleaned = df.dropna()

# Basic statistics
print("\nBasic statistics:")
print(df_cleaned.describe())

# Group by species and compute mean
grouped_means = df_cleaned.groupby('species').mean()
print("\nGrouped means by species:")
print(grouped_means)

# Line chart - Petal Length over Species
plt.figure(figsize=(8, 5))
sns.lineplot(data=grouped_means['petal length (cm)'])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

# Bar chart - Sepal Width per Species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_means.index, y='sepal width (cm)', data=grouped_means)
plt.title("Average Sepal Width per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

# Histogram - Petal Length
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned['petal length (cm)'], bins=20, kde=True)
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

# Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs. Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()
