#!/usr/bin/python
# coding: utf-8

from item import Item
import PrintFmt



# we can describe our items(plans) in different view, not just classify them in several classes... i.e. Before a computer, we can programming, write documents, play PC games, but we can only play games on weekend, or we just like write documents when we are working. In this example, we can view our items(plans) by time & space. And we can also classify items with the people spend time with, the feeling, the physical condition, etc.

class View:
    def __init__(self, name = None, color = None):
        if name is None:
            name = "Others"
        self.name = name
        if color is None:
            color = PrintFmt.RED
        self.color = color

    self.list = []

    def add(self, item):
        self.list.append(item)

    def del(self, item):
        del self.list.remove(item)

    def echo(self):
        print self.list



