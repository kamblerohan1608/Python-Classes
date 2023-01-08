
# w+ mode 

# overrghts file first if existing 
#  creats fle if not existng

# Example 1 :

with open ("test.txt","w+") as file:

    d = input("Enter data : ")
    file.write(d)

    file.seek(5)

    data = file.read()
    print(data)


# Example 2 :

with open ("test.txt","w+") as file:
    file.seek(5)

    data = file.read()
    print(data)
