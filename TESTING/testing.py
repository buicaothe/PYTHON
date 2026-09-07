# Python program to insert a given element at the beginning
# of an array

arr = [10, 20, 30, 40]
element = 5000
print("Array before insertion")
for i in range(len(arr)):
    print(arr[i], end=" ")

# Insert element at the beginning
arr.insert(3, element)

print("\nArray after insertion")
print(len(arr))
for i in range(len(arr)):
    print(arr[i], end=" ")
