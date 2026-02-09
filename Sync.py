import threading
import time


seat = True
lock = threading.Lock()


def book(user):
    global seat
    with lock:
        if seat:
            time.sleep(1)
            seat= False
            print(user ,"book the seat !")
        else:
            print(user,"faild to book the seat ")

t1 = threading.Thread(target=book ,args=("ayush",))
t2 = threading.Thread(target=book , args=("unkown123",))
t3=threading.Thread(target=book, args=("unkown2",))

t1.start()
t2.start()
t3.start()