class Strut:
    @staticmethod
    def find_median():
        nums1 = [1, 3]
        nums2 = [2, 4]
        l1 = len(nums1)
        l2 = len(nums2)
        k = (l1 + l2 + 1) // 2
        left = 0
        right = l1
        while left < right:
            n1 = left + (right - left) // 2
            n2 = k - n1
            if nums1[n1] < nums2[n2 - 1]:
                left = n1 + 1
            else:
                right = n1

        n1 = left
        n2 = k - n1
        c1 = max(nums1[n1 - 1] if n1 > 0 else float('-inf'), nums2[n2 - 1] if n2 > 0 else float('-inf'))
        if (l1 + l2) % 2 == 1:
            return c1
        c2 = min(nums1[n1] if n1 < l1 else float('inf'), nums2[n2] if n2 < l2 else float('inf'))
        return (c1 + c2) / 2




Strut.find_median()







