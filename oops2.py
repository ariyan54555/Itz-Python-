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

#Inheritence
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started...")
    def stop():
        print("Car stopped...")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self,type,name):
        self.type = type
        super().__init__(name)


car1 = Fortuner("Dissel","Fortuner")
car1.start()

#Multiple inheritance

class A:
    varA ="Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "Welcome to class C"
c1 = C()
print(c1.varA,c1.varC,c1.varB)

#use of property

class Student1:
    def __init__(self,phy,chem,math):
        self.phy = phy 
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"

stu = Student1(98,99,95)
print(stu.percentage)

stu = Student1(90,99,95)
print(stu.percentage)

#practice question

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius

c = Circle(1)
print(c.area())
print(c.perimeter())

#practice 2

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("Role =",self.role)
        print("Dept =",self.dept)
        print("Salary =",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","750000")
e1 = Employee("accountant","Finance","60000")
e1.showDetails()



