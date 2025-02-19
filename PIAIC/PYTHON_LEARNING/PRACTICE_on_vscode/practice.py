# Best python notes 
# https://github.com/Sid-Taha/learning-python/blob/main/python_notes.md


# my_name :str= "faiza"
# print(my_name)
# print(type(my_name))
# full_name=f"{my_name} naaz"
# print(full_name)
# # paython me hm nam full_name snak case me hi deta he

# my_num :int=10.3
# # . waly decimale ki type yha hogi float
# print(my_num)
# print(type(my_num))

# # /////////////////////////
# is_running :bool=True
# print(is_running)
# print(type(is_running))

# # /////////////////////////
# num_1:int=10
# num_2:int=13
# print(num_1+num_2)
# # /////////////////////////
# a=10
# b=20
# result=a+b
# print(result)
# # /////////////////////////
# c=10
# d=13
# print(c/d)
# # /////////////////////////
# c=10
# d=13
# print(c%d)

# # /////////////////////////

# e=10
# f=10
# print(e**f)
# # exponent yani 10 ki power 10

# # /////////////////////////

# g=10
# h=10
# print(g//h)


# # /////////////////////////


# # arrat
# namess=list = ["faiza","naaz"]
# # /////////////////////////

# # for absc in qsjj=
# #     print(my_name)
# #     print(absc)
# # /////////////////////////
# # promt engineer

# # promate (actinw)
# # persona (Acting)
# # task(what to do)
# # context (data->pdf-> text->excel)
# # format (pdf ->je=son->excel)

# # /////////////////////////
# num_3:int=10
# num_4:int=num_3+10
# print(num_3+num_4)

# # /////////////////////////
# # short hand method
# num_3 +=20
# print(num_3)
# # /////////////////////////
# num_7:float=10.232892
# print(
#     round(num_7)
      
#       )
# # ismy wo 2 value dikha dega .ke bad wali
# print(
#     round(num_7,2)
      
#       )

# # //////////////////////////

# name_me:str="Faiza Naaz"
# print(name_me.upper())
# print(name_me.lower())
# print(name_me.title())
# print(
#     len(name_me)
#     # ye length btay ga sath sath space bhi cout hoga
# )
# # //////////////////////////
# multi line string

# name_me:str=""" me,
# faiza naaz"""
# print(name_me)

# # //////////////////////////

# my_name_is:str="faiza"
# my_namee:str="""me,
# {my_name_is} naaz"""
# print(name_me)

# # //////////////////////////

# # f string
# my_f_string:str=f"me ,{my_name_is} naaz"
# # ismy hm esy kr skty lekin multiple lie nhi le skty 
# print(my_f_string)

# # //////////////////////////

# my_list =["faiza","naaz","areeba","honen"] 
# print(my_list)
# print(my_list[0])

# my_list.append("nawaz")
# print(
#    my_list 
#     # ye and me add krdega list ke
#       )

# my_list.pop()
# # list ke end me sy remove krdega
# print(my_list)

# delete_name=my_list.pop()
# # ye jisko delete kiya he os name ko return krwayga


# my_list.remove("faiza")
# # list ke faiza ko remove krdega ye name sy remove krta he
# print(my_list)

# # //////////////////////////
# # ye for loop he for in loop
# new_list :list =["faiza","areeba","faizan","shoaib","daniya"]

# for name in new_list:
#  print(name)
#  print("hello")
# #  ismy hga ye ke loop har ak value ko print to krwayga or nichy hmny jo helo likha he ye bhi loop ka part he wo phly name ko print krwayga or phir hellow phir dosra name phir hello 

# # ismy curly braket nhi hota oski jga hota he space matlb agr hm 1 space dengy or next word ko bhi nichy ak space dekr likhengy jis jis ko hm
# # blkl ak hi line me likhty jaygy ak space ke sath to wo loop ka part bnta jayga age hm bina space likhengy koch wo lopp sy bari chala jayga 
# # //////////////////////////
# for name in new_list:
#  print(name)
# print("hello")# jesy yha pe hello ka rint bina space ke liye he to yw loop mw cout nhi hoga

