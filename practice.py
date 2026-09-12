#merge two list
list1 = [2,34,53,5,0]
# list2 = [2,5,7,2,3]

# merge = []

# for i in range(len(list1)):
#     merge.append(list1[i])

# for i in range(len(list2)):
#     merge.append(list2[i])

# print(merge)
# merge.sort()
# print(merge)


r = list1.index(min(list1))
if list1[r] >0:
    print(r+1)
else:
    print(r)



