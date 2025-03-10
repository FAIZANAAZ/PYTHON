import random
import string

class password : 
    def __init__(self):
        print("🔐 Welcome to the Password Generator! 🔐")
        self.password_length=int(input("How many passwords do you want to generate?  "))
        self.password_correcter_length = int(input("Enter password length: "))
        
    def game_password(self):
     try:
         if self.password_length <= 0 or self.password_correcter_length <= 0:
            print("❌ Please enter a valid positive number.")
            return

         print("\n📝 Here are your secure passwords:\n")  
         
         for i in range(self.password_length):  
            self.characters = string.ascii_letters + string.digits + string.punctuation # ye bnayga 6r722663hhgfdfjdhg&&#%)
            password = ''.join(random.choice(self.characters)   for _ in range(self.password_correcter_length)) #ye loop 5 bar chlyga  otha kr le ayga  or paswpr me save krdega  
            print(password)
            
            
     except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")        
        
        
password_run = password()
password_run.game_password()        


