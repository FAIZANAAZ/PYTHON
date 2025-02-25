import random

class GuessTheNumber:
    def __init__(self):
        self.computer_guess = random.randint(1, 10)
        self.number_of_guesses = 0
        self.user_guess = None  # Initial value set kar di
        
    def guess(self):
        while True:
            try:
                self.user_guess = int(input("Enter your guess: "))  # Ensure user input is an integer
                
                if self.user_guess == self.computer_guess:
                    print("You win!")
                    print(f"Number of guesses: {self.number_of_guesses}")
                    break
                elif self.user_guess > self.computer_guess:
                    print("Too high!")
                else:
                    print("Too low!")
                
                self.number_of_guesses += 1  # Guess count badhao
                
            except ValueError:
                print("Invalid input! Please enter a number.")

# Game start karo
game = GuessTheNumber()
game.guess()
