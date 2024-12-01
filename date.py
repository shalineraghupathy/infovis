import pandas as pd

# Step 1: Load the CSV
df = pd.read_csv('matches.csv')

# Step 2: Ensure match_date is in datetime format
df['match_date'] = pd.to_datetime(df['match_date'], errors='coerce')

# Step 3: Drop rows where 'match_date' is NaT (Not a Time)
df.dropna(subset=['match_date'], inplace=True)

# Step 4: Extract the year and create a new column 'year'
df['year'] = df['match_date'].dt.year

# Step 5: Convert the 'year' column to an integer type
df['year'] = df['year'].astype(int)

# Step 6: Save the modified DataFrame to a new CSV file (or you can choose a different name)
df.to_csv('matches_cleaned.csv', index=False)

# Display the cleaned DataFrame
print("New file saved with year column and removed rows with no match_date.")
print(df.head())
