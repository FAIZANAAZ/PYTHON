# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5


def main():
    print("\n*********Welcome to the Triangle Perimeter Calculator! 🛠️*********\n")
    
    # User input with emojis
    one_side = float(input("Enter the length of the first side  ➡️: "))
    second_side = float(input("Enter the length of the second side ➡️: "))
    third_side = float(input("Enter the length of the third side  ➡️: "))
    
    # Calculating perimeter
    perimeter_of_triangle = one_side + second_side + third_side
    
    # Clear output with formatted message and emojis
    print(f"\nThe perimeter of the triangle with sides {one_side}, {second_side}, and {third_side} is: {perimeter_of_triangle} 🟩🟦🟧")

if __name__ == '__main__':
    main()
