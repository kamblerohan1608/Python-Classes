#
'''
* * * * * *
*         *
*         *
*         *
*         *
* * * * * *

n=7
for row in range(1,n):
    for col in range(1,n):
        if (row == 1) or (row == n-1) or (col == 1) or (col == n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

#
'''
n=7
for row in range(1,n):
    for col in range(1,n):
        if (row==n-1) or (col==1) or(row==col):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''

#
'''
for row in range(0,6):
    for col in range(0,11):
        if (row==5) or(row+col==5) or (col-row==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
'''
#
'''
n=7
for row in range(n):
    for col in range(n):
        if(row==0)or(row==n-1)or(col==0)or(col==n-1):
            print("*",end=" ")
        elif (row==3)and(col>1)and(col<5):
            print("*",end=" ")
        elif (col==3)and(col>1)and(col<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
    '''
#
'''
n=12
for row in range(1,12):
    for col in range(1,12):
        if (row+col==7) or (col-row==5) or (row-col==5) or (row+col==17):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
'''
#

for row in range(11):
    for col in range(8):
        if (row==0) and (col<5):
            print("*",end=" ")
        elif (col==1):
            print("*",end=" ")
        elif (row==1) and (col==5) or ((row==2) and (col==6)):
            print("*",end=" ")
        elif (col==6) and (row>2) and(row<5):
            print("*",end="")
        elif ((row==5) and (col==5)) or ((row==6) and (col==4)):
              print("*",end=" ")
        elif (row==6) and (col>0) and (col<4):
            print("*",end=" ")
        elif ((row==7) and (col==2)) or((row==8) and (col==3)) or((row==9) and (col==4)) or (row==10) and (col==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )

#
'''
n=5
for row in range(5):
    for col in range(5):
        print("*",end=" ")
    print()
''' 
