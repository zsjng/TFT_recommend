# coding=utf-8
# @Time : 2022/7/8 18:46
# @Author : zsjng
# @File : 03_List_Box.py
# @Software : PyCharm

import tkinter as tk

window = tk.Tk()

window.title('my window')
window.geometry('400x400')

var1 = tk.StringVar()

l = tk.Label(window, textvariable=var1, bg='green', width=4)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15, height=2,
               command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()
