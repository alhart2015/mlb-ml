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

    def __str__(self) -> str:
        return f"""Stats(
            \tgames_played={self.games_played}
            \tground_outs={self.ground_outs}
            \truns={self.runs}
            \tdoubles={self.doubles}
            \ttriples={self.triples}
            \thome_runs={self.home_runs}
            \tstrike_outs={self.strike_outs}
            \tbase_on_balls={self.base_on_balls}
            \tintentional_walks={self.intentional_walks}
            \thits={self.hits}
            \thit_by_pitch={self.hit_by_pitch}
            \tavg={self.avg}
            \tat_bats={self.at_bats}
            \tobp={self.obp}
            \tslg={self.slg}
            \tops={self.ops}
            \tcaught_stealing={self.caught_stealing}
            \tstolen_bases={self.stolen_bases}
            \tstolen_base_percentage={self.stolen_base_percentage}
            \tground_into_double_play={self.ground_into_double_play}
            \tnumber_of_pitches={self.number_of_pitches}
            \tplate_appearances={self.plate_appearances}
            \ttotal_bases={self.total_bases}
            \trbi={self.rbi}
            \tsac_bunts={self.sac_bunts}
            \tsac_flies={self.sac_flies}
            \tground_outs_to_airouts={self.ground_outs_to_airouts}
        )"""
