def number_list():
    lst = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            num_convert = int(user_input)
            lst.append(num_convert)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return lst

def dictionary(user_list):
    dict = {}
    for num in user_list:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict

def print_dict(dict):
    for num, count in dict.items():
        # loop ko is trha likhny sy num me keys or count me values aygi oe dict.items sy wo hr items ko alag krdega ak likht me rakhdega jesy [(5, 2), (3, 1), (2, 1)] kioky itms array ka metod he
        
        print(f"{num} appears {count} times.")

def main():
    user_list = number_list()
    dict = dictionary(user_list)
    print_dict(dict)

if __name__ == '__main__':
    main()