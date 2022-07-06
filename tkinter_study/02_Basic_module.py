# coding=utf-8
# @Time : 2022/7/6 18:23
# @Author : zsjng
# @File : 02_Basic_module.py
# @Software : PyCharm

from tkinter import *
from PIL import Image, ImageTk

"""
Basic module
"""

''' Label '''
# # Label(parent, option=value)
# root = Tk()
# Label(root, text='It\'s a Label').pack()
#
# bitmap_list = ['error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass',
#                'info', 'questhead', 'question', 'warning']
# for bitmap in bitmap_list:
#     Label(root, bitmap=bitmap).pack()
# ''' show picture at Tk '''
# image = Image.open(r'./files/my_logo.jpg')
# photo = ImageTk.PhotoImage(image)
# Label(root, image=photo).pack()
#
# mainloop()

'''Button'''

# def click_me():
#     global count
#     count += 1
#     print(f'You press {count} times button!')
#
#
# root = Tk()
# count = 0
# Button(root, text='click me', command=click_me).pack()
#
# root.mainloop()

'''Check Button'''

# def select():
#     print(f'Checkbutton value is {var.get()} + {count.get()}')
#
#
# root = Tk()
# var = StringVar()  # return bool value into 1 or 0.
# count = IntVar()
# check_button = Checkbutton(root, text='click me', variable=var, command=select)
#
# check_button.pack()
#
#
# root.mainloop()


'''Entry'''

# root = Tk()
# str_var = StringVar()
#
# entry = Entry(root, textvariable=str_var)
# str_var.set('please input info.')
# print(entry.get())
# entry.pack()
#
# root.mainloop()

'''Radiobutton'''

# def sel():
#     select = f'You selected {str(var.get())}'
#     print(select)
#
#
# root = Tk()
# var = IntVar()
# Radiobutton(root, text='1', variable=var, value=1, command=sel).pack(anchor=W)
# Radiobutton(root, text='2', variable=var, value=2, command=sel).pack(anchor=W)
# Radiobutton(root, text='3', variable=var, value=3, command=sel).pack(anchor=W)
#
# root.mainloop()

'''scale'''
#
# root = Tk()
# var = IntVar()
# Scale(root, orient='v', variable=var, from_=0, to=100, tickinterval=50, length=200).pack()
#
# root.mainloop()

'''get value from module'''
"""
python     tkinter
string     StringVar()
bool       BooleanVar()
int        IntVar()
float      DoubleVar()
"""
# root = Tk()
# tk_str = StringVar()
# tk_str.set('input something')
#
# tk_bool = BooleanVar()
# tk_int = IntVar()
# tk_float = DoubleVar()
#
# Entry(root, textvariable=tk_str).pack()
# Checkbutton(root, text='choose me!', variable=tk_bool).pack()
# Radiobutton(root, text='click me!', variable=tk_int).pack()
# Scale(root, label='volume', variable=tk_float).pack()
#
# print(tk_str.get())
# print(tk_bool.get())
# print(tk_int.get())
# print(tk_float.get())
#
# root.mainloop()

# from tkinter import *
# def click_me():
#     print(f'You press {count + 1} times button!')
#
#
# root = Tk()
# count = 0
# Button(root, text='click me', command=click_me).pack()
#
# root.mainloop()
