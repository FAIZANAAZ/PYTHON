

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# ////////////////////////////////////

# //          START OF CODE          //
def main():
    print("🔢 Let's add two numbers! 😊")
    
    first_number = int(input("👉 Enter the first number: "))
    second_number = int(input("👉 Enter the second number: "))

    sum_of_numbers = first_number + second_number
    print(f"🎉 Woohoo! The sum of {first_number} and {second_number} is {sum_of_numbers} 🚀")

if __name__ == '__main__':
    main()
