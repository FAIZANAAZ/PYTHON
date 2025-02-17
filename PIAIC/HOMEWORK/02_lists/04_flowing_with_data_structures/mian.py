def add_three_copies(my_list,message):
    for lists in range(3):
        my_list.append(message)
   
def main():
    message=input("Enter a message: ")
    my_list=[]
    print("My list before function call:",my_list)
    add_three_copies(my_list,message)
    print("My list after function call:",my_list)
if __name__ == "__main__":
    main()       