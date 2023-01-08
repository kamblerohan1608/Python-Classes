 # thread based multi tasking

import threading as th

def cube(num):
        for i in num:
                print(f"Cube is {i**3}")
def square(num):
        for i in num:
                print(f"square is {i**2}")

num = [1,2,3,4,5]

p1 = th.Thread(target = cube, args = (num,))
p2 = th.Thread(target = square, args = (num,))

p1.start()
p2.start()

p1.join()
p2.join()

