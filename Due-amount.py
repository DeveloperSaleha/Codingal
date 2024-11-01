def calculate_due_amount(principle, rate, time):
    interest = (principle * rate * time) / 100
    total_amount_due = principle + interest 
    return total_amount_due

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

due_amount = calculate_due_amount(principle, rate, time)
print(f"The total amount due after {time} years is: {due_amount}")