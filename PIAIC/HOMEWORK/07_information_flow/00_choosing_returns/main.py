
ADULT_AGE=18
def adult_func(age:int):
    if age >=ADULT_AGE:
        return True
    return False


def main():
    age = int(input("Enter your age: "))
  
    if adult_func(age):
        print("You are an adult")
    else:
        print("You are not an adult")
   
if __name__ == '__main__':
    main()