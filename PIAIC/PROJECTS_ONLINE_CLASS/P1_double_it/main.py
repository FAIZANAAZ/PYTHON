import time  # Delay effect ke liye

def main():
    print("\n" + "="*40)
    print("🎲✨ WELCOME TO THE GAME ✨🎲")
    print("="*40 + "\n")
    
    user_input = int(input("👉 Choose a number: "))  #sbsy phly ak input bnaya taky yha user input me number dy OR INT ISI LIYE LGAYA HE kioky input me hmesha string ki form me hi at he
    
    current_value = user_input  # hmny curenvalue me number ko store krdiya input ke taky hm isko multiplykrwa sken

    print("\n🚀 Starting the game...\n")
    time.sleep(1)  # Thoda delay taa ke better effect aaye
    
    while current_value < 100:  # Jab tak value 100 se choti hai, loop chalta rahega
        next_value = current_value * 2 
        
# jo bhi input me value aygi wo current me save hogi or * hokr double ho jaygi ak bar or wahi value save hofi next me wohmny isi liye bnya he taky hm ak to print e dikhanahe or dosra * ki hoi value ko bhi store krwana he taky osko bad me hm current value ko update kr sken kioky agr current value update hi hogi to wo wapas oper jaygi jb loop chalyga or curent me wapas wahi value set hogi jo input me phli bar ai thi
        
        print(f"🎲 {current_value}  ➡️  {next_value}")  # Behtareen format aur emoji
        
        time.sleep(0.5)  # Thodi der ka delay taa ke smooth lage
        current_value = next_value  # Current value ko update karna zaroori hai

    print("\n🎉 CONGRATULATIONS! 🎉")
    print("🚀 You have reached 100 or more! 🎯\n")

if __name__ == '__main__':
    main()
    
# Agar hum if __name__ == '__main__': nahi likhte, to:

# Jab bhi file import hoti hai, uska main() function bhi automatic chal jata hai! 
# Humne khud nahi chalaya, phir bhi run ho jata hai.

