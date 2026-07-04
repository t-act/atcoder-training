# https://atcoder.jp/contests/abc465/submissions/77179213

x, y, l, r, a, b = map(int, input().split())
fee = 0
for t in range(a, b):
    if l <= t < r:
        fee += x
    else:
        fee += y
print(fee)