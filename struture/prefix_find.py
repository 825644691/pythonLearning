def find_prefix():
    s = ["a"]
    i = 1
    res = ''
    while i < len(s[0]):
        pattern = s[0][:i]
        for item in range(len(s)):
            if pattern in s[item]:
                res = pattern
                if item == len(s) - 1:
                    i += 1
            else:
                i = len(s[0])
                res = pattern[0:len(pattern)-1]
                break
    return res


print(find_prefix())


s = 'flower'
p = 's'
print(s.index(p))