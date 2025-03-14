from graphics import *


def main():
    win = Window(800, 600)
    cell1 = Cell(win, 25, 25, 50, 50)
    cell2 = Cell(win, 100, 100, 200, 200)
    cell1.draw()
    cell2.draw()
    win.wait_for_close()



main()