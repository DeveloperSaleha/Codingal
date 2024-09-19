def CalculatePower(n,x):
    p =1
    for i in range(1, x+1):
     p=p*n 
    return p
n,x=2,3
print(CalculatePower(n,x))
n,x=3,4
print(CalculatePower(n,x))

