
# a+ mode    append + write 

with open("test.txt","a+") as file :
    d = input("Enter the data : ")
    file.write(d+'\n')
    file.seek(0)
    data = file.read()
    print(data)


