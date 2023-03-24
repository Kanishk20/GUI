from tkinter import *

window =Tk()
window.title(" PURE GAS SOLVER ")
label = Label(window,text= " PURE GAS SOLVER" , font=('Arial' , 13 , 'bold'))
#label.place(x=0,y=0)
label.pack()

dimensions_of_the_domain = Label(window , text= "Dimensions of the Domain" , font = ('Arial' , 10 , 'bold'))
dimensions_of_the_domain.place(x=0, y =30)

length = Label(window , text="Enter the length" )
length.place(x=0 , y =53)
length_entry = Entry(window)
length_entry.place(x=0 , y=70)

height = Label(window , text="Enter the height" )
height.place(x=150 , y =53)
height_entry = Entry(window)
height_entry.place(x=150 , y=70)

breadth = Label(window , text="Enter the breadth" )
breadth.place(x=300 , y =53)
breadth_entry = Entry(window)
breadth_entry.place(x=300 , y=70)

Grid_dimensions_of_the_domain = Label(window , text= "Grid dimensions of the Domain" , font = ('Arial' , 10 , 'bold'))
Grid_dimensions_of_the_domain.place(x=0, y =120)

Nx = Label(window , text="Nx" )
Nx.place(x=0 , y =143)
Nx_entry = Entry(window)
Nx_entry.place(x=0 , y=170)

Ny = Label(window , text="Ny" )
Ny.place(x=150 , y =143)
Ny_entry = Entry(window)
Ny_entry.place(x=150 , y=170)

Nz = Label(window , text="Nz" )
Nz.place(x=300 , y =143)
Nz_entry = Entry(window)
Nz_entry.place(x=300 , y=170)

Grid_Type = Label(window , text= "Grid Type" , font = ('Arial' , 10 , 'bold'))
Grid_Type.place(x=0, y =240)






window.mainloop()
