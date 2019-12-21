def searchInsert():
    nums = [1, 3, 5, 6]
    target = 7
    count = len(nums) - 1
    left = 0
    right = count
    while left <= right:
        m = (right - left) // 2 + left
        if nums[m] < target:
            left = m + 1
        elif nums[m] > target:
            right = m - 1
        elif nums[m] == target:
            return m
    return left

print(searchInsert())

one_set = set()
one_set.update([1, 2, 3])

print(one_set)