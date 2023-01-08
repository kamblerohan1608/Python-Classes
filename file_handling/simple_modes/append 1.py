
# a mode : (append)

# It will create a file if not existing.
# If file already exists it will write data at the end of the file

with open("test4.txt","a") as file:
    data = input("Enter the data : ")
    file.write(data+'\n')
