from hashlib import sha256  # SHA256 hashing ke liye module import kar rahe hain

def login(email, stored_logins, password_to_check):
    # Yeh function check karega ke user ka entered password correct hai ya nahi
    # Database me mojood hashed password ko entered password ke hash se compare karega
    
    if stored_logins[email] == hash_password(password_to_check):  # Agar dono hash match karein
        return True  # Login successful
    
    return False  # Login failed

# Yeh function password ko hash (encrypt) karega taake secure rahe
def hash_password(password):
    return sha256(password.encode()).hexdigest()  # Password ko SHA256 me convert kar rahe hain


def main():
    # Yeh ek dictionary hai jo emails ko unke hashed passwords se map kar rahi hai
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password = "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # password = "karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password = "123!456?789"
    }
    
    # Login test cases
    print(login("example@gmail.com", stored_logins, "word"))  # ❌ Incorrect password
    print(login("example@gmail.com", stored_logins, "password"))  # ✅ Correct password
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # ❌ Case-sensitive incorrect password
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # ✅ Correct password
    
    print(login("student@stanford.edu", stored_logins, "password"))  # ❌ Incorrect password
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # ✅ Correct password


if __name__ == '__main__':
    main()  # Program start hone ka main point