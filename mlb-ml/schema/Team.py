"""
Respresent a Team with info provided by the api
"""

class Team:

    team_id: int
    name: str
    link: str

    def __init__(self, team_id: int, name: str, link: str) -> None:
        self.team_id = team_id
        self.name = name
        self.link = link