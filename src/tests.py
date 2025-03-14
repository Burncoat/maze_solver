import unittest

from maze import Maze
from graphics import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset_cells(self):
        num_cols = 11
        num_rows = 8
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0]._visited, False)
        self.assertEqual(m1._cells[5][5]._visited, False)

if __name__ == "__main__":
    unittest.main()