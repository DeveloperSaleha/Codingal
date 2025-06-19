from tkinter import *
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        dob = date(year, month, day)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result_label.config(text=f"Hello {name}, you are {age} years old.")
    except ValueError:
        result_label.config(text="Please enter valid numbers for date, month, and year.")

# Main Window Setup
root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")

# Input Fields
Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Date of Birth - Day:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
day_entry = Entry(root)
day_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Month:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
month_entry = Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Year:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
year_entry = Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=10)

# Button
submit_button = Button(root, text="Calculate Age", bg="#d0efff", command=calculate_age)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Output
result_label = Label(root, text="", fg="green")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run Loop
root.mainloop()
