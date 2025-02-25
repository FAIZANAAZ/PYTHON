class Story:
    def __init__(self):
        self.verb: str = input("Enter a verb: ")
        self.noun: str = input("Enter a noun: ")
        self.adjective: str = input("Enter an adjective: ")
        self.adverb: str = input("Enter an adverb: ")
        self.place: str = input("Enter a place: ")
        self.number: float = float(input("Enter a number: "))  # Number ko float me convert kiya
        self.emotions: str = input("Enter an emotion: ")
        self.food: str = input("Enter a food: ")

    def story_func(self): 
        print(f"""
        One day, a {self.adjective} {self.noun} went to the {self.place}.  
        There, it saw {self.number} people who were {self.verb}.  
        Seeing this, it felt very {self.emotions}.  
        Then, it ate some {self.food} and {self.adverb} went back home!
        """)

# Object create karna
funny_story = Story()  
funny_story.story_func()
