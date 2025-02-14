# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def main():
    print("Welcome to the Square Calculator! 🔢➡️🔲\n")
    
    # User input with emoji
    user_answer = float(input("Enter a number to see its square (e.g., 3, 4.5) ✍️: "))
    
    # Calculating square
    square = user_answer ** 2
    
    # Display result with emojis for fun and clarity
    print(f"\nThe square of {user_answer} is {square} 🔳✨")

if __name__ == '__main__':
    main()
