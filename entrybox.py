#entrybox accepts single line of user input
from tkinter import *
window = Tk()
def submit():
    username = entry.get()
    print("Hello your Username is" + username)
def delete():
    entry.delete(0,END)    
entry = Entry(window,font=("Arial" , 50))
entry.pack(side=LEFT)
submit_button = Button(window , text = "submit" , command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window , text="Delete", command= delete)
delete_button.pack(side=RIGHT)
window.mainloop()
