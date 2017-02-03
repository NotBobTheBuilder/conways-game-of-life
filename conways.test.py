import unittest
from conways import CGOL

class CGOL_Tests(unittest.TestCase):

    def test_grid_creation(self):
        """
        ensure the initial grid is read correctly

        """

        grid = CGOL([[True]])
        self.assertEqual(True, grid.cell_alive((0,0)))

        grid = CGOL([
          [True, False, True],
          [False, True, False],
          [True, True, True]
        ])
        self.assertEqual(True, grid.cell_alive((0, 0)))
        self.assertEqual(False, grid.cell_alive((0, 1)))
        self.assertEqual(True, grid.cell_alive((2, 1)))

    def test_underpopulation_death(self):
        grid = CGOL([[True]])
        next(iter(grid))
        self.assertEqual(False, grid.cell_alive((0,0)))

    def test_overpopulation_death(self):
        grid = CGOL([
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ])

        next(iter(grid))
        self.assertEqual(False, grid.cell_alive((1,1)))

    def test_stable_population_survival(self):
        grid = CGOL([
            [True, True, True],
        ])

        for i in range(4):
            next(iter(grid))
            self.assertEqual(True, grid.cell_alive((0,1)))

    def test_dead_cell_three_neighbours_born(self):
        grid = CGOL([
            [True, True, True]
        ])

        next(iter(grid))
        self.assertEqual(True, grid.cell_alive((-1,1)))

    def test_dead_cell_two_neighbours_dead(self):
        grid = CGOL([
            [True, True, False]
        ])

        next(iter(grid))
        self.assertEqual(False, grid.cell_alive((-1,1)))

if __name__ == "__main__":
    unittest.main()
