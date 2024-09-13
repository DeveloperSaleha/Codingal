a = 10
b = 12
c = 0
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

    a = 10
    b = -10
    c = 0
    if a > 0 or b > 0:
        print("Either of the number is greater than 0")
    else:
        print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either  of the number is greater than 0")
        
else:
    print("No number is greater than 0")

    #NOT-equal operator
    a = 10
    b = 12
    c = 12
    print(a != b)
    print(b != c)

    a = "python"
    b = "coding"

    if a!= b:
        print(a, "and", b, 'are different.')

    a = 4
    b = 5
    if(a == 1) != (b == 5):
        print("Hello")

    a = int(input("Enter a number:"))
    if a%2 !=0:
        print(a, "is not even number.")
