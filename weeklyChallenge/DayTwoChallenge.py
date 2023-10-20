"""
Over the Speed Limit by:
1 to 10 11 to 20 21 and more
Penalty Fines
$20 $55 $70
"""


def beginner():
    speedLimit = int(input("Speed Limit: "))
    speedCar = int(input("Speed of Car: "))

    overLimit = speedCar - speedLimit
    if overLimit <= 0:
        print("Congratulations, you are within the speed limit!")
    else:
        print("You are speeding and your fine is: ", end="")
        if  overLimit <= 10:
            print("$20")
        elif overLimit <= 20:
            print("$55")
        else:
            print("$70")


def intermediate():

    nOffense = 0
    speedLimit = int(input("Speed Limit: "))
    while nOffense < 5:
        speedCar = int(input("Speed of Car: "))

        overLimit = speedCar - speedLimit
        if overLimit <= 0:
            print("Congratulations, you are within the speed limit!")
        else:
            print("You are speeding and your fine is: ", end="")
            if overLimit <= 10:
                print("$20")
            elif overLimit <= 20:
                print("$55")
            else:
                print("$70")
        nOffense += 1

    print("Your license has been suspended.")


def advanced():
    import math

    nOffense = 0
    speedLimit = int(input("Speed Limit: "))
    while nOffense < 5:
        speedCar = int(input("Speed of Car: "))

        overLimit = speedCar - speedLimit
        if overLimit <= 0:
            print("Congratulations, you are within the speed limit!")
        else:
            print("You are speeding and your fine is: ", end="")
            nOffense += 1
            print(round(nOffense**2 * math.sqrt(overLimit), 2))
    print("Your license has been suspended.")


[beginner, intermediate, advanced][int(input("nMeth: "))]()

