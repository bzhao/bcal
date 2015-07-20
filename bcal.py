#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *
#from Tkinter import messagebox
import tkMessageBox

import re
import os

texi_file = "./texi.txt"

taxi_pattern = re.compile(r'\s*taxi\s*=\s*(.*)',re.S)

rfile = open(texi_file, 'r')

xxx_line=rfile.read()
print 'Line:', xxx_line

match = taxi_pattern.match(xxx_line)
if match:
   print "555555555:"+match.group(1)
   taxi = match.group(1)

def removing_header(x):
   header_pattern = re.compile(r'\s*\S+\s*=\s*(.*)', re.S)
   match_h = header_pattern.match(x)
   if match_h:
      print "llllll:"+match_h.group(1)
      return match_h.group(1)

def on_click():
   try:
      label['text'] = "%2.2f" % eval(removing_header(entry.get("0.0", "end")).replace('\n',''))
   except:
      tkMessageBox.showinfo("Error", "Input Error!!!")
      print 'there is an error in your input'

root = Tk(className='baoxiao caculator')

def on_closing():
#    if messagebox.askokcancel("Quit", "Do you want to quit?"):

   wfile = open(texi_file+'.new', 'w')
   wfile.write(entry.get("0.0", "end"))
   wfile.close()
   os.rename(texi_file, texi_file+'.old')
   os.rename(texi_file+'.new', texi_file)

   root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.option_add("*Font", "courier 25")

label = Label(root)
label['text'] = 'be on your own'
label.pack()

text = StringVar()
text.set('taxi = '+taxi)

entry = Text(root, height=5, width=50)
entry.insert(1.0, text.get())
print "ffffff:"+entry.get("0.0", "end")
entry.pack()

button = Button(root)
button['text'] = 'cal it!'
button['command'] = on_click
button.pack()

root.mainloop()


