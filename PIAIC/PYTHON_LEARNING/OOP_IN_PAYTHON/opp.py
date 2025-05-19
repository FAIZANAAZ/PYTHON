#  OOP


# data/attributes
# methods/functions
# manipulation the data
# instance /object
# class

# CLASSS KA name hmesha capital hoga
# class Human ():
    
#      # isfunc kebina hm class ko use nhi kr skty ye functon khod call ho jata he jb instance create krtyy hen
#     #  or ismy jo parameters hoty  hen wo hm class me hi ( ) ke ander arguments dety hen alag sy nhi dety lekin 
#     # method ko hm call krty hen name sy osky ander dety hen arguments 

#     def __init__(self , name):
#         # iska name __init__ hi hoga hmesha init matlb initialize krna class ko 
#         # self ismy lganazarori he self apny ander parameters ko chopa leta he osky bina hm parameters ya variable ko nhi likh skty init me 
#         # construction class sy lekr ata intence ko data he or instence sy lekr class ko 
#         self.name=name
#         # HMNY isko dynammic bna diya name assign krkky paameter wla hm normal koi bhi value bhi de sky hen jesy faiza lekin phir wo chnage  nhi ho skta
        
      
#    #METHODS
#     def speak(self):
#         return (f"hello my name is {self.name}")
#     # ismy hm kam krty hen logic likhty hen zda tkontruction me diye gy variables ka use krky ye bhi self leta he wrna acces nhi kr skty koch na hi
#     # contruction func ko na hi kisi atributes ko class ke 
    
#     def walk (self):
#         return self.speak() 
#     #    yani  method bhi dosry method ko rkhta he lekin self ke ander 
    
# # ///*********************instance/object
# # class ko call kky use krny ko instance khte he
# human=Human("Rohan")
# print(human.name)
# # is trha human. krky hm name ya method sb call kr skty hen
# print(human.walk())

# # //// ******************* Inheritance********
# # iska matlab ekka class ka use dusry class me krna he

# class Student(Human):
#      # ismy hm student class ko human class ke inherit kr diya
#     # ye methods or class ki sb chizeon ko apny ander laata he
#     def __init__(self , name ,age   ):
        
#         # hmy agr esa krna he ke ye same contructer ly apny parent ka to hm isko wahi waly parameters dengy or osko bhejengy apny parent ka contructer ko or otny hi dengy jitny parameters apny parent ka contructer me hote hen agr zada hongy toosko hm nhi bhejengy yahi pr rakhengy
#        super().__init__(name)
#     #    super ke ander hm bhej rhy hen ye lazim he 
#     #    yha hoga koch yun ke ye values jaengy parent ke contructer me or phir wo wha sy run hongi 
#        self.age=age
   
#     def student_info(self):
#         return f"{self.name} is {self.age} years old"
    
#     def speak(self):
#         return f"hello my name is {self.name} and i am a student"
    
# student  = Student("Rohit",20)
# # hlaky student class me to name he hi nhi osko  hm acces kry hen husman class sy 
# print("inherited student class",student.name,student.age)


# #******** multiple classes inherited

# class Teacher(Student,Human):
#       def __init__(self , name ,age ,teacher_own):
#           Student.__init__(self,name,age)
#           Human.__init__(self,name)
#         #   hm is trha phonchaygy multiple classes ko inherit krty wy super sy nhi krengy 
#         # ye self wha sy lakr ara he name age ko
#           self.teacher_own=teacher_own
          
      
       
  
# teacher=Teacher("Rohit",20,"Physics")     
# print(teacher.name,teacher.age,teacher.teacher_own)
# teacher.speak()
# #   jb multiple inherited hoti hen classes or osmy same name ke methods hon orhm iskoaa acces krty hen to wo osko leta he jiska name phly hota 
# # he yani student sy kioky wo phly sy class Teacher(Student,Human):  ismy agr hm human phly likhengy to wo human wala speak othayga




# # /************magical functions *****************/

# class Vectors:
    
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
#     def __str__(self):
#         return f"{self.name} is a teacher and teach {self.teacher_own}"
    
#     def   __add__(self,other):
#         if isinstance(other,Teacher):
#             return Teacher(self.age+other.age)
#         raise TypeError("can only add teacher")
    
#     def __call__(self, *args, **kwds):
#         return super().__call__(*args, **kwds)
    
