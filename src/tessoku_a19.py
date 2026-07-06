# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s

import numpy as np
n, w = map(int, input().split())
item = [[0,0]]
for _ in range(n):
    weight, value = map(int, input().split())
    item.append([weight, value])

dp = np.full((n+1, w+1), -10**(-15))
dp[0,0] = 0

for i in range(1,n+1):
    weight = item[i][0]
    value = item[i][1]
    for j in range(w+1):
        if j >= weight:
            dp[i,j] = max(dp[i-1, j-weight]+value, dp[i-1, j])
        elif dp[i-1, j] >= 0:
            dp[i, j] = dp[i-1, j]

print(int(dp.max()))