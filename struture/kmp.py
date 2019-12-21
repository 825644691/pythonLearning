s = "aaaaab"
t = "aaab"
def find():
    if not t:
        return 0
    _next = [0] * len(t)
    def getNext():
        i = 0
        j = -1
        _next[i] = j
        while i < len(t) - 1:
            if j == -1 or t[i] == t[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]

    getNext()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = _next[j]
            if j == -1:
                i += 1
                j += 1
    if j > len(t) -1:
        return i - j
    res = -1
    return res

print(find())
# i = 0
# res = 0
# j = 0
# while j <= len(haystack) - 1:
#     print(str(haystack[j])+ "->"+ str(needle[i]))
#     if needle[i] == haystack[j]:
#         if len(needle) -1 == i:
#             res = j - len(needle) + 1
#             break
#         if i + 1 < len(needle):
#             i += 1
#             j += 1
#     else:
#         if i == 0:
#             j += i + 1
#         else:
#             j  = j - i +1
#             i = 0
#
#
#
# print(res)