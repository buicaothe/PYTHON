for num1 in range(3):
    print(num1, end = ': ')
    for num2 in range(num1,14):
        print(num2, end = ' ________ ' if num2 < 13 else '')
    print()
print()
# INCREMENT 2
max = 20
sum = 0
for i in range(1,max,2): # 2 INCREMENT
    sum = sum + i
    print(i, end =' + ' if i < (max-1) else ' = ')
print(sum)
print()
