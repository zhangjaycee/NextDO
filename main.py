#!/usr/bin/python
# coding: utf-8

from structs import *
import PrintFmt


def main():

    print "haha... under developing... test mode..."
    print ""

    s = Status("zjc")
    s.create_new_view("in Lab")
    s.create_new_item("read papers", "in Lab")

    s.create_new_view("at home")
    s.create_new_item("play games", "at home")
    s.create_new_item("learn English", "at home")

    for i in s.views:
        s.views[i].echo()

    






if __name__ == "__main__":
    main()
