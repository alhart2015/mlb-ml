class Division:

    division_id: int
    name: str
    link: str
    
    def __init__(self, division_id: int, name: str, link: str) -> None:
        self.division_id = division_id
        self.name = name
        self.link = link

    def __str__(self) -> str:
        return f"""Division(
        \tdivision_id={self.division_id}
        \tname={self.name}
        \tlink={self.link}
        )"""