list1 = list(range(1, 11))
list2 = [i * 2 for i in list1]

print(list1)
print(list2)

list3 = [i * 3 for i in list1 if i % 3 == 0]
print(list3)

list4 = [ i * j for i in list2 for j in list3]
print(list4)