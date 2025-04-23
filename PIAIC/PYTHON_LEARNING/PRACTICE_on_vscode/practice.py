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


# ye slow hota he set sy kioky yeye linear searching krta he yani ak name dhondny ke liye wo start sy har name ko dkehna start krta he


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

  
# 

# Checking if an element exists in a set is much faster than lists because sets use hashing .
# example :
# ismu ak hash function hota he jo  list ki har value ke badly ak hash code bnata he khod or osko ak baket me rkh deta he jiski wja sy wo extra memory let he 
# hash collision : ismy hota ye he ke iska process ye hota he ke wo har value ka hash code bnata he or osy rkhta he ak nuket me or wo has esy bnta he ke wo ak has code bnata he or list me jitni value hoti hen osy devide krdeta he or jo number ata he os number ki buket me wo rakh deta he os value ko jes
# list me 5 value hen {1,2,3,4,5} ab 1 ka hash code bnaya osny 305 osko deive kryga total number of value jesy 305/5 =2 ab 2 ans aya to wo 2 number wali basket me rakhdega 1 ko lekin ab esa bhi to ho skta he ke 2 ka hash code bnyga to diffent lekin 5 sy deivide krny sy bhi wo ay
# 2 to same buket ho gai to wo same buket me rkhdega 1 or 2 dono ko or phir osy jb dhondna hoga to wo 2 number wali buket me jayga or onky has
# code ko dekh kr le ayga kioky hash code to alg hi hoga dono ka 

# hash buket *********

       
# set1 : set[str]  ={"faiza","faizan","shoaib","alina","alina"}
# set2:set[str]={"12","13","14"}
# # # print(set1)

# # set1.add("faiza")#add kryga
# # set1.remove("faiza")#remove kryga
# # set1.pop()
# # Removes and returns an arbitrary element from the set.

# # set1.clear()
# # Removes all elements from the set.


# set1.update(set2)
# # Adds elements from another set (or any other sets) to the set.

# print(set1)
# # set1.discard("alina") # ye krta ye he ke jo dlet kry hen wo mil jata to delet krdeta nhi milta to chor deta errro nhi deta

# # print(set1)

# set3 = {1, 2, 3}
# set4 = {3, 4, 5}
# print(set3 | set4)  # Union → {3, 2, 3, 4, 5}
# print(set3 & set4)  # Intersection → {3}
# print(set3 - set4)  # Difference → {1, 2}

# # ye normal union intersection math waly ki trha he

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


# # function ***************
# # we use function to avoid the repetition of code and make the code more readable
# # function is a block of code which only runs when it is called
# # function is defined by def keyword
# # function is called by function name followed by ()
# def function_name(parameters:str)->str:
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

# Output: 15

# def func(post1,post2,*args,**kwargs):
#     print(post1,post2)
# func("first","second","extera1","extre2",key1="value1",key2="value2") 
# # first and seccond khlayga position parameters jo ke os prameters me ayga jo hmny diye hen or alag alg print hoga
# # extra waly arguments yani wo jiska parameters hmny nhi diya jo ke *args me ayga or khlayga (arbitary positional parameters) or ye sb ak tuples me bn kr print hoga
# # key1, key2 ye hota he key word arguments or ye jayga **kwargs me or khlayga (arbitary keyword parameters) or ye print ak dictinary ki sorat me hoga 


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

# from math import *
#  is trha hm isi chiz k sary methods koimport kr skty hen 

# //////////////// Dicshionarries ////////////////

# # Dictionaries are used to store data values in key:value pairs.
# # Dictionaries are written with curly brackets, and they have keys and values.

# userdata:dict[str,any]= {
#     "name": "faiza",
#     "age": 18,
#     "gender": "female"
# }

# print(userdata["name"])
# print(userdata["age"])
# print(userdata["gender"])

# # hm esy print krwaty hen signgle value ko 
# # print(userdata)

# # hm esy print krwaty hen sari value ko

# userdata["name"] = "gulshan"
# # REASIGN KRNA
# userdata["student"] =   True
# # full property add krna

# del userdata["gender"]
# # ye delete krdega gender ko

# userdata.pop("student",None)
# # ye delete krdega student ko ismy ye faida he pop ka del ke mokably me ke agr osko del krny wali value mil gai to delete krdega nhi mili to errro nhi dega

# print(userdata.get("name", "not found"))
# # ye get krdega name ko ismy agr name ko value mil gai to wo print krdeta he nhi mil gai to not found print krdeta he

# for key, value in userdata.items():
#     print(f"{key}: {value}")
# # ye for looP BHI HOTA HE CHAHY TO SIRF KE VALUE PRINT KRDYGA YA SIRF KE KEY PRINT KRDYGA YA DONO PRINT KRDYGA    

# for key in userdata.keys():
#     print(key)

# for value in userdata.values():
#     print(value)
# # ismy functions bhi hoty hen values waly sy bs values print hongi or keys waly sy sirf keys print hongi
# for item in userdata.items():
#     print(item)
# #ye key value dono dyga tuple me ()isky ander 


