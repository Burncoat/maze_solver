from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(100, 100, 200, 200)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(300, 100, 400, 200)

    c1.draw_move(c2, True)










    win.wait_for_close()



main()