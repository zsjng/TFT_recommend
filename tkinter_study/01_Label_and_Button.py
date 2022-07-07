# coding=utf-8
# @Time : 2022/7/7 20:21
# @Author : zsjng
# @File : 01_Label_and_Button.py
# @Software : PyCharm

'''example'''
import tkinter as tk

window = tk.Tk()  # init class Tk()
window.title('my window')  # Set windows title
window.geometry('400x240')  # init window size width and height

var = tk.StringVar()

l = tk.Label(window,
             textvariable=var,
             bg='green',
             font=('Microsoft YaHei', 18),
             width=15, height=3)
l.pack()
show_or_not = False


def hit_me():
    global show_or_not
    if show_or_not is False:
        var.set('clicked')
        show_or_not = True
    else:
        var.set('')
        show_or_not = False


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)

b.pack()


window.mainloop()

