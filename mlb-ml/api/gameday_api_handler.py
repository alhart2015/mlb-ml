"""
Read from the MLB Gameday API.

Base URL: https://statsapi.mlb.com/docs/#operation/stats
Hitter stat URL: https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting
"""
import requests

from typing import List

def get_hitter_stats(url: str) -> List[str]:
    """
    Pull from the MLB Gameday API for hitter stats. Eventually we want this to
    return a list of players, but for now we'll make do with strings.
    """
    response = requests.get(url)

def test():
    print("here")