# # some additional list methods

# # 1 - copy()

# ls = ["rohan","shubham","kedar","suman"]
# ls1 = ls.copy()
# print(ls)
# print(ls1)

# # 2 - index()

# ls = ["rohan","shubham","kedar","suman"]

# ls1 = ls.index("kedar")
# print(ls1)

# # 3 - count()

# ls = ["rohan","shubham","kedar","suman","rohan","shubham","kedar","suman","kedar","suman"]

# ls1 = ls.count("suman")
# print(ls1)

# # 4 - sort()

# ls = ["rohan","shubham","kedar","suman","a","b","c","d"]
# ls1 = ls.sort()
# print(ls)

# ls= ls.sort(reverse = True)
# print(ls)

# # 5 - clear()

# ls = ["rohan","shubham","kedar","suman"]

# ls.clear()
# print(ls)

# problem 1

# ls = [1,2,-3,-5,7,-5,8,-9,10,-17]
# print(ls)

# pos = []
# neg = []

# for i in ls:
#     if i < 0:
#         neg.append(i)
#     else :
#         pos.append(i)

# print(pos)
# print(neg)

# problem 2

# ls = [1,2,3,5,4,7,8,6,56,42,66,15,23]
# print(ls)

# odd = []
# eve = []

# for i in ls:
#     if i%2 == 0:
#         eve.append(i)
#     else :
#         odd.append(i)

# print(eve)
# print(odd)

# # comprihension : 

# 1. reversing a list :

ls = ["a","b","c","d","e"]
ls1 = [ls[i] for i in range (len(ls)-1,-1,-1) ]
print(ls1)

# 2. positive negative : 

ls = [1,-9,6,-8,6,-7,55,-46,-87,22,54]
pos = [i for i in ls if i > 0]
neg = [i for i in ls if i < 0]
print(pos)
print(neg)

# 3.even odd 

ls = [1,56,47,5,65,4,69,75,26,45,14]
even = [i for i in ls if i%2 == 0]
print(even)
odd = [i for i in ls if i%2 != 0]
print(odd)

# pos negative together

# filter (function,itterable data)
#           filters the data according to the function 

ls = [1,-9,6,-8,6,-7,55,-46,-87,22,54,45,14]
neg=[]
pos=[i if i > 0 else neg.append(i) for i in ls]
print(pos)
print(neg)

def fil(data):
    return data != None

pos1 = list(filter(fil,pos))
print(pos1)

# filter 