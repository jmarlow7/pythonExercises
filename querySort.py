# JACOB MARLOWE 03-23-2019
# Randomly generated numbers are placed into a list six strings. These strings are then manipulated.

# Import statements & declarations
import string
import sys
import random

numPool = string.digits
data = bool(input("\nHello! Would you like a free number? (Yes or No): "))

# Exception handling
while True:

    numList = []

    # 5 digit # x1
    print("\nOne random 5 digit number:")
    numRand = str(''.join(random.choice(numPool) for _ in range(5)))
    numList.append(numRand)
    print(numList)
    print("\n")

    # 5 digit # x6
    print("Six randomly generated 5 digit numbers:")
    for i in range(0, 5):
        numRand = str(''.join(random.choice(numPool) for _ in range(5)))
        numList.append(numRand)
        i = i + 1
    print(numList)
    print("\n")

    # #'s in ascending order
    print("The same 6 numbers in ascending order:")
    numList.sort()
    print(numList)
    print("\n")

    # #'s in descending order
    print("The same 6 numbers in descending order:")
    numList.sort(reverse = True)
    print(numList)
    print("\n")

    data = bool(input("\nWant to do it again? (Yes or No): "))
    if data != True:
        break
    else:
        continue

#If answered False or hit prev. break statement:
print("Goodbye!")
sys.exit()