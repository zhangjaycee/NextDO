#!/usr/bin/python
# coding: utf-8

import PrintFmt
from datetime import datetime


class Item:
    def __init__(self, content_str, color = None):
        self.create_time = datetime.now()
        self.content = content_str
        self.level = 2
        if color is None:
            color = PrintFmt.RED
        self.color = color

        self.content = content_str
        self.detail = ""
        #self.ddl_time = 
        #self.xpct_time = time

    #print & format: color
    def change_color(self, color):
        self.color = color
    def echo(self):
        PrintFmt.printc(self.color, self.content, self.detail)
