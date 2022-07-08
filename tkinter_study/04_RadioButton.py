# coding=utf-8
# @Time : 2022/7/8 19:18
# @Author : zsjng
# @File : 04_RadioButton.py
# @Software : PyCharm

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

var = tk.StringVar()

var2 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you selected ' + var.get())


r1 = tk.Radiobutton(window, text='Option_A', variable=var, value='A', command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option_B', variable=var, value='B', command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option_C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
