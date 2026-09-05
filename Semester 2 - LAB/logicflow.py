string = input('Enter a string: ')
x = len(string)
print(x)
if x > 5: print('The word is more than 5 characters!')
else: print('The word is less than or equal to 5 characters')

num = int(input("Enter a positive integer: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(f"{divisor} is a factor of {num}")