import threading
import time


def security(student):
    print(f"wait{student} where is  your ID! 😡")
    time.sleep(2)
    print(f"{student}ok now you can go !")

t1 = threading.Thread(target=security,args=("summer",)) 
t2 = threading.Thread(target=security,args=("nitin",))

t1.start()
t2.start()

t1.join()
t2.joinn()

print("welcome to hell")
