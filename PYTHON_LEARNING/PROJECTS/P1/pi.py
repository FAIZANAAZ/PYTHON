# https://github.com/panaversity/learn-modern-ai-python/tree/main/PROJECTS/online_class_projects  
# yha hen sary projects 
#1) project documents  https://github.com/panaversity/learn-modern-ai-python/blob/main/PROJECTS/online_class_projects/01_basics/00_joke_bot.md

# name ******Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.****

joke ="Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
Sorry ="I can only tell jokes"

def bot():
    
        print("Hello, I am a joke bot")
        while True: 
            user_input = input("what you want ? ")
            if "joke" in user_input:
                print(joke)
            else: 
                print(Sorry)
  

bot()  
