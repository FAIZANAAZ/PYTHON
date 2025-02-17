def main():
 message:str = "I am capable of doing anything I put my mind to"  
 user_sentence:str = input("Enter a sentence: ")
 while message != user_sentence:
     print("Hmmm That was not the affirmation. Try again!")
     user_sentence = input("Enter a sentence: ")
 print("That's right!")
if __name__ == '__main__':
    main()