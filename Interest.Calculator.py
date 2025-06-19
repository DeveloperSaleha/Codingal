from tkinter import *

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = (p * t * r) / 100

        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(
            text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}",
            fg="green"
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric values.", fg="red")

window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

Label(window, text="Principal (₹):").grid(row=0, column=0, padx=10, pady=10, sticky='e')
principal_entry = Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Time (years):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
time_entry = Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

Label(window, text="Rate (%):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
rate_entry = Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

calc_button = Button(window, text="Calculate", bg="#d0efff", command=calculate_interest)
calc_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = Label(window, text="", font=("Arial", 10))
result_label.grid(row=4, column=0, columnspan=2)

window.mainloop()
