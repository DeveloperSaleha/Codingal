#Define function to calculate cube
def cube(number):
    return number*number*number
#Define a function which will execute cube function if the user entered number divisible by 3
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
    #Display result
print(by_three(12))
print(by_three(3))