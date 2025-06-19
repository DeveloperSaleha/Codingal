from tkinter import *
import random

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(options)

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = f"You win! Computer chose {comp_choice}."
    else:
        result = f"You lose! Computer chose {comp_choice}."

    result_label.config(text=result)

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")
Label(root, text="Choose Rock, Paper, or Scissors:", fg="blue").pack(pady=20)

btn_rock = Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=20)

root.mainloop()
