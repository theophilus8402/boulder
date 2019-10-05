
import curses

from drawille import Canvas
from math import floor
from random import choice
from time import sleep

from draw_simple_map import Point#, draw_simple_map

simple_player_design = """00000000
00011000
00100100
01010010
00100100
00011000
00000000"""

def translate_into_coords(simple_design):
    coords = []
    x = 0
    y = 0
    for row in simple_design.split("\n"):
        for bit in row:
            if bit == "1":
                coords.append(Point(x, y))
            x += 1
        y += 1
        x = 0
    return coords


def find_center(coords):

    xs = [p.x for p in coords]
    ys = [p.y for p in coords]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    center_x = min_x + floor((max_x-min_x)/2)
    center_y = min_y + floor((max_y-min_y)/2)

    return (center_x, center_y)


def move(coords, dir_coord):
    new_coords = [coord + dir_coord for coord in coords]
    return new_coords


def draw_coords(stdscr, design):

    c = Canvas()

    for i in range(10):

        for point in design:
            c.set(point.x, point.y)
    
        df = c.frame(-40, -40, 80, 80)
        stdscr.addstr(1, 0, df)
        stdscr.refresh()

        new_move_delta = Point(choice([-1, 0, 1]), choice([-1, 0, 1]))
        design = move(design, new_move_delta)

        sleep(.5)
        c.clear()

    sleep(6)
    c.clear()


if __name__ == "__main__":

    stdscr = curses.initscr()

    design_coords = translate_into_coords(simple_player_design)
    center = find_center(design_coords)

    curses.wrapper(draw_coords, design_coords)

