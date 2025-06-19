from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Length Converter App')

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Enter a valid number.")

label = Label(root, text="Enter length in inches:", fg="blue")
label.place(x=120, y=100)

entry = Entry(root)
entry.place(x=140, y=130)

button = Button(root, text="Convert", bg="#d0efff", command=convert)
button.place(x=170, y=170)

result_label = Label(root, text="", fg="green")
result_label.place(x=120, y=220)

root.mainloop()
