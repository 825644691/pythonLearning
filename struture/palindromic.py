    def find_palindromic():
    s = "abababa"
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    max_len = float('-inf')
    for i in range(n):
        for j in range(i+1):
            if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                dp[i][j] = 1
            if dp[i][j] and i - j + 1 > max_len:
                max_len = i -j + 1
                res = s[j : i + 1]
    return res


print(find_palindromic())