str= "My name is Ariyan.\nI am a cse student.\nI am learning python programming."
print(str)
str1="Ariyan"
str2="Zaman"
print(len(str1))
print(len(str2))
#concatenation
final_str=str1+" "+str2
print(final_str)
print(len(final_str))
#indexing
print(str1[0])
#slicing
print(str2[0:3])
print(final_str[3:len(final_str)])
#minus indexing
st="Apple"
print(st[-4:-1])
#String Functions
str3="i am learning Python"
print(str3.endswith("Python"))
print(str3.capitalize())#work only this line. capatilize the first letter of the string
print(str3)
print(str3.replace("Python","Java"))
print(str3.find("learning"))
print(str3.count("a"))
#Practice
"""
Problem 01:WAP to input users fist name and print its length

"""
#Solve-->Problem 01
name=input("Enter your first name:")
print("Length of the name is: ",len(name))

"""
Problem 02:WAP to find the occurance of "$" in the string

"""
#Solve-->Problem 02
str4=input("Enter a string: ")
print("Occurance: ",str4.count("$"))

#conditional statement
age = 12;
if(age>=18):
    print("Can drive and can vote")
else:
    print("Can not do vote and drive")
#Marks of student
marks=int(input("Enter the marks : "))
if(marks>=80):
    print("A+")
elif(marks>=70):
    print("A")
else:
    print("Fail")

#Nesting
age=54
if(age>=18):
    if(age>=60):
        print("Cannot drive")
    else:
        print("Can drive")

else:
    print("Cannot drive")

#practice
"""
Problem 01:WAP to input a number and check whether it is even or odd

"""
number=int(input("Enter a number: "))
if(number%2==0):
    print("Even number")
else:
    print("Odd number")

"""
Problem 02:WAP to find the greatest of three numbrs input by user

"""
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if(n1>n2 and n1>n3):
    print("Greater :",n1)
elif(n2>n1 and n2>n3):
    print("Greater :",n2)
else:
    print("Grater: ",n3)

"""
Problem 02:WAP to check if a number multiple of 7 or  not
"""
n=int(input("Enter a number"))
if(n%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")
    
