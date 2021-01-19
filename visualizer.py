import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def render(self, cells, step):
        plt.figure(figsize=(8, 8))
        plt.axis('equal')

        for cell in cells:
            plt.fill(np.array([cell[1], cell[1] + 1, cell[1] + 1, cell[1]]),
                     np.array([cell[0], cell[0], cell[0] + 1, cell[0] + 1]))

        plt.savefig(f'data/{step}.png')
