
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