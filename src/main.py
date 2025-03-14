from graphics import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    
    m1 = Maze(
        20,
        20,
        20,
        20,
        20,
        20,
        win
    )











    win.wait_for_close()



main()