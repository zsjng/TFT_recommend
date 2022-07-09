# coding=utf-8
# @Time : 2022/7/10 0:17
# @Author : zsjng
# @File : 06_Checkbutton.py
# @Software : PyCharm

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x300')

label = tk.Label(window, bg='green', width=20, text='empty')
label.pack()


def print_sel():
    if var1.get() == 1 and var2.get() == 0:
        label.config(text='I only love Python!')
    elif var1.get() == 1 and var2.get() == 1:
        label.config(text='I love both language!')
    elif var1.get() == 0 and var2.get() == 1:
        label.config(text='I only love C++!')
    else:
        label.config(text='I don\'t like program!')


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_sel)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_sel)
c2.pack()

window.mainloop()
