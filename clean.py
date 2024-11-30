# Ensure necessary libraries are loaded
import pandas as pd

# Reload dataset
file_path = "/Users/shalineraghupathy/Desktop/infovis/2021-12-21/starbucks.csv"
data = pd.read_csv(file_path)

# Clean text fields
data['product_name'] = data['product_name'].str.strip()
data['size'] = data['size'].str.lower().str.strip()

# Map milk types to descriptive labels
milk_mapping = {
    0: "None",
    1: "Nonfat",
    2: "2%",
    3: "Soy",
    4: "Coconut",
    5: "Whole"
}
data['milk'] = data['milk'].map(milk_mapping)

# Ensure 'whip' is binary
data['whip'] = data['whip'].apply(lambda x: 1 if x == 1 else 0)

# Handle missing or incorrect numeric columns
numeric_cols = ['fiber_g', 'trans_fat_g', 'calories', 'total_fat_g', 
                'saturated_fat_g', 'cholesterol_mg', 'sodium_mg', 
                'total_carbs_g', 'sugar_g', 'caffeine_mg']
data[numeric_cols] = data[numeric_cols].fillna(0)  # Replace NaN with 0

# Add derived metrics
data['calories_per_ml'] = data['calories'] / data['serv_size_m_l']
data['sugar_to_calorie_ratio'] = data['sugar_g'] / data['calories']
data['sugar_to_calorie_ratio'] = data['sugar_to_calorie_ratio'].fillna(0)

# Categorize beverages
def categorize_beverage(product_name):
    if "coffee" in product_name.lower():
        return "Coffee"
    elif "frappuccino" in product_name.lower():
        return "Frappuccino"
    elif "tea" in product_name.lower():
        return "Tea"
    elif "espresso" in product_name.lower():
        return "Espresso Drinks"
    elif "smoothie" in product_name.lower():
        return "Smoothie"
    else:
        return "Other"

data['Beverage_Category'] = data['product_name'].apply(categorize_beverage)

# Aggregate data for visualizations
nutrient_cols = ['total_fat_g', 'total_carbs_g', 'sugar_g', 'fiber_g']
category_nutrients = data.groupby('Beverage_Category')[nutrient_cols].mean().reset_index()

# Aggregate data by milk type
milk_aggregates = data.groupby('milk').agg({
    'calories': 'mean',
    'sugar_g': 'mean',
    'caffeine_mg': 'mean'
}).reset_index()

# Save cleaned datasets
data.to_csv("/Users/shalineraghupathy/Desktop/infovis/2021-12-21/starbucks_cleaned.csv", index=False)  # Full cleaned dataset
category_nutrients.to_csv("/Users/shalineraghupathy/Desktop/infovis/2021-12-21/starbucks_nutrient_by_category.csv", index=False)  # For stacked bar chart
milk_aggregates.to_csv("/Users/shalineraghupathy/Desktop/infovis/2021-12-21/starbucks_aggregated_by_milk.csv", index=False)  # For pie chart

print("Datasets cleaned and saved successfully.")
