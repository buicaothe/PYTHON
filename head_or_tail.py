# HEAD OR TAIL
import random
toss = random.randint(0,1) #
selection = input('heads or tails [H or T]:' ).upper()

if selection[0] == 'H' and toss == 0 or\
      selection[0] == 'T' and toss == 1:
    print(f"You win with' {'HEADS' if selection[0] == 'H' else 'TAILS'}!!!!!!!")

else:
    print('You losst!')

# [0] is teh first letter of the string!asd
# f" - format