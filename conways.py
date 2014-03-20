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

    def __getitem__(self, key):
        return self.get(key, False)

    def only_neighbours(self, x, y):
        return list(set(product(range(x-1,x+2), range(y-1,y+2))) - {(x, y)})

    def neighbours(self, x, y):
        return list(product(range(x-1,x+2), range(y-1,y+2)))

    def items(self):
        neighbours = (self.neighbours(row, col) for row, col in self.keys())

        uniques = set()

        for group in neighbours:
            for elem in group:
                uniques.add(elem)

        return ((cell, self[cell]) for cell in uniques)

    def next_grid(self):
      newgrid = {}

      for ((row, col), alive) in self.items():
          neighbours = sum(self[n] for n in self.only_neighbours(row, col))
          if alive:
              newgrid[(row, col)] = (2 <= neighbours <= 3)
          else:
              newgrid[(row, col)] = (neighbours == 3)

      return newgrid

    def merge(self, grid):
        for ((row, col), cell) in grid.items():
            self[(row, col)] = cell
            if not cell and (row, col) in self:
                del self[(row, col)]
