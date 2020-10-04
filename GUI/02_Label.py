'''
let's checkout the first widget in this series

  Labels 

simple implementation of labels is shown below 
'''
from tkinter import *

root = Tk()

simpleLabel = Label(root, text=" checkout I'm a Lable ")
simpleLabel.pack()#this a way of aligning the widgets in tkinter  

root.mainloop()