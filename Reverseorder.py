#Take input from user
#n = int(input("Enter a number: ")) 
#i=0
#while n != i:
   # n //= 10
   # i += 1
   # print(str(i))
n = int(input("Enter a number :"))
i = 0 
while n > 0:
    n //= 10
    i += 1
print(i)