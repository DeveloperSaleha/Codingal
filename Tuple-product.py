def prod(a) :
    res = 1
    for ele in a:
        res *= ele
    return res
test_tup = (9, 3, 2, 1, 5, 10)
print("The original tuple is : " + str(test_tup))
res = prod(list(test_tup))
print("The product of tuple elements are: " + str(res))