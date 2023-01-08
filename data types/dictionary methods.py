
# dictionary methds

# 1. copy()    # copies the dictionary

# d1 = {"name" : "Rohan","age" : 12, "location" : "Thane"}

# d2 = {}

# d2 = d1.copy()

# print(d2)
 
# # 2. clear()           # clears the dictionary

# d1 = {"name" : "Rohan","age" : 12, "location" : "Thane"}

# d1.clear()

# print(d1)



# Q. take below list.
# ls = [2,3,4,5,6,7,8,9,10]
# create a dictionary of output : { 2:8, 3:27 ,4:64.......,10:1000}


ls = [2,3,4,5,6,7,8,9,10]
d1 = {}

# for i in ls:
#     d1.update({i:i**3})
# print(d1)

# comprihension : 

# d1 = {i:i**3 for i in ls}
# print(d1)



# Q.
# ls = ['a','b','c','d','e','f']
# ls1 = [1,2,3,4,5,6]
# output : -  d1 = {a:1,b:2,c:3,d:4,e:5,f:6}


# solution 1 : 

key = ['a','b','c','d','e','f']
value = [1,2,3,4,5,6]
# d1 = {}
# for i in range(5):
#     d1[ls[i]] = ls1[i]
# print(d1)

# comprehansion :

#d2 = {ls[i] : ls1[i] for i in range (0,len(ls))}
#print(d2)

# solution 2 :

# d={}

# z = list(zip(key,value))
# print(z)

# for k,v in z:
#     d[k] = v
# print(d)

# # or in simpler manner 

# d1 = {}
# for k,v in list(zip(key,value)):
#     d1[k] = v
# print(d1)

# comprehension :

d2 = {k:v for k,v in list(zip(key,value))}
print(d2)

