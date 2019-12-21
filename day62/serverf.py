import socket
import select


sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8880))
sk1.listen(3)


sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8881))
sk2.listen(3)
inp = [sk1, sk2]
while True:
    r, w, e = select.select(inp, [], [])
    for obj in r:
        if obj == sk1 or obj == sk2:
            conn, addr = obj.accept()
            inp.append(conn)
        else:
            data = obj.recv(1024)
            print(data.decode('utf-8'))
            send = input('>>>')
            obj.sendall(send.encode('utf-8'))
