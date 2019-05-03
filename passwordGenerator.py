# JACOB MARLOWE 03-23-2019
# Randomly generated password

# Import statements
import random

# Array declarations
adj = ["Stupid", "Crazy", "Bright", "Vocal",
       "Violent", "Extreme", "Noteworthy", "Stinky",
       "Colorful", "Loud", "Extra", "Mean", "Beautiful",
       "Shiny", "Arrogant", "Intelligent", "Wise",
       "Funny", "Red", "White", "Orange", "Yellow",
       "Green", "Blue", "Brown", "Tall", "Furious", "Fast"]

sub = ["Chicken", "Sludge", "Gangrene", "Marbles",
       "Bananas", "Potato", "Tiger", "Car", "Soda", "Machine",
       "Vanguard", "Alarm", "Jesus", "Yeezy",
       "Zombie", "Elephant", "Doggo", "Dragon", "Bear",
       "Chair", "Moose", "Waterfall", "Clock", "Basement",
       "Clone", "Reactor", "Shark", "Acorn"]

symb = ['!', '?' , '&', '+', '-', '*', '%', '$', '#', '@', '(', ')', '/']

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

adjLength = len(adj)
subLength = len(sub)
symbLength = len(symb)
numLength = len(num)
print("\n----------------------------------------------------------------------")
print("ARRAY SIZES:")
print("----------------------------------------------------------------------")
print("Size of adjective array: "), print(adjLength)
print("Size of subject array: "), print(subLength)
print("Size of symbol array: "), print(symbLength)
print("Size of number array: "), print(numLength)

# Random value generation (password with one adjective, one noun, one symbol, three numbers)
print("\n----------------------------------------------------------------------")
print("PASSWORD WITH SCRIPTED FORMAT:")
print("----------------------------------------------------------------------")
print(adj[random.randint(0,27)]
      +sub[random.randint(0,27)]
      +symb[random.randint(0,12)]
      +num[random.randint(0,9)]
      +num[random.randint(0,9)]
      +num[random.randint(0,9)])

print("\n----------------------------------------------------------------------")
print("RANDOM PASSWORD:")
print("----------------------------------------------------------------------")
i = 1

while i <= 4:
       rand = num[r]
       if rand == 1:
              print("Adj")
       elif rand == 2:
              print ("Sub")
       elif rand == 3:
              print("Symb")
       elif rand == 4:
              print("Num")
       i = i + 1