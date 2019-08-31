import threading
import time


class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name,'gotlockA',time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name,'gotlockB',time.ctime())
        lock.release()
        lock.release()


    def doB(self):
        lock.acquire()
        print(self.name,'gotlockB',time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name,"gotlockA",time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.doA()
        self.doB()

if __name__ == "__main__":
    lock = threading.RLock()
    threads = []
    for i in range(5):
        threads.append(myThread())

    for t in threads:
        t.start()

    # for t in threads:
    #     t.join()
