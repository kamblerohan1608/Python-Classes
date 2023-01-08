
#Nested for loop
'''

#program for pattern

* * * * *
* * * *
* * *
* *
*



#static

for i in range(6,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print( )
    
#dynamic

a=int(input("Enter the number : "))    
for i in range(0,a+1):
    for j in range(0,i):
        print("*",end=" ")
    print( )
'''
* * * * *
  * * * *
    * * *
      * *
        *

n=5
for row in range(n,0,-1):
    for col in range(0,n-row):
        print(" ",end=" ")
    for col2 in range(0,row):
        print("*",end=" ")
    print()




