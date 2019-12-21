import redis
import json
import pymysql

pool = redis.ConnectionPool(host='192.168.18.128', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# keys = r.keys()[0]
# l = r.lrange("song",0,-1)
#
# print(len(l))
r.set('a','123')







