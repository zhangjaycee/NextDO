#!/usr/bin/python
# coding: utf-8

from structs import Item
from structs import View
import PrintFmt
import json
import time
from datetime import datetime

def save_json(items, path):
    with open(path, 'w') as json_file:
        for item in items:
            data = {
                'content': item.content,
                'create_time': item.create_time.strftime('%Y-%m-%d %H:%M:%S:%f'),
                'level': item.level,
                'color': item.color,
                'detail': item.detail
            }
            json_file.write(json.dumps(data))
            json_file.write('\n')


def load_json(path):
    load_strs = []
    items = []

    with open(path) as json_file:
        for line in json_file:
            data = json.loads(line)
            load_strs.append(data)
    for i in load_strs:
        t = Item(i['content'])
        t.create_time = datetime.strptime(i['create_time'], '%Y-%m-%d %H:%M:%S:%f')
        t.level = i['level']
        t.color = i['color']
        t.detail = i['detail']
        items.append(t)
    return items

    
def unique_color(exists):
    for i in PrintFmt.COLORS:
        if i in exists:
            continue
        else:
            return i

    min_color = PrintFmt.RED
    min_count = exists[PrintFmt.RED] 
    for i in PrintFmt.COLORS:
        if exists[i] < min_count:
            min_count = exists[i]
            min_color = i
    return min_color
   


    
def create_new_item(items, content_str, color, exist_colors):
    i = Item(content_str, color)
    items.append(i)
    update_exist_colors(i, exist_colors)

def update_exist_colors(i, d):
    if i.color not in d:
        d[i.color] = 1
    else:
        d[i.color] += 1


def refresh_exist_colors(items, d):
    for i in items:
        if i.color not in d:
            d[i.color] = 1
        else:
            d[i.color] += 1
            

def test():
    # status
    items = []  # list of all items
    exist_colors = {} # maintain a dict for unique colors

    # test create
    create_new_item(items, "learn English.", unique_color(exist_colors), exist_colors)

    create_new_item(items, "play game.", unique_color(exist_colors), exist_colors)
    create_new_item(items, "sleep.", unique_color(exist_colors), exist_colors)

    print items
    print exist_colors

    '''
    # refresh exist colors
    print "refresh exist colors..........."
    exist_colors = {} # maintain a dict for unique colors
    refresh_exist_colors(items, exist_colors)
    print items
    print exist_colors
    '''

    # test save
    save_path = "hello1.data"
    save_json(items, save_path)

    # test load
    load_path = "hello1.data"
    t_load = load_json(load_path)
    for i in t_load:
        i.echo()
        print i.create_time

if __name__ == "__main__":
    test()
