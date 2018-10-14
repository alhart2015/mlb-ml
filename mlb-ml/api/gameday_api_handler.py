"""
Read from the MLB Gameday API.

Base URL: https://statsapi.mlb.com/docs/#operation/stats
Hitter stat URL: https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting
"""
from typing import Dict, List

from schema.player import Player
from schema.team import Team

import requests

import utils

def get_top_hitter_stats() -> List[Player]:
    """
    Pull from the MLB Gameday API for hitter stats.

    todo: figure out how to get all players and not just the top 50
    """
    url = utils.HITTER_STATS_URL

    response = requests.get(url)
    response_json: Dict = response.json()
    
    splits_list = response_json['stats'][0]['splits']

    players = []

    for split in splits_list:
        players.append(Player.from_splits_json(split))

    return players

def get_team_info() -> List[Team]:
    """
    Pull from the MLB Gameday API for teams. This will give you a comprehensive
    list of all teams, hopefully we can use that to pull all stats for all
    players on all teams.
    """
    url = utils.TEAM_INFO_URL

    response = requests.get(url)
    response_json: Dict = response.json()

    teams = response_json['teams']

    parsed_teams = []
    for team in teams:
        parsed_teams.append(Team.from_json(team))

    return parsed_teams

    # print(response.text)

def get_hitter_stats_for_team_id(team_id: int, season: int, game_type: str) -> List[Player]:
    """
    Get hitter stats for the provided team, season, and game type.

    todo: this should def be combined with get_top_hitter_stats()
    """
    url = utils.hitter_url_for_team(team_id, season, game_type)

    response = requests.get(url)
    response_json: Dict = response.json()
    
    splits_list = response_json['stats'][0]['splits']

    players = []

    for split in splits_list:
        players.append(Player.from_splits_json(split))

    return players

def test():
    print("here")