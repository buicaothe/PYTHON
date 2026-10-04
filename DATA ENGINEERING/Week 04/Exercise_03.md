# Exercise 3 - Permutations

These are the data columns: ['Your favorite color','Dream Holiday Destination', 'Favorite Pet', 'Favorite Season', 'Music','Favorite Food'].

Lets regard 3 permutations. Select different columns from the list and use `value_counts()`. Select only combinations which have count over 1. 

Can you use pandas.concat to add up these columns?

Bonus:

Can you write a loop that goes through all 3 permutations and find the ones that have more than 1 value count.

Hint: This code gives you the permutations:

```python
from itertools import permutations

columns = [
    "Your favorite color",
    "Dream Holiday Destination",
    "Favorite Pet",
    "Favorite Season",
    "Music",
    "Favorite Food",
]

trios = list(permutations(columns, 3))
trios[:3]
```

** PUT THE ANSWERS TO student_work/homework_answers/exercise_03.md**
