

def list_get(lst:int):
    print(f"your input is bigger than {lst}")
    
def main():
    lest=[]
    value = input("Enter a value: ")
    while value != "":
       lst = input("Enter a value: ")
       lest.append(lst)
    list_get(lst)
if __name__ == '__main__':
    main()   

 