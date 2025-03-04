************OOP (Object-Oriented Programming) Kya Hota Hai?**************

🔥 Step 1: Object-Oriented Programming (OOP) Kya Hai?
OOP ek programming paradigm hai jo real-world objects ko represent karne ke liye use hoti hai. Iska purpose code ko reuse, maintainable, aur organized rakhna hota hai.

OOP ke 4 Pillars (Maha Important Concepts)
Encapsulation
Inheritance
Polymorphism
Abstraction

****************//**********************

📌 Step 2: Encapsulation (Data Ko Chhupana)
Definition:
Encapsulation ka matlab hai data aur functions ko ek saath bundle karna aur unnecessary access ko restrict karna. Iska main purpose security aur data hiding hai.

Example (Encapsulation)
python

class BankAccount:
def **init**(self, account_number, balance):
self.account_number = account_number # Public attribute
self.**balance = balance # Private attribute (double underscore **)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.__balance  # Private attribute ko access karne ka method

# Object bana rahe hain

account1 = BankAccount("12345", 5000)

# Public method call kar sakte hain

account1.deposit(1000) # Deposited 1000. New Balance: 6000

# Private attribute ko direct access nahi kar sakte

# print(account1.__balance) ❌ ERROR: AttributeError

# Private data ko method ke through access kar sakte hain

print(account1.get_balance()) # ✅ Output: 6000
Encapsulation ka Benefit:
🔹 Private data (__balance) ko direct access nahi kar sakte, sirf defined methods se hi update ya access kar sakte hain.
🔹 Isse security aur data integrity ensure hoti hai.

****************//**********************

📌 Step 3: Inheritance (Ek Class Se Dusri Class Banana)
Definition:
Inheritance ka matlab ek class doosri class ki properties aur methods ko inherit karti hai, yani reusability badhti hai.

Example (Inheritance)
python


# Parent Class

class Animal:
def **init**(self, name):
self.name = name

    def make_sound(self):
        return "Some sound"

# Child Class (Jo Animal se inherit ho rahi hai)

class Dog(Animal):
def make_sound(self): # Method override kar diya
return "Bark!"

# Objects

dog1 = Dog("Buddy")
print(dog1.name) # ✅ Output: Buddy
print(dog1.make_sound()) # ✅ Output: Bark!
Types of Inheritance:
Single Inheritance: Ek class sirf ek parent se inherit kare
Multiple Inheritance: Ek class multiple parents se inherit kare
Multilevel Inheritance: Ek class, ek aur class se inherit kare jo already ek aur class se inherit ho chuki ho
Hierarchical Inheritance: Ek parent class se multiple child classes banayen
Hybrid Inheritance: Inheritance ka combination ho
Example (Multilevel Inheritance)
python

class Animal:
def eat(self):
print("I can eat")

class Dog(Animal): # Dog, Animal se inherit kar raha hai
def bark(self):
print("I can bark")

class Puppy(Dog): # Puppy, Dog se inherit kar raha hai
def weep(self):
print("I can weep")

puppy = Puppy()
puppy.eat() # ✅ Output: I can eat
puppy.bark() # ✅ Output: I can bark
puppy.weep() # ✅ Output: I can weep

****************//**********************

📌 Step 4: Polymorphism (Ek Method, Multiple Forms)
Definition:
Polymorphism ka matlab hai ek hi function ya method different classes me different tarikon se behave kar sakta hai.

Example (Method Overriding)
python

class Bird:
def make_sound(self):
return "Some generic sound"

class Sparrow(Bird):
def make_sound(self):
return "Chirp Chirp"

class Crow(Bird):
def make_sound(self):
return "Caw Caw"

birds = [Sparrow(), Crow(), Bird()]

for bird in birds:
print(bird.make_sound())

# ✅ Output:

# Chirp Chirp

# Caw Caw

# Some generic sound

🔹 make_sound() method har class me alag tarike se behave kar raha hai.

