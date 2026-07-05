# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
import numpy as np
n, s = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0,0)

dp = np.zeros((n+1, s+1), dtype=bool)
dp[0,0] = True

for i in range(1,n+1):
    for j in range(s+1):
        if dp[i-1,j]:
            dp[i,j] = True
        elif j-a[i]>=0 and dp[i-1,j-a[i]]:
            dp[i,j] = True
if dp[n,s]:
    print("Yes")
else:
    print("No")