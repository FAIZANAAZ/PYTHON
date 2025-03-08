#  OOP


# data/attributes
# methods/functions
# manipulation the data
# instance /object
# class

# CLASSS KA name hmesha capital hoga
class Human ():
    
     # isfunc kebina hm class ko use nhi kr skty ye functon khod call ho jata he jb instance create krtyy hen
    #  or ismy jo parameters hoty  hen wo hm class me hi ( ) ke ander arguments dety hen alag sy nhi dety lekin 
    # method ko hm call krty hen name sy osky ander dety hen arguments 

    def __init__(self , name):
        # iska name __init__ hi hoga hmesha init matlb initialize krna class ko 
        # self ismy lganazarori he self apny ander parameters ko chopa leta he osky bina hm parameters ya variable ko nhi likh skty init me 
        # construction class sy lekr ata intence ko data he or instence sy lekr class ko 
        self.name=name
        # HMNY isko dynammic bna diya name assign krkky paameter wla hm normal koi bhi value bhi de sky hen jesy faiza lekin phir wo chnage  nhi ho skta
        
      
   #METHODS
    def speak(self):
        return (f"hello my name is {self.name}")
    # ismy hm kam krty hen logic likhty hen zda tkontruction me diye gy variables ka use krky ye bhi self leta he wrna acces nhi kr skty koch na hi
    # contruction func ko na hi kisi atributes ko class ke 
    
    def walk (self):
        return self.speak() 
    #    yani  method bhi dosry method ko rkhta he lekin self ke ander 
    
# ///*********************instance/object
# class ko call kky use krny ko instance khte he
human=Human("Rohan")
print(human.name)
# is trha human. krky hm name ya method sb call kr skty hen
print(human.walk())

# //// ******************* Inheritance********
# iska matlab ekka class ka use dusry class me krna he

class Student(Human):
     # ismy hm student class ko human class ke inherit kr diya
    # ye methods or class ki sb chizeon ko apny ander laata he
    def __init__(self , name ,age   ):
        
        # hmy agr esa krna he ke ye same contructer ly apny parent ka to hm isko wahi waly parameters dengy or osko bhejengy apny parent ka contructer ko or otny hi dengy jitny parameters apny parent ka contructer me hote hen agr zada hongy toosko hm nhi bhejengy yahi pr rakhengy
       super().__init__(name)
    #    super ke ander hm bhej rhy hen ye lazim he 
    #    yha hoga koch yun ke ye values jaengy parent ke contructer me or phir wo wha sy run hongi 
       self.age=age
   
    def student_info(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self):
        return f"hello my name is {self.name} and i am a student"
    
student  = Student("Rohit",20)
# hlaky student class me to name he hi nhi osko  hm acces kry hen husman class sy 
print("inherited student class",student.name,student.age)


#******** multiple classes inherited

class Teacher(Student,Human):
      def __init__(self , name ,age ,teacher_own):
          Student.__init__(self,name,age)
          Human.__init__(self,name)
        #   hm is trha phonchaygy multiple classes ko inherit krty wy super sy nhi krengy 
          self.teacher_own=teacher_own
      
  
teacher=Teacher("Rohit",20,"Physics")     
print(teacher.name,teacher.age,teacher.teacher_own)
teacher.speak()
#   jb multiple inherited hoti hen classes or osmy same name ke methods hon orhm iskoaa acces krty hen to wo osko leta he jiska name phly hota he yani student sy kioky wo phly sy class Teacher(Student,Human):  ismy agr hm human phly likhengy to wo human wala speak othayga