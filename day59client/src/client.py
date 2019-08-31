import socket
import os, sys
import json
import subprocess
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
                data_byte = obj.recv(1024)
                if not data_byte: break
                path = os.path.join(settings.server_dir, name)
                subprocess.getstatusoutput('mkdir '+ path)


                data_str = json.loads(str(data_byte, 'utf-8'))
                for j in data_str.items():
                    data_str = j
                MyClient.create_dir(data_str[1], path)
                while True:
                    try:
                        file_data_name, file_data_len = str(obj.recv(1024), 'utf-8').split('|')
                    except Exception as e:
                        break
                    print(file_data_name)
                    print(file_data_len)
                    obj.sendall(bytes('1', 'utf-8'))
                    str_len = 0
                    with open(os.path.join(settings.server_dir, file_data_name), 'wb') as f:
                        while str_len < int(file_data_len):
                            data = obj.recv(700)
                            f.write(data)
                            str_len += len(data)
                            print(1)
                        f.close()
                    obj.sendall(bytes('1', 'utf-8'))






            else:
                print(data_str)
        obj.close()



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