# print(userdata)
# print(userdata["name"]) 
# print(type(userdata["name"])) 
# print(type(userdata["name"])) 


# hm esy kisi value ko update kr skty hen 


# ////////////////// COMPRIHENSION ////////////////
# ye dictionary or list ko bnany ka quick tarika he 
# list_me:list[str]=["x","y","z"]
# name_list :list[str] = [old_name+"f" for old_name in list_me]
# print(name_list)

# my_dict :dict[str,str] = {old_name:old_name.capitalize() for old_name in list_me  if old_name != "x"}
# print(my_dict)
# ismy hoga ye ke jo list me he orignal wo key bn jayga or jo hmny modification ki he jesy capital wo value bn jayga ye hmny ak list ko dictionary  bnaya he
# ye har name ke sath concatinate krwayga or f ko add krwayga jesy x ko xf yko yf zko zf hm ismy koch bhi kr skty hen jesy lower func uper sb
# kr wa skty hen hm ak line me 

# //////////////////// LIST FUNCTION //////////////
# # Reduce function
# # reduce ye krta he ke  hmara sari value pr condition lga kr ak value return krdeta he
# # hmy isko import krna prhta he 
# from functools import reduce 
# # isko ak list chiye hoti he or ak function 
# # isko hm likhty esy hen phly function phir parameter : phircondition phir list
# my_list_reduce:int=[1,2,3,4,5]
# total=reduce(lambda num1,num2 : num1+num2,my_list_reduce)
# # ismy ye hota he ke phly waly parameter hota he 0 or dosra list ka phla value hota he or next me num1 me wahi total save ho jayga 
# print(total) 

#  Lamda ********

# lambda_func =lambda num :num*2 
# # lambda function ak bina name ka func hota he anonimus fuc bhi khlata he ye or isko hm variable me rkh kr name ety hen 

# # num parameter he or num*2 ye consition he yani jo bhi krwana he or ismy return likhny ki zarorat nhi hoti wo direct krta he return 
# print(lambda_func(5))

# # # map function******
# # numbers:int=[1,2,3,4,5]
# # new_list=map(lambda num : num*2,numbers)
# # # map ak function leta he jismy hm kam krty hen lambta leta he or ak list jisky liye kam krta he
# # # ye ak new list create krta he
# # map() function mein output ko list mein convert karna zaroori hai
# # print(list(new_list))

# # Filter function
# filter_list:list[int]=[1,2,3,4,5]
# filter(lambda num : num>3,filter_list)
# # ye bhi akfun or list leta he or filter krky nikalta he yanijo conditioan pas hoti osko ye filter yani rkhta he baqi sb nikal deta he
# # ye bhi new list create krta he orignalko change nhi krta



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
   
# /////////////// Modules ////////////////
# import math
# # ak ye tarika he kisi bny wy func ko import krny ka pathon sy
# from math import pow
# from math import comb
# # FORM MATLB SY YANI KISI func sy YE hmny math ke function sy pow ko nikala he yani kisi func sy oski chizen import krwna ..or sirf pow hi hm ismy use kr skty hen
# # math ko use nhhi kr skty osky liye math imort krNA HOGA kioky wo math sy pow ko lekr aya he naky 

# import streamlit as st
# YE KHLATA HE  nick name dena yani (alias) yani strreamlite ko st sy  hm acces krengy ab 

# hm ksi file ka name agr kikhen import app to wo khod hi sari file run  ho jayga 

# //////////////// AUTO CALL /////////////////

# def hello():
#     print("hello")
    
# hello()
# # agr hm isko esy hi chlaygy toagr hm is function ko kisi next file me jakr import krky use krengy to wo bina call kiye hi run hoa
# # oskorokny ke liye hm use krty hen
# if __name__ == "__main__":
#     hello()

# ismy ye hota he ke if ki condition pr depend ho jata he ye or jb hm isko kisi or file me import krty hen to ye __main__ apnifilenamekr
# braber  ho jata he yani main ki jga app agr file ka name app heto 


# ///////////// try excep //////////////
# # try exeptkause hm isi liye krty hen kioky agr koi errror ata he to wo agy ka code rok detahe runnhi hony deta sara 
# # kamrok jata he 
# number=0
# try:
#     print(10/number)
# except ZeroDivisionError:
#     print("you cant divide by zero")

# #ismy hm try me true code likhty hen or exception me false code likhty hen
# # or hmyjopta hon ke is type ka error any wala he tohm isme usi type ka error likh skty hen
# # agr nhita to hoderror create krky hm isme usi type ka error likh skty hen
# # or agr esa error jiski typenaho ya zada nhi likhna chaly to hm Exception likh skty hen ya bs except : print("error") likh skty hen

# try :
#     print(10/number)
# except Exception as e:
#     print("error",e)
#     # ismy kisi bhi type kaerrro ayga to wo catch ho jayga
    
#  # jesy kisi bhi jha 2 kismke errro bhiaskty hen tohm dono type de dengy
 
  

