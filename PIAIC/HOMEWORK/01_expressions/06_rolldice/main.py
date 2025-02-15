import random

# Simulate rolling two dice, and prints results of each roll as well as the total.

side_dice=6
def main():
  dice1=random.randint(1,side_dice)
  dice2=random.randint(1,side_dice)
  total=dice1+dice2
  print("Dice have", side_dice, "sides each.")
  print("First die:", dice1)
  print("Second die:", dice2)
  print("Total of two dice:", total)
  
if __name__ == '__main__':
    main()