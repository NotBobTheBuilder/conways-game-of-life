from itertools import product
from random import choice

def cells_3x3(row, col):
    """Set of the cells around (and including) the given one"""
    return set(product(range(row-1, row+2), range(col-1, col+2)))

def neighbours(row, col):
    """Set of cells that directly border the given one"""
    return cells_3x3(row, col) - {(row, col)}

class CGOL(object):
    """Iterator representing the generations of a game"""
    def __init__(self, grid):
        """
        Takes a 2d list of bools as a grid which is used to create
        internal representation of game state (a set of living coordinates)
        """
        self.cells = {(row_i, col_i) for row_i, row in enumerate(grid)
                                     for col_i, alive in enumerate(row)
                                     if alive}

    def __iter__(self):
        """Iterator progressing through each round until all cells are dead"""
        yield self
        while self.cells:
            self.cells = set(filter(self.cell_survives, self.cells_to_check()))
            yield self

    def __str__(self):
        """Represent the round as a 2d grid of + or . for alive or dead"""
        return '\n'.join(''.join('+' if self.cell_alive((r, c)) else '.'
                                 for c in range(20)) for r in range(20))

    def cell_alive(self, cell):
        """Checks if the given cell is alive or dead"""
        return cell in self.cells

    def cell_survives(self, cell):
        """Checks if the given cell makes it to the next generation"""
        neighbours = self.neighbour_count(*cell)
        return neighbours == 3 or neighbours == 2 and self.cell_alive(cell)

    def neighbour_count(self, row, col):
        """Number of living neighbours surrounding the given cell"""
        return len(set(filter(self.cell_alive, neighbours(row, col))))

    def cells_to_check(self):
        """Cells which could be alive in the next generation"""
        return {border for cell in self.cells for border in cells_3x3(*cell)}

if __name__ == "__main__":
    game = CGOL([[choice([True, False]) for r in range(20)] for c in range(20)])
    for round, grid in zip(range(40), game):
        print("===== round {} =====".format(round))
        print(grid)
