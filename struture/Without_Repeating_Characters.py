class Foo:
    @staticmethod
    def find():
        content = ' '
        progress = []
        result = []
        content = list(content)
        max = 0
        for i in content:
            if i in progress:
                count = len(progress)
                val = progress[0:count]
                result.append(val)
                for d in range(len(progress)):
                    progress.pop()
            progress.append(i)
        result.append(progress)
        for item in result:
            if len(item) > max:
                max = len(item)
        return max

    @staticmethod
    def hash_find():
        s = 'asdasdaa'
        dic = dict()
        l = 0
        res = 0
        data = []
        for i, m in enumerate(s):
            if m in dic:
                l = max(dic[m], l)
                data.append(s[l:i+1])
            dic[m] = i + 1
            res = max(dic[m] - l, res)
        return data




r = Foo.hash_find()
print(r)

r= [1,2,3]





