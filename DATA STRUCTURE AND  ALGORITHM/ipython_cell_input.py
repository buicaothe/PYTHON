# OPTION 1:
A = [1,2,3,4,9,6]
B = [6,5,4,3,2,1]
if len(A) != len(B):
    print(False)
else:
    from collections import Counter
    freq_A = Counter(A)
    freq_B = Counter(B)
    freq_A == freq_B 
    print(True if freq_A == freq_B else False)

# OPTION 2:
if len(A) != len(B):
    print(False)
else:
    print(True if sorted(A) == sorted(B) else False)
