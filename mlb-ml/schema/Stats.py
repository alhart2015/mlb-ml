"""
The Stats provided by the api
"""

class Stats:

    games_played: int
    ground_outs: int
    runs: int
    doubles: int
    triples: int
    home_runs: int
    strike_outs: int
    base_on_balls: int
    intentional_walks: int
    hits: int
    hit_by_pitch: int
    avg: float
    at_bats: int
    obp: float
    slg: float
    ops: float
    caught_stealing: int
    stolen_bases: int
    stolen_base_percentage: float
    ground_into_double_play: int
    number_of_pitches: int
    plate_appearances: int
    total_bases: int
    rbi: int
    sac_bunts: int
    sac_flies: int
    ground_outs_to_airouts: float

    def __init__(self, games_played: int, ground_outs: int, runs: int,
                    doubles: int, triples: int, home_runs: int, strike_outs: int,
                    base_on_balls: int, intentional_walks: int, hits: int,
                    hit_by_pitch: int, avg: float, at_bats: int, obp: float,
                    slg: float, ops: float, caught_stealing: int, stolen_bases: int,
                    stolen_base_percentage: float, ground_into_double_play: int,
                    number_of_pitches: int, plate_appearances: int, total_bases: int,
                    rbi: int, sac_bunts: int, sac_flies: int, ground_outs_to_airouts: float
                    ) -> None:
    self.games_played = games_played
    self.ground_outs = ground_outs
    self.runs = runs
    self.doubles = doubles
    self.triples = triples
    self.home_runs = home_runs
    self.strike_outs = strike_outs
    self.base_on_balls = base_on_balls
    self.intentional_walks = intentional_walks
    self.hits = hits
    self.hit_by_pitch = hit_by_pitch
    self.avg = avg
    self.at_bats = at_bats
    self.obp = obp
    self.slg = slg
    self.ops = ops
    self.caught_stealing = caught_stealing
    self.stolen_bases = stolen_bases
    self.stolen_base_percentage = stolen_base_percentage
    self.ground_into_double_play = ground_into_double_play
    self.number_of_pitches = number_of_pitches
    self.plate_appearances = plate_appearances
    self.total_bases = total_bases
    self.rbi = rbi
    self.sac_bunts = sac_bunts
    self.sac_flies = sac_flies
    self.ground_outs_to_airouts = ground_outs_to_airouts
    