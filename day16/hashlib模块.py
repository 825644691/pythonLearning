#加密模块
import hashlib


m = hashlib.md5()
m.update('hello world'.encode('utf-8')) #转化成md5
print(m.hexdigest()) #再取出来
m.update('lxl'.encode('utf-8'))
print(m.hexdigest())

s = hashlib.sha256()
s.update('hello world'.encode('utf-8'))
print(s.hexdigest())
