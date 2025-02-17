def get_fruits_list():
    
    fruits_list_item = {}
    while True :
       
       user_ask = input("What do you want to buy? ") 
       if user_ask == "":
            break
       fruit_quantity = float(input("How many do you want to buy? "))
       fruits_list_item[user_ask] = fruit_quantity
    return fruits_list_item
       
def total_price(fruits_list):
    total_price = 0
    for fruit ,count in fruits_list.items():
        total_price += count * 2
    return total_price

def main():
    fruits_list = get_fruits_list()
    print(fruits_list)
    print("Total price: ", total_price(fruits_list),"$")

if __name__ == '__main__':
    main()    
        
        
      