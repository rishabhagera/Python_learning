#not to show error dirctly
#error handling '

# [try,except] block

try:
    age=int(input("age : "))
    income=2000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("number cant be divided by zero")
except ValueError:
    print("Invalid value")
    
    
#comments

#single line comment
 




