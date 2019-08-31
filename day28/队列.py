import queue
import json
#队列 FIFO先进先出
#队列自己有一把shuo

d = queue.Queue(3)

d.put("hjw")
d.put("hjw")
d.put("goulin")



# print(d.get(0))
# print(d.get(0))
# print(d.get(0))
# try:
#     d.get(0)
# except Exception as e:
#     print(1)

dic = {"/data2/day59": {"bin": {"lxl": {}}, "config": {"__pycache__": {}}, "src": {}}}

data = ('/data2/day59', {'bin': {'lxl': {}}, 'config': {'__pycache__': {}}, 'src': {}})
dir, name = data
print(dir)



