import random


class rock_paper_scissors:
    def __init__(self):
        self.COMPUTER_selection = random.choice(['rock', 'paper', 'scissors'])
        self.USER_selection = input('Enter your selection: ')
        self.steps=0
        
    def win_loss(self):
        while True:
                

           
                if self.COMPUTER_selection == self.USER_selection:
                    print("It's a tie")
                elif self.COMPUTER_selection == 'rock' and self.USER_selection == 'paper':
                    print("You win")
                elif self.COMPUTER_selection == 'rock' and self.USER_selection == 'scissors':
                    print("You lose")
                elif self.COMPUTER_selection == 'paper' and self.USER_selection == 'scissors':
                    print("You win")
                elif self.COMPUTER_selection == 'paper' and self.USER_selection == 'rock':
                    print("You lose")
                elif self.COMPUTER_selection == 'scissors' and self.USER_selection == 'rock':
                    print("You win")
                elif self.COMPUTER_selection == 'scissors' and self.USER_selection == 'paper':
                    print("You lose")   
                else:
                    print("Invalid selection")
                
                self.steps += 1
                self.user_input = input('Do you want to play again? (yes/no): ')
                if self.user_input.lower() == 'yes':
                    rock_paper_scissors()
                    continue
            
                else:
                  print('Goodbye')  
                  print('You played', self.steps, 'times')
                  break
            
game=rock_paper_scissors()
game.win_loss()
            
 #second way to do it


# class RockPaperScissors:
#     def __init__(self):
#         self.steps = 0  # Track number of games played

#     def play_game(self):
#         while True:
#             self.COMPUTER_selection = random.choice(['rock', 'paper', 'scissors'])
#             self.USER_selection = input('Enter your selection (rock/paper/scissors): ').lower()

#             if self.USER_selection not in ['rock', 'paper', 'scissors']:
#                 print("Invalid selection, try again.")
#                 continue

#             print(f"Computer chose: {self.COMPUTER_selection}")

#             if self.COMPUTER_selection == self.USER_selection:
#                 print("It's a tie!")
#             elif (self.COMPUTER_selection == 'rock' and self.USER_selection == 'paper') or \
#                  (self.COMPUTER_selection == 'paper' and self.USER_selection == 'scissors') or \
#                  (self.COMPUTER_selection == 'scissors' and self.USER_selection == 'rock'):
#                 print("You win!")
#             else:
#                 print("You lose!")

#             self.steps += 1
#             play_again = input('Do you want to play again? (yes/no): ').lower()
#             if play_again != 'yes':
#                 print(f'Goodbye! You played {self.steps} times.')
#                 break

# # Start the game
# game = RockPaperScissors()
# game.play_game()
 