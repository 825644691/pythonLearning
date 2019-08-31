def generateParenthesis(N):
    ans = []

    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    backtrack()
    return ans

def maxStr():
    s = 'abcabcbb'
    dic = {}
    max_len = 0
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
        else:
            max_len =max(i - dic[s[i]],max_len)
            dic[s[i]] = i
    return max_len


def twoSum():
    nums = [2, 7, 11, 15]
    target = 9
    dic = {}
    res = []
    for i,v in enumerate(nums):
        dic[v] = i

    for item in nums:
        if dic.get(target - item) is not None:
            res.append(dic[target - item])
            print(target)

    return res





def maxStr2():
    s = 'abcabcbb'
    lookup = set()
    left = 0
    l = 0
    res = 0
    for i in range(len(s)):
        l += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            l -= 1
        lookup.add(s[i])
        res = max(l, res)
    return res




def find_subString(s = ('a', 'b', 'c', 'd')):
    for k in range(len(s)):
        if 0 == len(s) - 1:
            yield s[0]
        for i in find_subString(s[1:]):
            yield s[k] + i


for j in find_subString():
    print(j)








