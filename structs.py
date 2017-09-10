#!/usr/bin/python
# coding: utf-8

import PrintFmt
import json
from datetime import datetime

DEBUG = 0


class Item:
    def __init__(self, content_str, color = None, view_name = None):
        self.create_time = datetime.now()
        self.content = content_str
        self.level = 2
        if color is None:
            color = PrintFmt.RED
        self.color = color
        if view_name is None:
            view_name = "Others"
        self.view_name = view_name

        self.content = content_str
        self.detail = ""
        #self.ddl_time = 
        #self.xpct_time = time

    #print & format: color
    def change_color(self, color):
        self.color = color
    def echo(self, prefix = ''):
        echo_str = "% 3s %-20s\t%-20s\t%-20s" % (prefix, self.content, self.create_time.strftime('%Y-%m-%d %H:%M'), self.view_name)
        PrintFmt.printc(self.color, echo_str)




# we can describe our items(plans) in different view, not just classify them in several classes... i.e. Before a computer, we can programming, write documents, play PC games, but we can only play games on weekend, or we just like write documents when we are working. In this example, we can view our items(plans) by time & space. And we can also classify items with the people spend time with, the feeling, the physical condition, etc.

class View:
    def __init__(self, name = None, color = None):
        if name is None:
            name = 'Others'
        self.name = name
        if color is None:
            color = PrintFmt.RED
        self.color = color
        self.list = []


    def add(self, view):
        self.list.append(view)


    def echo(self):
        prefix_str = '*' * 78
        view_str = "% 75s   " % self.name
        PrintFmt.printc(self.color, prefix_str)
        PrintFmt.printc(self.color, view_str)
        for i in self.list:
            i.echo()
        PrintFmt.printc(self.color, prefix_str)



class Status:
    def __init__(self, status_name):
        self.name = status_name
        self.items = []
        self.exists_colors = {}     # color: color count
        self.views = {}             # 'view_name': a View object

    def create_new_item(self, content_str, view_name = None):
        if view_name is None:
            view_name = 'Others'
        if view_name not in self.views:
            self.create_new_view(view_name)
        color = self.views[view_name].color
        i = Item(content_str, color, view_name)
        self.items.append(i)
        self.views[view_name].add(i)

        if DEBUG:
            self.items[-1].echo()
            self.views[view_name].echo()

    def delete_item(self, item):
        self.views[item.view_name].list.remove(item)
        self.items.remove(item)
        

    def create_new_view(self, view_name, color = None):
        if color is None:
            color = self.__unique_color()
        else:
            if color not in self.exists_colors:
                self.exists_colors[color] = 1
            else:
                self.exists_colors[color] += 1
        v = View(view_name, color)
        self.views[v.name] = v 

        if DEBUG:
            print self.views
         
    def delete_view(self, view):
        print  "to del view:", view.name
        for item in view.list:
            item.view_name = 'Others'
        del self.views[view.name]
        
    def __unique_color(self):
        for i in PrintFmt.COLORS:
            if i in self.exists_colors:
                continue
            else:
                self.exists_colors[i] = 1
                return i
        min_color = PrintFmt.RED
        min_count = self.exists_colors[PrintFmt.RED] 
        for i in PrintFmt.COLORS:
            if self.exists_colors[i] < min_count:
                min_count = self.exists_colors[i]
                min_color = i
        self.exists_colors[min_color] += 1
        return min_color

    def save(self):
        with open(self.name + '.data', 'w') as json_file:
            for item in self.items:
                data = {
                    'content': item.content,
                    'view_name': item.view_name,
                    'create_time': item.create_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                    'level': item.level,
                    'color': item.color,
                    'detail': item.detail
                }
                json_file.write(json.dumps(data))
                json_file.write('\n')

    def load(self):
        with open(self.name + '.data') as json_file:
            count = 0
            for line in json_file:
                i = json.loads(line)
                t = Item(i['content'])
                t.view_name = i['view_name']
                t.create_time = datetime.strptime(i['create_time'], '%Y-%m-%d %H:%M:%S:%f')
                t.level = i['level']
                t.color = i['color']
                t.detail = i['detail']
                self.items.append(t)
                if t.view_name not in self.views:
                    self.create_new_view(t.view_name, t.color)
                self.views[t.view_name].add(t)
                count += 1
        return count
