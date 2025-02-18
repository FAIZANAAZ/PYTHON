import random
def rang_in(n,high,low):
    if n in range(low,high):
        return True
    else:
        return False
    
def main():
 while True:
     
    n = random.randint(1, 100)
    user_input = int(input("Enter a high number number you can stop enter 0: "))
    user_input2 = int(input("Enter a low number number you can stop enter 0: "))
    
    if user_input == 0 or user_input2 == 0:
        break
    
    if rang_in(n,user_input,user_input2):
        print("The number is in the range")
    else:
        print("The number is not in the range")
    
if __name__ == '__main__':
    main()    