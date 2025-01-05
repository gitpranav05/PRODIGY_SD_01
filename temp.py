from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg

def conv():

    if unit.get()== "Select Unit":
        tmsg.showerror("Unit Error", "Please select a valid SI unit")

    elif unit.get()== "Celcius":
        C=value.get()
        K=C+273.15
        F=(9/5)*C + 32
        print(f"{K} ,{F}")
        q1val.set(f"{K:.2f} Kelvin and {F:.2f} Fahrenheit")

    elif unit.get() == "Kelvin":
        print("K to rest")
        K=value.get()
        C=K-273.15
        F=1.8*(K-273.15)+32
        print(f"{C:.2f} ,  {F:.2f}")
        q1val.set(f"{C:.2f} Celcius and {F:.2f} Fahrenheit")

    else:
        print("F to rest")
        F=value.get()
        C=(F-32)*(5/9)
        K=(F-32)*(5/9)+273.15
        print(f"{C:.2f} , {K:.2f}")
        q1val.set(f"{C:.2f} Celcius and {K:.2f} Kelvin")

root =Tk()
root.geometry("655x170")
root.title("Temperature Converter")
text= Label(root, text="Temperature Converter", font="comicsans 18 bold",justify="center")
text.grid(row=0,column=2)

q4=Label(root, text="")
q4.grid(row=1, column=2)

a= Label( text="Enter Temperature", font="comicsans 15 bold", padx=12)
a.grid(row=2,column=1)

value=IntVar()
unit=StringVar()
q1val= StringVar()
q2val = StringVar()
q1val.set("")




Entry(root, textvariable=value ).grid(row=2, column=2)
unit= ttk.Combobox(root, values=["Celcius", "Kelvin", "Fahrenheit"])
unit.grid(row=2, column=3)


unit.set("Select Unit")
Button(text="Convert", command=conv).grid(row=4, column=2)

q0=Label(root, text="")
q0.grid(row=5, column=2)

q1=Label(root, textvariable=q1val)
q1.grid(row=6, column=2)

root.mainloop()