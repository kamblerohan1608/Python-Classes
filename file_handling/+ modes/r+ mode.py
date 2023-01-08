
# # Advances modes  :

# 1  r+ mode   :

#Example 1 :

with open("test.txt", "r+") as file:

    data = file.read()
    print(data)

    file.seek(0)

    d = input("Enter data : ")
    file.write(d)

# Example 2 :

with open("test.txt", "r+") as file:
    file.seek(0)
    d = input("Enter data : ")
    file.write(d)
