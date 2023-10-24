listOfNumber = [1,2,3,4]                                    # Mutable, ordered      # Square bracket
tupleOfNumber = (1,2,3,4)                                   # Immutable, ordered    # Round bracket
setOfNumber = {2,5,6,8}                                     # Immutable, unordered  # Curly bracket
dictOfNumber = {"one": 1, 3: 'Three', "four": 'FOUR??'}     # Mutable, unordered    # Curly bracket + colon

"""
print(listOfNumber[0])
print(tupleOfNumber[2])
print(dictOfNumber[3])

setOfNumber.add(3)
print(len(setOfNumber))
print(setOfNumber)
"""

for i in setOfNumber:
    print(i)