#loop are used to do a task multiple time
#range create object 


"""
for item in range(10):
    print(item,"\n")

for item in range(5,10):
    print(item)
"""    
# 2 is step 
"""
for item in range(1,10,2):
    print(item)
"""
#sum and Axis Find
"""
sum=0
price=[10,20,30]
for i in price:
    sum=sum+i
print(f"Total :{sum}")

for X in range(4):
    for Y in range(3):
        print(f"{X},{Y}")
"""

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




"""
list=[5,2,5,2,2]
for i in list:
    output=""
    for count in range(i):
        output+="X"
    print(output)
    
lis=[1,1,1,4]
for i in lis:
    out=""
    for count in range(i):
        out+="X"
    print(out)
    
    
for i in range(5,-1,-1):
        print(i*"$")
print(i.reverse())
"""


"""
    1 2 3 4 
    5 6 7 
    8 9 
    10

patten=[[1,2,3,4],[5,6,7],[8,9],[10]]
for i in patten:
    out=""
    for count in i:
        out+=str(i)+" "
    print(out)
    # print(out.split())
"""
"""
patten=[[1,2,3,4],[5,6,7],[8,9],[10]]
#print(patten)  
for i in patten:
    output=""
    for count in range(len(i)):
        output+="X"
    print(output)    

XXXX
XXX
XX
X
"""

#loop 
"""
1
22
333
4444
55555

"""
i=1
j=1
for i in range(5):
    for j in range(i):
        print(j*i," ")
    print("\n")
    #  output=" "
    # for j in range(i):
    #     output=(str(j) + " ")
    # print(output) 
        
