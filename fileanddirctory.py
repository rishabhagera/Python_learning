#file and dirctory

from pathlib import Path

# 2 way to give Path

# Absolute path 
# c:\prrogram file \microsoft
#     /user/local/bin

# relative path --- ecommerce access


#path = Path("ecommerce")
#print(path.exists()) #give boolean value

#create new dictionary if dosnt exists then
#path = Path("email") 
#print(path.mkdir())#none doesnt return any value

#print(path.rmdir())#none doesnt return any value

path = Path()
#print(path.glob("*.py"))#xml
#print(path.glob("*.*"))
for file in path.glob("*"):
    print(file)
    
    