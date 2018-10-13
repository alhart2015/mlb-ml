"""
Class to represent a player.
"""
from typing import Dict

from .stats import Stats
from .team import Team

class Player():

    season: int
    player_id: int
    full_name: str
    link: str
    first_name: str
    last_name: str
    rank: int
    stats: Stats
    team_id: int
    team_name: str
    team_link: str

    def __init__(self, season: int, player_id: int, full_name: str, link: str,
                    first_name: str, last_name: str, rank: int, 
                    # stats fields
                    games_played: int, ground_outs: int, runs: int, doubles: int, 
                    triples: int, home_runs: int, strike_outs: int, base_on_balls: int,
                    intentional_walks: int, hits: int, hit_by_pitch: int, 
                    avg: float, at_bats: int, obp: float, slg: float, ops: float, 
                    caught_stealing: int, stolen_bases: int, stolen_base_percentage: float, 
                    ground_into_double_play: int, number_of_pitches: int,
                    plate_appearances: int, total_bases: int, rbi: int, sac_bunts: int, 
                    sac_flies: int, ground_outs_to_airouts: float,
                    # team fields
                    team_id: int, team_name: str, team_link: str
                    ) -> None:

        stats = Stats(games_played, ground_outs, runs, doubles, triples, home_runs,
                        strike_outs, base_on_balls, intentional_walks, hits, hit_by_pitch, 
                        avg, at_bats, obp, slg, ops, caught_stealing, stolen_bases,
                        stolen_base_percentage, ground_into_double_play, number_of_pitches,
                        plate_appearances, total_bases, rbi, sac_bunts, sac_flies,
                        ground_outs_to_airouts)

        self.season = season
        self.player_id = player_id
        self.full_name = full_name
        self.link = link
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank

        self.stats = stats
        self.team_id = team_id
        self.team_name = team_name
        self.team_link = team_link

    @staticmethod
    def from_splits_json(splits_json: Dict):
        """
        Generate a Player object from a json object received from the api. Note
        that for some reason this errors if you tell it the return type is Player
        (eg def from_splits_json(splits_json: Dict) -> Player: )

        Look into that.
        """
        season = splits_json['season']
        stats = splits_json['stat']
        team = splits_json['team']
        player_info = splits_json['player']
        rank = splits_json['rank']

        return Player(season,
                player_info['id'], player_info['fullName'], player_info['link'],
                player_info['firstName'], player_info['lastName'], rank,
                stats['gamesPlayed'], stats['groundOuts'], stats['runs'],
                stats['doubles'], stats['triples'], stats['homeRuns'],
                stats['strikeOuts'], stats['baseOnBalls'], stats['intentionalWalks'],
                stats['hits'], stats['hitByPitch'], stats['avg'], stats['atBats'],
                stats['obp'], stats['slg'], stats['ops'], stats['caughtStealing'],
                stats['stolenBases'], stats['stolenBasePercentage'], stats['groundIntoDoublePlay'],
                stats['numberOfPitches'], stats['plateAppearances'], stats['totalBases'],
                stats['rbi'], stats['sacBunts'], stats['sacFlies'], stats['groundOutsToAirouts'],
                team['id'], team['name'], team['link'])

    def __str__(self) -> str:
        return f"""Player(
        player_id={self.player_id}
        link={self.link}
        first_name={self.first_name}
        last_name={self.last_name}
        rank={self.rank}
        stats={self.stats}
        team_id={self.team_id}
        team_name={self.team_name}
        team_link={self.team_link}
        )"""


