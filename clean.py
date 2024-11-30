# Step 1: Preprocess the Dataset
import pandas as pd

# Load the dataset
file_path = "path/to/starbucks.csv"  # Replace with your file path
starbucks_data = pd.read_csv("/Users/shalineraghupathy/Desktop/Info Vis/2021-12-21/starbucks.csv")

# Clean categorical data
starbucks_data['size'] = starbucks_data['size'].str.lower().str.strip()
starbucks_data['product_name'] = starbucks_data['product_name'].str.strip()

# Add derived metrics
starbucks_data['calories_per_ml'] = starbucks_data['calories'] / starbucks_data['serv_size_m_l']
starbucks_data['sugar_to_calorie_ratio'] = starbucks_data['sugar_g'] / starbucks_data['calories']

# Aggregate data for grouped visualizations
# 1. Average metrics by size
size_aggregates = starbucks_data.groupby('size').agg({
    'calories': 'mean',
    'sugar_g': 'mean',
    'caffeine_mg': 'mean',
    'calories_per_ml': 'mean'
}).reset_index()

# 2. Average metrics by milk type
milk_aggregates = starbucks_data.groupby('milk').agg({
    'calories': 'mean',
    'sugar_g': 'mean',
    'caffeine_mg': 'mean',
}).reset_index()

# Save preprocessed datasets
processed_file_path = '/Users/shalineraghupathy/Desktop/Info Vis/2021-12-21/starbucks_processed.csv'
aggregated_by_size_path = '/Users/shalineraghupathy/Desktop/Info Vis/2021-12-21/starbucks_aggregated_by_size.csv'
aggregated_by_milk_path = '/Users/shalineraghupathy/Desktop/Info Vis/2021-12-21//starbucks_aggregated_by_milk.csv'

starbucks_data.to_csv(processed_file_path, index=False)
size_aggregates.to_csv(aggregated_by_size_path, index=False)
milk_aggregates.to_csv(aggregated_by_milk_path, index=False)

processed_file_path, aggregated_by_size_path, aggregated_by_milk_path
