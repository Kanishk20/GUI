from tkinter import *
# button = you click it , then it does stuff
window =  Tk()
def click():
    print("You clicked the button")
button = Button(window,text="click me!", command=click , font = ("Comic Sans" , 30))
def click():
    print("You clicked the button")
button.pack()
window.mainloop()
