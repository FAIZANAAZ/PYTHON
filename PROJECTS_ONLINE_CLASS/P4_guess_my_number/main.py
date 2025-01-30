import random
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
# import random  # Random module import karo

import random

def guess_number():
    # Welcome message
    print("\n" + "🟢🟢🟢 Welcome to the 'Guess the Number' Game! 🟢🟢🟢".center(50))
    print("\n" + "🎲 Let's have some fun! 🎲".center(50))
    print("\n" + "💥 Try your luck and guess the number between 1 and 99! 💥".center(50))
    print("\n" + "🌟🌟🌟" + "\n")


    # Random number generation
    number_to_guess = random.randint(1, 99)  # 1 se 99 tak random number
    user_guess = int(input("🔢 Guess a number between 1 and 99: "))  # Ye bs ek hi bar chalayga 

    while user_guess != number_to_guess:
      try: 
         
         if user_guess > number_to_guess:
            print("📉 Your guess is too high. Try again!")
         elif user_guess=="":
            print("📉 Your guess is too high. Try again!")   
         else:
            print("📈 Your guess is too low. Try again!")

         user_guess = int(input("🔄 Enter a new guess: "))  # Naya guess lena
      except ValueError:
            print("❌ Invalid input! Please enter a valid number.")   

    # Congratulatory message when the number is guessed correctly
    print(f"\n🎉 Congrats! You guessed it right 🎯 The number was {number_to_guess}!")

# 🏁 Run Program
if __name__ == '__main__':
 guess_number()

