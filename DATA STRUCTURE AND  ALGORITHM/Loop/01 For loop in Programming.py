for i in range(1, 6):
    print(i, end=" ")
print()

for i in range(2, 11, 2):
    print(i, end=" ")

    numbers = [1,2,3,4,5]
for num in numbers:
    print(num, end=" ")

    i, j = 0, 10
while i < 5 and j > 0:
    print("i=", i, ", j=", j)
    i += 1
    j -= 1
# 5. Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# 6. For Loop with Step/Stride
for i in range(0, 10, 2):
    print(i, end=" ")