import random

for i in range(3):
   # print(random.random())
    print(random.randint(10,20))
    
member=["rishabh","chetna","anil","pammy","vinu","vishnu","urvesh"]

leader=random.choice(member)
print(leader)


dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
numb1=random.choice(dice1)
numb2=random.choice(dice2)
print(f"2 dice result :{numb1},{numb2}")


class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second #its take answer as tuple


droll=Dice()
print(droll.roll())