# V1=Vectors(1,2)
# V2=Vectors(1,2)
# print(V1+V2)


# # pilar 2) Polymorphism *************************/

# # polymorphism is allow us to use same method name with different parameters or return types
# # 1) method overloading

# class Dog :
#     def speak(self):
#         print("Dog is speaking")
    
# class Cat(Dog):
#     def speak(self):
#       print("Cat is speaking")
    
    
# class AnimalChild2(Dog):
#     def speak(self):
#         print("AnimalChild2 is speaking")
    

        
        
# dog=Dog()

# cat=Cat()

# animal_child=AnimalChild2()



# dog.speak()
# cat.speak()
# animal_child.speak()


# # jiska intance pr hm .speak likhengy wo osi ka chaly ga matb har method ke pas 2 speak hen ak apna or ak Dog ka inherited kiye howy lekin hm agr jis class ke instence ke sath . lgaygy wo usi ka chaly ga Dog ka nhi clyga or hn agr apny pass he hi nhi to phir animal wala chalyga

# # DUCK TYPING **********************
# def Animal_sound(animal :Dog):
#         print(f"the animal makes a {animal.speak()} sound")
        
# dog=Dog()
# Animal_sound(dog)
# # ismy hmy class dena hoga kioky oski type he Dog ya to dog hi dedo ya wo class bhi de skty hen jismy Dog ke baraber hon sb method property sb with same name 

# # ak to same name ka method hona lazmi he agr koi dosra method he jiska name dosra he to wo  bhi hm pass kr skty hen lekin hm osko use nhi kr skty 

# def Animal_sound_array(animal:list[Dog,Cat]):
#     pass

# dog=Dog()
# cat=Cat()
# Animal_sound_array([dog,cat])

# polimarisation **********************

# privat # ye pyhton sanbhalta he
# public
# protected # ye developersanbhalta he
# public or private hota same hi he

# class Mother:
#     def __init__(self):
#         self.__private_var = 10  # ✅ Private variable
#         self.public_var = 20  # ✅ Public variable
#         self._protected_var = 30  # ✅ Protected variable
        
#     def get_age(self):
#         return self.__private_var  # ✅ Private variable access
#     # ismy hm bs get kr skty modify ke liye hmy seter ka use krna hoga
    
#     def set_age(self, age):
#         self.__private_var = age  # ✅ Private variable modify
        
#   #seter me or geter e farq ye he ke geter me privat ko return kiya wa hoga or seter me privat ko modify kiya wahoga kioky name to koch bhi ho skta he 

# class Child(Mother):
#     def __init__(self):
#         super().__init__()  # ✅ Parent class ka constructor call karna zaroori hai

# # ✅ Objects create karna
# mother = Mother()    
# child = Child()

# # ✅ Ab error nahi aayega
# print(child.public_var)  # Output: 20
# print(child.get_age())   # Output: 10

# # private var ko access nhi kr skte

# print(Child.__mro__)
# # ISY HM wo sb kvoh dekh skty hen jo chid class me he yani wo object or kon konsi class inherited ki hoi he ismy to chiz phly
# # print hogi yani oski value zada he bad wali class sy 


# ************ Abstraction ********************

# Abstraction or Abstraction Class alag alag chizen hen

# Abstraction is the process of hiding the implementation details and showing only the essential features of an object to the user.
# jesyy hm protected wagera lga kr hm hide krty hen isimko abstraction khty he 

# **Abstraction Class**

# abc stand for abstract base class
# kisi class ko abstrackt bnany ke liye hm abc module ka use krty hen ABC inheritet krwaty hen or abstractmethod use krty hen jis method ke oper 
# abstractmethod likh hoga to osko agrkoi class inherit krygi to osko apny ander zaror bnayga dobara

#  osabstraction ka instance nhi banta
# from abc import ABC , abstractmethod
# class Abstract_class(ABC):
#     @abstractmethod
#     def walk (self):
#         pass
  
    
# # class_abc=Abstract_class() # error aayega kyunki abstract class ka instance nhi banta  

# class  Faiza(Abstract_class):
#     def __init__(self):
#         super().__init__()
#     def walk(self):
#             print("Faiza is walking")
#             # ye lazim he kyunki abstract me isky oper abstractmethod likh hua he
            
#             # OR AGR 2 METHOD HEN OR AK BNA LIYA TO WO AK BHI NHI CHALY ga jb tb hm 2 waly ko bhi na bana len
            
