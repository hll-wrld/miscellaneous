from threading import Thread
from time import sleep


# sleeps for 5 secs
def task():

    sleep(5)



# thread method 1
thread_method1 = Thread(target=task)
thread_method1.start()

# thread method 2
Thread(target=task).start()


print("### here ###")

