name=["rishabh","anil","chetna","pammy","urvesh"]
"""print(name)
print(type(name))
print(name[1:4])
name[0]="raghav" #changing item threw index value
print(name)"""

"""
number=[100,32,70,20,101,201,77,7,1111]
print(number)

max=number[0]
for i in number:
    if max<i:
        max=i
print(f"MAXIMUM IS :{max}") 
"""

#2d LIst
#matrix 
"""
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0][1]=20
print(matrix[0][1])
print(matrix[2][2])
matrix[0][1]+=1
print(matrix[0][1])
print(matrix,"\n")


#only row check
for row in matrix:
    print(row)

print("\n")
#threw this we go on every single element
for row in matrix:
    for i in row:
        print(i)
"""
#list method
"""
number =[10,25,23,43,23,1]
number.append(40)#number is added at last
print(number)
number.insert(1,24)#can insert at any place by chosing index
print(number)
number.remove(10)
print(number)
#number.clear()#whole list would be clear [empty]
#print(number)
number.pop()#remove list item from end
print(number)

print(number.index(25)) #show the index number of element
print(number)

print(23 in number)#given boolean value
print(number.count(23))#count the numbers repeated

print(number.sort())  #NONE MEANS ABSENCE OF VALUE
number.sort()
print(number)

#for descinding order
number.sort()
number.reverse()
print(number)

#copy of list
number1=number.copy()
number.append(26)
print("OLD LIST",number)
print("Copy of list",number1)

"""
#pratice program

list=[23,63,23,78,10,89]
unique=[]
for number in list:
    if number not in unique:
        unique.append(number)
print(unique)
"""
"""
l=[23,23,22,12,21,23,45,34]
isr=[]
for i in l:
    if i not in isr:
        isr.append(i)
print(isr)