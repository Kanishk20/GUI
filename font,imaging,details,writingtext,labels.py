from tkinter import *
#We use labels to add text
window = Tk()
window.geometry('5000x5000')
photo = PhotoImage(file = 'screen saver.2.PNG')
label = Label(window , text="Hello World Meet The World's Greatest Cricketer",font =('Arial',40,'bold'),bg = 'blue', relief = RAISED ,bd = 10,image=photo,compound = 'bottom')
#label.pack() # use this if u want label header to appear in centre of window
#label.place(x=10,y=10) # use this to place label according to coordinate system


label.pack()

window.mainloop()
#RELIEF is used for border