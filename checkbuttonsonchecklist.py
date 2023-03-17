from tkinter import *
window = Tk()
x = IntVar()
def display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("Do not agree :(")    
       
python_photo = PhotoImage(file= 'Python.svg.png')    
check_button = Checkbutton(window,
                           text = "I agree to something",
                           variable=x,
                           onvalue=1, 
                           offvalue= 0,
                             command=display,
                               bg = 'black',
                             activebackground='black',
                               image = python_photo,
                               compound= 'left')
check_button.pack()
window.mainloop()
