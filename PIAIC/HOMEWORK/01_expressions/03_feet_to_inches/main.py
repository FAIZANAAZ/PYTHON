# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_IN_FOOT: int = 12 
def main():
   feet=float(input("Enter the length in feet: "))
   inch=feet*INCHES_IN_FOOT
   print(f"{feet} feet is equal to {inch} inches")
   
if __name__ == '__main__':
    main()