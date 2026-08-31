#Dictionary
# It is used to store data in key:value pairs
# It is Unordered, mutable and don't allow duplicate keys
# Have no index

Apurba_Info={
    "Key" : "Value",
    "Name" : "Apurba Das Arpan",
    "Age" : 23,
    "Id" : "251-15-103",
    "University CGPA" : 4.00,
    "Gender" : "Male",
    "Phone Number" : "01634283759",
    "List Of GF" : ["Ratri Paul","Brishty Paul","Antara Mondal"],

}
#value can be chcanged

print(Apurba_Info)
print(type(Apurba_Info))
print(Apurba_Info["Age"])
print(Apurba_Info["Id"])
print(Apurba_Info["List Of GF"])

#nested dictionary

student={

    "Name":"Ariyan",
     "Marks":{
         "Obeject Oriented Programming":"A+",
         "Programming and Problem Solving":"A+",
         "Data Structure":"A+"
     }

}
print(student)
print(type(student))
#dict methods
print(student.values())
print(student.keys())
print(list(student.keys()))
print(student.items())# This method return tuple
#print(student["Name2"])#This line throw an error
print(student.get("Name"))
#update method in dictionary

student.update({"Age":23})
print(student)
#We also can create a new dicetionary pass it in old dictionary
dict2={"Gender":"Male"}
student.update(dict2)
print(student)

#SET in Python
#Immutable and store unique value
# element mutable 
Money = {33,453,223,33,33,566,776,"AriyansMoney","Dhaka","Dhaka"}#Ignore duplicate values
print(Money)
print(type(Money))
#create empty set
Taka = set()
Taka.add(1)
Taka.add(10)
Taka.add(11)
Taka.add(11)
print(type(Taka))
print(Taka)
print(Taka.pop())#Picks value randomly
print(Taka.pop())
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))