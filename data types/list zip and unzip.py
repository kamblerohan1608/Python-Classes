
# list zip and unzip

# ls1 = [12,"Vipul","Kalyan"]
# ls2 = [55,"Rohan","Thane"]
# ls3 = [65,"Sagar","Kurla"]
# ls4 = [89,"Ramesh","Vashi"]

# zipping

# student = list(zip(ls1,ls2,ls3,ls4))
# print(student)

# unzipping

student1 = [(12, 55, 65, 89), ('Vipul', 'Rohan', 'Sagar', 'Ramesh'), ('Kalyan', 'Thane', 'Kurla', 'Vashi')]

# to see no of columns

print(len(student1))

#to see no of rows

stu = len(student1[0])
print(stu)


# to unzip the data

a,b,c,d = zip(* student1)
print(a)
print(b)
print(c)
print(d)