# a = [x*2 for x in range(10)]
# print(a)
def aaa():
    value = yield 2
    value='hhjk'
    yield value




a = aaa()
print(next(a))
print(a.send("jhkj"))
for i in aaa():
    print(i)


# import time
# print(time.gmtime())
# print(time.localtime())
# print(time.ctime())