# # //////////////////////////
# list_method :list =["faiza","areeba","faizan","shoaib"]

# # add element in the list
# list_method.append("alina")
# print(list_method)

# # remove last element in the list 
# list_method.pop()
# print(list_method)

# #remove kryga ye index number 1 wala element 
# list_method.pop(1)
# print(list_method)

# # ye jisko remove kiya he os value ko return krwayga
# return_value=list_method.pop(1)
# print(return_value)


# list_method.remove("faizan")
# print(list_method)
# # ye jisko name diy he isko remove kryga 

# list_method.insert(1,"dua")
# print(list_method)
# # ye index number 1 wala element ko dua name sy replace krwayga

# print(list_method.count("faiza"))
# ye faiza ko count krwayga ke faiza name kitni bar he list me yani koi name repeate hira ho to btayga

# list_method.sort()
# print(list_method)
# # ye list ko sort krwayga yani alphabetically sort krwayga jesy a sy jo ayga iskophy b sy ayga osko

# list_method.reverse()
# print(list_method)

# ye list ko reverse krwayga end wali element ko first wali element ko replace krwayga  orosky  bad phir 3 phir 2 phir 1 or phir phir pichy sy sort kryga yani phly z waly name phir y

# list_method.reverse()
# list_method.sort()
# print(list_method)

# # ye list ko reverse krwayga end wali element ko first wali element ko replace krwayga  orosky  bad phir 3 phir 2 phir 1

# list_method.clear()
# print(list_method)
# # ye list ko clear krwayga yani list ko khali krwayga

# ////////////////////////

# nested_list=["faiza","areeba","faizan","shoaib",["alina","nawaz"]]
# second_list=nested_list.copy()
# print(second_list)
# # ye list ko copy krwayga shalo copy krwayga  yani agr hmchanging krengy second list me to original list  change nhi hogi 
# # lekinagr list ke andr koiak or list he yani nested list agr second list me hm nested list ko  change krengy to original list me change hoga

# second_list[0]="samina"
# print(nested_list)
# print(second_list)
# # ismy srif second wallist change hogi original list nhi change hogi  

# second_list[4][0]="rabia"
# print(nested_list)
# print(second_list)
# # ismy wo change nhi kryga nested list ko lekin wo nested wali ko sath change krdega



# //////////////////////////

# multiple_list=["faiza"]*5
# print(multiple_list)
# # ismy faiza ko 5 bar print krwayga

# slice_list=["faiza","areeba","faizan","shoaib","alina"]
# print(slice_list[1:3])
# # ismy 1 wala index sy lekr  2 wala index tk yani 3 sy phly phly tk print  krwayga orwocopy bna kr krta he agr hm print krwaygy khali name again to wo wesa hi rhyga orginal
# print(slice_list)

# ////////// ***touple///////////////////
#Definition: A tuple is an ordered, immutable sequence of values.

# Touple =("faiza","areeba","faizan","shoaib","alina")
# # Touple.remove("faiza") # wrong

# # toubleis afixed value do not change remove add 
# # agr hm krna chahty hen update to hm osko list bnaengy 
# my_touple=list(Touple)
# my_touple.remove("faiza")
# Touple=tuple(my_touple)
# # Phiragain bnalo tuple
# print(Touple)

# names: tuple[str, str, str] = ("Taha", "Ahmed", "Alex")
# print(names[0])  # Output: Taha

# # jo method applay ho skty hen touple pr
# print(Touple.index("faizan"))# output 1 index lekr ayga
# print(Touple.count("faizan"))#output 1 .yani kitni bar faizan likha he list me
# # Tuples support slicing like lists.
# print(Touple[2:4])

# ////////////////////////***Set***/////////////////////////////////

#A set is an unordered collection of unique elements. Because it is unordered, you cannot access elements via indexing. Instead, you iterate over the set or use membership tests.
# ismy hm uniq chizen rakhty hen jha hm doblicate nhi krty na updatena change only one
# hmny alina ko 2 bar likha he lekin wo my ak hi bar dikhayga kioky wo doblicate leta hi nhi he 
# ismy koi order bhi nhi hota yani ye change bhi hota rhta he jesy 1 pr faiza he wha print me alina a jayga is trha hr word ka change hota rhta he

