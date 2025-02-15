"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# 🎲 Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total_num = die1 + die2
    
    print("\n🎲 Rolling Dice...")  
    print("🎯 Total Number:", total_num, "\n")

def main():
    die2 = 20  
    print("\n🔹 Inside main() - die2 =", die2, "\n")  
    
    roll_dice()
    roll_dice()
    
    print("🔹 Exiting main() - die2 =", die2, "\n")

# 📌 Calling the main function
if __name__ == '__main__':
    main()
