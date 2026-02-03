import threading
import time 

def task(name):
    print(f"{name} strated")
    time.sleep(2)
    print(f"{name} finished")
    
    
t1 = threading.Thread(target=task, args=("Thread A",))
t2 = threading.Thread(target=task, args=("Thread B",))

t1.start()
t2.start()

t1.join()  # join wait until thread ends 
t2.join()

print("All tasks done")
