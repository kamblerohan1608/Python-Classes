#number pattern


'''
n=1
for row in range(1,6):
    for col in range(row):
        print(n,end=" ")
        n=n+1
    print()
'''

# print all characters:
'''
for i in range(200):
    print(str(chr(i))+"\t"+str(i))
'''
#print A-Z
'''
for i in range(5):
    for j in range(65,91):
        print(chr(j),end=" ")
    print()
'''
#Break:
'''
for i in range(10):
    if i>=5:
        break
    else:
        print(i) 
'''
#continue
'''
for i in range(10):
    if i==4:
        continue
    else:
        print(i) 
'''

#pass

if(10<5):
    pass
else:
    print("no")









