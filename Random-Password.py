import random
import string

def generate_password(length):
 
    characters = string.ascii_letters + string.digits  

    password = ''.join(random.choice(characters) for i in range(length))
    
    password = ''.join(random.sample(password, len(password)))
    
    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)
print(f"Generated password: {password}")
