

def main():
  
  user_year=int(input("Enter a year: "))
#   jb bhi hmy ye cheq krna ho ke kis number sy devisible he ya nhi to hm % ye lga kr krty hen jesy num % 2 ===0yani 
# ye cheq ho rha he ke num 2 sy devide ho skta he ya nhi
  if user_year % 4 == 0:
    if user_year % 100 == 0:
      if user_year % 400 == 0:
          print("This is a leap year")
      else :
          print("This is not a leap year")   
    else:
       print("This is not a leap year")
  else:
          print("This is  a leap year")



if __name__ == '__main__':
    main()