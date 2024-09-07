import math
# Function to calculate the sqyare root
def calculate_square_root(number):
    if number < 0:
        return "square root of a negative number is imaginary"
    else:
        return math.sqrt(number)
    
    # Input from the user
num = float(input("Enter a number: "))

    # Calculate and display the square root
result = calculate_square_root(num)
print(f"The square root of {num} is {result}")