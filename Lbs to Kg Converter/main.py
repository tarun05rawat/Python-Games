from tkinter import *

window = Tk()     #initializes a window screen but doesn't do anything after
window.title("lbs to kg Converter")
window.minsize(width=100,height=100)
window.config(padx=20,pady=20)

def lbs_to_kg():
  lbs_value = float(entry.get())
  kg_value = lbs_value * 0.45359237
  label_3.config(text=f"{kg_value}")


entry = Entry(width=7)
entry.grid(column=1,row=0)

label_1 = Label(text="is equal to")
label_1.grid(column=0,row=1)

label_2 = Label(text="lbs")
label_2.grid(column=2,row=0)

label_3 = Label(text="0")
label_3.grid(column=1,row=1)

label_4 = Label(text="kg")
label_4.grid(column=2,row=1)

button = Button(text="Convert",command=lbs_to_kg)
button.grid(column=1,row=2)




window.mainloop()         #keeps the window on/ must be at the end of the program

