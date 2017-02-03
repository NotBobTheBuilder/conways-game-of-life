from itertools import product
from random import choice

def cells_3x3(row, col):
    return set(product(range(row-1, row+2), range(col-1, col+2)))

def neighbours(row, col):
    return cells_3x3(row, col) - {(row, col)}

class CGOL(object):
    def __init__(self, grid):
        self.cells = {(row_i, col_i) for row_i, row in enumerate(grid)
                                     for col_i, alive in enumerate(row)
                                     if alive}

    def __iter__(self):
        while self.cells:
            self.cells = set(filter(self.cell_survives, self.cells_to_check()))
            yield self

    def __str__(self):
        char = lambda r, c: "+" if self.cell_alive((r, c)) else "."
        return "\n".join("".join(char(r, c) for c in range(20))
                                            for r in range(20))

    def cell_alive(self, cell):
        return cell in self.cells

    def cell_survives(self, cell):
        neighbours = self.neighbour_count(*cell)
        return neighbours == 3 or neighbours == 2 and self.cell_alive(cell)

    def neighbour_count(self, row, col):
        return len(filter(self.cell_alive, neighbours(row, col)))

    def cells_to_check(self):
        return {neighbour for cell in self.cells
                          for neighbour in cells_3x3(*cell)}

if __name__ == "__main__":
    game = CGOL([[choice([True, False]) for r in range(20)] for c in range(20)])
    print("==== init state ====")
    print(grid)
    for round, grid in zip(range(40), game):
        print("===== round {} =====".format(round))
        print(grid)
