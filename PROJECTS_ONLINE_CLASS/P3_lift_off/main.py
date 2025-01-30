def countdown(n):
    print("\n✨********** Welcome to the Space Launch Countdown **********✨")
    
    print("\n🌟 Get ready! The countdown begins now...\n")
                #  start , stop, step
    for i in range(  n,     -1,    -1):  # Reverse countdown from n to 1
        print(f"🌠 {i}...")  

    print("\n LIFTOFF! 🔥")

# 🏁 Program Execution
if __name__ == '__main__':
    user_input = int(input("🔢 Enter a number to start the countdown:"))  # User input
    countdown(user_input)  
