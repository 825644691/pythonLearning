import os


print(os.getcwd()) #获取当前工作目录
print(os.path.dirname(os.getcwd())) #获取当前工作目录的上一级目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #获取当前目录的上一级目录
print(os.path.abspath(__file__)) #获取当前文件的绝对路径
os.chdir('e:/bookstore') #改变当前的工作目录
print(os.getcwd())
# os.curdir .
# os.pardir ..
# print(os.path.join(os.getcwd(), 'aaa.txt')) #路径合并
# os.makedirs('lxl/lxlxl.txt') #递归创建空文件/空文件夹
# os.removedirs('lxl') #只能删空文件
# os.mkdir('sdsa/asd') #如果sdsa目录不存在就报错
# os.rmdir('asd') #只删除一个空目录
print(os.listdir())
print(os.listdir(r'e:\bookstore')) #列出目录下的文件或者文件夹
# os.remove('asd.txt') #删除asd.txt文件(只能删除文件不能删除目录)
# os.rename('lxl', 'lxlxl') #os.rename('old name', 'new name')
print(os.stat(r'lxlxl\tmd.txt'))
print(os.sep) #返回系统的路径分隔符
print(os.linesep) #获取操作系统的换行符 linux \r\n  win \n
print(os.pathsep) #环境变量的分隔符
print(os.environ) #获取环境变量
print(os.system('dir')) #运行shell命令
print(os.path.split(r'E:\bookstore\lxlxl\tmd.txt'))
print(os.path.dirname(r'E:\bookstore\lxlxl\tmd.txt')) #获取指定文件/文件夹所在的文件夹
print(__file__)
print(os.path.basename(r'E:\bookstore\lxlxl\tmd.txt')) #返回路径最后的文件名，如果是分割符结尾就返回空
print(os.path.isabs(r'E:\bookstore\lxlxl\tmd.txt')) #如果path是绝对路径返回True
print(os.path.exists(r'E:\bookstore\lxlxl\tmd.txt')) #如果path存在就返回True
print(os.path.isdir(r'E:\bookstore\lxlxl\tmd.txt')) #判断path是否是一个文件夹
print(os.path.getatime(r'E:\bookstore\lxlxl\tmd.txt')) #返回path指向的目录或者文件的最后存取时间
print(os.path.getmtime(r'E:\bookstore\lxlxl\tmd.txt')) #返回path所指向的目录或者文件的最后修改时间