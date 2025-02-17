
def shorten(lst):
    while len(lst) > 3:  # Jab tak list ki length 3 se zyada hai
        removed_element = lst.pop()  # Last element remove karo
        print(removed_element)  # Print karo

def main():
    lst = [1, 2, 3, 4, 5, 6]  
    shorten(lst)  # Function call
    print("Final List:", lst)  # Bacha hua list print karne ke liye

if __name__ == '__main__':
    main()
