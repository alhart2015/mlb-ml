class Sport:

    sport_id: int
    name: str
    link: str

    def __init__(self, sport_id: int, name: str, link: str) -> None:
        self.sport_id = sport_id
        self.name = name
        self.link = link

    def __str__(self) -> str:
        return f"""Sport(
        \tsport_id={self.sport_id}
        \tname={self.name}
        \tlink={self.link}
        )"""