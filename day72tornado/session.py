# coding:utf-8

# class A:
#     def __init__(self):
#         print('aaa')
#         super().__init__()
#
# class B:
#     def __init__(self):
#         print('bbb')
#
#
# class C(A, B):
#     def test(self):
#         print('test')
#
# C().test()
import uuid
container = {}

class Session:
    def __init__(self, handler):
        # 获取用户cookie，如果有不操作，否则给用户生成随机字符串
        # 写给用户
        # 保证session
        nid = handler.get_cookie('session_id')
        if nid in container:
            pass
        else:
            nid = str(uuid.uuid4())
            handler.set_cookie('session_id', nid)
            print(nid)
            container[nid] = {}
        self.nid = nid
        self.handler = handler

    def __getitem__(self, item):
        return container[self.nid].get(item)

    def __setitem__(self, key, value):
        container[self.nid][key] = value




