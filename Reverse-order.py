#Input number greater than 1
n = int(input("Enter the value of n: "))
#Print the numbers from n to 1
print("Numbers from {0} to {1} are: ".format(n,1))
#Loop to print numbers
for i in range(n,0,-1):
    print(i)