# fz=Faiza()
# fz.walk()
# # iska bn jayga            
 
 
 
#*****************CLASS VARIABLE & STATIC METHOD & DIR ************************
# class instance ke bina hm class constracter ke ander ke variable ko access NHI  kr skty hen 

# lekin hm class ke ander ke variable ko access kr skty hen

# class Human:
#     species="human"
#     def __init__(self):
#         self.name=43
       
#     @staticmethod        
#     def static_method():    
#         print("this is static method")
#         # ISMY selfnhi hota isiliye hm iske ander static variable ko access kr skty hen jesy self.name=name
#         # ye todynamic ho jata he ismy self hi nhi he YE CHANGE NHI HO SKTA 
        
#         # yebina instance bnay hm isko get kr skty hen bahir
    
    
  
# print(Human.species) # ye result de dega        
# # print(Human.name) # ye result nhi de dega
# print(Human().name) # ye result de dega
# Human.static_method() # ye result de dega

# print(dir(Human))
# # ye sb koch dikha dega ke kiya kiya hen variables methods sb LEKIN ATRIBUTES NHI DIKHAYGA OSKO DEKHNYKE LIYE HMY INTANCE KO BANA kr print krna hoga instance

# human=Human()
# print(dir(human))
# # ye dikha dega atribues bhi 

# ************ IMPORT & EXPORT ********************

# class IMPORT_EXPORT:
#     def __init__(self):
#         self.input=0
#         self.output=0
#         self.IMPORT_EXPORT:=0
#         self.input_output=0
        
#  next file main.py
#  from app import IMPORT_EXPORT
 
# is trha krty hen hm  import class ko or export 



     
# ********************* call and str method dir ****************

# class Class_call:
#     def __init__(self):
#         self.name="Rahul"
#         self.age=21
#         def __str__(self):
#             return f"Name: {self.name}, Age: {self.age}"
#         def __call__(self):
#             print("Hello, my name is", self.name, "and I am", self.age, "years old.")
#             # ye intance ko call krne ke liye use krna hota he
            
# per=Class_call()
# print(per())  # ye error dega agr hmny ismy __call__ nhi likha heto      __call__ ka method isky intance ko call krne ke liye use krna hota he

# # ******
# print(dir()) # ye sb dikha dega jjitny bhi magic method hoty hen

# # ******
# print(per) # jb hm instance ko chalaty hen bina koch acces kiye to str chal jata he khod ab hm osmy koch bhi de skty koi bhi sms wagera

# *************************FILE READ AND WRITE IN DIFFERENT FILE ***************************
# with open("file.txt","r") as f:
#     print(f.read())
    
# #ismy hm 2 oarameter dety hen string me jo file name he aur second wala string me jo mode he r w ya w+ ya a+ ya a
# # r yani read mode
# # w yani write mode
# # a yani append mode
# # r+ yani read and write mode
# # a+ yani append and write mode
# # w+ yani write and read mode

# with open("file.txt","w") as f:
#     f.write("hello world")
#     f.write("\nfaiza naaz")
    
#     # ismy hm jo likhengy wo file.txt me save ho jata he
    
#***********************  DECORATOR FUNCTION ******************** 

# def decorator_function(original_function):
#     def wrapper_function():
#         print("Before calling the original function")# ye phly me chalyga
#         original_function()#isky parameter me wo func ayga jo hmne decorator_function ko pass kiya he
#         print("After calling the original function")# ye bad me chalyga func ke jispr decorater lgaya he
#     return wrapper_function
        
#  #DECORATION FUNCTION WRAPPER FUNCTION ko return krta he iska kam ye he ke hm apni class ya func kisi bhi kam ke oper or nichy koch print krwana chahty hen to hm isy decorator function ka use kr krty hen bina os func ko chery 


# @decorator_function
# def greet():
#     print("Hello, how are you?")
    
#     # jesy ismy bs ak sms he lekin osky oper meny decorate ke use kiya he to os function me jo koch he osy phly decorater wala kam chalyga
    
# greet()    
# ********Generator Function********
# generator function ye krta he ke hm return ke bad koch or nhikam kr skty lekin generatorisko posible bnata he
# yield lgata he ye return ki jga pr or vriable ko hm next ke ander likhty hen print krty waqt
# def generator_function():
#     yield "Hello"
#     yield "World"

