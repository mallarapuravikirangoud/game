from tkinter import *
root=Tk()
root.title("game")
root.geometry("1000x450")
#root.resizable(0,0)
x=StringVar()
e3=Entry(root,fg="red",bg="white",font=("Arial",20),textvariable=x)
e3.grid(row=0,column=3,padx=10)
y=StringVar()
e4=Entry(root,fg="red",bg="white",font=("Arial",20),textvariable=y)
e4.grid(row=0,column=4,padx=10)

e2=Label(root,text="Winner Is",fg="red",bg="white",font=("Arial",25))
e2.grid(row=1,column=3,columnspan=3,padx=20)

z=StringVar()
e1=Entry(root,fg="red",bg="white",font=("Arial",20),textvariable=z)
e1.grid(row=2,column=3,padx=10,columnspan=3)


c=1
def show(b):
   global c
   c=c+1
   if (c%2==0):
       if (b["text"]==""):
               b["text"]="0"
   else:
       #if (b["text"]==" "):
               b["text"]="x"


   if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
         s = x.get()
         z.set(s)


   elif (b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0"):
         s = x.get()
         z.set(s)

   elif (b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):
         s =x.get()
         z.set(s)


   elif (b1["text"] == "x" and b2["text"] == "x" and b3["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b4["text"] == "x" and b5["text"] == "x" and b6["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b7["text"] == "x" and b8["text"] == "x" and b9["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b1["text"] == "x" and b4["text"] == "x" and b7["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b2["text"] == "x" and b5["text"] == "x" and b8["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b3["text"] == "x" and b6["text"] == "x" and b9["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b1["text"] == "x" and b5["text"] == "x" and b9["text"] == "x"):
         s = y.get()
         z.set(s)

   elif (b3["text"] == "x" and b5["text"] == "x" and b7["text"] == "x"):
         s =y.get()
         z.set(s)
        




b1= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b1))
b1.grid(row=0,column=0)

b2= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b2))
b2.grid(row=0,column=1)

b3= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b3))
b3.grid(row=0,column=2)

b4= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b4))
b4.grid(row=1,column=0)

b5= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b5))
b5.grid(row=1,column=1)


b6= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b6))
b6.grid(row=1,column=2)

b7= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b7))
b7.grid(row=2,column=0)


b8= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b8))
b8.grid(row=2,column=1)

b9= Button(root,text="",width="10", height="5",font=10,command=lambda :show(b9))
b9.grid(row=2,column=2)
root.mainloop()