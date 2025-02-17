def read_phone_numbers():
    phone_numbers = {}
    while True:
        name = input("Enter name  ")
        if name == "":
            break
        number = input("Enter phone number  ")
        phone_numbers[name] = number
    return phone_numbers
    
def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))
        
def find_number (phonebook):  
    name = input("Enter name to find phone number  ")
    if name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))
    else:
        print("Name not found")
        

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    find_number(phonebook)
 
if __name__ == '__main__':
    main()