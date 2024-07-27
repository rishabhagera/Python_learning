#Weight convertor

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

#gusse game

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


        
#patten
"""
XXXXX
XX
XXXXX
XX
XX

"""
"""
for i in range(1):
    for j in range(1):
        print("XXXXX")
    print("XX") 
    for j in range(1):
        print("XXXXX")
    print("XX")
    print("XX")
"""    
"""
list=[5,2,5,2,2]
for i in list:
    print("X"*i)
"""
"""
number=[5,2,5,2,2]
for x_count in number:
    output=""
    for count in range(x_count):
        output+="X" 
    print(output)
"""
"""
*
*
*
****

list=[1,1,1,4]
for i in list:
    count=""
    for l_build in range(i):
        count+="*"
    print(count)
"""

#digit to word


phone=input("phone : ")
digit_map={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "7":"seven",
    "6":"six",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}

output=""
for ch in phone:
    output += digit_map.get(ch,"?")+" "
print(output)


#emojies
message=input(">")
word=message.split(" ")#set boundries betwwen words with space in them
                #split method convert this into list
#print(word)
emojie={
":)":"😊",
"p":"✌"
}
output=""
for i in word:
    output+=emojie.get(i,i)+" "
print(output)