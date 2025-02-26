import random

class HangmanGame:
    def __init__(self):
        self.attempts = 6
        self.score = 0
        self.right_answer = 0
        self.wrong_answer = 0
        self.correct_letters = set()  # ✅ Sahi guessed letters track karne ke liye

        print("🎭 Welcome to Hangman! Try to guess the word before you run out of attempts. 🎭")
        self.random_word: str = random.choice(["python", "developer", "hangman", "computer", "artificial", "intelligence"])
        print(f"💡 The word has {len(self.random_word)} letters. Attempts left: {self.attempts}")

    def start_game(self):
        while self.wrong_answer < self.attempts:  # ✅ Jab tak attempts khatam na ho jayein
            self.user_guess = input("Guess a letter: ").lower()

            if len(self.user_guess) != 1 or not self.user_guess.isalpha():
                print("⚠️ Please enter a **single letter** only!")
                continue  # ✅ Dubara input maangne ke liye

            if self.user_guess in self.correct_letters:
                print("⚠️ You already guessed that letter!")
                continue

            if self.user_guess in self.random_word:
                print("🎉 You guessed it right! 🎉")
                self.correct_letters.add(self.user_guess)
                self.right_answer += 1
                self.score += 1
            else:
                print("❌ Wrong guess! Try again. ❌")
                self.wrong_answer += 1
                self.score -= 1

            print(f"💡 Your current score: {self.score} | Attempts left: {self.attempts - self.wrong_answer}")

            if set(self.random_word) <= self.correct_letters:
                print(f"🎉 Congratulations! You guessed the word '{self.random_word}' 🎉")
                break  # ✅ Agar user jeet gaya to game end ho jaye

        if self.wrong_answer == self.attempts:
            print(f"❌ Game Over! The correct word was '{self.random_word}'. ❌")
        print(f"💡 Your final score: {self.score}")

game_call = HangmanGame()
game_call.start_game()
import random

class HangmanGame:
    def __init__(self):
        self.attempts = 6
        self.score = 0
        self.right_answer = 0
        self.wrong_answer = 0
        self.correct_letters = set()  # ✅ Sahi guessed letters track karne ke liye

        print("🎭 Welcome to Hangman! Try to guess the word before you run out of attempts. 🎭")
        self.random_word: str = random.choice(["python", "developer", "hangman", "computer", "artificial", "intelligence"])
        print(f"💡 The word has {len(self.random_word)} letters. Attempts left: {self.attempts}")

    def start_game(self):
        while self.wrong_answer < self.attempts:  # ✅ Jab tak attempts khatam na ho jayein
            self.user_guess = input("Guess a letter: ").lower()

            if len(self.user_guess) != 1 or not self.user_guess.isalpha():
                #  Agar user koi number ya symbol likhta hai, to mana karna hai  ya gr 1 sy zada letter likhta hai
                print("⚠️ Please enter a **single letter** only!")
                continue  # ✅ Dubara input maangne ke liye

            if self.user_guess in self.correct_letters:
                print("⚠️ You already guessed that letter!")
                continue

            if self.user_guess in self.random_word:
                print("🎉 You guessed it right! 🎉")
                self.correct_letters.add(self.user_guess)
                self.right_answer += 1
                self.score += 1
            else:
                print("❌ Wrong guess! Try again. ❌")
                self.wrong_answer += 1
                

            print(f"💡 Your current score: {self.score} | Attempts left: {self.attempts - self.wrong_answer}")

            if set(self.random_word) <= self.correct_letters:
                print(f"🎉 Congratulations! You guessed the word '{self.random_word}' 🎉")
                break  # ✅ Agar user jeet gaya to game end ho jaye

        if self.wrong_answer == self.attempts:
            print(f"❌ Game Over! The correct word was '{self.random_word}'. ❌")
        print(f"💡 Your final score: {self.score}")

game_call = HangmanGame()
game_call.start_game()
