class Foo:
    @staticmethod
    def add(nums,target):
        count = len(nums) - 1
        for i, m in enumerate(nums):
            j = i + 1
            while j <= count:
                if m + nums[j] == target:
                    return [i,j]
                else:
                    j += 1
    @staticmethod
    def hash_add(nums,target):
        _dict = dict()
        for i, m in enumerate(nums):
            _dict[m] = i
        for i, m in enumerate(nums):
            j = _dict.get(target - m)
            if j is not None and i != j:
                return [i,j]


        print(_dict)

    @staticmethod
    def hash_add_one():
        _dict = dict()
        for i, m in enumerate(nums):
            j = _dict.get(target - m)
            if j is not None:
                return [j, i]
            _dict[m] = i


nums = [2, 7, 11, 15]
target = 9
result = Foo.hash_add_one()
print(result)