
# write :

# w mode creates the file if not existing and overrights the file if already existing.

# ways to use w mode :

# 1. on same path :

# with open("test2.txt","w") as file :
#     data = input("Enter the data : ")
#     file.write(data)

# 2. on different path

# direct mentioning path

# with open("/home/luser/Desktop/zz.txt","w") as file:
#     data = input("Enter the data : ")
#     file.write(data)

# using os 

import os

#print(os.getcwd())

# Changing working directory :

# os.chdir("/home/luser/Desktop")

# print(os.getcwd())

# with open("zzz.txt","w") as file:
#     data = input("Enter the data : ")
#     file.write(data)


# in same path but in a folder 

# with open("txt_files/test3.txt","w") as file:
#     data  = input("Enter the data : ")
#     file.write(data)