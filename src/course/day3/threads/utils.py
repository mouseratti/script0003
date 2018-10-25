import threading
from  time import  sleep

def threaded(f):
    def wrapper(*args, **kwargs):
        t = threading.Thread(
            target=f,
            args=args,
            kwargs=kwargs,
)
        t.start()
        return t
    return wrapper



@threaded
def func1():
    while True:
        print("imalive!!!!")
        sleep(3)
        print(threading.enumerate())


if __name__ == '__main__':
    result = func1()
    print("result is {} {}".format(type(result), result))
    counter = 1
    while counter:
        sleep(3)
        print(result)
        counter -=1