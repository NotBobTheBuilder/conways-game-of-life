from itertools import product

class CGOL(dict):
    def __init__(self, grid):
        for row_index, row in enumerate(grid):
          for col_index, alive in enumerate(row):
            self[(row_index, col_index)] = alive

    def __iter__(self):
        while len(self.keys()) > 0:
            self.update(self.next_grid())
            yield self

    def __str__(self):
        char = lambda alive: "+" if alive else "."
        rows = ("".join(char(self[row, col]) for col in range(70)))
        return "\n".join(rows)

    def __getitem__(self, key):
        return self.get(key, False)

    def __setitem__(self, key, val):
        if val:
            dict.__setitem__(self, key, val)
        else:
            self.pop(key, None)

    def cell_survives(self, alive, neighbours):
        return neighbours == 3 or alive and neighbours == 2

    def neighbour_count(self, row, col):
        return sum(self[n] for n in self.neighbours(row, col))

    def neighbours(self, row, col):
        return set(self.cells_3x3(row, col)) - {(row, col)}

    def cells_3x3(self, row, col):
        return product(range(row-1, row+2), range(col-1, col+2))

    def cells_to_check(self):
        return {(cell, self[cell]) for live in self.keys()
                                   for cell in self.cells_3x3(*live)}

    def next_grid(self):
        return {cell: self.cell_survives(alive, self.neighbour_count(*cell))
                      for (cell, alive) in self.cells_to_check()}

if __name__ == "__main__":
    game = iter(CGOL([[True for i in range(20)] for i in range(20)]))
    for i in range(40):
        next(game)
