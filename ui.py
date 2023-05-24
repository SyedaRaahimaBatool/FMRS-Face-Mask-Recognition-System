from tkinter import ttk, Tk
import random
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import Entry
import os
from subprocess import call
import sys

        
    
    
def ui2_():
        pro.withdraw()
        call(["python","ui2.py"])
    
    




if __name__ == '__main__':
    global pro
    pro = Tk()
    pro.title("Face Mask Recognition")
    pro.geometry("480x325")
    pro.resizable(width=False,height=False)
    pro.configure(background='cadet blue')
    Cm = Canvas(width=500, height=320)
    photo_wel = PhotoImage(file='download.png')
    Cm.create_image(0, 0, image=photo_wel, anchor=NW)
    Cm.pack()

    Exe = Button(pro, text="Face Recognition", width=15,
                     border=1, height=2,
                     font="Arial 0 bold", command=ui2_)
    
    Exe.place(x=0, y=285, height=40, width=500)


    pro.mainloop()