list1 = list(range(1, 11))
i = 0

while i < len(list1):
    if i % 2 == 0 and i != 0:
        i = i + 1
        break
        #continue
    print(list1[i])
    i = i + 1

for i in list1:
    if i % 2 == 0:
        break
        #continue
    print(i)