# Checking if an element exists in a set is much faster than lists because sets use hashing.
# example :
       
set1 : set[str]  ={"faiza","faizan","shoaib","alina","alina"}
set2:set[str]={"12","13","14"}
# # print(set1)

# set1.add("faiza")#add kryga
# set1.remove("faiza")#remove kryga
# set1.pop()
# Removes and returns an arbitrary element from the set.

# set1.clear()
# Removes all elements from the set.


set1.update(set2)
# Adds elements from another set (or any other sets) to the set.

print(set1)
# set1.discard("alina") # ye krta ye he ke jo dlet kry hen wo mil jata to delet krdeta nhi milta to chor deta errro nhi deta

# print(set1)

set3 = {1, 2, 3}
set4 = {3, 4, 5}
print(set3 | set4)  # Union → {3, 2, 3, 4, 5}
print(set3 & set4)  # Intersection → {3}
print(set3 - set4)  # Difference → {1, 2}

# ye normal union intersection math waly ki trha he

# ////////////////////////***INDEX***/////////////////////////////////







# /////////////////////////////////////////////////////////


# for loop

# numbers_list:list[list[int]]=[1,2,3,4,5,6,7,8,9,10]
# for number in numbers_list:
#     print(number)
# print(numbers_list)  
  
# jo chiz hm print me space dekr likhengy wo for loop ke ander ho agr print ko blkl line sy lga kr likhengy to wo for loop ke ander nhi ho ga
# or jis jis ko bhi hmy loop ke ander rkhna he osko hm ak hi line ki squence me dengy matlb 2 word ka ya 1 lekin dengy zaror

# /////////////////////////////

# num=0
# for i in range(1,11):
#     num+=i
#     print("faiza",i)
# ye range wla he jismy hm ander sbky sath koch + krty hen ya - ya ye ke 1 ,11 yani start or end pont dety ke itni bar chalao map ko 



# for i in range(1,11,2):
#     print(i)
 
# #ismy 3rd value ye kryga ke  matlb he ke kitna + (incriment) krna he to wo 1 sy 10 tk a jayga lekin agr hm likhengy 2 to wo 2 +kryga lekin wo rokyga 11 sy phly hi 



# for i in range(10,1,-1):
#     print(i)
    
# #yha sy wo reverce ho jayga 10 to  1 - me dengy 

# for i in range(1,11,2):

#  for i in range(1,11,2):
#   print(i)
#   if i==5:
#     break
# # ye 5 tk hi chalay ga phir break ho jayga esy if else likhety yha hm 

# namess=["faiza","areeba","faizan","shoaib","alina"]
# for index,item in enumerate(namess):
#     print(index,item)
    
# # is trha hm index number ke sath vlue print krwa skty hen index ak varibale he oski jga koch bhi likh skty hen or item bhi ak variable he oski jga koch bhi likh skty hen
# # /////////////////////////////

# # while loop

# while True:
#     print("hello")
    
# num=0    
# while num==5:
#     print("hello") 
# #ye print nhi hoga kioky condition false he 
# numm=0
# while numm<=5:
#     print("hello")
#     numm+=1

# ////////////////////////////
# python me do-while loop nhi hota he
# ////////////////////////////
# num_list =[1,2,3,4,5,6,7,8,9,10]

# def my_function(num):
#     return num*2
   

# myvar=list(map (my_function,num_list))
# print(myvar)

# # ismy function alag sy likh kr pas krengy or osmy conditon dengy jo pa krni he sb me 

# ////////////////////////////
# comperison operator with if else
# ye input hota he jo sawal ke liye kam ata he form wagera ke liyye
# input_name=input("enter your name")
# print("hello",input_name)

# input_age=int(input("enter your age"))
# print("your age is",input_age)

