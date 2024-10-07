def total_calc(bill_amount,tip_perc):
#Define function to calculate the tip on bill
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
#Specify only bill_amount
#Default value of tip percentage is used
total_calc(146,211)
