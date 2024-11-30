import pandas as pd

# Load the dataset
matches_data = pd.read_csv('matches.csv')  # Replace 'matches.csv' with the path to your file

# Initialize a dictionary to store the results
team_stats = {}

# Teams list from both team1 and team2
teams = pd.concat([matches_data['team1'], matches_data['team2']]).unique()

# Calculate statistics for each team
for team in teams:
    # Total matches played
    total_matches = matches_data[(matches_data['team1'] == team) | (matches_data['team2'] == team)].shape[0]

    # Home and away matches
    home_matches = matches_data[matches_data['team1'] == team].shape[0]
    away_matches = matches_data[matches_data['team2'] == team].shape[0]

    # Wins
    home_wins = matches_data[(matches_data['team1'] == team) & (matches_data['winner'] == team)].shape[0]
    away_wins = matches_data[(matches_data['team2'] == team) & (matches_data['winner'] == team)].shape[0]

    # Losses
    home_losses = home_matches - home_wins
    away_losses = away_matches - away_wins

    # Store results in the dictionary
    team_stats[team] = {
        'no_of_matches': total_matches,
        'no_of_home_matches': home_matches,
        'no_of_away_matches': away_matches,
        'no_of_home_wins': home_wins,
        'no_of_home_losses': home_losses,
        'no_of_away_wins': away_wins,
        'no_of_away_losses': away_losses,
    }

# Convert the dictionary to a DataFrame for better representation
team_stats_df = pd.DataFrame.from_dict(team_stats, orient='index')

# Save the DataFrame to a CSV file
team_stats_df.to_csv('team_match_statistics.csv', index=True)

print("The CSV file has been generated: 'team_match_statistics.csv'")
