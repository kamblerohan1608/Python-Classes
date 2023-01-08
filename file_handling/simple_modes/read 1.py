
# reading file :

# read()

file = open("test1.txt","r")
data = file.read()
print(data)

file.close()

# readline()

with open("test1.txt","r") as file :
    data = file.readline()
    print(data)

