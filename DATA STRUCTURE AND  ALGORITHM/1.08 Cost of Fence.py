# 1.08 Cost of fencing a rectangle at a given rate

while True:
    try:
        a = float(
            input('Enter the First 2 side length of the rectagular fence (m), a = '))
        b = float(
            input('Enter the First 2 side length of the rectagular fence (m), b = '))
        rate = float(
            input('Enter the cost rate per meter length of fence ($/m), Rate = '))
        if (a > 0) and (b > 0) and (rate > 0):
            break
        else:
            print('The number should be positive! Please re-type:')
    except ValueError:
        print('Not a NUMBER!!!!!')
# Total length:
length = 2*(a+b)
totalcost = length*rate
print(f"The total cost of the Fence is: ${totalcost:.2f}.")
