def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")
    
    # Teeno values ek tuple me pack ho rahi hain aur return ho rahi hain kioky jb hm ak sath 1 sy zada chizon ko
    # , lga kr return krty hen towo ak tuple me save hoti he or return hotin hen (ismy)
    return first_name, last_name, email_address  # (Tuple Packing)

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()  # Function se tuple receive ho raha hai
    print("Received the following user data:", user_data)  # Tuple print ho raha hai

if __name__ == "__main__":
     main()
