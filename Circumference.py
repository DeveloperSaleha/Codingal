def findCircum(radius):
    return 2 * 3.14 * radius

print("Enter Radius of Circle: ", end="")
r = float(input())

c = findCircum(r)
print("\nCircumference = {:.2f}".format(c))