# if (input_age>=18):
#     print("you can vote")
# elif (input_age<18):
#     print("you can not vote")
# else:
#     print("you can vote")
# 
# ////////////////////////////
# logical operator with if else
# name_age=input("enter your name ")
# age_name=int(input("enter your age "))
# if (name_age=="faiza" and age_name==18):
#     print("you can vote")
# else:print("you can not vote")

# name_agee=input("enter your name ")
# age_namee=int(input("enter your age "))
# if (name_agee=="faiza" or age_namee==18):
#     print("you can vote")
# else:print("you can not vote")

# ismy bhi wo dono hi cheq kryga dono true hongi to hi code run hoga  ak true or dosri ismy false waly di he
# nname_age=input("enter your name ")
# aage_name=int(input("enter your age "))
# if (nname_age=="faiza" and not aage_name==18):
#     print("you can vote")
# else:
#     print("you can not vote")

# ////////////////////////////

# add = lambda num1 ,num2:num1+num2

# # ye ak function he jo perameters leta he 
# # num1 ,num2  ye dono perameter he jo function ke andar leta he
# # num1+num2 ye dono perameter ko add krwayga yanihe wo he jo hm {} ke ander likhty hen

# print(add(10,4))


# def add2(num1:int,num2:int):
#     return num1+num2
# # YE DEFINITION WAALA FUNC HE 
    
# print(add2(10,4))

# ///////////// FUNCTIONS /////////////////

# # 5 ki table banane ke liye variable define kiya
# table_of = 5

# # range() function se 5 se start karte hue 100 tak numbers ka sequence banaya,
# # jo har 5 ke gap ke saath chalega (5, 10, 15, ...100)

# # x=range(start, stop, step)
# x = range(table_of, 100, table_of)

# # Counter shuru kiya 1 se, or lopp sy hm 1  2  3  ak ak + krwygy
# counter = 1

# # Loop x ke har number ke liye chalega
# # or n me current number store hota jayga 5  10 
# for n in x:
#     # Agar counter 10 se zyada ho gaya, loop ko todh do (break)
#     # or x bhi khoood 50 pr rok jayga
#     if counter > 10: 
#         break

#     # Current number aur counter ko formatted output ke saath print karte hain
#     # Example: "5 x 1 = 5"
#     print(f'{table_of} x {counter} = {n}')

#     # Har baar counter ko 1 se badhate hain
#     counter += 1
# # //////////////////////////////

# # function ***************
# # we use function to avoid the repetition of code and make the code more readable
# # function is a block of code which only runs when it is called
# # function is defined by def keyword
# # function is called by function name followed by ()
# def function_name(parameters):
#     # function body
#     return parameters
# func=function_name("gulshan")
# print(func)

# # 2nd example

# def greeting(name):
#     # function body
#     print(f"Hello, {name}!")
# greeting("gulshan")
# greeting("ali")
# greeting("ahmed")


# # 3nd example

# def limit(age=9):
#     # function body
#     print(f"your age is, {age}!")
# limit(5)
# limit()
# # AGR KOCH NHI DENGY TO DEFAULT VALUE CHALYGA 9

# // /////////// ERROR HANDLING /////////////////

# try : 
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     # yejo hmny likha he ZeroDivisionError ye hmy esy pta lgyga ke kiya likhna he hm phly cheq krygy bina try or except ke to wo jo terminal me jb error dega to osmy payhthon khod btata he type ke kis type ka error he hm wahi sy otha kr krdengy 
#     # code to handle the error
#     print("Error: division by zero")
    
# # isy try me hm error ko handle krwa skty taky error ki jga sms ay kioky 10/0 nhi hoskta error ayga isi liya hmny ye kiya

# # /////////////////////////////
# try : 
#     result2  = 10 / 0
#     print(result2)
# except ZeroDivisionError:    
#     print("Error: division by zero")    
# except ValueError:
#     print("Error: value error")
# except Exception as e:
#     print("Error: unknown error")    

# # esy hm do do bhi likh skty hen iska matlb koi dosra error ay to ye likhengy lekin type dekh kr ye value erro wb ata he jb koi number ko/krwa deta he alphabat ko 

