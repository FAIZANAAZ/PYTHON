# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

def main():
    # Individuals ki umar calculate karna
    Anton: int = 21
    Beth: int = Anton + 6
    Chen: int = Beth + 20
    Drew: int = Chen + Anton
    Ethan: int = Chen

    # Decorative Output
    print("\n" + "*" * 30)
    print(" 🎂 AGE CALCULATOR 📅 ".center(30))
    print("*" * 30 + "\n")

    # Ages Display
    print(f"👦 Anton is {Anton} years old")
    print(f"👧 Beth is {Beth} years old")
    print(f"👨 Chen is {Chen} years old")
    print(f"🧑 Drew is {Drew} years old")
    print(f"🧑 Ethan is {Ethan} years old")

    # Ending Line
    print("\n" + "*" * 30)

# Program Execution
if __name__ == '__main__':
    main()
