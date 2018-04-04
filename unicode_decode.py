# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys
from Tkinter import *

#make the window center and set the window's width and height
def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    root.geometry(size)
    return 

def trans_unicode_to_chinese(unicode_str,lable):
    lable['text'] = unicode_str.encode('utf-8').decode('unicode_escape')
    return

if __name__ == '__main__':

    root = Tk()
    center_window(root,200,100)

    l1 = Label(root, text="输入unicode:")
    l1.grid(row=3)

    e = Entry(root)
    e.grid(row=4,column=0)

    l2 = Label(root, text="")
    l2.grid(row=5)

    Button(root, text='转换', command=lambda : trans_unicode_to_chinese(e.get(),l2)).grid(row=4, column=1,sticky=W, pady=4)
    
    mainloop()