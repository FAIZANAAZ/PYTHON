
def make_sentence(word, part_of_speech):
    
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else :
        print("invalid number")        
        
def main():
   word = input("Enter a word: ")
   part_of_speech = int(input("Enter a number (0, 1, 2)"))
   sentence=make_sentence(word, part_of_speech)
   return sentence
if __name__ == '__main__':
    main()        