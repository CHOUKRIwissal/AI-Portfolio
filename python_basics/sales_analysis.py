import numpy as np

# 1. Create sales data: 8 stores × 5 categories × 6 months
sales = np.random.randint(1000, 50001, size=(8, 5, 6))
print(f"Sales shape: {sales.shape}")  

# 2. Store and category names
stores = np.array(['Store 1', 'Store 2', 'Store 3', 'Store 4', 
                   'Store 5', 'Store 6', 'Store 7', 'Store 8'])
categories = np.array(['Electronics', 'Clothing', 'Food', 'Books', 'Toys'])

# 3. Monthly growth rates
growth_rates = np.random.uniform(-0.05, 0.08, size=6)
print(f"Growth rates: {growth_rates.round(3)}")

# AGGREGATIONS

# 4. Total sales per store (sum across categories and months)
store_totals = np.sum(sales, axis=(1, 2))
print(f"\nStore totals: {store_totals}")

# 5. Total sales per category (sum across stores and months)
category_totals = np.sum(sales, axis=(0, 2))
print(f"Category totals: {category_totals}")

# 6. Monthly total sales (sum across stores and categories)
monthly_totals = np.sum(sales, axis=(0, 1))
print(f"Monthly totals: {monthly_totals}")

# 7. Store with highest total sales
best_store_idx = np.argmax(store_totals)
best_store = stores[best_store_idx]
print(f"\nBest store: {best_store} (${store_totals[best_store_idx]:,})")

# 8. Category with highest total sales
best_cat_idx = np.argmax(category_totals)
best_category = categories[best_cat_idx]
print(f"Best category: {best_category} (${category_totals[best_cat_idx]:,})")

# 9. Average sales per store per month (collapse categories)
avg_store_monthly = np.mean(sales, axis=1)  
print(f"\nAverage monthly sales per store: {avg_store_monthly.mean(axis=1).round(0)}")

# FILTERING 

# 10. Stores above average
store_avg = np.mean(store_totals)
high_performers = stores[store_totals > store_avg]
print(f"\nHigh performers: {high_performers}")

# 11. Categories with > $100,000 total
strong_categories = categories[category_totals > 100000]
print(f"Strong categories: {strong_categories}")

# 12. Find the month with highest sales
best_month_idx = np.argmax(monthly_totals)
best_month = best_month_idx + 1
best_sales = monthly_totals[best_month_idx]
print(f"Best month: {best_month} (${best_sales:,})")

# 13. Underperforming stores (below average in ALL categories)
store_category_avg = np.mean(sales, axis=2) 
cat_overall_avg = np.mean(store_category_avg, axis=0)  # Average per category
below_all = np.all(store_category_avg < cat_overall_avg, axis=1)
underperforming = stores[below_all]
print(f"Underperforming stores: {underperforming}")

# 14. Correlation between Store 1 and Store 2 sales (across months)
store1_monthly = np.sum(sales[0, :, :], axis=0)  # Store 1 monthly totals
store2_monthly = np.sum(sales[1, :, :], axis=0)  # Store 2 monthly totals
correlation = np.corrcoef(store1_monthly, store2_monthly)[0, 1]
print(f"\nCorrelation between Store 1 and Store 2: {correlation:.3f}")

# ADVANCED OPERATIONS 

# 15. Normalize sales to 0-1 range
min_sales = sales.min()
max_sales = sales.max()
normalized_sales = (sales - min_sales) / (max_sales - min_sales)
print(f"\nNormalized sales range: {normalized_sales.min():.2f} to {normalized_sales.max():.2f}")

# 16. Top 3 stores
top_3_indices = np.argsort(store_totals)[::-1][:3]
top_3_stores = stores[top_3_indices]
print(f"Top 3 stores: {top_3_stores}")

# 17. Month-over-month percentage change
mom_change = np.diff(monthly_totals) / monthly_totals[:-1] * 100
print(f"Month-over-month change (%): {mom_change.round(1)}")

# 18. Most consistent category (lowest variance across stores)
category_variances = np.var(np.sum(sales, axis=2), axis=0)  # Variance across stores
most_consistent_idx = np.argmin(category_variances)
most_consistent = categories[most_consistent_idx]
print(f"Most consistent category: {most_consistent}")

# 19. Store-month matrix (collapse categories)
store_month_matrix = np.sum(sales, axis=1) 
print(f"\nStore-Month matrix shape: {store_month_matrix.shape}")

# 20. Store volatility (std of monthly sales)
store_volatility = np.std(store_month_matrix, axis=1)
print(f"Store volatility: {store_volatility.round(0)}")