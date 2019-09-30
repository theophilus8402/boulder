
import curses

from drawille import Canvas, line
from time import sleep

stdscr = curses.initscr()
stdscr.refresh()

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.x}, {self.y}>"


def main(stdscr):

    c = Canvas()

    v1 = Point(-20, 20)
    v2 = Point(20, 20)
    v3 = Point(-20, -20)
    v4 = Point(20, -20)

    lines = [   (v1, v2),
                (v1, v3),
                (v3, v4),
                (v4, v2),
            ]

    for start, end in lines:
        for x,y in line(start.x, start.y, end.x, end.y):
            c.set(x, y)

    df = c.frame(-40, -40, 80, 80)
    stdscr.addstr(1, 0, f"{df}")
    stdscr.refresh()

    sleep(10)
    c.clear()


if __name__ == "__main__":

    curses.wrapper(main)

