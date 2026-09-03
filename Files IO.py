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


