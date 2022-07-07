# coding=utf-8
# @Time : 2022/7/7 21:09
# @Author : zsjng
# @File : 02_Entry_and_Text.py
# @Software : PyCharm

'''example'''
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x300')


def insert_point():
    var = e.get()
    t.insert('insert', var)  # add t to the curser place.


def insert_end():
    var = e.get()
    t.insert('end', var)  # add t to the end of e.


''' can also use t.insert(2.2, var) it will insert to row 2,column 3.'''

e = tk.Entry(window, show='*')

b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)

b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
t = tk.Text(window, height=2)

e.pack()
b1.pack()
b2.pack()
t.pack()

window.mainloop()
