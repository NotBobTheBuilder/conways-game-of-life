from itertools import product

class CGOL(dict):
    def __init__(self, grid):
        for row_index, row in enumerate(grid):
          for col_index, cell in enumerate(row):
            self[(row_index, col_index)] = cell

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
            rows.append("".join("+" if c else "." for c in r))

        return "\n".join(rows)

    def __getitem__(self, key):
        return self.get(key, False)

    def neighbours(self, x, y):
        return list(set(self.cells_3x3(x, y)) - {(x, y)})

    def cells_3x3(self, x, y):
        return list(product(range(x-1,x+2), range(y-1,y+2)))

    def cells_to_check(self):
        cells_to_check = (self.cells_3x3(row, col) for row, col in self.keys())
        uniques = set(elem for group in cells_to_check for elem in group)

        return ((cell, self[cell]) for cell in uniques)

    def next_grid(self):
      newgrid = {}

      for (position, alive) in self.cells_to_check():
          neighbour_count = sum(self[n] for n in self.neighbours(*position))
          if alive:
              newgrid[position] = (2 <= neighbour_count <= 3)
          else:
              newgrid[position] = (neighbour_count == 3)

      return newgrid

    def merge(self, grid):
        for ((row, col), cell) in grid.items():
            self[(row, col)] = cell
            if not cell and (row, col) in self:
                # we don't need to store False values explicitly since our
                # lookup in __getitem__ uses False as a default value
                del self[(row, col)]
