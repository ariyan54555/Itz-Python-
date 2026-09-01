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
        print("Finding...." \
        "")
    idx+=1

#using of continue statement

i=1
while i<=10:
    if i==5:
        continue
    print(i)