# coding=utf-8
# @Time : 2022/7/6 22:11
# @Author : zsjng
# @File : 05_OOP_example.py
# @Software : PyCharm
"""OOP:Object Oriented Programming"""


'''example 1'''
# from tkinter import *
# class App:
#     def __init__(self,root):
#         self.root = root
#         self.set_window()
#         self.create_top()
#         self.create_body()
#         self.create_bottom()
#
#     def set_window(self):
#         self.root.title('Test')
#         self.root.resizable(False,False)
#
#     def create_top(self):
#         Label(self.root,text='Top').pack()
#
#     def create_body(self):
#         self.input = StringVar()
#         Entry(self.root,textvariable=self.input).pack()
#
#     def create_bottom(self):
#         Button(self.root,text='click me!',command=self.click_it).pack(fill=X)
#
#     def click_it(self):
#         print(self.input.get())
#
# if __name__ == '__main__':
#     root =Tk()
#     App(root)
#     root.mainloop()
'''example 2'''
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.set_window()
        self.create_top()
        self.create_body()
        self.create_bottom()

    def set_window(self):
        self.title('Test')
        self.resizable(False,False)

    def create_top(self):
        Label(self,text='Top').pack()

    def create_body(self):
        self.input = StringVar()
        Entry(self,textvariable=self.input).pack()

    def create_bottom(self):
        Button(self,text='click me!',command=self.click_it).pack(fill=X)

    def click_it(self):
        print(self.input.get())

if __name__ == '__main__':
    app = App()
    app.mainloop()