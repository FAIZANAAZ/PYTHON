# # ////////////////////////////////////////
# # 1) name hmy camelcase me hi likhna he 
# # 2) data type lazmi deni he with every variable
  
# #   ///////////////  Data Types ////////////////  #  

# # 1) int = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# # 2) float = 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1
# # 3) str = "hello", f"hello {ye f string he yani ${} iski trha lekin ismy sirf { lgaty hen} }", """ ye multi line string he """
# # 4) bool = True, False
# # 5) list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 6) tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # 7) dictionary = {"name": "John", "age": 20, "city": "New York"}
# # 8) set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# #   ///////////////  cases ////////////////  #  

# # my_name : str = "FAIZA"
# # print(len(my_name))# length of the string
# # print(my_name.upper())# upper case me convert krega
# # print(my_name.lower())# lower case me convert krega
# # print(my_name.title())# title case me convert krega
# # print(my_name.capitalize())# first letter upper case me convert krega
# # print(my_name.count("A"))# count krega ki A kitni bar aayi hai
# # print(my_name.find("A"))# find krega ki A konsi index pr aayi hai
# # print(my_name.replace("A", "B"))# replace krega ki A ko B se replace krega
# # print(my_name.split("A"))# split krega ki A ko B se split krega
# # print(my_name.isalpha())# check krega ki name alphabets se bna hai ya nahi agr number howa to false krdyga nhi hoga to true
# # print(my_name.isdigit())# check krega ki name digits se bna hai ya nahi agr number howa to true krdyga
# # print(my_name.istitle())# check krega ki name title case me hai ya nahi
# # print(my_name.isupper())# check krega ki name upper case me hai ya nahi/
# # print(my_name.islower())# check krega ki name lower case me hai ya nahi

# # ////////////////////// list //////////////////////

# # LIST ME HM Data stype nhi dety hm list me ak jesi chizen hi store krengy jesy name to sary name 
# # my_list :list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(my_list) #accessing the list
# # print(my_list[0])# first element of the list
# # print(my_list[-1])# last element of the list
# # print(my_list[0:5])# first 5 elements of the list

# # //// list methods ////
# # my_list.insert(0, 12)# insert krega add kryga index ke hisab sy
# # print(my_list)
# # my_list.append(11)# append krega last me add krega
# # print(my_list)
# # my_list.extend([12, 13, 14])# extend krega last me add krega ye ak or list add krta he 
# # print(my_list)
# # my_list.remove(12)# remove krega
# # print(my_list)
# # my_list.pop(0)# pop krega last element ko remove krega
# # print(my_list)
# # my_list.clear()# clear krega list ko clear krega
# # print(my_list)
# # my_list.sort()# sort krega list ko sort  krega YANI LINE BS LINE union ki trha  phly 1 2 3 4 5 6 7 8 9 10
# # print(my_list)
# # my_list.reverse()# reverse krega list ko reverse krega yani olta
# # print(my_list)
# # slice=my_list[0:5]
# # print(slice)

# # ////////////////////// arthimatic operators //////////////////////

# # a : int = 10
# # b : int = 20
# # print(a + b)# addition
# # print(a - b)# subtraction
# # print(a * b)# multiplication
# # print(a / b)# division
# # print(a % b)# modulus
# # print(a ** b)# power
# # print(a // b)# floor division

# # ////////////////////// comparison operators //////////////////////

# # a : int = 10
# # b : int = 20
# # print(a == b)# equal to
# # print(a != b)# not equal to
# # print(a > b)# greater than
# # print(a < b)# less than

# # ////////////////////// logical operators //////////////////////

# # a : bool = True
# # b : bool = False
# # print(a and b)# and
# # print(a or b)# or
# # print(not a)# not


# # ////////////////////// membership operators //////////////////////

# # a : str = "hello"
# # print("h" in a)# in check krega ki h mojood  hai ya nahi true 
# # print("h" not in a)# not in  true 

