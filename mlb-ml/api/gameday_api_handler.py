"""
Read from the MLB Gameday API.

Base URL: https://statsapi.mlb.com/docs/#operation/stats
Hitter stat URL: https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting
"""
import requests

from typing import Dict, List

from schema.player import Player

def get_hitter_stats(url: str) -> List[Player]:
    """
    Pull from the MLB Gameday API for hitter stats. Eventually we want this to
    return a list of players, but for now we'll make do with strings.
    """
    response = requests.get(url)
    response_json: Dict = response.json()
    
    splits_list = response_json['stats'][0]['splits']

    players = []

    for split in splits_list:
        players.append(Player.from_splits_json(split))

    return players


def test():
    print("here")