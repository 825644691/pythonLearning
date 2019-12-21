from multiprocessing import Process,Queue
import time
# import queue


# begin = time.time()
# def add(n):
#     for i in range(n):
#         sm = 0
#         sm +=i
#     print(sm)
#
#
# add(10000000)
# add(20000000)


# p1 = Process(target=add,args=(10000000,))
# p2 = Process(target=add,args=(20000000,))
# p1.run()
# p2.run()
# end = time.time()
# print(end - begin)


def say(q):
    time.sleep(1)
    # print('queue pop is' + str(q.get(0)))
    print(id(q))


if __name__ == '__main__':
    processes = []
    q = Queue()
    for i in range(10):
        q.put(i)
    for i in range(4):
        processes.append(Process(target=say, args=(q,)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print('end')

