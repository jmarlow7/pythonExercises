# JACOB MARLOWE 03-23-2019
# Randomly generated password

# Import statements
import random

# Array declarations
adj = ["Stupid", "Crazy", "Bright", "Vocal", "Violent", "Extreme", "Noteworthy", "Stinky", "Colorful", "Loud", "Extra", "Mean", "Beautiful", "Shiny",
       "Arrogant", "Intelligent", "Wise", "Funny", "Red", "White", "Orange", "Yellow", "Green", "Blue", "Brown", "Tall", "Furious", "Fast"]
sub = ["Chicken", "Sludge", "Gangrene", "Marbles", "Bananas", "Potato", "Tiger", "Car", "Soda", "Machine", "Vanguard", "Alarm", "Jesus", "Yeezy",
       "Zombie", "Elephant", "Doggo", "Dragon", "Bear", "Chair", "Moose", "Waterfall", "Clock", "Basement", "Clone", "Reactor", "Shark", "Acorn"]
symb = ['!', '?' , '&', '+', '-', '*', '%', '$', '#', '@', '(', ')', '/']
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Random value generation (password with one adjective, one noun, one symbol, three numbers)
print(adj[random.randint(0,28)]
      +sub[random.randint(0,28)]
      +symb[random.randint(0,13)]
      +num[random.randint(0,9)]
      +num[random.randint(0,9)]
      +num[random.randint(0,9)])

