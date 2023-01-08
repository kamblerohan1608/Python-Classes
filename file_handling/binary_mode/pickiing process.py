
# pickling

# converson of python objects in to byte stream.

# dump :- write
# load :- read

import pickle

with open("test.txt","wb") as file:
    obj = "Rohan"
    obj1 = "kamble"
    pickle.dump(obj,file)
    pickle.dump(obj1,file)

