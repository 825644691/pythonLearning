import socket
import subprocess
import os



# socket.socket(family=AF_INET,type=SOCK_STREAM)
# AF_INET6用于IP_V6 ,AF_INET用于IP_V4,SOCK_STREAM流式socket，用于建立TCP协议，还有一个SOCK_DGRAM用于UDP协议，
# family = AF_INET : 服务器之间的通信
# family = AF_UNIX : Unix不同进程间的通信

# 1024前都是系统用的
# server:
# sk.bind(address):address必须是一个元组
# sk.listen(3):3是等待的个数
'''
传送的内用一定是BYTES类型
server下的方法
    recv()#等待接受信息，如果没有信息接收就一直阻塞
    send()
    sendll()

client下的方法
    connet
通用方法：
    sk.getsockname():返回套接字自己的地址
    sk.getpeername():返回套接字远程地址

'''
sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)
'''
conn,addr = sk.accept()


while True:
    data = conn.recv(1024)
    if not data:
        conn.close()
        conn, addr = sk.accept()
        print(addr)
        continue

    print(str(data,'gbk'))
    inp = input(">>>")
    conn.send(bytes(inp,'gbk'))

'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024)
        cmd,filename,filesize = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'yuan',filename)
        filesize = int(filesize)

        with open(path,'wb') as f:
            has_accept = 0
            while has_accept !=filesize:
                result = conn.recv(1024)
                f.write(result)
                has_accept += len(result)






