
def create_list():
    list=[]
    while True:
        user_input=input("Enter an integer or press enter to stop: ")
        if user_input !="":
            num_list=int(user_input)
            list.append(num_list)
        else:
            break
    return list

def even_numver_list(list):
    for i in list:
        if i % 2 == 0:
            print(i)  
        




def main():
/*************  ✨ Codeium Command ⭐  *************/
/******  db23ceaa-5ebf-4381-a96e-963c91641b12  *******/
    list=create_list()
    even_numver_list(list)
if __name__ == '__main__':
    main()