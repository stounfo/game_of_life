import random
import time

from core import Core
from field import Field
from visualizer import Visualizer


class Game:
    def __init__(self, initial_cells: list, neighbours_to_born: list,
                 neighbours_to_survive: list, last_step: int):
        self._field = Field(initial_cells)
        self._core = Core(neighbours_to_born, neighbours_to_survive)
        self._visualizer = Visualizer()
        self._last_step = last_step
        self.step = 0

    def run(self):
        while self.step < self._last_step:
            self._visualizer.render(self._field.cells, self.step)
            t = time.time()
            self._find_born_at_next_step()
            print(time.time() - t)

            t = time.time()
            self._find_killed_at_next_step()
            print(time.time() - t)
            self._next_step()

    def _find_born_at_next_step(self):
        self._born_at_next_step = []

        potential_live_cells = set()
        for cell in self._field.cells:
            neighbours = self._field.get_dead_neighbours(cell)
            for neighbour in neighbours:
                potential_live_cells.add(neighbour)

        for cell in potential_live_cells:
            neighbours_count = len(self._field.get_live_neighbours(cell))
            if self._core.check_born(neighbours_count):
                self._born_at_next_step.append(cell)

    def _find_killed_at_next_step(self):
        self._killed_at_next_step = []
        for cell in self._field.cells:
            neighbours_count = len(self._field.get_live_neighbours(cell))
            if self._core.check_kill(neighbours_count):
                self._killed_at_next_step.append(cell)

    def _next_step(self):
        print(self.step, len(self._field.cells))
        self._field.born_cells(self._born_at_next_step)
        self._field.kill_cells(self._killed_at_next_step)
        self.step += 1


# Game([(1, 1), (1, 2), (1, 3), (2, 1), (3, 2),
#       (10, 11), (11, 10), (11, 11), (10, 10)],
#      [3],
#      [3, 2],
#      5).run()

# Game([(i, j) for i in range(100) for j in range(100)],
#      [3],
#      [2, 3],
#      float('inf')).run()

Game([(i, j) for i in range(100) for j in range(100)
      if random.choice([True, False])
      if random.choice([True, False])],
     [3],
     [2, 3],
     float('inf')).run()
