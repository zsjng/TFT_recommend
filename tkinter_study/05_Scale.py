# coding=utf-8
# @Time : 2022/7/8 19:28
# @Author : zsjng
# @File : 05_Scale.py
# @Software : PyCharm

import tkinter as tk

window = tk.Tk()  # init
window.title('my window')  # Set window title
window.geometry('400x400')  # Set window size

label = tk.Label(window, bg='green', width=20, text='empty')
label.pack()


def print_sel(v):
    label.config(text='you choosed' + v)


s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=True,
             tickinterval=1, resolution=1, command=print_sel)
s.pack()

window.mainloop()
