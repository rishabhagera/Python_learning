#we use dictionary when we want to store datain key and value

#each key should be unique in dictionary cant repeat

customer={
    "name":"rishabh",
    "age":22,
    #"age":40    not allowed in dictionary
    "is_verified":True
}
print(customer)
print(customer["name"])

#print(customer["birthdate"])  # #not present in dictionary so show error
#print(customer["Name"])# name N is capital here


#another method of access

#print(customer.get("name"))
#print(customer.get("birthdate")) #none
print(customer.get("birthdate","june 22 2002"))#define date

#if we use get method its doesnt return and error


customer["birthdate"]="june 22 2002"
print(customer)#birthdate will be added
print(customer["birthdate"])

"""
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
"""

#emojies
message=input(">")
word=message.split(" ")#set boundries betwwen words with space in them
                #split method convert this into list
print(word)















