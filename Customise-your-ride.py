print("Select your ride:")
print("1.Bike")
print("2.Car")

#Take input of number 1 or 2
#Select your ride
choice= int(input("Enter your choice: "))
#User entering option 1
if(choice == 1): #Condition 1 outer if statement
    print("What type of bike?")
    print("1.Scooty/n")
    print("2.Scooter/n")

    #Condition for selecting the type of bike
    choice2= int(input("Enter your choice2: "))
    if choice2==1: #Inner statement
        print('You have selected scooty')
    else:
        print("You have selected scooter")