from tkinter import *
# button = you click it , then it does stuff
window =  Tk()
photo = PhotoImage(file = 'imagesthumbsup.png')
def click():
    print("You clicked the button")
button = Button(window,text="click me!", command=click , font = ("Comic Sans" , 30), image = photo, compound = 'bottom')
def click():
    print("You clicked the button")
button.pack()
window.mainloop()