# # /////////////////// Input //////////////////////
# # ye input leta he user se input lete he sawal pochta he yani
# # name : str = input("Enter your name: ")
# # print("Hello " + name)

# # //////////////// ROUNDING A FLOAT NUMBER ////////////////

# # a : float = 3.14159
# # print(round(a))# round krega ki 3
# # print(round(a, 2))# round krega ki 3.14

# # ///////////////// LOOP //////////////////////
# # # for loop
# # name_lst= ["alina", "Rohan", "Rahul", "sania"]
# # for name in name_lst:  #ismy ak ak krky values ay gi 
# #     print(name)  
    
# # for i in range(1, 11): # 1 se 10 tak
# #    pass # Agar aap ek for loop likh rahe hain lekin abhi uske andar koi logic nahi likhna chahte, toh aap pass use kar sakte hain:

    
# # for i in enumerate(name_lst): # ye index number ke sath lekr ayga value
# #     if i == "sania":
# #         break # ye loop break krega
# #     print(i)
    
# # for i in name_lst: # ye index number se start krega
# #     print(i)
# # else : # ye loop complete ho jayega to ye else block chal jayega lekin chlyga lazim
# #     print("Loop completed") 
       
# # for index, name in enumerate(name_lst): # ye index number se start krega
# #     print(index, name)  
# # ////////////////////// while loop //////////////////////
# #while loop 
# # count =1 
# # while count <= 10:
# #     print(count)
# #     count += 1
    
#  # //////////////////////  TUPLE //////////////////////
# # tuple is a collection of items that are ordered and immutable
# # touple_list =("alina", "sania", "Rohan", "Rahul")
# # ye change nhi hota fix value store krega imutible
# # touple_list[0] = "DUA" # ye error dekhega or add remove op bhi nhi hota 
# # print(touple_list)


# # //////////////////////  SET //////////////////////
# # set is a collection of items that are unordered and immutable
# # ye curly brases me hoga
# # ye agypichy ho jata he iski squence ni hoti
# # ye uniq hota he yani duplicate value store nhi hoti agr oi name duplicate he towoak rakhyga ak nkaldega 
# # set_list={"faiza","numra","rabia","dua"}
# # set_list.add("faiza") # ye add krega
# # print(set_list)
# # set_list.remove("faiza") # ye remove krega
# # print(set_list)
# # set_list.pop() # ye remove krega last element ko
# # print(set_list)
# # set_list.clear() # ye clear krega set ko
# # print(set_list)
# # set_list.discard("faiza") # ye remove krega faiza ko agr faiza nhi mikyga to error bhi nhi dega bs wesy hi run hoga
# # print(set_list)
# # set_list.pop() # ye remove krega last element ko
# # print(set_list)
# # set_list.remove("kghj") # ye error deg ke kghj tohe hi nhi jbky  discard error nhi dega
# # print(set_list)

# # my_list :list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # uniq_list =list(set(my_list))
# # print(uniq_list)

# # ismy hmny list kophly set me kiya taky wo osko uniq krde or phr osko list me convert krde taky hm uniq list ko use krsky

# # ////////////////////// DICTIONARY   //////////////////////

# # dictionary is a collection of key-value pairs
# # dictionary is mutable
# # my_dict: dict[str,any]= {
# #     "name": "John",
# #     "age": 20, 
#     # "city": "New York"}

# # my_dict["name"] = "Doe" # update krega
# # my_dict["work"] = "student" # isko ye mily ga nhi to ye add krdega khd
# # # dics me keys hmesha "" me hoti hen or values kisi bhi data type me ho skti hen
# # print(my_dict)
# # # print(my_dict["name"])# accessing the value by key

# # del  my_dict["age"] # ye remove krega yeerror bhi dega agr key nhi hogi to unknown key 
# # # print(my_dict)

