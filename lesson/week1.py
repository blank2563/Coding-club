print('Hello World!')
# I can type whatever i want here and python will ignore me

integerVar = 1
stringVar = 'abc'
floatVar = 3.1415
inputVar = input('Please input something: ')

print(integerVar, stringVar, floatVar, inputVar)

hayson = int(input('Hayson? '))

if hayson >= 1:
    print('Hi Hayson!')
elif hayson <= -1:
    print('Where is Hayson?')
else:
    print('Hayson doesnt exist!!!')

import random

rand = random.randint(0,9)
guess = int(input('Guess a number: '))

if guess == rand:
    print('You guessed correctly, the number is', rand)
else:
    print('Better luck next time, the correct number was', rand)
