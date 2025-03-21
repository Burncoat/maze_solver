from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        if not self.has_left_wall:
            self._win.draw_line(left_wall, "white")
        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        if not self.has_right_wall:
            self._win.draw_line(right_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        if not self.has_top_wall:
            self._win.draw_line(top_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        if not self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")
        

    def draw_move(self, to_cell, undo=False):
        half1 = abs(self._x2 - self._x1) // 2
        x_center = half1 + self._x1
        y_center = half1 + self._y1

        half2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half2 + to_cell._x1
        y_center2 = half2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line((Point(x_center, y_center)), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
