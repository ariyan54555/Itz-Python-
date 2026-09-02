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
