import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(2026)

#  DATA GENERATION 

# 1. Create customer data (500 customers)
customers = pd.DataFrame({
    'Customer_ID': np.arange(1, 501),
    'Name': [f'Customer_{i}' for i in range(1, 501)],
    'Age': np.random.randint(18, 71, 500),
    'City': np.random.choice(['NY', 'LA', 'SF', 'CHI', 'MIA', 'SEA'], 500),
    'Signup_Date': pd.date_range('2023-01-01', '2023-12-31', periods=500),
    'Total_Spent': np.random.randint(100, 10001, 500)
})

print("Customers created:")
print(customers.head())
print(f"Shape: {customers.shape}")

#  Create order data (1000 orders)
# Define products by category
products = {
    'Electronics': ['Laptop', 'Phone', 'Headphones'],
    'Clothing': ['Shirt', 'Jeans', 'Jacket'],
    'Food': ['Pizza', 'Burger', 'Sushi'],
    'Books': ['Fiction', 'Non-Fiction', 'Sci-Fi']
}

# Generate random categories and products
categories = np.random.choice(list(products.keys()), 1000)
product_list = []
for cat in categories:
    product_list.append(np.random.choice(products[cat]))

orders = pd.DataFrame({
    'Order_ID': [f'ORD{str(i).zfill(4)}' for i in range(1, 1001)],
    'Customer_ID': np.random.randint(1, 501, 1000),
    'Product': product_list,
    'Category': categories,
    'Price': np.random.randint(10, 501, 1000),
    'Quantity': np.random.randint(1, 11, 1000),
    'Order_Date': pd.date_range('2024-01-01', '2024-12-31', periods=1000)
})

print("\nOrders created:")
print(orders.head())
print(f"Shape: {orders.shape}")

#  Add Revenue column
orders['Revenue'] = orders['Price'] * orders['Quantity']

print(f"\n Data generation complete!")
print(f"Customers: {customers.shape[0]} rows, {customers.shape[1]} columns")
print(f"Orders: {orders.shape[0]} rows, {orders.shape[1]} columns")

# DATA EXPLORATION 

#  Basic info about customers
print("\n" + "="*50)
print("CUSTOMERS INFO")
print("="*50)
customers.info()

#  Statistics for numeric columns in orders
print("\n" + "="*50)
print("ORDERS STATISTICS")
print("="*50)
print(orders.describe())

#  Check missing values
print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print("Customers missing:\n", customers.isnull().sum())
print("\nOrders missing:\n", orders.isnull().sum())

#  First and last orders
print("\n" + "="*50)
print("FIRST AND LAST ORDERS")
print("="*50)
print("First 5:\n", orders.head())
print("\nLast 5:\n", orders.tail())

#  Unique values
print("\n" + "="*50)
print("UNIQUE VALUES")
print("="*50)
print(f"Unique Categories: {orders['Category'].unique().tolist()}")
print(f"Unique Cities: {customers['City'].unique().tolist()}")

# FILTERING 

#  Customers older than 40
older_customers = customers[customers['Age'] > 40]
print(f"\nCustomers older than 40: {len(older_customers)}")

#  Orders with price > $300
expensive_orders = orders[orders['Price'] > 300]
print(f"Orders with price > $300: {len(expensive_orders)}")

#  Electronics orders with quantity > 3
electronics_bulk = orders[(orders['Category'] == 'Electronics') & (orders['Quantity'] > 3)]
print(f"Electronics bulk orders (qty > 3): {len(electronics_bulk)}")

#  High value customers (NY or LA, spent > $5000)
high_value_customers = customers[(customers['City'].isin(['NY', 'LA'])) & 
                                  (customers['Total_Spent'] > 5000)]
print(f"High value customers (NY/LA, spent > $5000): {len(high_value_customers)}")

#  Recent book orders (after 2024-02-01)
recent_books = orders[(orders['Category'] == 'Books') & 
                       (orders['Order_Date'] > '2024-02-01')]
print(f"Recent book orders (after Feb 1): {len(recent_books)}")

#  Top 5 most expensive orders
top_orders = orders.nlargest(5, 'Revenue')
print("\nTop 5 orders by revenue:")
print(top_orders[['Order_ID', 'Product', 'Revenue']])

#  Customers with missing values
customers_with_missing = customers[customers.isnull().any(axis=1)]
print(f"\nCustomers with missing values: {len(customers_with_missing)}")

#  AGGREGATIONS 

#  Overall statistics
print("\n" + "="*50)
print("OVERALL STATISTICS")
print("="*50)
print(f"Total Revenue: ${orders['Revenue'].sum():,.2f}")
print(f"Average Order Value: ${orders['Revenue'].mean():,.2f}")
print(f"Total Orders: {len(orders)}")

# Revenue by category
category_revenue = orders.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Category:")
print(category_revenue)

#  Orders per category
orders_per_category = orders.groupby('Category')['Order_ID'].count()
print("\nOrders per Category:")
print(orders_per_category)

#  Average price per category
avg_price_category = orders.groupby('Category')['Price'].mean().round(2)
print("\nAverage Price by Category:")
print(avg_price_category)

