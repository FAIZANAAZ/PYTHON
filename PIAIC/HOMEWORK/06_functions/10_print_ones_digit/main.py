
def count_digits(digit):
 
    print("The ones digit is",digit%10)
    # isy yehoga ke jo last digit hoga wahi print hoga jesy 799786 print 6

def main():
  usr_input = int(input("Enter a number: "))
  count_digits(usr_input)

if __name__ == '__main__':
    main()