
# Deamon thread :

# It is used for background apps to run even after closing of the app.



import threading as th

def e1():
    print(f"Deamon thread")
def e2():
    print(f"non Deamon thread")


num = [1,2,3,4,5]
if __name__ == "__main__":

    p1 = th.Thread(target = e1,daemon=True)

    p2 = th.Thread(target = e2)
    p2.setDaemon(True)

    p1.start()
    p2.start()

    print(f"Active threads are {th.active_count()}")
    print(f"Enumerate {th.enumerate()}")
    print(f"Current Thread {th.current_thread()}")


    p1.join()
    p2.join()