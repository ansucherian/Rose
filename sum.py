from tkinter import*
root=T(k)
root.geometry("500*300")
def sum():
    no1=Int(E1.get())
    no2=Int(E2.get())
    r=no1+no2
    res.config(text="sum+%d"%r)
    return
root.title("calculator")
L1=label(root,text="enter a number")
L1.place(x=100,y=200)
E1=Entry(root)
E1.place(x=90,y=200)
L2=Label(root,text="enter a number")
L2.place(x=60,y=180)
E2=Entry(root)
E2.place(x=90,y=180)
res=Label(root)
bSum=Button(text="sum",command=sum())
bSum=place(x=70,y=180)
res=Label(root)
res.place(x=70,y=140)
root.mainloop()
             
