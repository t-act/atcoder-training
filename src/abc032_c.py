# http://atcoder.jp/contests/abc032/tasks/abc032_c

n, k = map(int, input().split())
s = []
for _ in range(n):
    ss = int(input())
    s.append(ss)

ans = 0

# 簡単な例
if 0 in s:
    print(n)
    exit()

# しゃくとり法
l, r = 0, 0
sum_s = 1
while r < n:
    # l固定でrを進めてみる
    if sum_s * s[r] <= k:
        sum_s *= s[r]
        r += 1
        ans = max(ans, r-l)
    
    # rとlを進める
    elif r == l:
        l += 1
        r += 1
    
    # lを進める
    else:
        sum_s //= s[l]  # 取り除く（積なので除算すれば取り除ける）
        l += 1
    
print(ans)