from collections import defaultdict

class CGOL:
    def __init__(self, grid):
        self._grid = defaultdict(bool)

    def __next__(self):
        yield self._grid

    def __getitem__(self, key):
        return self._grid[key]
