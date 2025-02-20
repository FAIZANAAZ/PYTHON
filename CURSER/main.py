# ////////////////////////////////////////
# 1) name hmy camelcase me hi likhna he 
# 2) data type lazmi deni he with every variable
  
#   ///////////////  Data Types ////////////////  #  

# 1) int = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2) float = 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1
# 3) str = "hello", f"hello {ye f string he yani ${} iski trha lekin ismy sirf { lgaty hen} }", """ ye multi line string he """
# 4) bool = True, False
# 5) list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 6) tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 7) dictionary = {"name": "John", "age": 20, "city": "New York"}
# 8) set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#   ///////////////  cases ////////////////  #  

# my_name : str = "FAIZA"
# print(len(my_name))# length of the string
# print(my_name.upper())# upper case me convert krega
# print(my_name.lower())# lower case me convert krega
# print(my_name.title())# title case me convert krega
# print(my_name.capitalize())# first letter upper case me convert krega
# print(my_name.count("A"))# count krega ki A kitni bar aayi hai
# print(my_name.find("A"))# find krega ki A konsi index pr aayi hai
# print(my_name.replace("A", "B"))# replace krega ki A ko B se replace krega
# print(my_name.split("A"))# split krega ki A ko B se split krega
# print(my_name.isalpha())# check krega ki name alphabets se bna hai ya nahi agr number howa to false krdyga nhi hoga to true
# print(my_name.isdigit())# check krega ki name digits se bna hai ya nahi agr number howa to true krdyga
# print(my_name.istitle())# check krega ki name title case me hai ya nahi
# print(my_name.isupper())# check krega ki name upper case me hai ya nahi/
# print(my_name.islower())# check krega ki name lower case me hai ya nahi

# ////////////////////// list //////////////////////

# LIST ME HM Data stype nhi dety hm list me ak jesi chizen hi store krengy jesy name to sary name 
# my_list :list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list) #accessing the list
# print(my_list[0])# first element of the list
# print(my_list[-1])# last element of the list
# print(my_list[0:5])# first 5 elements of the list

# //// list methods ////
# my_list.insert(0, 12)# insert krega add kryga index ke hisab sy
# print(my_list)
# my_list.append(11)# append krega last me add krega
# print(my_list)
# my_list.extend([12, 13, 14])# extend krega last me add krega ye ak or list add krta he 
# print(my_list)
# my_list.remove(12)# remove krega
# print(my_list)
# my_list.pop(0)# pop krega last element ko remove krega
# print(my_list)
# my_list.clear()# clear krega list ko clear krega
# print(my_list)
# my_list.sort()# sort krega list ko sort  krega YANI LINE BS LINE union ki trha  phly 1 2 3 4 5 6 7 8 9 10
# print(my_list)
# my_list.reverse()# reverse krega list ko reverse krega yani olta
# print(my_list)
# slice=my_list[0:5]
# print(slice)

# ////////////////////// arthimatic operators //////////////////////

# a : int = 10
# b : int = 20
# print(a + b)# addition
# print(a - b)# subtraction
# print(a * b)# multiplication
# print(a / b)# division
# print(a % b)# modulus
# print(a ** b)# power
# print(a // b)# floor division

# ////////////////////// comparison operators //////////////////////

# a : int = 10
# b : int = 20
# print(a == b)# equal to
# print(a != b)# not equal to
# print(a > b)# greater than
# print(a < b)# less than

# ////////////////////// logical operators //////////////////////

# a : bool = True
# b : bool = False
# print(a and b)# and
# print(a or b)# or
# print(not a)# not


# ////////////////////// membership operators //////////////////////

# a : str = "hello"
# print("h" in a)# in check krega ki h mojood  hai ya nahi true 
# print("h" not in a)# not in  true 

# /////////////////// Input //////////////////////
# ye input leta he user se input lete he sawal pochta he yani
# name : str = input("Enter your name: ")
# print("Hello " + name)

# //////////////// ROUNDING A FLOAT NUMBER ////////////////

# a : float = 3.14159
# print(round(a))# round krega ki 3
# print(round(a, 2))# round krega ki 3.14

# ///////////////// LOOP //////////////////////
# for loop
name_lst= ["Rahul", "Rohan", "Rahul", "Rohan"]
for name in name_lst:  #ismy ak ak krky values ay gi 
    print(name)  
    
for i in range(1, 11): # 1 se 10 tak
   pass # Agar aap ek for loop likh rahe hain lekin abhi uske andar koi logic nahi likhna chahte, toh aap pass use kar sakte hain:

    
for i in enumerate(name_lst): # ye index number ke sath lekr ayga value
    print(i)
    
for i in name_lst: # ye index number se start krega
    print(i)
else : # ye loop complete ho jayega to ye else block chal jayega lekin chlyga lazim
    print("Loop completed")    