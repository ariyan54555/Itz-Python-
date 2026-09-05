#creating class

class Student:
    def __init__(self,name,marks):#constructor with parameter
        self.name = name
        self.marks = marks

    def display(self):#Method to display student details
        print("Name: ",self.name)
        print("Marks: ",self.marks)

    def get_name(self):
        return self.name
    def get_marks(self):
        return self.marks


s1 = Student("Apurba",100)
s1.display()

s2 = Student("Smrity",90)
s2.display()

print(s1.get_name())
print(s2.get_marks())


class Car:
    colour = "Blue"
    brand = "Marcedes"

c1 = Car()
print(c1.colour)
print(c1.brand)

#creating constructor

class Bike:
    def __init__(self):#constructor default
        pass
    #constructor with parameter
    def __init__(self,name):
        self.name = name
        print("This is constructor")

b1 = Bike("Honda")
print(b1.name)


#creating a class of student with constructor which take parameter name and marks and create a method to calculate the average marks of student

class Student1:
    @staticmethod#decorator to create static method
    def Hello():
        print("Hello")
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum=0
        for i in self.marks:
            sum +=i

        avg = sum/len(self.marks)
        print("Hi,",self.name," your average marks is: ",avg)

s = Student1("Apurba",[90,80,70,60])
s.average()
Student1.Hello()

#practice
#create a class of account with two attributes balance and account no
#create methods for debit,credit and printing balance

class Account:
    def __init__(self,accNo,balance):
        self.accNo = accNo
        self.balance = balance

    def debit(self,amount):
        self.balance -= amount
        print(amount,"is debited from the account")

    def credit(self,amount):
        self.balance += amount
        print(amount,"is credited in the account")

a11 = Account(111,1222)
a11.debit(100)
print(a11.balance)
a11.credit(3000)
print(a11.balance)
        
    