****************//**********************

📌 Step 5: Abstraction (Sirf Zaroori Details Show Karna)
Definition:
Abstraction ka matlab hai unimportant details hide karna aur sirf important functionalities show karna.

Example (Abstraction using ABC - Abstract Base Class)
python

from abc import ABC, abstractmethod

class Vehicle(ABC): # Abstract class
@abstractmethod
def start_engine(self):
pass

class Car(Vehicle):
def start_engine(self):
print("Car engine started")

class Bike(Vehicle):
def start_engine(self):
print("Bike engine started")

car = Car()
bike = Bike()

car.start_engine() # ✅ Output: Car engine started
bike.start_engine() # ✅ Output: Bike engine started
🔹 Abstract class ka direct object nahi banta, sirf derived classes isko implement kar sakti hain.

🔹 Recap: Abstraction Method Ka Matlab
Jo zaroori methods hain, sirf unko define karna (jaise start() aur stop())

Lekin unko implement nahi karna, sirf blueprint dena

Abstract class (ABC) ko use karke ensure karna ke koi bhi subclass agar isko inherit kare, to wo unko zaroor implement kare

Subclass me hum asli functionality likhenge (matlab start() aur stop() ka actual kaam wahan likha jayega)

****************//**********************

📌 Step 6: Access Modifiers (Public, Private, Protected)
Modifier Syntax Access Allowed
Public self.name Class + Subclass + Object
Protected self._name Class + Subclass
Private self.**name Class ke andar
Example (Access Modifiers)
python

class Person:
def **init**(self, name, age, salary):
self.name = name # Public
self._age = age # Protected
self.**salary = salary # Private

person1 = Person("Ali", 25, 50000)
print(person1.name) # ✅ Public: Accessible
print(person1._age) # ✅ Protected: Accessible but not recommended

# print(person1.__salary) ❌ Private: Error

🔹 Private (__) ko direct access nahi kar sakte, Protected (_) subclass use kar sakta hai.

🎯 Conclusion:
Encapsulation: Data ko hide karna
Inheritance: Ek class doosri se properties inherit kare
Polymorphism: Ek method different tarikon se behave kare
Abstraction: Sirf zaroori functionalities expose karna
Access Modifiers: Data ko public, protected ya private karna

****************//**********************

Class:
Ek blueprint ya template hoti hai jisme hum object ki properties aur behaviors define karte hain. Isme hum methods ke zariye object ki properties aur behaviors ko control karte hain. Ye ek object (dictionary) ki tarah hoti hai, jese hum ek object me functions, variables, properties waghera likh sakte hain.

Object:
Class ka ek real-world instance hota hai.

Attributes (Properties):
Object ki characteristics hoti hain (jaise: naam, age, color).

Methods (Behaviors):
Functions hote hain jo object ke actions ko define karte hain.

Constructor Function:
Agar hume dynamic properties banani hoon, toh hum constructor function ka use karte hain. Jaise hum normal functions me parameters dete hain aur arguments ke zariye unki values change karte hain, waise hi constructor function ka use kar ke class ke andar properties ko dynamic banate hain.
Python me ise def **init** se likha jata hai.

self:
self ka use har method aur constructor function me zaroori hota hai. Iske zariye hum object ki properties aur methods ko access aur modify kar sakte hain.

Access Modifiers:
Public:
Public properties aur methods ko direct access kar sakte hain.
Ye inherited class me bhi use ho sakti hain.

Private (__)
Private properties ko direct access nahi kar sakte.
Ye subclass me use nahi hoti, lekin ek method bana kar return karwa ke access ki ja sakti hain.

Protected (_)
Protected properties ko direct access kar sakte hain, lekin ye subfunctions me use nahi hoti.
Class ko Kaise Use Karte Hain?
Pehle class ka ek object (instance) ek variable me store karte hain.
Phir us variable ke through dot (.) operator laga kar uske methods aur properties ko access karte hain.


