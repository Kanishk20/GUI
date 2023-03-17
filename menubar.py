from tkinter import *
window = Tk()
def openfile():
    print("File has been opened")
def savefile():
    print("File has been saved")   
def cut():
    print("Cut")
def paste():
    print("Paste")
def copy():
    print("Copy")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "file" , menu = fileMenu)
fileMenu.add_command(label="open" , command= openfile)
fileMenu.add_command(label="save" , command= savefile)
fileMenu.add_command(label="exit",command= quit)

editMenu = Menu(menubar , tearoff= 0)
menubar.add_cascade(label = "edit" , menu=editMenu )
editMenu.add_command(label="Cut" , command= cut )
editMenu.add_command(label="paste" , command= paste)
editMenu.add_command(label="copy" , command =copy)

window.mainloop()