import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('assessment.csv')

# Calculate average price by category
category_sales = df.groupby('Category')['Price'].mean().reset_index()

# Create the plot
plt.figure(figsize=(12, 6))
plt.bar(category_sales['Category'], category_sales['Price'])

# Customize the plot
plt.title('Average Price by Category')
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show() 