# # remove_item = my_dict.pop("chity", None)# ye remove krega iska faida ye he del  ke mokably me keye error nhi deta or remove krta he or none returnkrdega ya wo jo hm likhengy  or remove krne ke bad value bhi return krta he
# # name_item=my_dict.pop("name","faiza")# ye remove krega or agr key nhi hogi to faiza return krdyga

# # name_item=my_dict.get("name","faiza") #ye get kryga or faiza return krdyga agr key nhi hogi 
# # print(name_item)

# # # itration in dictionary
# # for key in my_dict:
# #     print(key)
# #     # ye key print kryga bs
# #     print(key,my_dict[key])
# #     # ye key or value print kryga
# # for value in my_dict.values():
# #     print(value)
# #     # ye value print kryga bs
# # for key, value in my_dict.items():
# #     print(key, value)
# #     # ye key and value print kryga dono
# # print(my_dict.keys())
# # print(my_dict.values())
# # print(my_dict.items())
# # # ya hm esy bhi likh skty hen

# # ////////////////////// list / dictionary Comparison  //////////////////////
# # list or lobject  kobnany kesath sath hi update conditionpass wagera krny ka tarika
# # list1 = ["faiza", "Rohan", "alina", "sania", "Rahul"]
# #         #  code       loop         extra condition 
# #         # code or lopp dena lazmi he or extra condition deni lazmi  nhi he
# # dict1 = {
# #     "name": "John",
# #     "age": 20,
# #     "city": "New York"
    
# # }        
        
# # my_comp=[i.capitalize()      for i in list1       if i !="faiza"]
# # NEW_DICT={key: value.capitalize() for key, value in dict1.items() if key !="name"}
# # print(NEW_DICT)
# # # ismy hmny list1 me jo name hen unko capitalize krdya or agr name faiza he to usko nhi uthaya or jo nhi he unko utha liya
# # # 
# # print(my_comp)


# # /////////////// FUNCTION /////////////////
# # lamda function
# # lemda_function = lambda cal1,cal2: print(cal1+cal2)

# # lemda_function(3,4)

# # # map is a class object 
# # # itretion 
# # # new modifier list 
# # # akneww list return krta he
# # n_list=[1,2,3,4,5,6,7,8,9,10]
# # map_list=map(lambda x: x*2 ,n_list)
# # print(list(map_list))

# # # filter
# # name_list=["faiza","alina","sania","Rohan","Rahul"]
# # filter_list=filter(lambda name: name=="faiza",name_list)
# # print(list(filter_list))
# # # isko bhilist me rkhna lazmime wrna wo list nhi bnata 
# # # ye bhi new list return krta he

# # ****** map modify krdeta he mapor filter nhi krta change cahnging nhi krta jesy mapfaiza ke sath naaz lga skta he
# # lekin filter nhi lga skta 

# # reduce
# name2_list=["faiza","alina","sania","Rohan","Rahul"]
# from functools import reduce
# reduce_list=reduce(lambda x,y: x+y,name2_list)
# # wo sary nameko join kRDY  GA KIOKY YE krta ye he ke list ka one word ans krta he 
# print(reduce_list)
# print(list(reduce_list))
# # isko hm list me nhi rkhty wesy agr rakhengy toye numbers koesitis krdega or names kotor dega f , i , z , a , a 

# *********** functions********
# reuse krny ka tarika code ko function khlata he 

# def my_function(name:str , age:int , *city, **kwargs): #signature
#      print(name,age,city,kwargs) #body
     
# my_function("faiza",18,"karachi","lahore",my_name="faiza",my_age=18)

# ismy name  or age normal parameters hen ju=ismy faiza or 18 strat wala jay ga
# karachi or lahore city parameters hen * lga kr hm jo parameter dety hen osmy hm jitny chahen parameter den sty hen result ak tople me ayga
# my_name or my_age keyword parameters hen jo hm ** lga kr dety hen us me hm key value ki trha arguments dety hen or resutl ak dic meata he 
     
     