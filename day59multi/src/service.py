import socketserver
import os, sys
import subprocess
import queue
import json
import threading
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config import settings


operation_type = ['cmd', 'get', 'post']






class multiServer:

    @staticmethod
    def run():
        socket = socketserver.ThreadingTCPServer((settings.BIND_HOST, settings.BIND_PORT), MyServer)
        print('服务启动')
        socket.serve_forever()

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes('欢迎来到梁晓礼的Tcp服务', 'utf-8'))
        while True:
            data_byte = conn.recv(1024)
            if not data_byte: break
            if str(data_byte, 'utf-8').split('|')[0] in operation_type:
                data_str = str(data_byte, 'utf-8')
                data_split = data_str.split('|')
                if len(data_split) < 2:
                    result = '请输入具体命令'
                    func = 1
                else:
                    obj = Action(data_split[1], conn)
                    func = getattr(obj, data_split[0])
                    result = func()
            # else:
            #     self.send(data_byte, conn)

        conn.close()


    def send(self, result, conn):
        conn.sendall(bytes(str(len(result)), 'utf-8'))
        conn.sendall(bytes(result, 'utf-8'))









class Action:
    def __init__(self, data, conn):
        self.data = data
        self.dir = settings.server_dir
        self.conn = conn
        self.path_dir = queue.Queue()
        self.dic = {}
        self.l = []
        self.fileDic = {}

    def post(self):
        result = bytes()
        get_data = self.conn.recv(1024)
        print(222)
        result += get_data
        file = os.path.join(self.dir, self.data)
        print(result)
        with open(file, 'wb') as f:
            f.write(get_data)
            f.close()
        print(333)
        return '成功'


    def get(self):
        file = os.path.join(self.dir, self.data)
        if os.path.isfile(file):
            with open(file, 'r') as f:
                data = f.read()
                f.close()
            return data
        dic = dict()
        dic[file] = {}
        self.recu_dir(self.data,dic[file])
        for item in self.fileDic.items():
            self.path_dir.put(item)
        self.send(json.dumps(dic))
        lock = threading.Lock()
        threads = []
        for r in range(4):
            threads.append(threading.Thread(target=self.multi_thread_download, args=(lock,)))
        for t in threads:
            t.start()
        for s in threads:
            s.join()
        # self.multi_thread_download(lock)

        self.conn.sendall(bytes('quit', 'utf-8'))

    def multi_thread_download(self, lock):
        while True:
            try:
                get_file = self.path_dir.get(0)
            except Exception as e:
                return
            file_dir, file_name = get_file
            for file in file_name:
                path = os.path.join(self.dir, file_dir, file)
                with open(path, 'rb') as f:
                    file_data = f.read()
                    f.close()
                data_len = str(len(file_data))
                lock.acquire()
                self.conn.sendall(bytes(os.path.join(file_dir, file) + '|'+ data_len, 'utf-8'))
                self.conn.recv(1024)
                self.conn.sendall(file_data)
                self.conn.recv(1024)
                lock.release()



    def recu_dir(self, file, dic):
        self.data = 'ls ' + os.path.join(self.dir, file)
        files = self.cmd()
        files = files.split('\n')
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


    def send(self, result):
        self.conn.sendall(bytes(result, 'utf-8'))

    def cmd(self):
        process = subprocess.getstatusoutput(self.data)
        if process[0] ==0 :
            return process[1]
        else:
            return '没有此命令'





if __name__ == '__main__':
    multiServer.run()