#List
marks=[45.5,98.7,78.6,44,93.4,76.9]#Different types of data can be stored in list
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])
#string immutable
"""
str="Hello"
str[0]="h" #not allowed
"""
#list mutable
"""
marks=[54,33,44,22,43,45]
marks[0]=67#allowed
"""
Student=["Arian","251-15-***","Dhaka,Bangladesh"]
print(Student)
Student[0]="Jishan"
print(Student)
#List Slicing
print(Student[1:3])
print(Student[-3:])
#List Methods
list=[2,3,1,7,5,6]
list.append(0)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(1,5) #Index 1 insert 5
print(list)
list.remove(5)
print(list) #Remove 1st founded 5
list.pop(5)
print(list)
#Tuple
tup=(4,6,2,7,8,)
print(type(tup))
print(tup)
tup1=("Car",)
print(type(tup1))
print(tup1)
tup2=("Ariyan","England","31-08-2026")
print(tup2)
print(type(tup2))
print(tup.count(4))
print(tup[1:4])#slicing
print(tup[2])
"""
Write a program to input 3 movies name from the user and store them in list

"""

#solve
movies=[]
movies.append(input("Enter the movie name 1: "))
movies.append(input("Enter the movie name 2: "))
movies.append(input("Enter the movie name 3: "))

print(movies)
"""
Write a program to check if a list is palindrome or not

"""
#Solve
lis=[1,2,1]
copy_list=lis.copy()
copy_list.reverse()
if(copy_list==lis):
    print("Palindrome")
else:
    print("Not Palindrome")

#Write a program to count the grade 'A' from a tuple
#solve
grade=("A","B","C","D","F","A","B","A","A","D","A")
print(grade.count("A"))
gra=["A","B","C","D","F","A","B","A","A","D","A"]
gra.sort()
print(gra)