fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]

# ✅ Access Element Function
def access_element(listed, index):
    if 0 <= index < len(listed):
        return f"Element at index {index}: {listed[index]}"
    else:
        return "Index out of range!"

# ✅ Modify Element Function
def list_index(listed, index, value):
    if 0 <= index < len(listed):
        listed[index] = value
        return listed
    else:
        return "Index out of range"

# ✅ Slice List Function
def slice_list(listed, start, end):  
    if start < end:
        return listed[start:end]
    else:
        return "Invalid input"

# ✅ Main Game Logic
def index_game():
    print("Welcome to the Index Game!")
    print("Choose an operation:")
    print("1. Access an element")
    print("2. Modify an element")
    print("3. Slice the list")

    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        user_index = int(input("Enter the index to access: "))
        print(access_element(fruit_list, user_index))
            
    elif choice == "2":
        user_index = int(input("Enter the index to modify: "))
        user_value = input("Enter the new value: ")
        print(list_index(fruit_list, user_index, user_value))
        
    elif choice == "3":
        start_index = int(input("Enter the start index: "))
        end_index = int(input("Enter the end index: "))
        print(slice_list(fruit_list, start_index, end_index))
        
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

def main():
    index_game()

if __name__ == "__main__":
    main()
