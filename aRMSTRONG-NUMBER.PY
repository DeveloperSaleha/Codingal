#Take input from user
num = int(input("Enter a number: "))
#Initialise sum
sum = 0
#Find the sum of the code of each digit
temp = num
while temp>0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
#Display the result
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
