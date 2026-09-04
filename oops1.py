#creating class

class Student:
    name="Ariyan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    colour = "Blue"
    brand = "Marcedes"

c1 = Car()
print(c1.colour)
print(c1.brand)

#creating constructor

class Bike:
    def __init__(self):
        print("This is constructor")

b1 = Bike()
