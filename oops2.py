class student:
    def __init__(self,name):
        self.name = name

s1 = student("Ariyan")
print(s1.name)
# del s1  --> this is "del" keyword by which we can delete an entire object from the memory

# private attribute and method

class Account:
    def __init__(self,name):
        self.__name = name

    def __hello(self):
        print("Heloo")
    def welcome(self):
        self.__hello()
a1 = Account("Aeiyan")
print(a1.welcome())


