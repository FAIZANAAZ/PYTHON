
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
  user_vote = int(input("Enter your age "))
  if user_vote >= 16 :
      print(f"Your age is {user_vote} you can vote in PETURKSBOUIPO ")
  else:
      print(f"Your age is {user_vote} you can't vote in PETURKSBOUIPO ")
  if user_vote >= 25 :
      print(f"Your age is {user_vote} you can vote in STANLAU ")
  else:
      print(f"Your age is {user_vote} you can't vote in STANLAU ")
  
   
  if user_vote >= 48 : 
      print(f"Your age is {user_vote} you can vote in MAYENGUA ")
  else: 
      print(f"Your age is {user_vote} you can't vote in MAYENGUA ")
      
if __name__ == '__main__':
    main()