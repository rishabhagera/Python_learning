#inheritance means re using the code again and again

#dont repeat your self
"""
dog walk()
cat walk()
this is not good
"""

class Animal:       #parent class
    def walk(self):
        print("Walk")


class Dog(Animal):
   # pass       #this means nothing you can pass this line
    def bark(self):
        print("bark")
     
class Cat(Animal):
    #pass
    def Meow(self):
        print("meow")

dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.Meow()
cat1.walk()