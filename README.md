# Sales Analytics Project

## Business Objective
Analyze retail sales data to identify revenue trends, top products, and underperforming categories to support decision-making.

## Tools & Skills
- PostgreSQL: SQL joins, aggregations, window functions
- Python: Data cleaning, EDA
- Power BI: Dashboard design and KPI visualization

## Dataset
- Source: Synthetic retail dataset (AU-focused)
- Tables: Sales, Customers, Products
- Columns: customer_id, product_id, quantity, revenue, date

## Approach
1. Data cleaning in Python (handle missing values, normalize columns)
2. SQL queries for KPI calculation:
   - Total revenue by product and region
   - Monthly revenue trend
   - Top 10 customers
3. Power BI dashboard:
   - KPI cards
   - Revenue trends
   - Product and region filters

## Results & Insights
- Top 5 products generate 55% of revenue
- Revenue dips in Q2 highlight potential marketing opportunities
- Certain regions underperform → promotional focus recommended

## Business Impact
- Improved inventory allocation
- Targeted marketing strategies
- Revenue optimization

## How to Run
1. PostgreSQL database setup
2. Run SQL scripts in `/sql`
3. Load CSV data into Power BI
4. Open dashboard PBIX file

## File Structure
- /data → CSV datasets
- /sql → SQL scripts
- /notebooks → Python EDA
- /PowerBI → Dashboard file

## Installation & Usage
1. Clone the repository:  
   ```bash
   git clone https://github.com/NiraliPatel10/Sales-Analytics-Project.git
   cd Sales-Analytics-Project

