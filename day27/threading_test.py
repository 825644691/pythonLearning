import time
import threading
import random

#一个线程就是一个指令机
#IO密集型任务或函数
#计算密集型任务或者函数
#python不能并行，因为cpython解析器有GIL的原因，全局解析器锁
#在同一时刻，只有一个线程进入解析器
#thread.join()阻塞



def foo(n):
    print("foo%s" %n)
    time.sleep(1)

def bar(n):
    print('bar%s' %n)
    time.sleep(2)

# t1 = threading.Thread(target = foo,args = (1,))
# t2 = threading.Thread(target = bar,args = (2,))
# t1.start()
# t2.start()

# print("=============in the main==============")


'''
多线程实验2
'''

def music(name):
    for i in range(2):
        a = random.randint(1,100)
        time.sleep(4)
        print(a)


def move(name):
    for i in range(2):
        print('Begin see movie %s. %s' %(name, time.ctime()))

        print('end see movie %s' %time.ctime())


# threads = []
# thread1 = threading.Thread(target=music, args=('七里香',))
# thread2 = threading.Thread(target=move, args=('速度与激情',))
# threads.append(thread1)
# threads.append(thread2)
#
# for thread in threads:
#     thread.start()
#
#
# print('all over the tasks %s' %time.ctime())


'''
多线程实验3 join(),把调用join的子线程执行的东西插入到主线程中
'''

threads = []
thread1 = threading.Thread(target=music, args=('七里香',))
thread2 = threading.Thread(target=music, args=('速度与激情',))
threads.append(thread1)
threads.append(thread2)

for thread in threads:
    thread.start()







