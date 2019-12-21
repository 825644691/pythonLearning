import socket
import os, sys
import json
import subprocess
import queue
import threading
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config import settings


class MyClient:
    @staticmethod
    def run():
        obj = socket.socket()
        conn = obj.connect((settings.BIND_HOST, settings.BIND_PORT))
        data_byte = obj.recv(1024)
        data_str = str(data_byte, 'utf-8')
        print(data_str)
        MyClient.notice()
        while True:
            inp = input('>>>')
            obj.sendall(bytes(inp, 'utf-8'))
            command, name = str(inp).split('|')
            if command == 'post':
                file = os.path.join(BASE_DIR, name)
                with open(file, 'rb') as f:
                    data = f.read()
                    obj.sendall(data)


            elif command == "get":
                file_queue = queue.Queue()
                data_byte = obj.recv(1024)
                if not data_byte: break
                path = os.path.join(settings.server_dir, name)
                subprocess.getstatusoutput('mkdir '+ path)


                data_str = json.loads(str(data_byte, 'utf-8'))
                for j in data_str.items():
                    data_str = j
                MyClient.create_dir(data_str[1], path)
                while True:
                    data_info = obj.recv(1024)
                    print(data_info)
                    if len(data_info) < 10 and str(data_info, 'utf-8') == 'quit':
                        break
                    try:
                        data_name, data_size = str(data_info, 'utf-8').split('|')
                    except Exception as e:
                        obj.sendall(bytes('1', 'utf-8'))
                        print(2)
                        break
                    obj.sendall(bytes('a', 'utf-8'))
                    split_data = obj.recv(1024)
                    data_len = len(split_data)
                    next(MyClient.gen(data_size,data_len, split_data))
                    while data_len != int(data_size):
                        split_data = obj.recv(1024)
                        MyClient.gen(data_size, data_len, split_data).send(split_data)
                        data_len += len(split_data)

                    file_info = MyClient.gen(data)
                    info = {'data_name': data_name, 'data_size':data_size, 'file_info': file_info}
                    file_queue.put(info)
                    obj.sendall(bytes('1', 'utf-8'))
                # for j in range(file_queue.qsize()):
                #     print(file_queue.get())
                threads = []
                for times in range(4):
                    threads.append(threading.Thread(target=MyClient.create_file, args=(file_queue,)))
                for t in threads:
                    t.start()
                # MyClient.create_file(file_queue)


            else:
                print(data_str)
        obj.close()

    @staticmethod
    def create_file(file_queue):
        while True:
            try:
                get_file = file_queue.get(0)
            except Exception as e:
                break
            path = os.path.join(settings.server_dir, get_file['data_name'])
            with open(path, 'wb') as f:
                for data in get_file['file_info']:
                    f.write(data)
                f.close()






    @staticmethod
    def gen(data_size, data_len, data):
        # data_len = 0    #第一种
        # while data_len != int(data_size):
        #     data = obj.recv(800)
        #     data_len += len(data)
        #     print(data)
        #     yield (data)
        # print(data_size)
        # print('act' + str(data_len))

        # for item in data:  #第二种
        #     yield item
        value = yield data
        while int(data_size) != data_len:
            value = yield value
            data_len += value









    @staticmethod
    def create_dir(data_str, path):
        for dir in data_str:
            abs_dir = os.path.join(path, dir)
            subprocess.getstatusoutput('mkdir ' + abs_dir)
            if data_str[dir]:
                MyClient.create_dir(data_str[dir], abs_dir)


    @staticmethod
    def notice():
        notice_info = '''
        'cmd': '请求返回系统消息',
        'post': '上传',
        'get': '下载'
        '''


        print(notice_info)


if __name__ == '__main__':
    MyClient.run()