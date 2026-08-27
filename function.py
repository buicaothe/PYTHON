'''
def produc(x,y):
    x = input('nhập x = ')
    y = input('nhập y = ')
    a = x * y
    return a

b = produc(2,6)

print(b)


import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()


def produc(x, y):
    a = x * y
    return a


b = produc(2, 3)

print(b)

mylist = [1, 5, 4, 6, 8, 11, 3, 12]
newlist = list(filter(lambda x: (x % 2 == 0), mylist))
print(newlist)

def result(x): return x+1
def a(y): return y*y
b = a(10)
print(b)

def greet(x):
    print(f'Hell0, {x}')
greet("buicasdf asdf sadfasd fsdfads asdf ")
def phepnhan(x, y):
    a = x*y
    return a
b = phepnhan(10, 20)
print(b)

def cube(x):
    x = x**3
    return x
print(cube(10))

def greet(name):
    print(f'Hello, {name}')
greet('BUI CAO THE    1 1 1  ')

C = float(input('Nhập nhiệt độ C: '))


def convert_cel_to_far(C):
    F = C*9/5+32
    return F


a = convert_cel_to_far(C)
print(f'Nhiệt độ đổi ra C = {a} độ C')

F = float(input('Nhập nhiệt độ F: '))


def convert_far_to_cel(F):
    C = (F-32)*5/9
    return C


b = convert_far_to_cel(F)
print(f'Nhiệt độ đổi ra F = {b} độ F')

def getinput():
    a = float(input('Nhập vào cạnh đáy a = '))
    h = float(input('Nhập vào chiều cao h = '))
    return a, h


a, h = getinput()


def tarea():
    area = 0.5*a*h
    print(f'The area of the triangle with a = {a} and h = {h} is {area}')

tarea()

def createList(items, y):
    return [i for i in range(0, items)], y*2


t = createList(7, 20)

print(type(t))
t1, t2 = createList(3, 'witches')
print(t)


def hello(name, surname, alias='', *others):
    print(f'{name}{surname}', end=' ')
    if alias:
        print('a.k', alias, end=' ')

    for item in others:
        print(item, end=' ')

    print()


hello('the', 'bui', 'cao', 'otherssss')



def getinput():

    pass


x = getinput()
print(x)



def cubearea(side):
    return 6 * side * side


def cubevolume(side):
    return side ** 3


def main():
    side = float(input('the side of a cube: '))
    print(
        f'Area of a cube with side {side} is {cubearea(side)} and volume {cubevolume(side)}')


main()


import math


def volume(radius):
    return 4 / 3 * math.pi * radius**3


def main():
    global radius
    radius = float(input('radius of a sphere: '))
    print(
        f'The sphere with radius {radius} has volume {round(volume(radius), 2)}')


main()
print('Gọi hàm volume bên ngoài: ')
print(volume(radius))


def cubearea():
    return 6 * side * side


def cubevolume():
    return side ** 3


print(f'{(side := float(input('The side of a cube: ')))} Area: {cubearea()} Volume {cubevolume()}')



def cubearea():
    return 6 * side * side


def cubevolume():
    return side ** 3


def main():
    side = float(input('the side of a cube: '))
    print(
        f'area of a cube with side {side} is {cubearea()} and volume {cubevolume()}')


main()

mylist = [1, 5, 4, 6, 8, 11, 3, 12]


def odd(x):
    return x % 2 == 0


def evenlist(mylist):
    newlist = []
    for x in mylist:
        if odd(x):
            newlist.append(x)
    return (newlist)


print(evenlist(mylist))



def longest(items: list | tuple | str) -> int:
    """ Calculates the length of each item in items

    :param items: a collection of items that have a length
    :type items: an iterable list, tuple or str

    :raises typeError: if the received items is not a list, tuple or str
    :raises TypeError: if the items do not contain values with length

    :return: returns the length of the longest item
    :rtype: int
    

    print(type(items))
    if type(items).__name__ not in ('str', 'list', 'tuple'):
        raise TypeError('list, tuple or str only')
    return max([len(item) for item in items])

try:
    print(longest('Hello there you all oppossums'))  # 1
    print(longest('Hello there you all oppossums'.split()))  # 9
    print(longest(('this', 'is', 'a', 'test')))  # 4
    # exception
    print(longest(tuple(map(len, 'Hello there you all oppossums'.split()))))
    print(longest(dict.fromkeys(('this', 'is', 'a', 'test'))))  # exception
    print(longest(list(('this', 'is', 'a', 'test'))))  # 4
except Exception as e:
    print('there was an error: ', e)
'''


def isPalindrome(a):
    a = a.lower()
    a = ''.join(a.split())
    return a[::-1] == a


tries = 'Nalle vai Viivi Avellan', \
    'Was it a cat I saw?', \
    'Was it a cat I saw', \
    'Red rum, sir, was murder', \
    'Red rum sir is murder'

for item in tries:
    if isPalindrome(item):
        print('\"', item, '\"', 'IS A PALINDROME.')
    else:
        print('\"', item, '\"', 'is not a palindrome.')

b = 'ho va ten bui cao the'

b = b.split()
print(b)
