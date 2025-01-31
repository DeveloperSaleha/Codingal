from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('400x400')
def msg():
    messagebox.showwarning('Alert', 'Stop! Virus found.') 
    messagebox.showerror('Error', 'Folder is deleted.')
button = Button(root, text='Scan for Virus', command=msg)
button.place(x=180, y=180)

button = Button(root, text='Delete folder', command=msg)
button.place(x= 100, y=100)
root.mainloop()