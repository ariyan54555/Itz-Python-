count=1
while count<5:
    print("CSE",count)
    count+=1

#print number 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#print numbers from 100 to 1
j=100
while j>=1:
    print(j)
    j-=1
#print the multiplication table of n
n=int(input("Enter the number:"))
k=1
while k<=10:
    print(n,"*",k,"=",n*k)
    k+=1
#Program to print the square of numbers from 1 to 10 in a list
g=1
list=[]
while g<=10:
    list.append(g*g)
    g+=1
print(list)
#found a number from a tuple
num=(1,2,3,4,5,6,7,8,9)
number=4
idx=0
while idx<len(num):
    if(num[idx]==number):
        print("Found at index",idx)
        break
    else:
        print("Finding....")
    idx+=1



#for loop
Fruits=["Mango","Banana","Apple","Orange"]
for el in Fruits:
    print(el)

tuple1=(1,2,3,4,5)
for el in tuple1:
    print(el)

str="Python"
for char in str:
    if(char=="h"):
        print("Found")
        break
    else:
        print("Finding....")

#print the element of the following list using for loop
list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)

#search for number x in this tuple using for loop
tuple2=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number you want to search: "))
for el in tuple2:
    if(el==x):
        print("Found",el)
        break
    else:
        print("Finding")

#range function

for i in range(10):
    print(i)

#range with start and end
for i in range(5,10):
    print(i)

#range with start, end and step
for i in range(1,10,2):
    print(i)
#even numbers from 1 to 100
for i in range(2,101,2):
    print(i)

#print number from 1 to 100
for i in range(1,101):
    print(i)

#print number from 100 to 1
for i in range(100,0,-1):
    print(i)
#print the multiplication table of n
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#pass statement
for i in range(1,100):
    pass
print("This is pass statement")

#WAP to find the sum of first n numbers using while loop
n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1

print("Sum of first",n,"numbers is:",sum)

#WAP to find the factiorial of first n numbers using for lo1op

a =int(input("Enter the number:"))
fact=1
for i in range(1,a+1):
    fact*=i
print("Factorial of",a,"is:",fact)