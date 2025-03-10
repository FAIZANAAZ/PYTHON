

import time

class countdown_timer:
    def __init__(self):
        self.user_input = int(input("Enter the time in seconds: "))
        
    def start_timer(self):
        for i in range(self.user_input, 0, -1):
            print(i)
            time.sleep(1)    
        print("Time's up!")

run= countdown_timer()
run.start_timer()
                