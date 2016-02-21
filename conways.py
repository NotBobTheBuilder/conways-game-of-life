import itertools

class CGOL(object):
    def __init__(self, grid):
        self.cells = {(row_i, col_i) for row_i, row in enumerate(grid)
                                     for col_i, alive in enumerate(row)
                                     if alive}

    def __iter__(self):
        while len(self.cells) > 0:
            self.cells = self.next_grid()
            yield self

    def __str__(self):
        char = lambda r, c: "+" if self.cell_alive((r, c)) else "."
        return "\n".join("".join(char(r, c) for c in range(20)) for r in range(20))

    def cell_alive(self, cell):
        return cell in self.cells

    def cell_survives(self, cell):
        neighbours = self.neighbour_count(*cell)
        return neighbours == 3 or neighbours == 2 and self.cell_alive(cell)

    def neighbour_count(self, row, col):
        return sum(self.cell_alive(n) for n in self.neighbours(row, col))

    def neighbours(self, row, col):
        return self.cells_3x3(row, col) - {(row, col)}

    def cells_3x3(self, row, col):
        return set(itertools.product(range(row-1, row+2), range(col-1, col+2)))

    def cells_to_check(self):
        return {neighbour for living_cell in self.cells
                          for neighbour in self.cells_3x3(*living_cell)}

    def next_grid(self):
        return set(filter(self.cell_survives, self.cells_to_check()))

if __name__ == "__main__":
    game = CGOL([[(r + c) % 2 == 0 for c in range(20)] for r in range(20)])
    for round, grid in zip(range(40), game):
        print("===== round {} =====".format(round))
        print(grid)
