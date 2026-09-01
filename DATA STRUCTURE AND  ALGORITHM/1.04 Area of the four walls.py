# 1.04 Area of the four walls of a rectangular room:
while True:
    try:
        a = float(input('Enter the First 2 wall bases, a = '))
        b = float(input('Enter the Second 2 wall bases, b = '))
        h = float(input('Enter the height of the Room, h = '))
        if (a > 0) and (b > 0) and (h > 0):
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')

area = 2*(a+b)*h
print(f'Area of the four walls of a rectangular room is {area}.')
