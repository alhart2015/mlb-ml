"""
Read from the MLB Gameday API.

Base URL: https://statsapi.mlb.com/docs/#operation/stats
Hitter stat URL: https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting
"""
import requests

from typing import Dict, List

from schema.player import Player
from schema.team import Team

def get_hitter_stats(url: str) -> List[Player]:
    """
    Pull from the MLB Gameday API for hitter stats.

    todo: figure out how to get all players and not just the top 50
    """
    response = requests.get(url)
    response_json: Dict = response.json()
    
    splits_list = response_json['stats'][0]['splits']

    players = []

    for split in splits_list:
        players.append(Player.from_splits_json(split))

    return players

def get_team_info(url: str) -> List[Team]:
    """
    Pull from the MLB Gameday API for teams. This will give you a comprehensive
    list of all teams, hopefully we can use that to pull all stats for all
    players on all teams.
    """
    response = requests.get(url)
    response_json: Dict = response.json()

    teams = response_json['teams']

    parsed_teams = []
    for team in teams:
        parsed_teams.append(Team.from_json(team))

    return parsed_teams

    # print(response.text)

def test():
    print("here")