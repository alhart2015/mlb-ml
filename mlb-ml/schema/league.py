class League:

    league_id: int
    name: str
    link: str
    # abbreviation: str
    # NOTE: ^^ spring leagues do have appreviations, but national and american
    # leagues don't have abbreviations. we'll leave it out for now.

    def __init__(self, league_id: int, name: str, link: str) -> None:
        self.league_id = league_id
        self.name = name
        self.link = link

    def __str__(self) -> str:
        return f"""League(
        \tleague_id={self.league_id}
        \tname={self.name}
        \tlink={self.link}
        )"""