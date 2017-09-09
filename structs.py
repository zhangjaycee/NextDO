#!/usr/bin/python
# coding: utf-8

import PrintFmt
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
    def echo(self):
        echo_str = "%-20s\t%-20s\t%-20s" % (self.content, self.create_time.strftime('%Y-%m-%d %H:%M'), self.view_name)
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


    def add(self, item):
        self.list.append(item)

#    def delete(self, item):
#        del self.list.remove(item)

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
            create_new_view(view_name)
        color = self.views[view_name].color
        i = Item(content_str, color, view_name)
        self.items.append(i)
        self.views[view_name].add(i)

        if DEBUG:
            self.items[-1].echo()
            self.views[view_name].echo()
        

    def create_new_view(self, view_name):
        v = View(view_name, self.__unique_color())
        self.views[v.name] = v 

        if DEBUG:
            print self.views
         
        
    def __unique_color(self):
        for i in PrintFmt.COLORS:
            if i in self.exists_colors:
                continue
            else:
                self.exists_colors[i] = 1
                return i
        min_color = PrintFmt.RED
        min_count = exists_colors[PrintFmt.RED] 
        for i in PrintFmt.COLORS:
            if exists_colors[i] < min_count:
                min_count = exists_colors[i]
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
            for line in json_file:
                i = json.loads(line)
                t = Item(i['content'])
                t.view_name = i['view_name']
                t.create_time = datetime.strptime(i['create_time'], '%Y-%m-%d %H:%M:%S:%f')
                t.level = i['level']
                t.color = i['color']
                t.detail = i['detail']
                self.items.append(t)
                self.views[t.view_name].add(t)