# generator = generator_function()
# print(next(generator)) # ye helo ko print krta he
# print(next(generator)) # ye world ko print krta he


# ********************************************

# 1. @property, @property.setter, @property.deleter Decorators:
# @property: Yeh decorator ek method ko getter bana deta hai. Iska matlab hai ki aap method ko attribute ki tarah access kar sakte hain.

# Example: product.price ko method ke tarah access kar sakte hain, jaise wo ek regular attribute ho.

# @price.setter: Yeh decorator method ko setter bana deta hai. Jab aap product.price = value likhte hain, to setter method execute hota hai.

# @price.deleter: Yeh decorator deleter method define karta hai, jo del product.price call karne par execute hota hai.

# 2. Custom Exception (InvalidAgeError):
# InvalidAgeError: Custom exception define kiya gaya hai jo age validation ke liye use hota hai. Agar age invalid ho (e.g., age < 18), to InvalidAgeError raise hota hai.

# try...except block ka use karke exception handle karte hain.

# 3. __iter__() and __next__() Methods (Making a Class Iterable):
# __iter__(): Is method ko implement kar ke object ko iterable bana dete hain. __iter__() method ke zariye object ko starting point se initialize karte hain.

# __next__(): Is method ko implement kar ke object ke next value ko return karte hain jab next() call kiya jata hai. Jab iteration complete ho jati hai, to StopIteration exception raise karte hain.

# self ko __iter__() mein return karna: Jab aap self ko __iter__() mein return karte hain, to aap apne object ko iterator object bana dete hain. Python ko pata chal jata hai ki is object mein __next__() method hai.

# 4. __call__() Method:
# __call__() method ka use object ko function ki tarah call karne ke liye kiya jata hai.

# Jab aap object ko object() ki tarah call karte hain, to __call__() method execute hota hai.

# Example: multiply_by_2(5) object ko function ki tarah call kiya jata hai aur __call__() method execute hota hai.

# 5. Aggregation and Composition:
# Aggregation: Ek class doosri class ka reference rakhti hai, lekin dono objects independently exist karte hain.

# Example: University class ka object Student class ka reference rakhta hai, lekin agar University ka object delete ho jaye, to Student ka object unaffected rehta hai.

# Composition: Ek class doosri class ka object apne andar rakhti hai, aur dono objects tightly coupled hote hain. Agar parent object delete ho jata hai, to child object bhi delete hota hai.

# __call__(): Is method ko implement karne se object ko function ki tarah call kiya ja sakta hai.

# 7. Method Resolution Order (MRO) and Inheritance:
# MRO: Python method resolution order (MRO) ko follow karta hai jab multiple inheritance hoti hai. Jab aap mro() call karte hain, to Python classes ke inheritance hierarchy ko follow karta hai.

# Example: Class D inherits from Class B and Class C, to MRO se yeh decide hota hai ki method kis class se call hoga.


# *****************************************

# CLASS METHOD 
# class Product:
#     age=0
#     def __init__(self, price, name):
#         self.price = price
        
#     @classmethod    
#     def greet(cls):
#         print("Hello, my name is", cls.name)
        
# Product.name # YE ACEESS NHI HOGA kioky bina instance ke hm kisi atrinute ko acces nhi kr skty 
# Product.age # ye acces ho jayga kioky ye he clss ko attribute yhi class variable bhi khlata he  he isi trha ak hota he class method lekin mehod to sb class me hi hoy hen lekin 
            #  osko class method hm bnaty hen or wo hm bnaty hen @classmethod decorator ko use krky wrna nhi bnta wo or self ki jha
            # cls lgaty hen atributes me
            
            # lekin ye class ki chizen instance ke sath bhi hm aceess  kr skty hen 
# Product.greet()

# withinstance=Product(100,"Rohan")
# withinstance.greet()      # ye intance method khlayga ab 

# *****************************************

# STATIC METHOD 
# class StaticMethod:
    

        
#     @staticmethod    
#     def HELLO(a,b):
#         print("i am static",a+b)
        
#         #ye hmy class ke name ke sath bhi acees hoga or instance ke sath bhi lekin ismy cls wagera ka koi kam ni he oe na hi ye self lega
#         instnce=StaticMethod()
#         instnce.HELLO(10,20)        
         
# # *****************************************

# def decorator_function(cls):
#     def greet(self):
#         return "hello "+self.name
#     cls.greet=greet
#     return cls
    
