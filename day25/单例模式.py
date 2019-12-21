#单例模式，只用一个实例（对象）

# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('%s-%s' %(self.name,self.age))


#obj = Foo('lxl',18) #obj就是一个实例
#第一个方法（不常用）
# v = None
# while True:
#     if v:
#         v.show()
#     else:
#         v = Foo('lxl',18)
#         v.show()


class Foo:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Foo, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

#用单例模式不在使用单例模式来创建对象
obj1 = Foo()
print(obj1)
obj2 = Foo()
print(obj2)
obj3 = Foo()
print(obj3)


class A:
    def __init__(self):
        print('A')

class B:
    def __new__(cls, *args, **kwargs):
        super(B, cls).__new__(cls, *args, **kwargs)
        orin = super(B, cls)
        print(orin)

b = B()

# class Fooo:
#     @classmethod
#     def get_instance(cls):
#         if not hasattr(Fooo,'_v'):
#             if not hasattr(Fooo,'_v'):
#                 cls._v = Fooo()
#         return cls._v
#
# obj1 = Fooo.get_instance()
# print(obj1)
# obj2 = Fooo.get_instance()
# print(obj2)
# obj3 = Fooo.get_instance()
# print(obj3)
# name = (1, 2, 3)
# print("hello %s" % (name,))
#
# print("hello {name}".format(name=name))


g = lambda x, y: x + y

var = g(2, 3)
print(var)

# reduce(lambda x,y:x*y,range(1,4))

a = map(lambda x:x*2, [1, 2, 3])
# for i in a:
#     print(i)
# c = lambda x:x>5
# for i in c:
#     print(i)


from functools import reduce

# print(reduce(lambda x:x,range(1,4)))
import copy

s = [1, 2, 3, [1, 2, 3]]
t = copy.copy(s)
print(id(s))
print(id(t))
s[3].append(4)
s[0] = 2
print(t)
print(s)

k = "梁晓礼"
import urllib.parse
k = urllib.parse.quote(k)
sb = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%BD%91%E7%BB%9C%E5%9F%BA%E7%A1%80%E7%BD%91%E9%A1%B5%E6%96%87%E6%A1%A3%E6%98%AF%E4%B8%80%E7%A7%8Duri%E5%90%97&oq=uri%25E5%2592%258Curl&rsv_pq=efd359a7000e01d8&rsv_t=48b3kT9yAlwuN0FElx9YTP1C%2FIvyYUjIiyZ3eDMARWble4ru7VCLx7TaoAc&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=8729&rsv_sug3=63&rsv_sug2=0&rsv_sug4=8729&rsv_jmp=slow"
print(urllib.parse.unquote(sb))
print(k)

l1 = ['b','c','d','b','c','a','a']
l2 = copy.copy(l1)
l2.sort(key=l1.index)
print(l2)
l3 = {}.fromkeys(l1, 10)
print(l3)
l4 = [[0]*5 for i in range(5)]
print(l4)
l5 = []
[l5.append(i) for i in l1 if i not in l5]
print(l5)
items=[('name','earth'),('port','80')]
dict2=dict(items)
print(dict2)


