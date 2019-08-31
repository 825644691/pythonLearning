def transform():
    s = 5504
    res = ''
    dic = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    for i in sorted(dic.keys())[::-1]:
        a = s // i
        if not a :
            continue
        res += dic[i]
        s -= a *i
        if s == 0:
            break
    return res


def reverse():
    s = 'MCMIXI'
    n = len(s)
    res = 0
    dic = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'X': 10,
        'IX': 9,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'M': 1000,
        'CM':900
    }
    for i in range(n):
        j = i + 1
        if j < n  :
            if s[i] < s[j]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        else:
            res += dic[s[i]]

    return res







print(reverse())