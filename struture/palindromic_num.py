import re


def find_num_palindromic():
    s = "ab"
    p = ".*c"
    res = re.findall(p,s)
    return True if not res else False

print(find_num_palindromic())