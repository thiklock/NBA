from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamelog
from nba_api.stats.endpoints import LeagueGameFinder
import os

nba_teams = teams.get_teams()


# Input for the Team

# Team_id = print(input('Type the teams abbreviation: '))

# Getting the ID for the Team
Mavericks = [team for team in nba_teams if team['abbreviation'] == 'DAL' ][0]
Mavericks_id = Mavericks['id']

print(f'Mavs Id is: {Mavericks_id}')

# Catching games
gamefinder = LeagueGameFinder(team_id_nullable=Mavericks_id)

# A DataFrame with those games.
Team_Games = gamefinder.get_data_frames()[0]
# print(Team_Games.tail(20))
# Saving the DataFrame into a .csv file so we can check it. 
Team_Games.to_csv(r'/home/tiktek/nba/nba.csv')
# counting amount of games
Number_of_games = int(Team_Games[['TEAM_ID']].count())
print(f'There is {Number_of_games} games in the DataFrame for all time')
# Counting games in season
Games_Season = Team_Games[Team_Games['SEASON_ID']  == '22019']
Number_of_games_Season = int(Games_Season[['SEASON_ID']].count())
Games_Season.to_csv(r'/home/tiktek/nba/NBA/Games_Season')
print(f'There is {Number_of_games_Season} games in this season.')