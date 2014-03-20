import unittest
from conways import CGOL

class CGOL_Tests(unittest.TestCase):

    def test_grid_creation(self):
        """
        ensure the initial grid is read correctly

        """
        
        grid = CGOL([[True]])
        self.assertEqual(True, grid[(0,0)])

if __name__ == "__main__":
    unittest.main()
