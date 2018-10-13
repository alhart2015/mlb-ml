"""
Utility file to store constants and util functions.
"""

# API URLs
BASE_STAT_URL = "https://statsapi.mlb.com/api/v1/stats"
HITTER_STAT_URL = "https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting"

AMERICAN_LEAGUE_ID = 103
NATIONAL_LEAGUE_ID = 104
TEAM_INFO_URL = f"https://statsapi.mlb.com/api/v1/teams?leagueIds={AMERICAN_LEAGUE_ID},{NATIONAL_LEAGUE_ID}"
