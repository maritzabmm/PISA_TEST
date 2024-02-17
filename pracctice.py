from tkinter import*
root = Tk() 
root.geometry('1000x800')
root.config(bg='white')

geop2=PhotoImage(file='geo2.png')
fondo=Label(root,image=geop2).place(x=100,y=20,width='800',height='900')

root.mainloop()