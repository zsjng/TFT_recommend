# coding=utf-8
# @Time : 522/7/6 5:35
# @Author : zsjng
# @File : 03_Layout.py
# @Software : PyCharm

from tkinter import *

'''pack'''
# root = Tk()
#
# Button(root, text='A').pack(side=LEFT, expand=1)
# Button(root, text='B').pack(side=LEFT, expand=1)
# Button(root, text='C').pack(side=LEFT, expand=1)
# ''' when use expand. it will cut the area to separate with same size .'''
#
# root.mainloop()

# root = Tk()
#
# frame4 = Frame(root)
# frame1 = Frame(frame4)
# frame2 = Frame(frame4)
# frame3 = Frame(frame4)
#
# Label(frame1, text='pack\'s side fill').pack()
# Button(frame1, text='1').grid(row=0, column=0, sticky=N)
# Button(frame1, text='2').grid(row=0, column=0, sticky=N)
# Button(frame1, text='3').grid(row=0, column=0, sticky=N)
# Button(frame2, text='4').grid(row=0, column=0, sticky=N)
# Button(frame2, text='5').grid(row=0, column=0, sticky=N)
# Button(frame2, text='6').grid(row=0, column=0, sticky=N)
# Button(frame3, text='7').grid(row=0, column=0, sticky=N)
# Button(frame3, text='8').grid(row=0, column=0, sticky=N)
# Button(frame3, text='9').grid(row=0, column=0, sticky=N)
#
# frame1.pack()
# frame2.pack()
# frame3.pack()
# frame4.pack()
#
# root.mainloop()
'''grid(recommend)'''
"""
ipadx,ipady means the button size will be (ipadx,ipady)
padx,pady means the distance from the button to the border or next to other
element will be (padx,pady)
"""
# root = Tk()
#
# Button(root, text='1').grid(row=0, column=0, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='2').grid(row=0, column=1, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='3').grid(row=0, column=2, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='4').grid(row=1, column=0, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='5').grid(row=1, column=1, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='6').grid(row=1, column=2, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='7').grid(row=2, column=0, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='8').grid(row=2, column=1, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
# Button(root, text='9').grid(row=2, column=2, sticky=NSEW, ipadx=10, ipady=10, padx=10, pady=10)
#
# root.mainloop()

