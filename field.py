class Field:
    def __init__(self, cells: list = None):
        self._cells = set(cells if cells else [])

    def born_cells(self, cells: list):
        for cell in cells:
            self._cells.add(cell)

    def kill_cells(self, cells: list):
        for cell in cells:
            self._cells.remove(cell)

    def get_live_neighbours(self, cell: tuple) -> list:
        return self._get_neighbours(cell, live=True)

    def get_dead_neighbours(self, cell: tuple) -> list:
        return self._get_neighbours(cell, live=False)

    @property
    def cells(self):
        return list(self._cells)

    def _get_neighbours(self, cell: tuple, live: bool) -> list:
        # TODO solve for n-metric space
        potential_neighbours = [
            (cell[0] - 1, cell[1] - 1),
            (cell[0] - 1, cell[1]),
            (cell[0] - 1, cell[1] + 1),
            (cell[0], cell[1] - 1),
            (cell[0], cell[1] + 1),
            (cell[0] + 1, cell[1] - 1),
            (cell[0] + 1, cell[1]),
            (cell[0] + 1, cell[1] + 1)
        ]

        neighbours = []
        for potential_neighbour in potential_neighbours:
            if live:
                if potential_neighbour in self._cells:
                    neighbours.append(potential_neighbour)
            else:
                if potential_neighbour not in self._cells:
                    neighbours.append(potential_neighbour)
        return neighbours
