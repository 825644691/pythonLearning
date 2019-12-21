#coding=utf8
import subprocess
import pymysql
from pymediainfo import MediaInfo
import json
import pymysql

BASE_DIR = 'f:\\diploma\\qqMusic\\'

def getDir():
    l = []
    conn = pymysql.connect(host='192.168.18.128', port=3306, user='liangxiaoli', passwd='123', db='liangxiaoli')
    cursor = conn.cursor()  # 可以取出列名，以字典的方式显示
    q = cursor.execute('select distinct sid from song where playTime=0')
    result = cursor.fetchall()
    sql = list(result)
    sqldata = []
    for s in sql:
        sqldata.append(str(*s))
    process = subprocess.getstatusoutput('dir /b ' + BASE_DIR)
    if process[0] == 0:
        for p in process[1].split('\n'):
            l.append(p.split('.')[0])
        l = list(set(l).intersection(set(sqldata)))
        return l
    else:
        return '没有此命令'

if __name__ == '__main__':
    conn = pymysql.connect(host='192.168.18.128', port=3306, user='liangxiaoli', passwd='123', db='liangxiaoli')
    cursor = conn.cursor()  # 可以取出列名，以字典的方式显示
    items = getDir()
    i = 1
    for item in items:
        media_info = MediaInfo.parse(BASE_DIR + str(item)+ '.m4a')
        data = media_info.to_json()
        playTime = json.loads(data)['tracks'][0]['duration']
        cursor.execute('update song set playTime='+ str(playTime) +' where sid='+str(item))
        conn.commit()
        complete = (i/604)*100
        print(str(item) + ' 添加完成' + str(complete))
        i += 1
