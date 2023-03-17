#there are various message boxes only used 2 over here
from tkinter import *
from tkinter import messagebox
def click():
    #messagebox.showinfo(title='This is an info message box' )
    while (True):
     messagebox.showwarning(title='Warning' , message= 'You have a Virus!')
     
window = Tk()

button = Button(window,command=click,text = 'click me')
button.pack()

window.mainloop()