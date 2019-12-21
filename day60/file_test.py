import os
import subprocess
from multiprocessing import Queue, Pipe
# import queue
import json
import pickle

BASE_DIR = '/data2'

def findAll_file():
    name = 'data2'
    try:
        with open(BASE_DIR, 'rb') as f:
            data = f.read()
    except Exception as e:
        process = subprocess.getstatusoutput('ls ' + BASE_DIR)
        l = []
        result = {}
        for i in process[1].split('\n'):
            l.append(i)
        result[name] = l
        q = queue.Queue()
        q.put(result)
        print(q.get())



# findAll_file()

class Test:
    def __init__(self):
        self.dir = BASE_DIR
        self.data = 'day59'
        self.path_dir = queue.Queue()
        self.dic = {}
        self.l = []
        self.fileDic = {}


    def get(self):
        file = os.path.join(self.dir, self.data)
        if os.path.isfile(file):
            with open(file, 'r') as f:
                data = f.read()
                f.close()
            return data
        dic = dict()
        dic[file] = {}
        self.recu_dir(self.data, dic[file])
        print(dic)
        for item in self.fileDic.items():
            self.path_dir.put(item)
        for i in range(self.path_dir.qsize()):
            print(self.path_dir.get())





    def recu_dir(self, file, dic):
        self.data = 'ls ' + os.path.join(self.dir, file)
        files = self.cmd()
        files = files.split('\n')
        print(files)
        if not files[0]:
            return
        for i in files:
            if os.path.isdir(os.path.join(self.dir, file, i)):
                dic[i] = {}
                self.recu_dir(os.path.join(file, i), dic[i])
            else:
                if file not in self.fileDic.keys():
                    self.fileDic[file] = []
                self.fileDic[file].append(i)

    def cmd(self):
        process = subprocess.getstatusoutput(self.data)
        if process[0] == 0:
            return process[1]
        else:
            return '没有此命令'


#
# obj   =  Test()
# obj.get()


# dic = dict()
#
# dic['name'] = []
#
# dic['name'].append(1)
# dic['name'].append(2)
# result = json.dumps(dic)
# print(bytes(result, 'utf-8'))

# def Foo():
#     for i in range(10):
#         yield i
# print(1 == '1')

# q = []
# for i in range(10):
#     q.append(i)
# print(type(q))
# q = pickle.dumps(q)
# print(type(q))
# q = pickle.loads(q)
# print(type(q))
# print(q.pop())
# asd = Queue()
# asd.put(1)
# print(asd.get())




# for i in Foo():
#     print(i)
#
# print(100)
# parent_conn, child_conn = Pipe()
#
# child_conn.recv()
# print(1)

s = set()
s.add(1)
print(s)
if 1 in s:
    print(1)