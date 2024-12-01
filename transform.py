import pandas as pd

# Read the CSV file
file_path = 'team_match_statistics.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Transform the data into the correct format
reshaped_data = pd.melt(
    data,
    id_vars=["team"],  # Keep the team column as is
    value_vars=["no_of_home_wins", "no_of_home_losses", "no_of_away_wins", "no_of_away_losses"],  # Columns to unpivot
    var_name="match_type",  # Name for the new column indicating the type
    value_name="count"  # Name for the new column holding the values
)

# Map the column names to more readable labels for match types
reshaped_data["match_type"] = reshaped_data["match_type"].map({
    "no_of_home_wins": "Home Wins",
    "no_of_home_losses": "Home Losses",
    "no_of_away_wins": "Away Wins",
    "no_of_away_losses": "Away Losses"
})

# Save or use the transformed data
reshaped_data.to_csv('transformed_team_match_statistics.csv', index=False)
print("Data transformed and saved to 'transformed_team_match_statistics.csv'.")
