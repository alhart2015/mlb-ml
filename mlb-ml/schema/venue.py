class Venue:

    venue_id: int
    name: str
    link: str

    def __init__(self, venue_id: int, name: str, link: str) -> None:
        self.venue_id = venue_id
        self.name = name
        self.link = link

    def __str__(self) -> str:
        return f"""Venue(
        \tvenue_id={self.venue_id}
        \tname={self.name}
        \tlink={self.link}
        )"""