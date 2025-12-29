import pandas as pd
import os

# Ensure the output folder exists
output_folder = '../data'
os.makedirs(output_folder, exist_ok=True)

# Load dataset
df = pd.read_csv('/Users/niralipatel/Downloads/Sales-Analytics-Project/data/SuperMarket_Analysis.csv')

# ... your existing cleaning code ...

# Save cleaned data
df.to_csv(f'{output_folder}/sales_data_cleaned.csv', index=False)
print("Data cleaned and saved!")
