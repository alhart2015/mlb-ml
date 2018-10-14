"""
Respresent a Team with info provided by the api
"""
from .division import Division
from .league import League
from .sport import Sport
from .venue import Venue

from typing import Dict

class Team:

    team_id: int
    name: str
    link: str
    venue: Venue
    team_code: str
    file_code: str
    abbreviation: str
    team_name: str
    location_name: str
    first_year_of_play: int
    league: League
    division: Division
    sport: Sport
    short_name: str
    spring_league: League
    active: bool

    def __init__(self, team_id: int, name: str, link: str,
        # Venue fields
        venue_id: int, venue_name: str, venue_link: str,
        team_code: str, file_code: str, abbreviation: str, team_name: str,
        location_name: str, first_year_of_play: int,
        # League fields
        league_id: int, league_name: str, league_link: str,
        # division fields
        division_id: int, division_name: str, division_link: str,
        # sport fields
        sport_id: int, sport_name: str, sport_link: str,
        short_name: str,
        # spring league fields
        spring_league_id: int, spring_league_name: str, spring_league_link: str,
        active: bool) -> None:

        self.team_id = team_id
        self.name = name
        self.link = link

        self.venue = Venue(venue_id, venue_name, venue_link)

        self.team_code = team_code
        self.file_code = file_code
        self.abbreviation = abbreviation
        self.team_name = team_name
        self.location_name = location_name
        self.first_year_of_play = first_year_of_play

        self.league = League(league_id, league_name, league_link, False)
        self.division = Division(division_id, division_name, division_link)
        self.sport = Sport(sport_id, sport_name, sport_link)

        self.short_name = short_name

        self.spring_league = League(spring_league_id, spring_league_name, spring_league_link, True)

        self.active = active

    def __str__(self) -> str:
        return f"""Team(
        team_id={self.team_id}
        name={self.name}
        link={self.link}
        venue={self.venue}
        team_code={self.team_code}
        file_code={self.file_code}
        abbreviation={self.abbreviation}
        team_name={self.team_name}
        location_name={self.location_name}
        first_year_of_play={self.first_year_of_play}
        league={self.league}
        division={self.division}
        sport={self.sport}
        short_name={self.short_name}
        spring_league={self.spring_league}
        active={self.active}
        )"""

    @staticmethod
    def from_json(json: Dict):
        venue_json: Dict = json['venue']
        league_json: Dict = json['league']
        division_json: Dict = json['division']
        sport_json: Dict = json['sport']
        spring_league_json: Dict = json['springLeague']

        return Team(
                    json['id'], json['name'], json['link'],
                    venue_json['id'], venue_json['name'], venue_json['link'],
                    json['teamCode'], json['fileCode'], json['abbreviation'], json['teamName'],
                    json['locationName'], json['firstYearOfPlay'],
                    league_json['id'], league_json['name'], league_json['link'],
                    division_json['id'], division_json['name'], division_json['link'],
                    sport_json['id'], sport_json['name'], sport_json['link'],
                    json['shortName'],
                    spring_league_json['id'], spring_league_json['name'], spring_league_json['link'],
                    json['active'])
