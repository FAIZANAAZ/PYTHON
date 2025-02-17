import random
def main():
  random_number = random.randint(1, 5)
  user_answer = int(input("guess the number: "))
  while user_answer != random_number:
      if user_answer > random_number:
          print("Your guess is too high")
      else:
          print("Your guess is too low")
      user_answer = int(input("guess the new number: "))
  print("Your guess is correct")    
if __name__ == '__main__':
    main()