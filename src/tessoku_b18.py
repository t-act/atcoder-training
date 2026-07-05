# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq

import numpy as np
from collections import defaultdict

n, s = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0,0)

def func_dp(i_max, j_max, a):
    dp = np.zeros((i_max+1, j_max+1), dtype=bool)
    dp[0:i_max, 0] = True

    for i in range(1, i_max+1):
        for j in range(j_max+1):
            if dp[i-1,j]:
                dp[i,j] = True
            elif j-a[i]>=0 and dp[i-1,j-a[i]]:
                dp[i,j] = True
    return dp

dp = func_dp(n, s, a)

if not dp[n,s]:
    print(-1)
else:
    ans = []
    j = s
    for i in range(n, 0, -1):
        if j >= a[i] and dp[i-1,j-a[i]]:
            ans.append(i)
            j -= a[i]
    ans.reverse()
    print(len(ans))
    print(*ans)