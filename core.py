class Core:
    def __init__(self, neighbours_to_born: list, neighbours_to_survive: list):
        self._neighbours_to_born = neighbours_to_born
        self._neighbours_to_survive = neighbours_to_survive

    def check_born(self, neighbours_count: int):
        return neighbours_count in self._neighbours_to_born

    def check_kill(self, neighbours_count: int):
        return neighbours_count not in self._neighbours_to_survive