#  Revenue by city (merge first)
merged = pd.merge(orders, customers, on='Customer_ID')
revenue_by_city = merged.groupby('City')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by City:")
print(revenue_by_city)

#  Top 3 products
top_products = orders.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Products by Revenue:")
print(top_products)

#  Monthly revenue
orders['Month'] = orders['Order_Date'].dt.month
monthly_revenue = orders.groupby('Month')['Revenue'].sum()
print("\nMonthly Revenue:")
for month, rev in monthly_revenue.items():
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1]
    print(f"  {month_name}: ${rev:,.2f}")

#  High frequency customers
customer_order_counts = orders.groupby('Customer_ID').size()
avg_orders = customer_order_counts.mean()
high_frequency = customer_order_counts[customer_order_counts > avg_orders]
print(f"\nHigh frequency customers (> avg): {len(high_frequency)}")

#  Age-spent correlation
age_spent_correlation = customers['Age'].corr(customers['Total_Spent'])
print(f"\nCorrelation between Age and Total Spent: {age_spent_correlation:.3f}")

#  Category summary
category_summary = orders.groupby('Category').agg({
    'Revenue': 'sum',
    'Price': 'mean',
    'Order_ID': 'count'
}).rename(columns={'Order_ID': 'Num_Orders'}).round(2)
print("\nCategory Summary:")
print(category_summary)

# DATA CLEANING

# Random 5 customers' Age to NaN
missing_age_indices = np.random.choice(customers.index, 5, replace=False)
customers.loc[missing_age_indices, 'Age'] = np.nan

# Random 10 orders' Quantity to NaN
missing_qty_indices = np.random.choice(orders.index, 10, replace=False)
orders.loc[missing_qty_indices, 'Quantity'] = np.nan

print(f"\nIntroduced missing values:")
print(f"Customers with missing Age: {customers['Age'].isnull().sum()}")
print(f"Orders with missing Quantity: {orders['Quantity'].isnull().sum()}")

#  Handle missing values
median_age = customers['Age'].median()
customers['Age'] = customers['Age'].fillna(median_age)

median_qty = orders['Quantity'].median()
orders['Quantity'] = orders['Quantity'].fillna(median_qty)

print(f"\nAfter handling missing values:")
print(f"Customers with missing Age: {customers['Age'].isnull().sum()}")
print(f"Orders with missing Quantity: {orders['Quantity'].isnull().sum()}")

#  Remove duplicates
orders_clean = orders.drop_duplicates()
print(f"\nDuplicates removed from orders: {len(orders) - len(orders_clean)}")


#  Add Customer_Segment
def get_segment(spent):
    if spent >= 5000:
        return 'Gold'
    elif spent >= 2000:
        return 'Silver'
    elif spent >= 1000:
        return 'Bronze'
    else:
        return 'Basic'

customers['Customer_Segment'] = customers['Total_Spent'].apply(get_segment)
print("\nCustomer Segment Distribution:")
print(customers['Customer_Segment'].value_counts())

#  Add Order_Status
def get_order_status(revenue):
    if revenue >= 1000:
        return 'High Value'
    elif revenue >= 500:
        return 'Medium Value'
    else:
        return 'Low Value'

orders['Order_Status'] = orders['Revenue'].apply(get_order_status)
print("\nOrder Status Distribution:")
print(orders['Order_Status'].value_counts())

#  MERGE 

#  Merge data
merged_df = pd.merge(orders, customers, on='Customer_ID')
print(f"\nMerged DataFrame shape: {merged_df.shape}")

#  Average age by segment
avg_age_by_segment = customers.groupby('Customer_Segment')['Age'].mean().round(1)
print("\nAverage Age by Segment:")
print(avg_age_by_segment)

#  Customers who ordered from ALL categories
customers_all_categories = merged_df.groupby('Customer_ID').agg({
    'Category': 'nunique'
}).reset_index()
customers_all_categories = customers_all_categories[
    customers_all_categories['Category'] == len(orders['Category'].unique())
]
print(f"\nCustomers who ordered from ALL categories: {len(customers_all_categories)}")

#  Most popular product in each category
most_popular_by_category = orders.groupby(['Category', 'Product']).size().reset_index(name='Count')
most_popular_by_category = most_popular_by_category.loc[
    most_popular_by_category.groupby('Category')['Count'].idxmax()
]
print("\nMost Popular Product in Each Category:")
print(most_popular_by_category[['Category', 'Product', 'Count']])

#  Month-over-month growth
monthly_revenue = orders.groupby('Month')['Revenue'].sum()
mom_growth = monthly_revenue.pct_change() * 100
print("\nMonth-over-Month Growth (%):")
for month, growth in mom_growth.items():
    if month > 1:
        month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1]
        print(f"  {month_name}: {growth:.1f}%")



#  Save to CSV
customers.to_csv('customers_cleaned.csv', index=False)
orders.to_csv('orders_cleaned.csv', index=False)
category_summary.to_csv('category_summary.csv')

print("\n Data exported to CSV files")

