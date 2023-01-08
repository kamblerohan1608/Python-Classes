
# for loop

# Example 1

#exexute name 10 times

'''
#example 1
for i in range(1,11,+1):
    print(i)

# example 2

for i1 in range(10,0,-1):
    print(i1)
    

#example 3

for i in range(1,10):
    print(i)    #if third parameter is not passed by default it takes +1

# exapmle 4

for i in range(10):
    print(i)             # if only one parameter is given system takes it as the ending position parameter

# example

a=int(input("Enter the itteration value : "))

for i in range(1,a+1):
    print(i)
# example 2 take input from user and execute the loop user input to 1


a=int(input("Enter the itteration value : "))

for i in range(a,0,-1):
    print(i)
'''
# calculate table 
'''
a=int(input("Enter the number : "))
for i in range(1,11):
    table=a*i
    print(table)
'''
# itteration using list
'''
a=["Rohan","sameer","Kiran"]
for i in a:
    print(i)


a=[1,2,3,4,5,6]
for i in a:
    print(i)
'''

#itteration using string
'''
a="abcdefg"

for i in a:
    print(i)
'''

#calculate the sum of a list
'''
ls=[5,7,9,11,13,15,17,19]    
s=0
for i in ls:
    s=s+i
print("The sum of the list is : " + str(s))
'''

#take user input and in each itteraton and print your name at last
'''
a=int(input("Enter the no of letters in your name : "))
name=""
for i in range(1,a+1):
    n=input("Enter letter of your name : ")
    name = name+n
print(name)
'''
#calculate the factorial of a number

a=int(input("Enter the number : "))
fact=1
for i in range(a,0,-1):
    fact=fact*i
print(fact)



















