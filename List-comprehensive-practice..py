num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]

even_numbers = [i for i in range(num) if i % 2 == 0]

print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Capitalized fruits: {capitalized_fruits}")
