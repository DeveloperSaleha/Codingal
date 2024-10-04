#Input a number
num = int(input('Enter the number:'))
t = num
numlen = 0
#iterate the loop
while t>0:
    numlen = numlen+1
    t = int(t/10)

    if numlen>=4: #condition 1
        numlen = int(numlen/2)
        chk = 0
        while num>0: #iterate loop
            rem = num%10
            if chk==numlen: #nested condition 1
                midone= rem
            elif chk==(numlen-1):
                midtwo = rem
            num = int(num/10)
            chl = chk+1
            prof = midone*midtwo #product of middle digits
            #displays the result
            print('\nproduct of mid digits (' +str(midone)+ '*' +str(midtwo)+')= ', prod)
    else:

        print('\nIt not a 4 or more than 4-digit number!')
