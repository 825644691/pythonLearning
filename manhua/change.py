#coding=utf8
import os
import subprocess
BASE_DIR = 'E:\download\端脑1\端脑'
print(BASE_DIR)

rule = {'一.jpg': '1.jpg',
        '二.jpg': '2.jpg',
        '三.jpg': '3.jpg',
        '四.jpg': '4.jpg',
        '五.jpg': '5.jpg',
        '六.jpg': '6.jpg',
        '七.jpg': '7.jpg',
        '八.jpg': '8.jpg',
        '九.jpg': '9.jpg',
        '十.jpg': '10.jpg',
        '十一.jpg': '11.jpg',
        '十二.jpg': '12.jpg',
        '十三.jpg': '13.jpg',
        '十四.jpg': '14.jpg',
        '十五.jpg': '15.jpg',
        '十六.jpg': '16.jpg',
        '十七.jpg': '17.jpg',
        '一十一.jpg': '11.jpg',
        '一十二.jpg': '12.jpg',
        '一十三.jpg': '13.jpg',
        '一十四.jpg': '14.jpg',
        '一十五.jpg': '15.jpg',
        '一十六.jpg': '16.jpg',
        '一十七.jpg': '17.jpg',
        '一十.jpg': '10.jpg'


        }

def getDir():
    l = []
    process = subprocess.getstatusoutput('dir /b ' + BASE_DIR)
    if process[0] == 0:
        for item in process[1].split('\n'):
            l.append(item)
        return l
    else:
        return '没有此命令'

def rename(path):
    process = subprocess.getstatusoutput('dir /b ' + path)
    if process[0] == 0:
        for item in process[1].split('\n'):
            file = os.path.join(path, item)
            try:
                os.rename(file,os.path.join(path, rule[item]))
            except Exception:
                print(file)




if __name__ == '__main__':
    dir = getDir()
    for item in dir:
        path = os.path.join(BASE_DIR, item)
        rename(path)