from tkinter import*
root=Tk()
root.geometry("300x300")

Lab1=Label(root,text="user name")
Lab2=Label(root,text="password")

Lab1.grid(row=0)
Lab2.grid(row=1)

ent1=Entry(root)
ent2=Entry(root)

ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

root.mainloop()


