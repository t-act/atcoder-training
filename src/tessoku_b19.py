# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr

import numpy as np
n, w = map(int, input().split())
item = [[0,0]]
max_value = 0
for _ in range(n):
    weight, value = map(int, input().split())
    if value > max_value:
        max_value = value
    item.append([weight, value])

value_max = sum(v for _, v in item)
dp = np.full((n+1, value_max+1), np.inf)
dp[0,0] = 0

for i in range(1, n+1):                       # 1から（i=0だとdp[-1]を誤参照）
    weight, value = item[i]
    for j in range(value_max+1):              # value_maxの列も含める
        dp[i, j] = dp[i-1, j]                 # アイテムiを使わない
        if j >= value and dp[i-1, j-value] + weight < dp[i, j]:
            dp[i, j] = dp[i-1, j-value] + weight   # 使う：価値をvalue戻し重量を足す

ans = max(j for j in range(value_max+1) if dp[n, j] <= w)
print(ans)