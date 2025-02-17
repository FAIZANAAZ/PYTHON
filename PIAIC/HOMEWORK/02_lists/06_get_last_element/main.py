
def get_last_element(lst):
    print(lst[-1])

def get_list ():
    user_input = input("Enter any word: ")
    lst = []
    while user_input != "":
         lst.append(user_input)
         user_input = input("Enter any word: ")
    return lst

def main():
   lest= get_list()
   get_last_element(lest)

if __name__ == '__main__':
    main()    