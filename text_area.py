from tkinter import *

window = Tk()
def submit():
    input = text.get("1.0" , END)
    print(input)
text = Text(window,bg = 'light yellow')
text.pack()
button = Button(window , text = "submit" , command= submit)
button.pack()


window.mainloop()