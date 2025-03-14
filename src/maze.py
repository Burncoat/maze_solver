from cell import Cell
from graphics import Window, Line, Point
import time


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            column = []
            for row in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        x_start = self._x1 + (self._cell_size_x * i)
        y_start = self._y1 + (self._cell_size_y * j)
        x_shift = x_start + self._cell_size_x
        y_shift = y_start + self._cell_size_y
        self._cells[i][j].draw(x_start, y_start, x_shift, y_shift)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
