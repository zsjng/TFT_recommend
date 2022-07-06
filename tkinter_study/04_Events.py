# coding=utf-8
# @Time : 2022/7/6 21:31
# @Author : zsjng
# @File : 04_Events.py
# @Software : PyCharm

from tkinter import *

'''add args to events'''
# def my_func(args):
#     print('clicked!',args)
#
#
# root = Tk()
#
# Button(root, text='click me!', command=lambda : my_func('this is a button')).grid\
#     (row=0,pady=50, padx=50)
#
# root.mainloop()

'''mouse events'''
# root = Tk()
#
# Label(root, text='click').pack()
#
#
# def my_func(event, a, b):
#     print(a, b)
#     print('Event_type =', event.type)
#
#
# frame = Frame(root, bg='pink', width=100, height=100)
# frame.bind('<Button-1>', lambda event: my_func(event, 3, 5))
# """
# <Button-1>          mouse left click
# <Button-2>          mouse scroll click
# <Button-3>          mouse right click
# <Double-Button-1>   mouse left double-click
# <Triple-Button-1>   mouse left triple-click
#
# """
# frame.pack()
# root.mainloop()
'''keyboard events'''