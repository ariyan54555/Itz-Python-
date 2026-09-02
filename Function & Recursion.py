#Define a function with return type

def calcSum(q,b):
    return q+b

sum = calcSum(5,10)
print("Sum=",sum)
#without return type
def sum(a,b):
    print("Sum=",a+b)

sum(5,10)
#average of three numbers

def average(a,b,c):
    return (a+b+c)/3

avg = average(3,4,5)
print("Avg = ",avg)

#WAF to find the length of a list
def len_City(city):
    return len(city)

city = ["Dhaka","khulna","Rajshahi","Barishal"]

length = len_City(city)
print("Length of the list = ",length)

#WAF to print the elements of a list in a single line
def printlist(city):
    for el in city:
        print(el,end=" ")

printlist(city)
print()
#WAF to find the factorial of n
def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact*i
    return fact

fact = factorial(5)
print("Factorial of 5 = ",fact)


#Recursion
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

show(5)

#Write a recursive function to find the sum of n natural numbers

def sum_calc(n):
    if n==0:
        return 0
    return n + sum_calc(n-1)

sum = sum_calc(3)
print("Sum = ",sum)

#write a recursive function to print the elements of a list
def printlist_recursion(city,index):
    if index == len(city):
        return
    print(city[index],end=" ")
    printlist_recursion(city,index+1)

printlist_recursion(city,0)