from collections import defaultdict

class CGOL:
    def __init__(self, grid):
        self._grid = defaultdict(bool)
        for row_index, row in enumerate(grid):
          for col_index, cell in enumerate(row):
            self._grid[(row_index, col_index)] = cell

    def __next__(self):
        yield self._grid

    def __getitem__(self, key):
        return self._grid[key]
