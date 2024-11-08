#Using a try and expect
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
#Using value error
except ValueError as ex:
    print("Exception:", ex)