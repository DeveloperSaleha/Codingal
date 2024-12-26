test_dict = {'Codingal': 3, 'is': 2, "best": 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
word_to_check = input("Enter the word you want to check the frequency of: ")
frequency = test_dict.get(word_to_check, 0)
print(f"The frequency of'{word_to_check}' is: {frequency}")