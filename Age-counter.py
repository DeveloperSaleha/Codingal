def check_age(age_input):
    try:
        age = int(age_input)
        if age % 2 == 0:
            return "The age entered is even."
        else:
            return "The age entered is odd."
    except ValueError:
        return "Invalid input! Please enter a valid integer value for age."
user_input = input("Please enter your age: ")
result = check_age(user_input)
print(result)