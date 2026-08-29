# 6 Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap


while True:
    try:
        year = int(input('Enter the year from 1900 to 10^5: '))
        if 1900 <= year <= 10**5:
            break
        else:
            print("This is not in the correct range!")
    except ValueError:
        print('Not a NUMBER!!!!!')

print(is_leap(year))
