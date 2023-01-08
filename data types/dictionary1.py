
# Dictionary : 

# built-in, mutable datatype, represented as {} 

# contains two things 1.key   2.value

# school = {"8th" : [25,65,89] , "9th" : (5,68,49) , "10th" : (45,65,98)}

# print(school)

# k = school.keys()
# print(k)

# v = school.values()
# print(v)

# # Adding element in a dictionary

d = {}

# 1.direct
 
# object["key"] = "value"

# language = ("java","python","js")
# d["language"] = language
# print(d)

# 2.update method

# object.update({dict})

# employee = "Rohan"

# d.update({"employee" : employee})
# print(d)

# # Accessing element from dictonary

s = {"8th":(45,65,89),"9th":[4,65,89],"10th":(1,56,58,[45,65,98])}

# 1. direct

data = s["8th"][1]
print(data)

data1 = s["10th"][-1][1]
print(data1)



# 2. get()

data3 = s.get("9th")
print(data3)



# deleting elements from dictionary


# 1. pop()

# 2. popiteam()

# 3. del()

