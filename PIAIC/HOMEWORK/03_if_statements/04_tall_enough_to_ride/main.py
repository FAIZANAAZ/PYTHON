height = 6  # Minimum height set kar liya 6 feet

def main():
    while True:  # Loop chalega jab tak user input deta rahe
        user_height = input("Enter your height: ")
        
        # Agar user ne khaali input diya, to loop ko break karo
        if user_height == "":
            break
        
        user_height = int(user_height)  # Input ko integer me convert karo
        
        # Height ko check karo
        if user_height >= height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
