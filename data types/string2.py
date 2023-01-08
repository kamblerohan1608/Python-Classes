
# Escape sequence / special sequence

# line = "This is \"python\" class"

# print(line)

#\n : new line

# st =("1 - Addition \n2 - Substraction \n3 - Multiplication")

# print(st)

# \t : tab space 

# st =("1 - \tAddition \n2 - \tSubstraction \n3 - \tMultiplication")
# print(st)

## Methods in string class

# 1. replace('old data','new data')    # replaces the word

# st = "Python is a good language. Python is easy to understand"
# print(st)
# print("\n")
# st1 = st.replace("Python","Java")
# print(st1)


# 2. upper()        # returns the upper case data

# st = "python"
# print(st)

# st1 = st.upper()
# print(st1)



# 3. lower()          # returns the lower case data

# st = "PYTHON"
# print(st)

# st1 = st.lower()
# print(st1)




# 4. capitalize()          # return first capital letter

# st = "python"
# print(st)

# st1 = st.capitalize()
# print(st1)



# 5. center()           # adds the no of spaces metoned in it at the start.

# st = "Python"
# print(st)
# st1 = st.center(100)
# print(st1)



# 6. split()          # splits the string and returns list data

# Exapmle 1

# st = "This is python calss"
# print(type(st),st)

# st1 = st.split()
# print(st1)

# Example 2

# st = "This is - python calss"
# print(type(st),st)

# st1 = st.split("-")
# print(type(st1),st1)


# 7. join             # joins a list into string

# ls = ["This","is","Python","lecture"]

# ls2 = ' '.join(ls)
# print(ls2)


# 8. strip            # this deletes the spaces from start and end of a string

# Example 1

# st = "                 Rohan                      "

# st1 = st.strip()
# print(st1)

# Example 2


# a="             rohan              "
# a=a.strip()
# user =  input("Enter the name : ")
# if user == a:
#     print(f"Welcome {user}") 
# else :
#     print("Does not match")


# 9. isdigit  # return boolean value true : if data in string is integer, false : if dats not integer

# st = "123a"

# if st.isdigit():                  #will return true or false value
#     print("digit data")
# else:
#     print("mixed data")



# 10. islower   # return boolean value true : if data is of lower case, false : if data is not of lower case

# st = "pythonH"
# if st.islower():
#     print("data is of lower case")
# else:
#     print("Data is mixed")

# 11. isuper  # returns boolean value true if data is of upper class false if data is not of upper class

# st = "PYTHON"
# if st.isupper():
#     print("data is of upper case")
# else:
#     print("Data is mixed")

st = "rohan"
print(id (st))