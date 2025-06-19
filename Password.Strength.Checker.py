from tkinter import *

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="orange")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="#90EE90")  
    else:
        result_label.config(text="Very Strong", fg="green")

root = Tk()
root.title("Length Converter App")  
root.geometry("400x400")

Label(root, text="Enter your password:", fg="blue").pack(pady=20)
entry = Entry(root, show='*', width=30)
entry.pack(pady=10)

btn = Button(root, text="Check Strength", bg="#d0efff", command=check_strength)
btn.pack(pady=20)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
