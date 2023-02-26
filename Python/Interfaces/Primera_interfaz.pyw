from tkinter import*

raiz=Tk()
raiz.title("Mi primera ventana :O")
#raiz.resizable(False,False) 
#raiz.geometry("650x540")
raiz.config(bg="white")

miFrame=Frame()
miFrame.pack(fill="both", expand="True") 
miFrame.config(bg="gray")
miFrame.config(width="650",height="540")
miFrame.config(bd=0)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")


raiz.mainloop()

