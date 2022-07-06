# coding=utf-8
# @Time : 2022/7/6 15:28
# @Author : zsjng
# @File : tkinter_study.py
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
from tkinter import ttk


def call_back():
    print('clicked!')


root = Tk()  # init tkinter

label = Label(root, text='Lable')  # show info

button = Button(root, text='Button', command=call_back)  # click it!

check_button = Checkbutton(root, text='select')  # select or not.

entry = Entry(root)  # write string in it.















label.pack()  # every module that shown on Tk need .pack()
button.pack()
check_button.pack()
entry.pack()










root.mainloop()  # write code before mainloop()
