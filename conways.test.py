import unittest
from conways import CGOL

class CGOL_Tests(unittest.TestCase):

    def test_grid_creation(self):
        """
        ensure the initial grid is read correctly

        """

        grid = CGOL([[True]])
        self.assertEqual(True, grid[(0,0)])

        grid = CGOL([
          [True, False, True],
          [False, True, False],
          [True, True, True]
        ])
        self.assertEqual(True, grid[(0, 0)])
        self.assertEqual(False, grid[(0, 1)])
        self.assertEqual(True, grid[(2, 1)])

    def test_underpopulation_death(self):
        grid = CGOL([[True]])
        next(grid)
        self.assertEqual(False, grid[(0,0)])

if __name__ == "__main__":
    unittest.main()
