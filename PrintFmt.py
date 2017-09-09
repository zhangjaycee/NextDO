#!/usr/bin/python
# coding: utf-8


from structs import Item

# define color
RED = "31"
GREEN = "32"
YELLOW = "33"
BLUE = "34"
PINK = "35"
CYAN = "36"
WHITE = "37" #hiden
BLACK = "30" #hiden
COLORS = [RED, GREEN, YELLOW, BLUE, PINK, CYAN]

# define background color
BG_RED = "41"
BG_GREEN = "42"
BG_YELLOW = "43"
BG_BLUE = "44"
BG_PINK = "45"
BG_CYAN = "46"
BG_WHITE = "47" #hiden
BG_BLACK = "40" #hiden
BG_COLORS = [BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_PINK, BG_CYAN]

ALL_COLORS = COLORS + BG_COLORS


def printc(color, my_str):
    color_str = "\033[" + color + "m" + my_str + "\033[0m"
    print color_str



def test():
    print COLORS
    for color in COLORS:
        printc(color, "hello, world!")
    for color in BG_COLORS:
        printc(color, "hello, world!")

if __name__ == "__main__":
    test()
