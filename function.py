#manage our code in chuncks
#reuse code
#organize our code

#function is a  container which perform a specific task

#parameters are  place holder which take value from argunment (variable)
#argunment are peace of information which we are pacing whn we  are calling function


"""
def greet_user():
    print("hello")
    print("welcome")


print("start")
greet_user()
print("finish")
"""

#with parameters
"""
def greet_user(fname,lname):#name is parameter
    print(f"hello {fname} {lname} !")
    print("welcome")


print("start")
#position argunmnet
greet_user("rishabh","upadhyay")#rishabh is a argunment
greet_user("upadhyay","rishabh")#upadhyay is a argunment
                    #we can call function multiple times

#we should always pass all argunmnets whicg are required to run function otherwise it would show error

#keyword arrgunment
greet_user(lname="Upadhyay",fname="Rishabh")
print("finish")

#first position argunment after that keyword argunmnet
greet_user("yeeeeeee",lname="Rishabh")
#first always should be position in function also
"""

#return values

#by default python function return NONE
"""
def Square(number):
    return number*number 

result=Square(10)
print(result)

"""

#function in emoji code
"""
def emg(message,emojie):
    word=message.split(" ")
    output=""
    for i in word:
        output+=emojie.get(i,i)+" " 
    print(output)


emojie={
":)":"😊",
"p":"✌"
}
message=input(">")
emg(message,emojie)

"""

#by another way

"""
def emg(message):
    emojie={
        ":)":"😊",
        "p":"✌"
        }
    word=message.split(" ")
    output=""
    for i in word:
        output+=emojie.get(i,i)+" " 
    return output


message=input(">")
result=emg(message)
print(result)
"""


def emoji(messagee):
    emojie={"happy":"😊","good":"👍"}
    word=messagee.split(" ")
    
    output=""
    for i in word:
        output+=emojie.get(i,i)+" "  
    return output


messagee=input(">")
result=emoji(messagee)
print(result)


