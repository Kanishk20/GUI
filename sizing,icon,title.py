from tkinter import *

window = Tk() # instansiating a window 
window.geometry("500x500")
window.title("First GUI program")
icon = PhotoImage(file = 'screen saver.2.PNG' )
window.iconphoto(True,icon)
window.mainloop()