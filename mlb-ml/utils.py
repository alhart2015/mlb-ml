"""
Utility file to store constants and util functions.
"""

# API URLs
BASE_STAT_URL = "https://statsapi.mlb.com/api/v1/stats"
HITTER_STAT_URL = "https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting"

AMERICAN_LEAGUE_ID = 103
NATIONAL_LEAGUE_ID = 104
TEAM_INFO_URL = f"https://statsapi.mlb.com/api/v1/teams?leagueIds={AMERICAN_LEAGUE_ID},{NATIONAL_LEAGUE_ID}"

REGULAR_SEASON_GAME_TYPE = 'REGULAR_SEASON'

def hitter_url_for_team(team_id: int, season: int, game_type: str) -> str:
    return f'http://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting&gameType={game_type}&season={season}&teamId={team_id}'
