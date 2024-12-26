class Reverse:
    def __init__(self, s=""):
    
        self.s = s
    
   
    def reverse_string(self):
       
        words = self.s.split()  
        words.reverse() 
        return ' '.join(words)  

input_string = input("Enter a string: ")

reverse_object = Reverse(input_string)

print(f"Reversed string: {reverse_object.reverse_string()}")


