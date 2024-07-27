"""
is_hot = False
is_cold = False
if is_hot:
    print("its hot")
    print("drink plenty of water")
elif is_cold:
    print("it cold")
    print("wear warm cloths")
else :
    print("its a lovely day") 
    
print("Enjoy your day")
"""
"""
good_credit=True

print("Price of house is $1M")
if good_credit:
    print("You need to put down 10%")
    payment=1000000*10//100
else:
     print("You need to putdown 20%")
     payment=1000000*20//100
    
print(f"DOWN PAYMENT :{payment}")

"""
#logical operator
"""
has_good_incme=True
has_good_credit=True
has_criminal_record=True

#if has_good_incme and has_good_credit:  #both should be true
#    print("Eligible for loan")
#if has_good_incme or has_good_credit:  #one should be true
#    print("Eligible for loan")
if has_good_credit and not has_criminal_record: #AND NOT (Check Boolean value)
    print("Eligible for loan")

else :
    print("Not eligble")
"""

#comparsion Operator
"""
temprature=30
if temprature>30:
    print("its hot")
elif temprature<10:
    print("its cold")
else :
    print("its neither hot nor cold")
"""
"""
print("\tINSTRUCTION\n name should be greater than 3 character and less than 50 character\n")
name=input("Enter your name : ")
length=len(name)
if length<3:
    print("NOT VALID BECAUSE LESS THAN 3 CHARACTER")
elif length>50:
    print("TOO LONG, its should be 50 character only")
else:
    print("name LOOKS good !!!!")
"""

#project weight calculator
"""
weight=int(input("Enter your Weight ? "))
conv=input("what you have enter in weight (L)bs or (k)g :")
if conv.upper() == "L":
    converted = weight *0.45
    print(f"your weight :{converted} in kilogram ")
elif conv.upper() == "K":
    converted =int(weight) //0.45
    print(f"your weight :{converted} in lbs(pound) ")
else :
    print("Enter Between L and K only")
"""

#while Loop

#block of code multiple time
#We need to increment because if we would not increment then code will be [INFINITE LOOP ]
#while loop also have their wo ELSE part
"""
i=1
while i<=5:
    print("*" * i)
    i=i+1
print("thai gayu saheb")
"""
#gusse game
"""
No=5
count=0
count_limit=3
while count<count_limit:
    gusse_no =int(input("Gusse :"))
    count=count+1
    if gusse_no == No:
        print("You Win !!!")
        break
else :  
    print("Wrong choice>> YOU FAILED")
 
"""

#CAR GAME

#true means repeat the task until quit 
command =""
car_started= False
while True:

    command = input("> ").lower()
        
    if command =="help":
        print("""
start - to start the car
stop - to stop the car
quite - to exit
        """)
    elif command =="start":
        if car_started :
           print("car is already started") 
        else:
            car_started = True
            print("car started")
    elif command =="stop":
        if not car_started:
            print("car is already Stoped")
        else:
            print("car stop")
    elif command =="quit":
        print("Exit game")
        break
    else :  
        print("wrong input")




