#merge two list
list1 = [2,34,53,5]
list2 = [2,5,7,2,3]

merge = []

for i in range(len(list1)):
    merge.append(list1[i])

for i in range(len(list2)):
    merge.append(list2[i])

print(merge)
merge.sort()
print(merge)


