list1 = [12, -7, 5, 64, -14]
num = 0

while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end = " ")
    num += 1



list2=[12,14,-95,3]
print([a for j, a in enumerate(list2) if a>=0])
