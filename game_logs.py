from nba_api.stats.endpoints import teamgamelog
from df_games_team import Mavericks_id

Teamlog = teamgamelog.TeamGameLog(Season = '22019', Season_Typo = 'Regular Season', TeamID = 'Mavericks_id')

print(Teamlog)
