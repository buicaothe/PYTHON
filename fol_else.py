max = 5
sum = 0
for i in range (max):
    if i ==5:
        print(' the loop has stopped')
        break #total break!!!!!!
    sum +=i
    print(i,end='+' if i < (max-1) else '=')
else:
    print(sum)
