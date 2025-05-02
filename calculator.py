from tkinter import *
from tkinter import ttk, messagebox

GUI =Tk()
GUI.title("bASIC Git & GitHub by Sirawit Juthong")
GUI.geometry("500x700")

L = Label(GUI, text="Sirawit Juthong")
L.pack()

L = Label(GUI, text="12qweza12")
L.pack()

L = Label(GUI, text="my password = gikdkd2559")
L.pack()

L = Label(GUI, text="Somchai Dev")
L.pack()

V1 = StringVar()
E1 = ttk.Entry(GUI,textvariable=V1)
E1.pack()

V2 = StringVar()
E2 = ttk.Entry(GUI,textvariable=V2)
E2.pack()

def cal():
    c = float(V1.get()) * float(V2.get())
    r1 = V1.get()
    r2 = V2.get()
    text = f"{r1}x{r2}={c}"
    messagebox.showinfo("Result",text)

b1 = ttk.Button(GUI,text="Calculator Now!", command=cal)
b1.pack()

GUI.mainloop()
