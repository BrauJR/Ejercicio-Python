from tkinter import *

root=Tk()

miFrame=Frame(root, width=600, height=500)
miFrame.pack()


miImagen=PhotoImage(file="bar.gif")

Label(miFrame, image=miImagen).place(x=100, y=200)
Label(miFrame, text="Quiubo", fg="blue", font=("Arial",16)).place(x=50, y=50) #Permite ubicar el texto en cualquier lugar 


root.mainloop()