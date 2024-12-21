class Student:
    __schoolName = 'XYZ School'
    def __init__(self, name, age):
        self.__name = name

    def __display(self):
        print('This is private method.')

std = student("bill", 25)
print(std.__schoolName)