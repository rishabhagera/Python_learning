"""
print("hello")
print(" * " * 10)
"""

#variable
"""
print("\n____________\n")
price =10
#price =20
rating =4.5
name = "Prime"
is_good=True
print("price :",price)
print("rating :",rating)
print("NAME :",name)
print("IS Good",is_good)
print("\n____________\n")
"""
"""
name ="Rishabh"
age = 20
is_new =True

print("Name :",name)
print("Age :",age)
print("IS new pacient :",is_new)

full_name=input("Enter our name ? ")
fav_color =input("Enter FAV color ? ")
print("Hi "+ full_name+" Like "+"favourate color "+fav_color)
"""

#type conversion
"""
birth_year =input("Enter your birth year")
print("birth_date",type(birth_year))
age = 2024 - int(birth_year)
print(" Your Age :",age)  
"""
"""
pound_wg=input("Enter your Weight in pound : ")
kg = 0.45 * int(pound_wg)
print("Your Weight in kilogram : ",kg)
"""

#string

course ="it's my  book"
#print(course)
co1='i am "Rishabh"'
#print(co1)

email_form="""Hy Rishabh,

this is my first email regrding issues

Thank you,
Roy
\n
"""
#print(email_form)


#string Function
"""
course ="Python for Beginners"
#python Index Starts From =>0
print(course[0])
print(course[-1],course[-2])

print(course[0:3])#from 0 to 2 index will not include <3>
print(course[0:])#this will go until end
print(course[1:])#this will go until end

print(course[:5])#will start from 0 till 4 index

another = course[:]#start from 0 till end OR COPY our COURSE STRING 
print(another)

sa="jennifer"
print(sa[1:-1])
"""

"""
name ="Rishabh"
surname="Upadhyay"
print(name+" [ "+surname+" ] " +"is a coder " )
#formated string
msg= f'{name},[{surname}] is a coder'
print(msg)#string formated without using concatination

course ="python for Beginners"
print(len(course))
#this function will not affect the original variable value
print(course.upper())
print(course.lower())
print(course.find('p'))#this will return index value
                        #find function is case sensitive letter should be capital or small case should be seen perfectly
print(course.find("Beginners"))#output 11 Because of index start
print(course.replace("Beginners","Absolute Bginners")) 

print('for'in course) # in function 
print(course.title())#giving title Formate
"""


#arithmatic operation
"""
a=100
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b) #ans in Float
print(a//b) #ans in INTEGER
print(a%b)
a=10
b=3
print(a**b) #10 to power of 3
"""

"""
X = 10+3*2
print(X)

x= (2+3)*10-3
print(x)

"""

#maths function
"""
x=2.6
print(round(x))#round up number 
print(abs(-2.9))# always give positive value

import  math

print(math.ceil(2.9))
print(math.floor(2.9))
"""

"""
weight = int(input("Enter your weight : "))
insert= input(" (l)bs or (K)g")
outcome=insert.upper()
if outcome == "L":
    converted = weight * 0.45
    print("Your weight converted in to KG",converted)
elif outcome == "K":
    converted = weight // 0.45
    print("YOUR WEIGHT CNVERTED IN TO LBS",converted)
else:
    print("Wromg input")
"""

car_started=False

while True:
    game_input=input(">").lower() 
    if game_input =="start":
        if car_started:
            print("car is already started")
        else :
            car_started = True
            print("car started")
    elif game_input =="stop":
        if not car_started  :
            print("car is already stop")
        else:
            car_started= False
            print("car stoped")
    elif game_input =="quit":
        print("Exit game")
        break
    elif game_input =="help":
        print("""
start -to start the car
stop -to stop the car
quit - to exit the game""")
    else:
        print("Wrong Input")
    
    
    
    
    
    
    
    
    
    
    
    
    