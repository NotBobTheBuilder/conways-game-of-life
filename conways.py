from itertools import product

class CGOL(dict):
    def __init__(self, grid):
        for row_index, row in enumerate(grid):
          for col_index, alive in enumerate(row):
            self[(row_index, col_index)] = alive

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys()) == 0:
            raise StopIteration

        self.merge(self.next_grid())
        return self

    def __repr__(self):
        return str(self)

    def __str__(self):
        rows = []
        for row in range(20):
            r = (self[row, col] for col in range(70))
            rows.append("".join("+" if alive else "." for alive in r))

        return "\n".join(rows)

    def __getitem__(self, key):
        return self.get(key, False)

    def __setitem__(self, key, val):
        if val:
            dict.__setitem__(self, key, val)
        else:
            if key in self:
                del self[key]

    def neighbours(self, row, col):
        return set(self.cells_3x3(row, col)) - {(row, col)}

    def cells_3x3(self, row, col):
        return product(range(row-1, row+2), range(col-1, col+2))

    def cells_to_check(self):
        return {(cell, self[cell]) for live in self.keys()
                                   for cell in self.cells_3x3(*live)}

    def next_grid(self):
      newgrid = {}

      for (cell, alive) in self.cells_to_check():
          neighbour_count = sum(self[n] for n in self.neighbours(*cell))
          newgrid[cell] = neighbour_count == 3 or alive and neighbour_count == 2

      return newgrid

    def merge(self, grid):
        for (cell, alive) in grid.items():
            self[cell] = alive