# # or last waly ka matlb agr isky ilawa koi error ay to e print krwayga yani e print krwayga unknown error


# ///////////////// MODULE IN PYTHON  ////////////////
# 1st file
# def say_hello():
#     return "Hello World"

# print(say_hello())

# # 2nd file 

# 1st method
# import say_hello 
# print(say_hello.say_hello())
# 2nd method
# from say_hello import say_hello
# print(say_hello())

# hm paython me is trha krty hen import  krty hen 


# //////////////// Dicshionarries ////////////////

# # Dictionaries are used to store data values in key:value pairs.
# # Dictionaries are written with curly brackets, and they have keys and values.

# userdata = {
#     "name": "faiza",
#     "age": 18,
#     "gender": "female"
# }

# print(userdata["name"])
# print(userdata["age"])
# print(userdata["gender"])

# # hm esy print krwaty hen signgle value ko 
# print(userdata)

# # hm esy print krwaty hen sari value ko

# userdata["name"] = "gulshan"
# print(userdata["name"]) 

# # hm esy kisi value ko update kr skty hen 

# ///////////////////// oPEN FILE //////////////////////
# # file = open("file.txt", "r")



# ////////// OBJECT ORIENTED PROGRAMING ///////////////
# YE CODE Likhny ka ak tarika ha bs
# ye hota ye he ke ak br bna kr bar bar use krna


# hm ismy sbsy phly ak blue print bnanty (object) hen or osi ko bar bar use krengy

# # ye hmny bnaya ak blue print
# class House :
#     adress :str ="Houser-Number 124"
#     numbers_of_rooms :int = 3
#     numbers_of_door :int = 2
    
#     # 
# House1 = House()
# print(House1.adress)
# print(House1.numbers_of_rooms)
# print(House1.numbers_of_door)
# # esy hm acees bhi kr skty hen phly ak variable me rkhna hoga

# # ye hmny ak  SY DOSRA BHI BNA LIYA or values change krli jo zarort thi chnage krny ki
# House2 = House()
# House2.adress = "Houser-Number 125"
# House2.numbers_of_rooms = 2
# House2.numbers_of_door = 1

# print(House2.adress)
# print(House2.numbers_of_door)


# //////
# CONSTRUCTER FUNCTION
# YE krta ye he ke blue print ko use krky object bnata he 
# class constructer_house :
#     adress :str
#     def __init__(self,adress:str):
#         self.adress = adress
        
#         # constructer func ka faida ye hota he ak ke hm isko ak normal function ki trha paameters pass kr skty hen or ye hm class ke nader bnaty hen to ye class ka part he 
#         # or isy ye hoga ke hm jitni bar class ko run krengy wo argument mangyga or har bar alag alg argument bna skty hen
#         # sef hm zaror rakhty wo iska part he isi sy hm dosri prperties ko acces krty hen
#     def str(self): 
#        return self.adress
       
           
#     #  ye simple function ki trha he bs he ye wesy hi contructer k trha same lekin ye ak function he isko hm property ki trha acees krengy . lga kr ismy bhi self likhty hen hm zaror

   

# faiza_house = constructer_house("Houser-Number 124")
# Alina_house = constructer_house("Houser-Number 125")
# print(Alina_house.str())
# print(faiza_house.adress)
# print(Alina_house.adress)
# ARGUMENT NHI DENGY TO ERROR AYGA 
# hm diffrent house bnary hen lekn blue print ak hi use kry hen hm 
   

   
# ////////////INFORMATION//////////////// 
  
# Ture or False me T or F capital me hota he
# paython --version ye cheq kryga ke paython install he ya nhi 
# paython 3.13.1 Yani paython instal he
    
# int , float ,str,bol, list ,tuple, set, any

# multiple line string=doc string 

# "2"+1 esy coordinate nhi krwa skty hm paython me

# code ko blkl start Sy likhengy space dekr nhi likh skty start me jesy print ya variable ka name

# agr hm double slash lgaegengy to so single value return kry ga 0.6 ANS HOGA / ka to // ye bhi kryga devide lekin ye int value return kryga 0






# ////////////READ////////////////
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# // devide