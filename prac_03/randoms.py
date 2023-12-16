import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"What did you see on line 1?"
"A: What I see in line 1 is a random number in the range 5-20."
"What was the smallest number you could have seen, what was the largest?"
"A: The smallest number I could have seen is 5, the largest number is 20."

"What did you see on line 2?"
"A: What I see in Line 2 is a random display of a number in the range 3-10, and the step of random number is 2."
"What was the smallest number you could have seen, what was the largest?"
"A: The smallest number I could have seen is 3, the largest number is 9."
"Could line 2 have produced a 4?"
"A: The line 2 cannot produced a 4 because the step is 2 and the smallest number is 3. 4 is not a random number in this formula."

"What did you see on line 3?"
"A: What I see in line 3 is a random number in the range 2.5-5.5."
"What was the smallest number you could have seen, what was the largest?"
"A: The smallest number I could have seen is 2.5, the largest number is 5.5."

print(random.randint(1, 100)) #Write code to produce a random number between 1 and 100 inclusive.
