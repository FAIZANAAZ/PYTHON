
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)



import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print("\n✨🎲 Welcome to the Random Number Generator! 🎲✨\n")
    print("🎯 Generating 10 Unique Numbers Between 1 and 100... 🎯\n")
    print("🌟🌟🌟🌟🌟\n")

    unique_numbers = []  # ✅ Empty list to store unique numbers

    while len(unique_numbers) < N_NUMBERS:  # ✅ Jab tak 10 unique numbers na mil jayen
        value = random.randint(MIN_VALUE, MAX_VALUE)

        if value in unique_numbers:  # ✅ Agar number pehle se list me hai to skip kar do
            continue
        else:
            unique_numbers.append(value)  # ✅ Unique number list me add karo

    # ✅ Har number ko **styled output** ke saath print karne ka tareeqa
    for idx, num in enumerate(unique_numbers, start=1):
        print(f"⭐ Number {idx}: {num}")

    print("\n ✅ S🎉 Done! All Numbers Are Unique! ✅ 🎉\n")

if __name__ == '__main__':
    main()
