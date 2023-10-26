import random

###### Easy ######

# Generating the player as tuple
Alice = ('Alice', random.randint(1, 13))
Bob = ('Bob', random.randint(1, 13))
player = [Alice, Bob]

# Sorting the player list to determine winner
ranked = sorted(player, key=lambda tuple: tuple[1], reverse=True)   

# Checking for tie
if Alice[1] == Bob[1]:
    print(f'Alice and Bob tied, both getting {Alice[1]} point(s)')
else:
    print(f'{ranked[0][0]} won getting {ranked[0][1]} point(s). {ranked[1][0]} lost, only having {ranked[1][1]} point(s)')

###### Intermediate #######

# Adding the 3rd player to list of player
Carol = ('Carol', random.randint(1,13))
player = [Alice, Bob, Carol]

# Sorting the list
ranked = sorted(player, key=lambda tuple: tuple[1], reverse=True)

# Checking for tie, and if they are 3-way or 2-way tie
if Alice[1] == Bob[1] == Carol[1]:                                  # 3-way tie check
    print(f'All three tied, getting {Alice[1]} point(s) each')
elif ranked[0][1] == ranked [1][1]:                                 # 2-way tie check
    print(f'{ranked[0][0]} and {ranked[1][0]} tied for first place, getting {ranked[0][1]} point(s) each')
else:                                                               # No tie happened, only displaying winner and points
    print(f'{ranked[0][0]} won with {ranked[0][1]} point(s)')

###### Advanced ######

# Since the list of player is already sorted from 2nd chall, we can reuse it
# Again checking for tie
if Alice[1] == Bob[1] == Carol[1]:                                  # 3-way tie check
    print(f'All three tied, getting {Alice[1]} point(s) each')
elif ranked[0][1] == ranked [1][1] or ranked[1][1] == ranked[2][1]: # 2-way tie check
    if ranked[0][1] == ranked [1][1]:                               # 1st place tie check
        print(f'{ranked[0][0]} and {ranked[1][0]} tied for first place, getting {ranked[0][1]} point(s) each. {ranked[2][0]} got last place with {ranked[2][1]} point(s)')
    else:                                                           # Tie happened for 2nd place
        print(f'{ranked[0][0]} won first with {ranked[0][1]} point(s). {ranked[1][0]} and {ranked[2][0]} tied second, each having {ranked[1][1]} point(s)')
else:                                                               # No tie happened, display player by rank and points
    print(f'{ranked[0][0]} won 1st, {ranked[0][1]} point(s). \n'
          f'{ranked[1][0]} got 2nd, {ranked[1][1]} point(s). \n'
          f'{ranked[2][0]} got 3rd, {ranked[2][1]} point(s)')
