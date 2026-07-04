# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

from bisect import bisect_left
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = bisect_left(a, x)
print(ans + 1)