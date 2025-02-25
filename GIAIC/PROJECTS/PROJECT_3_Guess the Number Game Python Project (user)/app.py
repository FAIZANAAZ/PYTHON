import random

class GuessingGame:
    def __init__(self):
        self.steps = 0  # Step counter
        self.computer_number = random.randint(1, 100)  # Computer ek number choose karega

    def guess(self):
        try:
            while True:
                user_guess = int(input("Guess a number between 1 and 100: "))
                user_response = input("Is the COMPUTER's number higher or lower? (Type 'high' or 'low'): ").lower()

                self.steps += 1  # Step count badh rahi hai

                if user_guess > self.computer_number and user_response == "low":
                    print(f"✅ Correct! The computer's number is {self.computer_number}")
                    break
                elif user_guess < self.computer_number and user_response == "high":
                    print(f"✅ Correct! The computer's number is {self.computer_number}")
                    break
                else:
                    print("❌ Incorrect guess. Try again!")

        except ValueError:
            print("❌ Please enter a valid number!")

        print(f"🎉 You found the answer in {self.steps} steps!")

game1 = GuessingGame()
game1.guess()
