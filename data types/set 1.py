
# set

# adding element in set :

# 1. add()  :

# s = set()
# s.add("rohan")
# print(s)

# s.add(23)
# s.add("kurla")
# print(s)

# 2.update()  :

# l=[1,2,3,4]

# s.update(l)
# print(s)

# Q...

# l=[1,2,3,4,5,6,7,8,9]
# s=set()
# s.update(l)
# s1 = set()

# for i in s:
#     s1.add(i**2)
# print(s1)

# comprehension : 

# s2 = {i**2 for i in s}
# print(s2)


# Deleting element :
# s = {1,2,3,4,5,6,7,8,9}
# print(s)

# s.remove(8)
# print(s)

# s.pop()
# print(s)

# s.discard(8)
# print(s)


# accessing elements :

s = {1,2,3,4,5,6,7,8,9}

# s = list(s)
# print(s)

s1 = frozenset(s)
print(s1)

s1 = list(s1)
print(s1)

