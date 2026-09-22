# Find the maximum number:

A = [10050,10,100,2,6,3,4,8,9,10,23,120,6099999]

def max(A):
    max = A[0]
    for i in range(1,len(A)):
        if A[i]>max:
            max = A[i]
    return max

print(max(A))
