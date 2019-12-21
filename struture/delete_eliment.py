def de():
    nums = [3, 2, 2, 3]
    val = 3
    i = 0

    j = len(nums) - 1
    while i < j:
        while i < j and nums[j] == val:
            j -= 1

        while i < j and nums[i] != val:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] == val:
            return i

print(de())