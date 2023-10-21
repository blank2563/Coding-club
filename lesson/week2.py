import time
a = 0

while a < 10:
    print("hello")
    a += 1
    
# range(1,6) = (1, 2, 3, 4, 5)
for i in range(1,6):
    print('hi ' * i)

# for loop work with any list, it will iterate through the index
animal = ['cat', 'dog', 'snake', 'hamster', 1, 5.3]
for i in animal:
    print(i)

# guessing game, now improved with while loop
import random

num = random.randint(1,10)

while True:
    print('Guess a number between 1 and 10:')
    guess = int(input())
    if guess == num:
        print('Correct')
        break
    else:
        print('You guessed wrong')

num = random.randint(1,10)

while guess != num:
    print('Guess a different number between 1 and 10')
    guess = int(input())
print('Correct')
