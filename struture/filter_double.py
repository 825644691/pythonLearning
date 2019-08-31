def delete():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i - 1)
        else:
            i = i + 1
    return nums


delete()