import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8881))


while True:
    inp = input('>>')
    sk.sendall(inp.encode('utf-8'))
    data = sk.recv(1024)
    print(data.decode('utf-8'))
