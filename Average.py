# Storing Values
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

# Finding the total of trees
sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the trees is: ", sum)

# Finding the average of trees
average = sum/5
print("the average of all the trees is: ", average)

# Taking total amount as input from user
amount =int (input("Please enter amount for withdraw :"))

# Calculating the number of notes of different denominations
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("notes pf 100 rupee" , note_1)
print("notes pf 50 rupee" , note_2)
print("notes pf 10 rupee" , note_3)

# take marks as input from user
print("Enter marks obtained in 4 subjects: ")
math = int(input("maths :"))
science = int(input("science :"))
history = int(input("history :"))
english = int(input("english :"))

# let's calculate the percentage of marks
sum = math+science+history+english
print("sum of math, science, history and english")
perc = (sum/400)*100

print(end = "Percentage Mark = ")
print(perc)
