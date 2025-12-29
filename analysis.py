import pandas as pd

# Load cleaned dataset
df = pd.read_csv('/Users/niralipatel/Downloads/Sales-Analytics-Project/data/sales_data_cleaned.csv')

# Summary statistics
print(df.describe())

# Top 5 products by sales
top_products = df.groupby('Product line')['Sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products by Sales:\n", top_products)

# Monthly sales trend
df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
print("Monthly Sales:\n", monthly_sales)