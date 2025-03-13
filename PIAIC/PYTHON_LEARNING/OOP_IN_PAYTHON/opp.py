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

class Human:
    species="human"
    def __init__(self):
        self.name=43
       
    @staticmethod        
    def static_method():    
        print("this is static method")
        # ISMY selfnhi hota isiliye hm iske ander static variable ko access kr skty hen jesy self.name=name
        # ye todynamic ho jata he ismy self hi nhi he YE CHANGE NHI HO SKTA 
    
    
  
print(Human.species) # ye result de dega        
# print(Human.name) # ye result nhi de dega
print(Human().name) # ye result de dega
Human.static_method() # ye result de dega

print(dir(Human))
# ye sb koch dikha dega ke kiya kiya hen variables methods sb LEKIN ATRIBUTES NHI DIKHAYGA OSKO DEKHNYKE LIYE HMY INTANCE KO BANA kr print krna hoga instance

human=Human()
print(dir(human))
# ye dikha dega atribues bhi 

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



     
# ********************* call and str method ****************

class Class_call:
    def __init__(self):
        self.name="Rahul"
        self.age=21
        def __str__(self):
            return f"Name: {self.name}, Age: {self.age}"
        def __call__(self):
            print("Hello, my name is", self.name, "and I am", self.age, "years old.")