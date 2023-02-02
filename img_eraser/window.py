from tkinter import *
from PIL import ImageTk, Image
import os

path = './images'

root = Tk()
root.config(background='white')
root.geometry('800x600')
root.title('UwU')

l_choice = ['enlever une forme']
l_files = []

files = os.listdir(path)
for name in files:
    l_files.append(name)

val = StringVar(root)
val2 = val
val.set('select something bitch')
val2.set('select a file you moron')


MenuD = OptionMenu(root, val, *l_choice)
MenuD.place(x=10, y=10)

MenuF = OptionMenu(root, val2, *l_files)
MenuF.place(x=10, y=40)

canvas = Tk.Canvas(root)




root.mainloop()