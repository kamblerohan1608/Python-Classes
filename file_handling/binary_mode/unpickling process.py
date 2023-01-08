
# unpickling

# conversion of byte stream into python object 

# load : read

import pickle

with open("test.txt","rb") as file:
    data = pickle.load(file)
    data1 = pickle.load(file)

print(data)
print(data1)