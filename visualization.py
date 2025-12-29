import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
current_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(current_folder, '../data')
outputs_folder = os.path.join(current_folder, '../outputs')
os.makedirs(outputs_folder, exist_ok=True)

# Load cleaned dataset
input_file = os.path.join(data_folder, 'sales_data_cleaned.csv')
df = pd.read_csv(input_file)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Monthly sales trend
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()

# Plot
plt.figure(figsize=(12,6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
output_file = os.path.join(outputs_folder, 'monthly_sales_trend.png')
plt.savefig(output_file)
plt.show()
print(f"Visualization saved at: {output_file}")
