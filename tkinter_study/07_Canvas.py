# coding=utf-8
# @Time : 2022/7/10 0:32
# @Author : zsjng
# @File : 07_Canvas.py
# @Software : PyCharm

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title('my window')
window.geometry('400x300')

canvas = tk.Canvas(window, bg='yellow', height=100, width=200, )

image = Image.open('files/my_logo.jpg')
image_resize = image.resize((100, 100))
image_tk = ImageTk.PhotoImage(image_resize)
image_show = canvas.create_image(0, 0, anchor='nw', image=image_tk)
canvas.pack()
window.mainloop()


# tkinter is too old and just know how to use script to drive module is ok.
# I will go to Pyside6.