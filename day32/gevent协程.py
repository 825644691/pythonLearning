import gevent
from urllib import request
import time
from gevent import monkey

def foo():
    print('running in foo')
    gevent.sleep(0)
    print('Explict context switch to foo again')


def bar():
    print('running in bar')
    gevent.sleep(0)
    print('Explict context switch to bar again')


# gevent.joinall(
#     [
#         gevent.spawn(foo),
#         gevent.spawn(bar)
#     ]
# )






def f(url):
    print('GET %s' %url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%s bytes received from %s' %(len(data), url))

l = ['http://www.baidu.com', 'http://xiaohuar.com/', 'http://www.zhihu.com']

start = time.time()

# for url in l :
#     f(url)
gevent.monkey.patch_all()
gevent.joinall(
    [
        gevent.spawn(f, 'http://www.baidu.com'),
        gevent.spawn(f, 'http://xiaohuar.com/'),
        gevent.spawn(f, 'http://www.sogou.com')
    ]
)

print(time.time() - start)