# try:
#     print(10/number)
# except ZeroDivisionError:
#     print("you cant divide by zero")
# except Exception as e:
#     print("error",e)
    
#     # ismy ye hoga ke jonsa error hoga wo catch ho jayga or dosra wla ignoree ho jayga khod

# ///////////////////// raise error /////////////////

# class ExeptionError(Exception):
#     pass

# try :
#     raise ExeptionError("this is a custom error")
# except ExeptionError as e:
#     print(e)

 #hm is trha error generate krty hen 
 


# ///////////////// MEMORY MANAGEMENT /////////////////
# python me hm jb koi bhi vaiable bnaty hen to wo print ho jata he agr name hta den to wo errro dega kioky jv name ka variable hi hta diya
# /to wo prin nhi ho skta iska matlb wokhi store hi nhi howa tha wrna to htany sy wo acces kr deta ye tempoary memory use krta he 

# # id 
# name1="faiza"
# name2="faiza"
# # id ak location hoti he ke variable kis location pr store he
# # in dono ki id same hogi jis bhi varible ki value same hogi oski id bhi same hogi
# name1=name2
# # iski id bhi same hogi kioky dono me same value he python apni memory kodublicate ke liye zaya nhi kta
# # lekin alag file me hoga agr to id same nhi hogi bhly value same ho kioky file alag alag time pr run hoti he 


# array1=[1,2,3]
# array2=[1,2,3]
# # ismy alag alag aygi id kioky ye mutible he jbky 
 
# aray1=array2
# # ye id same  hogi kioky ismy to ak variable hi as kr diya he jisny apni memory phky sy bnai thi to 2 wala bhi dhondnywahi jayga 1 me same location pr
# # dictionary ka bhi blkl same array ki trha he 

# # ///////// ASYN CHRONOUS PROGRAMMING /////////////////
# import asyncio
# # async me time west nhi hota syncronous program me hota he kioky wo agy koi code run na ho to agy ke code ko run nhi hony deta
# async def greet (name):
#     await asyncio.sleep(3)
#     # await tb tk rokta he jb tk nam1 ki value na  mil jaye await means pose ho jana rokna 
#     print(f"hello {name}")
#     # ismy aync ef sy ply lgta he await ko hm async def me hi likh skty hen


# async def greet1(name2):
#     await asyncio.sleep(1)
#     print("hello ",name2)

# async def main():
#     await asyncio.gather(greet("faiza"),greet1("areeba"))
#     # kisi do function ko ak sath chalaty hen to gather ka use krty hen 
    
# asyncio.run(main())
    
    
    
#  # //////////// UNPACKING IN PYTHHON  ////////////////
# #  yani kii touple sy value nikalna ya list sy value nikalna ya dictionary sy value nikalna

# name =["faiza","areeba"]
# print(name[1])
# # ye normal tarika 
# n1,n2=name
# print(n1)
# # ye hmny unpaking krli 
# # esy hi same karna hai  touple ke liye 

# # for dictionary
# user={"name":"faiza","age":22}
# name1,age1=user.values()
# print(name1)
# # variable ka name koch bhikh skty hen unpacking ke liye

# # ////// TERNARY OPERATOR //////
# # ternary operator ka use krty hen jab hum ek condition ko check krna hai aur us
# result=12 
# ans="true" if result > 10 else "false"
# print(ans)

# ////////////
# """ismy hm multi line comment likh skty hen """

# ////////FROZEN SET/////////
# FROZEN set ka matlb he kisi chiz ka frize ho jana rok jana
# frozen set memory Chang kr deta he kisi value ki agr koi 2 variable me same value he or ak ko frozen me rakh diya to wo different khlaigi
# my_set = {1, 2, 3, 4, 5}
# frozen_set = frozenset([1, 2, 3, 4, 5])
# ye same nhi khlayga matlb === nhi

# lekin agr variable pass kr diya frozen me to wo phir ho jayga same Yani true
# my_set == frozen_set
# ab ye true hoga 

# awt or frozen set ak trha ka hi hota he yani uniq value rkhta he lekin forzen change nhi krny deta yani remove add wagera 
 
 
 
#  ////////////MATCH CASES ////////////
# value = 3
# match value:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Other")

# ye swich cases ki trha hota he sahi condition ko run kr deta he
#  ////////////////////////

#  network error hm except me wb likhty hen JB api me error ata he
#  SQL mean starcture query language
# python me nhihota number or string concatinate
# Print is a built-in function in Python

print(2**2**3**4**5)
# ye right side sy calculate hona start hota he phly 4 *4*4*4*4 hoga jo anser ayga wo phir otni bar 3 hoga phir jo ans ayga phir wo 2 ka exponent bn jayga

# VERLAS OPERATOR
# ye ak hi line me likhy jay hen jismy hm asign bhikrty hen or condition ko check krty hen isko hm :=sy show krty hen
(a := 1 )>2
print(a)
#  ///////////////////////////-----------*********************************///////////////////////////

# python in development mood
# source code =>ready to use
# python in production mode
# source code => interpreter => operting sytem => hardware
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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