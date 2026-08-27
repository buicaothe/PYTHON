phrase = 'hello my name is bui cao the nice to meet you'
y = phrase.replace('bui cao the', 'BUI CAO THE')
print(y)

a = input('What word do you want to find?')
x = phrase.find(a)
if x == -1:
    print('I can not find this word!!!! Please try another one!')
    a = input('What word do you want to find [2nd time]?')
    if x == -1:
         print('I can not find this word!!!! Please try another one!')
         a = input('What word do you want to find [3rd time]?')
         if x == -1: print('I can not find this word!!!! You have no more chance!')
        
else:
    print(f'Your word are found in the location of {x} of the Phrase!')
    