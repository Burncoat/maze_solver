from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self._top_left = Point(self._x1, self._y1)
        self._top_right = Point(self._x2, self._y1)
        self._bottom_left = Point(self._x1, self._y2)
        self._bottom_right = Point(self._x2, self._y2)
    
    def draw(self):
        if self.has_left_wall:
            left_wall = Line(self._top_left, self._bottom_left)
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(self._top_right, self._bottom_right)
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(self._top_left, self._top_right)
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(self._bottom_left, self._bottom_right)
            self._win.draw_line(bottom_wall, "black")