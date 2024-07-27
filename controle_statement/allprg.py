def sum1(num):
    sum=0
    for i in range(num+1):
        sum+=i
    return sum 

def factorial1(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
        if num == 0:
            print("zero dont give factorial !!!!")
    return fact

"""
def SumofN(num):
    sum=num(num+1)/2
    return sum
"""

def Table(num):
    line=1
    for i in range(1,10+1):
        line=i*num
        ans =print(num,"*",i,"=",line)
    return ans


def Prime1(num):
    if num == 0 or num == 1:
        print("not a prime")
    if num == 2:
        print("prime")
    if num%2==0:
        print("Not a prime")
    for i in range(3,num/2):
        if num%i==0:
            print("not a prime ")
        else:
            print("prime")


    
num =int(input("number >"))
# 1
print(sum1(num))
#2
print(factorial1(num))

#3
#print(SumofN(num))

#4
print(Table(num))

#5
print(Prime1(num))