# @decorator_function  
# class Person:
#     def __init__(self,name):
#         self.name=name
        
# taha=Person("taha")
# taha.greet()

# decorater hm jisky oper bhi ayga decorater ki chizen osky ander a jaygi jesy greet ka functionnhi tha cllass me lekin a gya wo


# *****************************************
# oop ak paradigm he jo ke object object wise kam krty hen

# mro
# class Father():
#     def __init__(self):
#         print("father")
        
        
# class Mother():
#     def __init__(self):
#         print("Mother")
# class child(Father,Mother):
#     def __init__(self):
#         self.name="child"


# print(child.mro())
# ye squence btata he order btata he ke sbsy phly to ans me child ayga phir wo class aygi jo phly inherite  hogi 
# or agr same method ya variable ho dono class me or child pr na ho to bhi child ke pas to a jayga or hm acees krengy child sy
# to wo os class ka othayga jo phly inherite hoi hogi 
# or agr child me bhi wahi ho towo to overwirde ho jayga 



# *****************************************

# CALLABLE
# class A():
#     def __init__(self):
#         print("A")
        
#     def __call__(self):
#         pass    
    
#     def __str__(self):
#         return "i am not callable  instance but i am without callable instance"
        
# instancee=A()
# print(instancee())
# print(instancee)
# hm instance ko call nhi kr skty lekin hm __call__ lga kr bnygy koi function to instace ko call krny sy wo call ho jayga ak trha sy instace callable bn gya  

# or hm agr instance ko chalaygy nhi () sy direct print krwaygy to wo weeor dega ak number dedega to osko bhi hm handle krty hen str sy to phir wo str 
# ko chalayga str ko error ki jga bina call kiye  

# *****************************************

# class Newfirst():
#     def __new__(cls):
#         print("first")
#         return super().__new__(cls)
#     def __init__(self):
#         print("second")
      
    #   def __del__(self):
    #       print("third")
# # ismy ye he ke he lekintance jesy hi bnaty hen init khod chal jata  he lekin osy bhi phky backend pr new run hota he or wo super ki madad sy init ko de deta he wrna init nh chlyga 
# # isi liye hm agr new likhengy to sbsy phly new hi chlyga 
# or hm nhi likhty to wo ander ander chlara hota he 
# isi trha del jb chalyga tb hm kisi object yani intance bna kr osko delet krdengy jesy

# isinstance=Newfirst()
# del isinstance



# instances=Newfirst()
# # phly print hoga first

# *****************************************
# Composition and Aggregation

# Composition
# iska matlb hota he strong relation bnana 
class Person():
    def __init__(self):
     self.name="faiza"   
    def info(self):
        return f"hello my name is {self.name}"
    
    
class Address():
    def __init__(self):
        self.street=Person()
        # yha hmny person ko hi pass kr diya
        
c=Address()
c.street.info() 
# yaha pr address class ka object bnaya he or usme person class ka function call kiya he or wo chlyga bhi ye ak strong relation he 

class Week:
    def __init__(self, day):
        self.day = day

    def __repr__(self):
        return f"Week(day={self.day})"

class Month:
    def __init__(self, weeks=None):
        # weeks ko list expected kar rahe hain, default None
        if weeks is None:
            self.weeks = []
        else:
            self.weeks = weeks

    def __repr__(self):
        return f"Month(weeks={self.weeks})"

# Week objects independently create karo
wee1 = Week("Monday")
wee2 = Week("Tuesday")

# Month ko weeks pass karo - aggregation relation
mon = Month([wee1, wee2])
# ye ak week relationship he yani ke hmny isko diya to he argument lekin agr hm na bhi den towo sahi chlyga errro nhi dega kioy by default hmny osko none rkha he 
# to week he yani dependent nhi he wo dosri class pr agr dosri class kabhi delet ho jati he to ospr koi effect nhi hoga wo phir bhi chal jayga 

print(mon)
print(wee1)

# 

# *****************************************

# incapsulation
# hm geter fuction ke oper likhengy @property private variable ko access krNT KE LIEY

# OR SETER KE OPER @private_variable_name.setter ko likhengy private variable ko modify krNT KE LIEY


# or del krny ke liye @private_variable_name.deleter ko likhengy or class ke bahir
# delinstance.private_variable

# *****************************************

# object/instance bnta he class sy or class bnta he ceate hota he meta/TYPE class sy


