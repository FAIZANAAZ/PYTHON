import random

NUM_ROUNDS = 10

def main():
    score = 0  # Score initialize
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    for round in range(1, NUM_ROUNDS + 1):
        random_number = random.randint(1, 100)  # Number range fixed
        print(f"Round {round}")

        # Validate user input (to avoid crash)
        try:
            user_num = int(input("Enter your number (1-100): "))
            if user_num < 1 or user_num > 100:
                print("Invalid number! Please enter a number between 1 and 100.")
                continue  # Skip this round if input is invalid
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  

        user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        if user_num > random_number:
            if user_guess == "higher":
                print(f"You were right! The computer's number was {random_number}")
                score += 1
            else:
                print(f"You were wrong! The computer's number was {random_number}")

        elif user_num < random_number:
            if user_guess == "lower":
                print(f"You were right! The computer's number was {random_number}")
                score += 1
            else:
                print(f"You were wrong! The computer's number was {random_number}")

        else:  # If both numbers are equal
            print(f"Your number and the computer's number are the same! ({random_number}) No points awarded.")

        print(f"Your score is: {score}\n")

    # Final Result
    if score >= 7:
        print(f"🎉 You won the game! Your final score is {score}.")
    else:
        print(f"😞 You lost the game! Your final score is {score}.")

if __name__ == "__main__":
    main()
