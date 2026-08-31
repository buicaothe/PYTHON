# 8 List Comprehesions:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

list1 = [num for num in range(x+1)]
list2 = [num for num in range(y+1)]
list3 = [num for num in range(z+1)]
a = [list1, list2, list3]
print(a)
