def main():
  for i in range(10):
      
    if IS_ODD(i): # true ayga to if chal jayga wrna else
      print(f"{i} is odd")
    else:
        print(f"{i} is even")
     
def IS_ODD(num):
    return num % 2 != 0 # ye true or false return kryga 

if __name__ == "__main__":
  main()
  