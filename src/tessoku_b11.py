# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)

questions = int(input())
for _ in range(questions):
    x_i = int(input())
    ans_idx = bisect_left(a_sorted, x_i)
    print(ans_idx)
