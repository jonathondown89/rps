import random
from datetime import datetime
now = datetime.now()

value = (input('Hi there, what is your name? '))
print() #line break
str1 = (' It is your lucky day today, '
        'as we are going to play a cool game '
        'of Rock:Paper:Scissors!')

if now.hour < 12: #defines time of day for greeting
    print(f"Good morning",value,", how are you?" + str1)
elif now.hour < 17:
    print(f"Good Afternoon",value,", how are you?" + str1)
elif now.hour < 24:
    print(f"Good evening", value,", how are you?" + str1)

print()#line break

print("Here are the rules: "
      "\n1. You must pick between Rock, Paper or Scissors."
      "\n2. The computer will, at random, also pick."
      "\n3. The result will follow after both you and the computer have chosen."
      "\n4. This is a totally random and fair game, good luck!")
print()
print("This is how to win:"
      "\n - Rock beats Paper"
      "\n - Paper beats Scissors"
      "\n - Scissors beats Rock")

print() # Line break

#defining the inputs
user_guess = (input("Do you choose Rock, Paper or Scissors? "))
comp_guess = (random.randint(0, 2))

#converting user guess from words to int
if user_guess in ('rock','Rock'):
    user_int = 0
if user_guess in ('paper','Paper'):
    user_int = 1
if user_guess in ('scissors','Scissors'):
    user_int = 2


#converting comp guess from int to words to display to user
if comp_guess == 0:
    print('Computer picks Rock')
if comp_guess == 1:
    print('Computer picks Paper')
if comp_guess == 2:
    print('Computer picks Scissors')

# printing result to user and determine winner
if user_int == comp_guess:
    print('Wow, it is a Draw!')
elif user_int == 0 and comp_guess == 2:
    print('You win as Rock beats Scissors, congratulations!')
elif user_int == 0 and comp_guess == 1:
    print('Computer wins as Paper beats Rock, sorry!')
elif user_int == 2 and comp_guess == 1:
    print('You win as Scissors beats Paper, congratulations!')
elif user_int == 1 and comp_guess == 0:
    print('You win as Paper beats Rock, congratulations')
elif user_int == 1 and comp_guess == 2:
    print('Computer wins as Scissors beats Paper, sorry!')
if user_int == 2 and comp_guess == 0:
    print('Computer wins as Scissors beats Rock, sorry!')
