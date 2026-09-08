# BACKGROUND: HOW A FUNCTION IS CALLED:
def fun1():
    print('      fun1() called')


def fun2():
    print('  Before fun1()')
    fun1()
    print('  After fun1()')


fun2()

print('-----------------------------')
print('Before fun2()')
fun2()
print('After fun2()')

# RECURSION FUCTION:


# def fun(n):
#     if n == 0:
#         return
#     print('Hellow World')
#     fun(n-1)

def funwhile(n):
    while n > 0:
        print('Hellow World')
        n -= 1


funwhile(5)
