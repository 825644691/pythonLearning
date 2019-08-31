def find_most_water():
    height = [1,8,6,2,5,4,8,3,7]
    n = len(height)
    area = 0
    i = 0
    j = n - 1
    while i < j:
        if height[i] < height[j]:
            area = max(area, height[i] * (j - i))
            i += 1
        else:
            area = max(area, height[j] * (j - i))
            j -= 1
    return area



find_most_water()