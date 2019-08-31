import json
# with open('E:/aaa.txt','w',encoding='utf-8') as file:
#     i=1
#     while i<10:
#         file.write(str(i))
#         file.write('\n')
#         i+=1

# with open('E:/aaa.txt','r',encoding='utf-8') as file1:
#     for i,v in enumerate(file1.readlines(),1):
#         if i == 6:
#             v=''.join([v.strip(),'jjjj'])
#         print(v.strip())


# a = 'quit'
# print(len(a))
#
# a = bytes(a, 'utf-8')
# print(len(a))


# def aaa():
#     yield "aaa"
#     yield "bbb"
#
# a = aaa()
# for i in  a:
#     print(i)

# dic = {'name': 'lxl', 'age':18}
# print(**dic)
# a = 'asdsadas'
# a = bytes(a, 'utf-8')
# print(a)
# a = str(a)
# print(bytes(a, 'utf-8'))
import queue

q = queue.Queue()
print(type(q))
q.put({'name': 'lxl', 'age': 18})
q.put({'name': 'gw', 'age': 18})
q.put({'name': 'lxlx', 'age': 18})
q = str(q)
q = bytes(q, 'utf-8')
print(q)
q = str(q, 'utf-8')
print(q)
q = queue.Queue(q)
print(q)
print(q.get(0))
