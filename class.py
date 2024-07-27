#class  ae used to define new type
#class is used to model new concept from real world
#class definne blue print or template for creating object


# we dont use [space] or [underscore] we capitalize the letter
""""
class Point:   #first word capitl piscal naming convention
    def move(self):  #self parameter should be added   
        print("move")
    def draw(self): #self parameter should be added
        print("draw")
    
    
#object is instance of class     

#threw object we can define class multiple times
p=Point() #defining a object 
p.draw()  #calling from class


#creating attributes

#attributes are like they belong to an object
#attributes can be placed anywhere in the program

point1=Point()
point1.x=10
point1.y=20
print(point1.x)
 """    
     
#construction
"""
class Point1:  
    #this method is a definaion of constructor or to crate an object
    def __init__(self, x, y):  #inti maens initlaization 
         self.x=x       #self is a referance to current object
         self.y=y  
    def move(self): 
        print("move")
    def draw(self): 
        print("draw")
        

point=Point1(100,200)
#changing value of X
point.x=11
print(point.x)
"""

class Person:
    def __init__(self,name):#constructor
       self.name=name
    def talk(self):
        print(f"Hi, i am {self.name}")
    
    
p123=Person("rishabh")
p123.talk()
    
pammy=Person("pammy")
pammy.talk()