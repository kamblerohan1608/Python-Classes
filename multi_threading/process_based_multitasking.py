
#Process based multi tasking

# 1 . function based:

import multiprocessing as pc

def cube(num):
    for i in num:
        print(f"Cube is {i**3}")
def square(num):
    for i in num:
        print(f"square is {i**2}")

num = [1,2,3,4,5]

p1 = pc.Process(target = cube, args = (num,))
p2 = pc.Process(target = square, args = (num,))

p1.start()
p2.start()

p1.join()
p2.join()

# 2 . class based:

class math:
    def cube(num):
        for i in num:
            print(f"Cube is {i**3}")
    def square(num):
        for i in num:
            print(f"square is {i**2}")

num = [1,2,3,4,5]

p1 = pc.Process(target = math.cube, args = (num,))
p2 = pc.Process(target = math.square, args = (num,))

p1.start()
p2.start()

p1.join()
p2.join()
