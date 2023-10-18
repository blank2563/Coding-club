# Easy
import math
import random

Alice = random.randint(1, 14)
Bob = random.randint(1, 14)
if Alice > Bob:
    print("Alice", Alice)
elif Alice < Bob:
    print("Bob", Bob)
else:
    print("Draw" )

# Medium

Alice = random.randint(1, 14)
Bob = random.randint(1, 14)
Carol = random.randint(1, 14)

# Approach 2
# Three Cases:
# One person has the highest score,
# Two people have the highest score,
# or all three people have the same score
maxNum = max(Alice, Bob, Carol)
if Alice == Bob == Carol:
    print("Draw")
elif Alice == Bob == maxNum:
    print("Draw between Alice and Bob")
elif Alice == Carol == maxNum:
    print("Draw between Alice and Carol")
elif Bob == Carol == maxNum:
    print("Draw between Bob and Carol")
elif Alice == maxNum:
    print("Alice")
elif Bob == maxNum:
    print("Bob")
else:
    print("Carol")


# Advanced
# Print the ranking, if draw, take the higher rank
winner = ""
second = ""
third = ""
maxNum = max(Alice, Bob, Carol)
if Alice == Bob == Carol:
    winner = "Alice, Bob, and Carol"
elif Alice == Bob == maxNum:
    winner = "Alice and Bob"
    third = "Carol"
elif Alice == Carol == maxNum:
    winner = "Alice and Carol"
    third = "Bob"
elif Bob == Carol == maxNum:
    winner = "Bob and Carol"
    third = "Alice"
elif Alice == maxNum:
    winner = "Alice"
    second = "Bob"
    third = "Carol"
elif Bob == maxNum:
    winner = "Bob"
    second = "Alice"
    third = "Carol"
else:
    winner = "Carol"
    second = "Alice"
    third = "Bob"
print("Winner: " + winner)
print("Second: " + second)
print("Third: " + third)
