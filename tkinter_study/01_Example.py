# coding=utf-8
# @Time : 2022/7/6 15:28
# @Author : zsjng
# @File : 01_Example.py
# @Software : PyCharm

"""
TK basic frame

from tkinter import *
from tkinter import ttk

root = Tk()
# code here
root.mainloop()
"""
from tkinter import *


def call_back():
    print('clicked!')


root = Tk()  # init tkinter

label = Label(root, text='Lable')  # show info

button = Button(root, text='Button', command=call_back)  # click it!

check_button = Checkbutton(root, text='select')  # select or not.

entry = Entry(root)  # write string in it.

radio_button = Radiobutton(root, text='male', value=1)

radio_button2 = Radiobutton(root, text='female', value=2)  # choose only one.

scale = Scale(root, orient='horizontal')  # orient must be horizontal or vertical.

label.pack()  # every module that shown on Tk need .pack()
button.pack()
check_button.pack()
entry.pack()
radio_button.pack()
radio_button2.pack()
scale.pack()

root.mainloop()  # write code before mainloop()
