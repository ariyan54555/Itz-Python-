f = open("data.txt","r")
#data = f.read()

# print(data)
# print(type(data))
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

f.close()

f = open("Samos.txt","w")
f.write("Hello, World!")
f.close()

f = open("Samos.txt","a")
f.write("\nHello, Python!")
f.close()

with open("Samos.txt","r") as f:  #with keyword automatically closes the file after the block of code is executed
    data = f.read()
    print(data)


#delete file
import os
os.remove("Samos.txt")

f = open("data.txt","r")

data = f.read()

new_data = data.replace("CSE","SWE")

print(new_data)

f.close()

f = open("data.txt","w")
f.write(new_data)
f.close()

#WAF to check a word is present in a file or not

def check_Word():
    word = "AIUB"
    with open("data.txt","r") as f:
        data = f.read()
        if(word in data):
            print("Word is present")
        else:
            print("Word is not present")

check_Word()           
#WAF to find a word in line by line and print the line number
def find_Word():
    word = "DIU"
    data = True
    line_number = 1
    with open("data.txt","r") as f:
            while data:
                data = f.readline()
                
                if(word in data):
                    print("Word is present in line number ",line_number)
                    return
                line_number += 1

    return -1          

find_Word()
# find even numbers from a file 

f = open("numbers.txt","w")
f.write("1,2,3,4,5,6,7,8,9,10")
f.close()

with open("numbers.txt","r") as f:
    data = f.read()
    numbers = data.split(",")
    even_numbers = []
    for num in numbers:
        if int(num) % 2 == 0:
            even_numbers.append(num)
    print("Even numbers are: ",even_numbers)
    print("Total even numbers are: ",len(even_numbers))
