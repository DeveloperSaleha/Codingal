decimal_num = 38
 
# Initialize an empty list to hold the binary digits
binary_list = []
 

# printing original number
print ("The original number is : " + str(decimal_num))
 

# decimal to binary number conversion 
res = [int(i) for i in list('{0:0b}'.format(decimal_num))]
 
# printing result 
print ("The converted binary list is : " +  str(res))