# https://atcoder.jp/contests/abc122/tasks/abc122_c

n, q = map(int, input().split())
s = input()

# ACが完成した時点で加算していく累積和リストを考える
acc = [0] * (n+1)

for i in range(2, n+1):
    if s[i-2] == "A" and s[i-1] == "C":
        acc[i] += acc[i-1] + 1
    else:
        acc[i] = acc[i-1]
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(acc[r] - acc[l])

for a in ans:
    print(a)
