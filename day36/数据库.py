#python连接数据库
#1pymysql
#2mysqldb ：不支持数据库
#coding=gbk

import pymysql
import redis


#创建连接
# conn = pymysql.connect(host = '192.168.18.128',port = 3306,user = 'liangxiaoli',passwd = '123',db = 'liangxiaoli')
# #cursor = conn.cursor()
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#可以取出列名，以字典的方式显示

# 数据库操作 - 增  -  (获取自增后的id)
# cursor.execute('insert into news(id,title,content)values(1,"嗄萨蒂","asd")')
# inp = input("请输入id")
# cursor.execute('insert into news(title,content)values(%s,%s)',(inp,inp))
# conn.commit()
# nid = cursor.lastrowid
# print(nid)

# 数据库操作 - 增多条数据
# l = ((1111,"嗄萨蒂","asd"),
#      (2222,"嗄萨蒂","asd"),
#      (3333,"嗄萨蒂","asd"))
# cursor.executemany('insert into news(id,title,content)values(%s,%s,%s)',l)
# conn.commit()


#数据库操作 - 改
# r = cursor.execute('update news set title = %s where id =%s ', ('危机2',5))
# conn.commit()

#数据库操作 - 删
# d = cursor.execute('delete from news where id = %s' ,5)
# conn.commit()

#数据库操作 - 查
#fetchall拿到的是一个元组
#fetchone拿到的是一条数据

# print(result)
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# 数据库操作 - 查(手动移动指针)
# cursor.scroll(0,mode='absolute')
# cursor.scroll(-1,mode='relative')
# result = cursor.fetchone()
# print(result)



#数据库操作 - 查(错误操作)：黑客入侵-数据库注入
# sql = 'select id as i,title from news where title = "%s" and id = "%s"'
# sql = sql %('嗄萨蒂',1)
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)



# conn = pymysql.connect(host = '192.168.18.128',port = 3306,user = 'liangxiaoli',passwd = '123',db = 'liangxiaoli')
# cursor = conn.cursor()#可以取出列名，以字典的方式显示
# q = cursor.execute('select sid, mid from song limit 2')
# result = cursor.fetchall()
# data = list(result)
# print(data)
# item = {'collection': 3740,
#  'desc': '梁晓礼',
#  'mtime': 1499899531,
#  'tag': [166, 148],
#  'tid': 3147052475
#         }
#
# cursor.execute('update songList set description="' + item['desc'] + '" , collection=' + str(item['collection']) + ' , mtime='
#                     + str(item['mtime']) + ' where tid=' + str(item['tid']))
# conn.commit()


conn = pymysql.connect(host='192.168.18.128', port=3306, user='liangxiaoli', passwd='123', db='liangxiaoli')
cursor = conn.cursor()  # 可以取出列名，以字典的方式显示
q = cursor.execute('select distinct sid from song where playTime=0')
result = cursor.fetchall()
list = list(result)
data = []
for l in list:
      data.append(*l)




