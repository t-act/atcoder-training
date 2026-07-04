# https://atcoder.jp/contests/abc465/tasks/abc465_c
import copy
def exchange(s: list, num: int):
    s_copy = copy.deepcopy(s)
    s_copy[:num+1] = s_copy[num::-1]
    return s_copy

n = int(input())
s = list(input())
a = [int(i+1) for i in range(n)]

for i, mark in enumerate(s):
    if mark == "o":
        a = exchange(a, i)

print(*a)