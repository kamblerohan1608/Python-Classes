
# List datatype

# # Two ways to define a list

# 1.

# a=[]
# print(type(a))

# # 2.

# a1 = list()
# print(type(a1))



# # Adding element into list



# 1. append() :                     adds element at end position of list            

# ls = []

# name = "Rohan"
# age = 22
# location = "Vashi"

# ls.append(name)
# print(ls)
# ls.append(age)
# print(ls)
# ls.append(location)
# print(ls)

# 2. insert() :                    It adds data at specific position
#                                  it takes 2 arguments ( position,data ) 

# ls = ["Rohan",22,"vashi"]
# print(ls)
# ls.insert(0,"Developer")
# print(ls)

# 3. extend()                      adding multiple data in a list
#                                  take 1 argument in form of a collection

# ls = ["Rohan","vaibhav",32]

# ls1 = ["suraj","rakesh",22]

# ls.extend(ls1)
# print(ls)



# # access  data in the list

# list follow index positioning system

# forward positioning
#        from left to right (0,1,2,3)

# reverse positioning
#        from right to left (-4,-3,-2,-1)

# accessing single data :

ls = ["rohan","sagar",2211,"Kishor","suman","ramesh"]

# forward index

name = ls[3]
print(name)

# reverse index

name = ls[-2]
print(name)

# acessing multiple data / list slicing :

# in index position it will always -1 from the last position

#  forward index

ls1 = ls[0:4]
print(ls1)

ls2 = ls[:4]
print(ls2)

ls3 = ls[3:]
print(ls3)

#  reverse index

ls1 = ls[-5:-1]            # for going till -2 have to write -1 as system do -1 by default
print(ls1)

ls2 = ls[-5:]
print(ls2)

ls3 = ls[:-4]
print(ls3)