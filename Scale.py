from tkinter import *
window = Tk()
def submit() :
    print("The temperature is : " + str(scale.get()) + "degrees C")
scale = Scale(window , from_=100,to=0 , font= ("Arial" , 50))
scale.pack()

button = Button(window,text = 'submit' , command= submit)
button.pack()
window.mainloop()