#!/usr/bin/python
# coding: utf-8

from structs import *
import PrintFmt
import os
import sys

TEST = 0


HINT_STR = ''' 
=================NextDO=================
Functions:

p(i)    list all items
pv      list all views
n(i)    create a new item 
nv      create a new view
d(i)    delete an item
dv      deltee a view
c       bind an item to a view       
u       unbund and item from a view
ld      load corresponding plan table 
s(v)    save current plan table

q(uit)	exit
help	this menu
========================================
'''

from cmd import Cmd  
import sys  
  
class CmdNextdo(Cmd):  
	def __init__(self):            #初始基础类方法  
		Cmd.__init__(self)  
		self.prompt = "<NextDO>> "
		self.status_name = sys.argv[1]
		self.s = Status(self.status_name)
		if os.path.exists(self.status_name + '.data'):
			load_n = self.s.load()
			print load_n, "items loaded from plan table", self.status_name
		print HINT_STR

	# helps
	def do_help(self, args):
		print HINT_STR

	
	# prints and echos
	def do_p(self, strarg = None):
		self.do_pi()  
	def do_pi(self, strarg = None):
		for i in self.s.items:
			i.echo()
	def do_pv(self, strarg = None):
		for i in self.s.views:
			self.s.views[i].echo()
      
	# create functions
	def do_n(self, strarg = None):
		self.do_ni()  
	def do_ni(self, strarg = None):
		content = raw_input("What's your new plan/idea?")
		view = raw_input("Do you have any views of this item?")
		print content, view
		self.s.create_new_item(content, view)
	def do_nv(self, strarg = None):
		self.s.create_new_view(strarg)

	# deletes

	# bind & unbind

	# save & load
	
	# exits
	def do_q(self, strarg = None): 
		do_exit()
	def do_quit(self, strarg = None): 
		do_exit()
	def do_exit(self, strarg = None):
		print 'Bye!'
		sys.exit()  
          

def main():
    if TEST:
        print HINT_STR
        test()
        return 

    if len(sys.argv) != 2:
        PrintFmt.printc(PrintFmt.RED, "Usage: %s plan_table_name" % sys.argv[0])
        return 

    cmd=CmdNextdo()  
    cmd.cmdloop()  




def test():
    print "haha... under developing... test mode..."
    print ""

    s = Status("zjc")
    s.create_new_view("in Lab")
    s.create_new_item("read papers", "in Lab")

    s.create_new_view("at home")
    s.create_new_item("play games", "at home")
    s.create_new_item("learn English", "at home")
    s.save()

    for i in s.views:
        s.views[i].echo()







if __name__ == "__main__":
    main()
