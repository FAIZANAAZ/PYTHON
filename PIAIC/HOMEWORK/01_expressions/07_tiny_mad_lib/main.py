

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

Sentence_Adjective = "I had such a **{adjective}** day today, and I still can't decide if it was good or bad!"
Sentence_Noun = "There was a **{noun}** sitting in front of my house, and I swear it looked like it wanted to have a conversation with me!"
Sentence_Verb = "I woke up this morning thinking I should **{verb}**, but then I decided to stop thinking!"

def main():
    print("\n" + "*" * 50)
    print("✨ WELCOME TO THE CRAZY MAD LIBS GAME ✨")
    print("*" * 50 + "\n")

    # Get user input and print the funny sentences
    adjective = input("📝 Please type an **adjective** and press enter: ")
    print("\n" + "-" * 50)
    print(Sentence_Adjective.format(adjective=adjective) + " 😆")
    print("-" * 50 + "\n")

    noun = input("📝 Please type a **noun** and press enter: ")
    print("\n" + "-" * 50)
    print(Sentence_Noun.format(noun=noun) + " 🤣")
    print("-" * 50 + "\n")

    verb = input("📝 Please type a **verb** and press enter: ")
    print("\n" + "-" * 50)
    print(Sentence_Verb.format(verb=verb) + " 😂")
    print("-" * 50 + "\n")

    print("🎉 Thank you for playing! Try again with different words! 🎉")

if __name__ == "__main__":
    main()
