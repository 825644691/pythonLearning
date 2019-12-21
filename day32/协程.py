import time


def fun1():
    while True:
        print("fun1")
        time.sleep(1)
        print('fun1' + str(time.ctime()))
        yield


def fun2():
    while True:
        print("fun2")
        time.sleep(1)
        print('fun2' + str(time.ctime()))
        yield


if __name__ == "__main__":
    f1 = fun1()
    f2 = fun2()
    while True:
        next(f1)
        next(f2)